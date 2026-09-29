"""Premium futuristic styling constants for the Travel Helper Gradio app."""


# ============================================================
# Theme
# ============================================================

CYAN = "#00F5FF"
BLUE = "#3B82F6"
PURPLE = "#A855F7"
PINK = "#EC4899"

BG = "#05070D"
SURFACE = "#0A0F1A"
SURFACE_2 = "#101827"
SURFACE_3 = "#151E2E"

BORDER = "#1D2A3D"
BORDER_STRONG = "#30415C"

TEXT = "#F8FAFC"
MUTED = "#94A3B8"


# ============================================================
# Example Prompts
# ============================================================

EXAMPLES = [
    "Plan a 7-day trip to Japan.",
    "What are the best attractions in Paris?",
    "What is the current weather in Tokyo?",
    "What should I know before traveling to Egypt?",
    "Compare Kyoto and Osaka for a short trip.",
]


# ============================================================
# CSS
# ============================================================

CSS = r"""
/* ============================================================
   ROOT / DESIGN TOKENS
   ============================================================ */

:root {
    --travel-cyan: #00F5FF;
    --travel-blue: #3B82F6;
    --travel-purple: #A855F7;
    --travel-pink: #EC4899;

    --travel-bg: #05070D;
    --travel-surface: #0A0F1A;
    --travel-surface-2: #101827;
    --travel-surface-3: #151E2E;

    --travel-border: #1D2A3D;
    --travel-border-strong: #30415C;

    --travel-text: #F8FAFC;
    --travel-muted: #94A3B8;

    --travel-glow-cyan:
        0 0 30px rgba(0, 245, 255, 0.10);

    --travel-glow-purple:
        0 0 30px rgba(168, 85, 247, 0.12);
}


/* ============================================================
   GLOBAL
   ============================================================ */

html,
body,
gradio-app {
    background:
        radial-gradient(
            circle at 15% 10%,
            rgba(0, 245, 255, 0.055),
            transparent 28%
        ),
        radial-gradient(
            circle at 85% 15%,
            rgba(168, 85, 247, 0.065),
            transparent 30%
        ),
        radial-gradient(
            circle at 50% 100%,
            rgba(59, 130, 246, 0.045),
            transparent 35%
        ),
        var(--travel-bg) !important;

    color: var(--travel-text) !important;
}


body {
    margin: 0 !important;

    font-family:
        Inter,
        -apple-system,
        BlinkMacSystemFont,
        "Segoe UI",
        sans-serif !important;
}


/* ============================================================
   HIDE GRADIO BRANDING
   ============================================================ */

footer,
.built-with,
.show-api,
.api-docs {
    display: none !important;
}


/* ============================================================
   MAIN CONTAINER
   ============================================================ */

.gradio-container {
    width: 100% !important;
    max-width: 1050px !important;
    min-width: 0 !important;

    margin: 0 auto !important;
    padding: 34px 24px 55px !important;

    background: transparent !important;
    color: var(--travel-text) !important;
}


.gradio-container .main,
.gradio-container .contain,
.gradio-container .wrap {
    width: 100% !important;
    max-width: 100% !important;
    min-width: 0 !important;
}


.gradio-container * {
    min-width: 0;
}


/* ============================================================
   HEADER
   ============================================================ */

.gradio-container h1 {
    position: relative;

    margin: 5px 0 12px !important;
    padding-left: 20px !important;

    color: #FFFFFF !important;

    font-size: 32px !important;
    font-weight: 800 !important;
    line-height: 1.15 !important;

    letter-spacing: -0.04em !important;

    text-align: left !important;

    text-shadow:
        0 0 25px rgba(0, 245, 255, 0.12);
}


/* Gradient accent bar */

.gradio-container h1::before {
    content: "";

    position: absolute;

    left: 0;
    top: 2px;
    bottom: 2px;

    width: 4px;

    border-radius: 10px;

    background:
        linear-gradient(
            180deg,
            var(--travel-cyan),
            var(--travel-blue),
            var(--travel-purple)
        );

    box-shadow:
        0 0 15px rgba(0, 245, 255, 0.45),
        0 0 25px rgba(168, 85, 247, 0.25);
}


/* ============================================================
   GLOBAL BLOCKS
   ============================================================ */

.block,
.form {
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
}


/* ============================================================
   CHATBOT
   ============================================================ */

.chatbot,
.chatbot.block {
    min-height: 520px !important;

    background:
        linear-gradient(
            180deg,
            rgba(255, 255, 255, 0.018),
            rgba(255, 255, 255, 0)
        ),
        linear-gradient(
            135deg,
            rgba(0, 245, 255, 0.018),
            transparent 35%,
            rgba(168, 85, 247, 0.025)
        ),
        var(--travel-surface) !important;

    border: 1px solid var(--travel-border) !important;

    border-radius: 18px !important;

    box-shadow:
        0 25px 70px rgba(0, 0, 0, 0.35),
        inset 0 1px 0 rgba(255, 255, 255, 0.025) !important;

    overflow: hidden !important;
}


/* ============================================================
   CHATBOT HEADER
   ============================================================ */

.chatbot > .block-label,
.chatbot > label,
.chatbot .label-wrap,
.chatbot .block-label,
.chatbot > .label-container {
    display: none !important;
}


/* ============================================================
   PLACEHOLDER
   ============================================================ */

.chatbot .placeholder,
.chatbot .placeholder * {
    color: var(--travel-muted) !important;
}


/* ============================================================
   MESSAGE ROWS
   ============================================================ */

.message-row,
.message-row > div,
.message-row .role,
.message-wrap,
.bubble-wrap {
    background: transparent !important;

    border: none !important;

    box-shadow: none !important;
}


/* ============================================================
   MESSAGE BUBBLES
   ============================================================ */

.message-row .message,
.message-row .message-bubble,
.message-row .bubble {
    padding: 11px 14px !important;

    border-radius: 13px !important;

    border: 1px solid transparent !important;

    box-shadow: none !important;

    font-size: 14px !important;
    line-height: 1.65 !important;
}


/* ============================================================
   USER MESSAGE
   ============================================================ */

.message-row.user-row .message,
.message-row.user-row .message-bubble,
.message-row.user-row .bubble,
.message-row[data-role="user"] .message,
.message-row[data-role="user"] .message-bubble,
.message-row[data-role="user"] .bubble {

    background:
        linear-gradient(
            135deg,
            rgba(59, 130, 246, 0.95),
            rgba(37, 99, 235, 0.95)
        ) !important;

    color: #FFFFFF !important;

    border:
        1px solid rgba(96, 165, 250, 0.35) !important;

    box-shadow:
        0 8px 25px rgba(37, 99, 235, 0.16) !important;
}


/* ============================================================
   ASSISTANT MESSAGE
   ============================================================ */

.message-row.bot-row .message,
.message-row.bot-row .message-bubble,
.message-row.bot-row .bubble,
.message-row[data-role="assistant"] .message,
.message-row[data-role="assistant"] .message-bubble,
.message-row[data-role="assistant"] .bubble {

    background:
        linear-gradient(
            135deg,
            rgba(16, 24, 39, 0.96),
            rgba(21, 30, 46, 0.96)
        ) !important;

    color: var(--travel-text) !important;

    border:
        1px solid rgba(168, 85, 247, 0.18) !important;

    box-shadow:
        0 8px 25px rgba(0, 0, 0, 0.18) !important;

    position: relative;
}


/* Assistant glow accent */

.message-row.bot-row .message::before,
.message-row[data-role="assistant"] .message::before {
    content: "";

    position: absolute;

    left: -1px;
    top: 12px;
    bottom: 12px;

    width: 3px;

    border-radius: 5px;

    background:
        linear-gradient(
            180deg,
            var(--travel-cyan),
            var(--travel-purple)
        );

    box-shadow:
        0 0 12px rgba(0, 245, 255, 0.35);
}


/* ============================================================
   REMOVE NESTED BORDERS
   ============================================================ */

.message-row .message .message,
.message-row .message .bubble,
.message-row .message .message-bubble,
.message-row .bubble .message,
.message-row .bubble .bubble,
.message-row .bubble .message-bubble,
.message-row .message-bubble .message,
.message-row .message-bubble .bubble,
.message-row .message-bubble .message-bubble {
    border-left: none !important;
}


/* ============================================================
   MESSAGE TYPOGRAPHY
   ============================================================ */

.message-row .message p,
.message-row .message-bubble p,
.message-row .bubble p,
.message-row .prose p {

    margin: 0 0 8px !important;

    color: inherit !important;

    font-size: 14px !important;
    line-height: 1.65 !important;
}


.message-row .message p:last-child,
.message-row .message-bubble p:last-child,
.message-row .bubble p:last-child,
.message-row .prose p:last-child {
    margin-bottom: 0 !important;
}


.message-row .message *,
.message-row .message-bubble *,
.message-row .bubble * {
    box-shadow: none !important;
    color: inherit !important;
}


/* ============================================================
   LINKS
   ============================================================ */

.message-row .message a,
.message-row .message-bubble a,
.message-row .bubble a {

    color: var(--travel-cyan) !important;

    text-decoration: none !important;

    border-bottom:
        1px solid rgba(0, 245, 255, 0.35);

    transition:
        color 0.2s ease,
        border-color 0.2s ease;
}


.message-row .message a:hover,
.message-row .message-bubble a:hover,
.message-row .bubble a:hover {

    color: #FFFFFF !important;

    border-color: var(--travel-cyan);
}


/* ============================================================
   CODE BLOCKS
   ============================================================ */

.message-row pre {
    background: #050912 !important;

    border:
        1px solid var(--travel-border) !important;

    border-radius: 10px !important;

    padding: 13px !important;

    overflow-x: auto !important;
}


.message-row code {
    color: #67E8F9 !important;

    font-family:
        "JetBrains Mono",
        "SF Mono",
        Menlo,
        monospace !important;
}


/* ============================================================
   INPUT AREA
   ============================================================ */

.input-row,
.gr-input-row,
.chat-input-row,
form[class*="input"] {
    align-items: stretch !important;
}


/* ============================================================
   TEXT INPUT
   ============================================================ */

textarea,
input[type="text"] {

    min-height: 52px !important;

    padding: 14px 16px !important;

    background:
        linear-gradient(
            180deg,
            rgba(255, 255, 255, 0.015),
            rgba(255, 255, 255, 0)
        ),
        var(--travel-surface) !important;

    border:
        1px solid var(--travel-border) !important;

    border-radius: 13px !important;

    color: var(--travel-text) !important;

    font-family:
        Inter,
        -apple-system,
        BlinkMacSystemFont,
        "Segoe UI",
        sans-serif !important;

    font-size: 14px !important;

    line-height: 1.5 !important;

    transition:
        border-color 0.2s ease,
        box-shadow 0.2s ease,
        background 0.2s ease !important;
}


/* ============================================================
   INPUT FOCUS
   ============================================================ */

textarea:focus,
input[type="text"]:focus {

    border-color: var(--travel-cyan) !important;

    outline: none !important;

    background:
        rgba(8, 15, 25, 0.98) !important;

    box-shadow:
        0 0 0 1px rgba(0, 245, 255, 0.55),
        0 0 25px rgba(0, 245, 255, 0.08) !important;
}


textarea::placeholder,
input::placeholder {
    color: #64748B !important;
}


/* ============================================================
   BUTTONS
   ============================================================ */

button {

    min-height: 48px !important;

    padding: 0 17px !important;

    background:
        rgba(10, 15, 26, 0.85) !important;

    border:
        1px solid var(--travel-border) !important;

    border-radius: 11px !important;

    color: var(--travel-text) !important;

    font-family:
        Inter,
        -apple-system,
        BlinkMacSystemFont,
        "Segoe UI",
        sans-serif !important;

    font-size: 12px !important;

    font-weight: 650 !important;

    letter-spacing: 0.02em !important;

    cursor: pointer !important;

    transition:
        transform 0.2s ease,
        background 0.2s ease,
        color 0.2s ease,
        border-color 0.2s ease,
        box-shadow 0.2s ease !important;
}


button:hover {

    border-color:
        rgba(0, 245, 255, 0.55) !important;

    color: var(--travel-cyan) !important;

    background:
        rgba(0, 245, 255, 0.045) !important;

    transform: translateY(-1px);

    box-shadow:
        0 7px 22px rgba(0, 0, 0, 0.20);
}


/* ============================================================
   PRIMARY / SEND BUTTON
   ============================================================ */

button.primary,
button[variant="primary"],
button.submit,
button.submit-button,
.submit-button,
button.lg.primary {

    min-height: 52px !important;

    padding: 0 19px !important;

    background:
        linear-gradient(
            135deg,
            var(--travel-cyan),
            var(--travel-blue)
        ) !important;

    border:
        1px solid rgba(0, 245, 255, 0.8) !important;

    border-radius: 12px !important;

    color: #031014 !important;

    font-weight: 800 !important;

    box-shadow:
        0 8px 25px rgba(0, 245, 255, 0.13) !important;
}


button.primary:hover,
button[variant="primary"]:hover,
button.submit:hover,
button.submit-button:hover,
.submit-button:hover,
button.lg.primary:hover {

    background:
        linear-gradient(
            135deg,
            #67F8FF,
            #60A5FA
        ) !important;

    border-color:
        #67F8FF !important;

    color: #02070A !important;

    transform:
        translateY(-2px) !important;

    box-shadow:
        0 12px 30px rgba(0, 245, 255, 0.22) !important;
}


/* ============================================================
   SEND ICON
   ============================================================ */

button.submit svg,
button.submit-button svg,
.submit-button svg,
button.primary svg,
button[variant="primary"] svg {

    width: 18px !important;
    height: 18px !important;

    margin: 0 !important;

    color: #031014 !important;

    fill: currentColor !important;
    stroke: currentColor !important;
}


/* ============================================================
   EXAMPLES
   ============================================================ */

.examples,
.examples-holder,
[data-testid="examples"] {

    margin-top: 18px !important;

    padding: 0 !important;

    background: transparent !important;
}


.examples table,
.examples-table {

    background: transparent !important;

    border: none !important;
}


/* ============================================================
   EXAMPLE BUTTONS
   ============================================================ */

.examples button,
.example,
.examples td button,
[data-testid="examples"] button {

    min-height: 0 !important;

    padding: 11px 14px !important;

    background:
        linear-gradient(
            135deg,
            rgba(16, 24, 39, 0.92),
            rgba(10, 15, 26, 0.92)
        ) !important;

    border:
        1px solid var(--travel-border) !important;

    border-radius: 10px !important;

    color: #AAB6C6 !important;

    font-family:
        Inter,
        -apple-system,
        BlinkMacSystemFont,
        "Segoe UI",
        sans-serif !important;

    font-size: 12.5px !important;

    font-weight: 450 !important;

    letter-spacing: 0 !important;

    text-transform: none !important;

    text-align: left !important;

    transition:
        color 0.2s ease,
        border-color 0.2s ease,
        background 0.2s ease,
        transform 0.2s ease !important;
}


.examples button:hover,
.example:hover,
[data-testid="examples"] button:hover {

    background:
        linear-gradient(
            135deg,
            rgba(0, 245, 255, 0.055),
            rgba(168, 85, 247, 0.055)
        ) !important;

    border-color:
        rgba(0, 245, 255, 0.45) !important;

    color:
        var(--travel-cyan) !important;

    transform:
        translateY(-2px) !important;

    box-shadow:
        0 8px 25px rgba(0, 0, 0, 0.18);
}


/* ============================================================
   ICON BUTTONS
   ============================================================ */

.icon-button,
.chatbot .icon-button {

    min-height: 0 !important;

    padding: 6px !important;

    background: transparent !important;

    border: none !important;

    color: var(--travel-muted) !important;
}


.icon-button:hover,
.chatbot .icon-button:hover {

    background:
        rgba(0, 245, 255, 0.06) !important;

    border: none !important;

    color: var(--travel-cyan) !important;

    box-shadow: none !important;

    transform: none !important;
}


/* ============================================================
   SCROLLBAR
   ============================================================ */

::-webkit-scrollbar {
    width: 8px;
    height: 8px;
}


::-webkit-scrollbar-track {
    background: #05070D;
}


::-webkit-scrollbar-thumb {

    background:
        linear-gradient(
            180deg,
            var(--travel-blue),
            var(--travel-purple)
        );

    border-radius: 20px;
}


::-webkit-scrollbar-thumb:hover {
    background: var(--travel-cyan);
}


/* ============================================================
   TEXT SELECTION
   ============================================================ */

::selection {

    background:
        rgba(0, 245, 255, 0.85);

    color: #031014;
}


/* ============================================================
   MOBILE
   ============================================================ */

@media (max-width: 640px) {

    .gradio-container {
        padding: 24px 13px 36px !important;
    }


    .gradio-container h1 {
        font-size: 25px !important;
    }


    .chatbot,
    .chatbot.block {
        min-height: 440px !important;

        border-radius: 14px !important;
    }


    textarea,
    input[type="text"] {
        font-size: 13px !important;

        border-radius: 11px !important;
    }


    button.primary,
    button.submit,
    button.submit-button {
        border-radius: 11px !important;
    }


    .examples button,
    .example,
    [data-testid="examples"] button {
        font-size: 12px !important;
    }
}
"""


