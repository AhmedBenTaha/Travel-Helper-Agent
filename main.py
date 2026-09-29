import os

import gradio as gr
from dotenv import load_dotenv
from openai import OpenAI

from context import TRAVEL_SYSTEM_PROMPT
from tools import tools, handle_tool_call
from styles import CSS, JS, EXAMPLES


# ============================================================
# Configuration
# ============================================================

load_dotenv(override=True)

MODEL_NAME = os.getenv(
    "DEFAULT_MODEL_NAME",
    "openai/gpt-oss-120b",
)

client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("GROQ_API_KEY"),
)

SYSTEM_MESSAGE = {
    "role": "system",
    "content": TRAVEL_SYSTEM_PROMPT,
}


# ============================================================
# Chat Logic
# ============================================================

def chat(message, history):
    """
    Main Travel Helper agent loop.

    The conversation history provides memory across turns.
    The LLM can decide whether to answer directly or call tools.
    """

    # ========================================================
    # Normalize Gradio history
    # ========================================================

    history = [
        {
            "role": item["role"],
            "content": item["content"],
        }
        for item in history
    ]

    # ========================================================
    # Build conversation
    # ========================================================

    messages = [
        SYSTEM_MESSAGE,
        *history,
        {
            "role": "user",
            "content": message,
        },
    ]

    # ========================================================
    # Agent Loop
    # ========================================================

    for step in range(10):

        print("\n" + "=" * 60, flush=True)
        print(f"Agent step: {step + 1}", flush=True)
        print("=" * 60, flush=True)

        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=messages,
            tools=tools,
            tool_choice="auto",
        )

        assistant_message = response.choices[0].message
        finish_reason = response.choices[0].finish_reason

        print(
            f"Finish reason: {finish_reason}",
            flush=True,
        )

        # ====================================================
        # No tool call -> final answer
        # ====================================================

        if not assistant_message.tool_calls:

            answer = assistant_message.content or ""

            print("\nFinal answer:", flush=True)
            print(answer, flush=True)

            return answer

        # ====================================================
        # Tool calls detected
        # ====================================================

        print(
            f"\nTool calls detected: "
            f"{len(assistant_message.tool_calls)}",
            flush=True,
        )

        # Add assistant tool-call message
        messages.append(assistant_message)

        # ====================================================
        # Execute tools
        # ====================================================

        tool_results = handle_tool_call(
            assistant_message.tool_calls
        )

        # Add tool results to conversation
        messages.extend(tool_results)

    # ========================================================
    # Maximum agent steps reached
    # ========================================================

    print(
        "\nAgent stopped: maximum steps reached.",
        flush=True,
    )

    return (
        "I couldn't complete the travel request within "
        "the allowed number of steps."
    )


# ============================================================
# Gradio App
# ============================================================

if __name__ == "__main__":

    demo = gr.ChatInterface(
        fn=chat,
        examples=EXAMPLES,
        title="Travel Helper",
        description=(
            "Your AI travel assistant for destination research, "
            "trip planning, travel information, and current weather."
        ),
        chatbot=gr.Chatbot(
            show_label=False,
            height=480,
        ),
    )

    # ========================================================
    # Launch
    # ========================================================

    demo.launch(
        css=CSS,
        js=JS,
        theme=gr.themes.Base(),
    )