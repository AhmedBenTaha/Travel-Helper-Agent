import json
import os
import requests

from functools import wraps
from pathlib import Path

from dotenv import load_dotenv
from tavily import TavilyClient


load_dotenv()


# ============================================================
# Configuration
# ============================================================

DATA_DIR = Path(__file__).resolve().parent / "data"

tavily_client = TavilyClient(
    api_key=os.getenv("TAVILY_API_KEY")
)


# ============================================================
# Custom @tool Decorator
# ============================================================

REGISTERED_TOOLS = {}


def tool(
    name: str,
    description: str,
    parameters: dict,
):
    """
    Register a Python function as an LLM tool.

    This is a lightweight custom decorator.
    It does not depend on Agno or another agent framework.
    """

    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        wrapper.tool_name = name
        wrapper.tool_description = description
        wrapper.tool_parameters = parameters

        REGISTERED_TOOLS[name] = wrapper

        return wrapper

    return decorator


# ============================================================
# Tool 1 — Web Search
# ============================================================

@tool(
    name="search_web",
    description=(
        "Search the web for current or general travel information "
        "about destinations, cities, countries, landmarks, "
        "travel activities, attractions, hotels, restaurants, "
        "and other travel-related topics. "
        "Use this tool when external web information is required."
    ),
    parameters={
        "type": "object",
        "properties": {
            "query": {
                "type": "string",
                "description": (
                    "A specific destination or travel-related "
                    "topic to search for on the web."
                ),
            },
        },
        "required": ["query"],
        "additionalProperties": False,
    },
)
def search_web(query: str) -> str:
    """
    Search the web for destination and travel information.
    """

    if not query or not query.strip():
        return "ERROR: Search query cannot be empty."

    try:
        response = tavily_client.search(
            query=query,
            search_depth="basic",
            max_results=5,
        )

        results = response.get("results", [])

        if not results:
            return f"No web results found for: {query}"

        output = []

        for result in results:
            output.append(
                f"Title: {result.get('title', 'N/A')}\n"
                f"Content: {result.get('content', 'N/A')}\n"
                f"URL: {result.get('url', 'N/A')}"
            )

        return "\n\n".join(output)

    except Exception as e:
        return f"Web search failed: {str(e)}"


# ============================================================
# Tool 2 — Local Travel Retrieval
# ============================================================

@tool(
    name="retrieve_travel_documents",
    description=(
        "Search the local travel knowledge base for relevant "
        "destination-specific information, transportation tips, "
        "planning advice, attractions, and other internal travel "
        "documents. "
        "Use this tool when information may exist in the local "
        "travel documents."
    ),
    parameters={
        "type": "object",
        "properties": {
            "query": {
                "type": "string",
                "description": (
                    "The travel question or topic to search "
                    "for in the local travel documents."
                ),
            },
        },
        "required": ["query"],
        "additionalProperties": False,
    },
)
def retrieve_travel_documents(query: str) -> str:
    """
    Search the local travel knowledge base
    using simple keyword matching.
    """

    if not query or not query.strip():
        return "ERROR: Retrieval query cannot be empty."

    query_words = set(query.lower().split())

    matches = []

    for file_path in DATA_DIR.glob("*.txt"):

        try:
            text = file_path.read_text(
                encoding="utf-8"
            )

            text_lower = text.lower()

            score = sum(
                1
                for word in query_words
                if len(word) > 2
                and word in text_lower
            )

            if score > 0:
                matches.append(
                    (
                        score,
                        file_path.name,
                        text,
                    )
                )

        except Exception as e:
            print(
                f"Could not read {file_path.name}: {e}",
                flush=True,
            )

    if not matches:
        return (
            f"No relevant travel information found "
            f"for: {query}"
        )

    matches.sort(
        key=lambda item: item[0],
        reverse=True,
    )

    output = []

    for score, filename, text in matches[:3]:
        output.append(
            f"Source: {filename}\n"
            f"Relevance score: {score}\n"
            f"Content:\n{text[:3000]}"
        )

    return "\n\n---\n\n".join(output)


# ============================================================
# Tool 3 — Weather
# ============================================================