# ============================================================
# JavaScript
# ============================================================

JS = r"""
() => {

    /* ========================================================
       Browser tab title
       ======================================================== */

    document.title = "Travel Helper | AI Travel Assistant";


    /* ========================================================
       Focus chat input
       ======================================================== */

    const focusInput = () => {

        const areas =
            document.querySelectorAll("textarea");

        if (areas.length > 0) {

            const area =
                areas[areas.length - 1];

            if (
                !area.disabled &&
                !area.readOnly
            ) {
                area.focus();
            }
        }
    };


    /* Initial focus */

    setTimeout(
        focusInput,
        500
    );


    /* ========================================================
       Watch textarea state
       ======================================================== */

    const watchTextarea = (area) => {

        if (area.dataset.travelWatched) {
            return;
        }

        area.dataset.travelWatched = "1";

        let wasDisabled =
            area.disabled ||
            area.readOnly;


        const observer =
            new MutationObserver(() => {

                const isDisabled =
                    area.disabled ||
                    area.readOnly;


                /*
                 * Gradio disables the input
                 * while the agent is generating.
                 *
                 * Automatically restore focus
                 * when the input becomes available.
                 */

                if (
                    wasDisabled &&
                    !isDisabled
                ) {

                    setTimeout(
                        () => area.focus(),
                        80
                    );
                }


                wasDisabled =
                    isDisabled;
            });


        observer.observe(
            area,
            {
                attributes: true,

                attributeFilter: [
                    "disabled",
                    "readonly"
                ]
            }
        );
    };


    /* ========================================================
       Scan for textareas
       ======================================================== */

    const scan = () => {

        document
            .querySelectorAll("textarea")
            .forEach(watchTextarea);
    };


    /* Initial scan */

    setTimeout(
        scan,
        600
    );


    /* ========================================================
       Watch Gradio dynamic DOM
       ======================================================== */

    new MutationObserver(scan)
        .observe(
            document.body,
            {
                childList: true,
                subtree: true
            }
        );
}
"""