@tool(
    name="get_weather",
    description=(
        "Get current weather information for a destination "
        "using its latitude and longitude. "
        "Use this tool when the user asks about current "
        "weather conditions."
    ),
    parameters={
        "type": "object",
        "properties": {
            "latitude": {
                "type": "number",
                "description": (
                    "Latitude of the destination "
                    "in decimal degrees."
                ),
            },
            "longitude": {
                "type": "number",
                "description": (
                    "Longitude of the destination "
                    "in decimal degrees."
                ),
            },
        },
        "required": [
            "latitude",
            "longitude",
        ],
        "additionalProperties": False,
    },
)
def get_weather(
    latitude: float,
    longitude: float,
) -> str:
    """
    Get current weather information using Open-Meteo.
    """

    try:
        response = requests.get(
            "https://api.open-meteo.com/v1/forecast",
            params={
                "latitude": latitude,
                "longitude": longitude,
                "current": (
                    "temperature_2m,"
                    "weather_code,"
                    "wind_speed_10m"
                ),
            },
            timeout=10,
        )

        response.raise_for_status()

        data = response.json()

        current = data.get("current")

        if not current:
            return (
                "Weather information was not available."
            )

        return (
            f"Temperature: "
            f"{current.get('temperature_2m')}°C\n"
            f"Weather code: "
            f"{current.get('weather_code')}\n"
            f"Wind speed: "
            f"{current.get('wind_speed_10m')} km/h"
        )

    except requests.RequestException as e:
        return (
            f"Weather request failed: {str(e)}"
        )


# ============================================================
# Generate OpenAI-Compatible Tool Schemas
# ============================================================

def get_tool_schemas() -> list[dict]:
    """
    Convert registered @tool functions into
    OpenAI-compatible tool schemas.
    """

    schemas = []

    for tool_name, function in REGISTERED_TOOLS.items():

        schemas.append(
            {
                "type": "function",
                "function": {
                    "name": function.tool_name,
                    "description": function.tool_description,
                    "parameters": function.tool_parameters,
                },
            }
        )

    return schemas


# ============================================================
# All Tools
# ============================================================

tools = get_tool_schemas()


# ============================================================
# Tool Call Handler
# ============================================================

def handle_tool_call(tool_calls):
    """
    Execute tool calls returned by the LLM.

    The LLM provides:
        - tool name
        - JSON arguments

    This function:
        1. Parses the arguments.
        2. Finds the registered tool.
        3. Executes the tool.
        4. Returns the result in OpenAI tool-message format.
    """

    results = []

    for tool_call in tool_calls:

        tool_name = tool_call.function.name

        # ----------------------------------------------------
        # Parse arguments
        # ----------------------------------------------------

        try:
            arguments = json.loads(
                tool_call.function.arguments
            )

        except json.JSONDecodeError as e:

            result = (
                "Tool arguments could not be parsed as JSON: "
                f"{str(e)}"
            )

            print(
                f"\nTool called: {tool_name}",
                flush=True,
            )

            print(
                f"Invalid arguments: "
                f"{tool_call.function.arguments}",
                flush=True,
            )

            results.append(
                {
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "name": tool_name,
                    "content": result,
                }
            )

            continue

        # ----------------------------------------------------
        # Trace
        # ----------------------------------------------------

        print(
            f"\nTool called: {tool_name}",
            flush=True,
        )

        print(
            "Arguments:",
            json.dumps(
                arguments,
                indent=2,
                ensure_ascii=False,
            ),
            flush=True,
        )

        # ----------------------------------------------------
        # Find Tool
        # ----------------------------------------------------

        tool_function = REGISTERED_TOOLS.get(
            tool_name
        )

        if tool_function is None:

            result = (
                f"Unknown tool: {tool_name}"
            )

        else:

            # ------------------------------------------------
            # Execute Tool
            # ------------------------------------------------

            try:
                result = tool_function(
                    **arguments
                )

            except Exception as e:

                result = (
                    f"Tool execution failed: "
                    f"{str(e)}"
                )

        # ----------------------------------------------------
        # Print Tool Result
        # ----------------------------------------------------

        print(
            "Tool result:",
            result,
            flush=True,
        )

        # ----------------------------------------------------
        # Return OpenAI-compatible tool message
        # ----------------------------------------------------

        results.append(
            {
                "role": "tool",
                "tool_call_id": tool_call.id,
                "name": tool_name,
                "content": str(result),
            }
        )

    return results

