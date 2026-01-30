"""
Gradio UI for RAG Chatbot - ChatGPT Dark Mode Style
"""
import gradio as gr
import requests
import json
from typing import List, Tuple

# Backend API URL
BACKEND_URL = "http://localhost:8000"


def format_sources(sources: List[dict]) -> str:
    """Format sources for display."""
    if not sources:
        return "\n\n*No sources found*"

    sources_text = "\n\n---\n\n**Sources:**\n\n"
    for i, source in enumerate(sources, 1):
        label = source.get('label', 'Unknown')
        entity_type = source.get('type', 'unknown')
        description = source.get('description', '')
        if len(description) > 200:
            description = description[:200] + "..."
        source_url = source.get('source_urls', 'N/A')

        sources_text += f"**{i}. {label}** *({entity_type})*\n"
        sources_text += f"{description}\n"
        sources_text += f"🔗 `{source_url}`\n\n"

    return sources_text


def chat(message: str, history: List[Tuple[str, str]], top_k: int, min_similarity: float) -> str:
    """Send message to backend and return response."""
    if not message.strip():
        return "Please enter a question."

    try:
        response = requests.post(
            f"{BACKEND_URL}/chat",
            json={
                "query": message,
                "top_k": top_k,
                "include_relationships": True,
                "min_similarity": min_similarity,
                "debug": False
            },
            timeout=30
        )

        if response.status_code == 200:
            data = response.json()
            answer = data.get('answer', 'No answer generated.')
            sources = data.get('sources', [])
            formatted_response = answer + format_sources(sources)
            return formatted_response
        else:
            error_detail = response.json().get('detail', 'Unknown error')
            return f"❌ Error: {error_detail}"

    except requests.exceptions.ConnectionError:
        return "❌ Cannot connect to backend API. Please ensure the FastAPI server is running on http://localhost:8000"
    except requests.exceptions.Timeout:
        return "❌ Request timed out. The query took too long to process."
    except Exception as e:
        return f"❌ Unexpected error: {str(e)}"


def check_backend_health() -> str:
    """Check if backend is healthy."""
    try:
        response = requests.get(f"{BACKEND_URL}/health", timeout=5)
        if response.status_code == 200:
            return "🟢"
        else:
            return "🟡"
    except:
        return "🔴"


# Example queries
EXAMPLES = [
    ["What is driving growth in the Asia Pacific toys market?"],
    ["Tell me about the kidults consumer segment"],
    ["What trends are affecting traditional toys and games?"],
    ["How is China's toys and games market performing?"],
]

# ChatGPT Dark Mode CSS
custom_css = """
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

/* Root Variables - ChatGPT Dark Theme */
:root {
    --bg-primary: #1e1e1e;
    --bg-secondary: #212121;
    --bg-tertiary: #2f2f2f;
    --text-primary: #ececec;
    --text-secondary: #b4b4b4;
    --text-tertiary: #8e8ea0;
    --border-color: #3f3f3f;
    --accent: #19c37d;
    --input-bg: #2f2f2f;
}

/* Global Reset */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: 'Inter', -apple-system, sans-serif !important;
}

/* Main Container */
body, .gradio-container {
    background: var(--bg-primary) !important;
    color: var(--text-primary) !important;
}

.gradio-container {
    max-width: 100% !important;
    padding: 0 !important;
}

/* Header Area */
.header-container {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    height: 60px;
    background: var(--bg-primary);
    border-bottom: 1px solid var(--border-color);
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 1rem;
    z-index: 100;
}

/* Remove default Gradio styling */
.block {
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
    padding: 0 !important;
}

/* Main Content - Centered */
.main-content {
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 2rem;
}

/* Empty State Text */
.empty-state {
    text-align: center;
    color: var(--text-primary);
    font-size: 2rem;
    font-weight: 500;
    margin-bottom: 2rem;
    letter-spacing: -0.02em;
}

/* Chatbot Container */
#chatbot {
    width: 100%;
    max-width: 900px;
    margin: 0 auto;
    background: var(--bg-primary) !important;
    border: none !important;
    border-radius: 0 !important;
    padding: 2rem 1rem !important;
}

/* Chat Messages */
.message {
    background: transparent !important;
    padding: 1.5rem 0 !important;
    border: none !important;
    color: var(--text-primary) !important;
}

.message.user {
    background: var(--bg-secondary) !important;
    padding: 1.5rem !important;
    border-radius: 1rem !important;
    margin: 0.5rem 0 !important;
}

.message.bot {
    background: transparent !important;
    padding: 1.5rem 0 !important;
}

/* Input Container - Centered Large Bar */
.input-container {
    position: fixed;
    bottom: 2rem;
    left: 50%;
    transform: translateX(-50%);
    width: 90%;
    max-width: 700px;
    z-index: 50;
}

/* Input Field - ChatGPT Style */
textarea, input[type="text"] {
    background: var(--input-bg) !important;
    border: 1px solid var(--border-color) !important;
    border-radius: 1.5rem !important;
    color: var(--text-primary) !important;
    padding: 1rem 3.5rem 1rem 3rem !important;
    font-size: 1rem !important;
    line-height: 1.5 !important;
    resize: none !important;
    min-height: 52px !important;
    max-height: 200px !important;
    box-shadow: 0 0 0 1px var(--border-color), 0 2px 12px rgba(0,0,0,0.3) !important;
    transition: all 0.2s ease !important;
}

textarea:focus, input[type="text"]:focus {
    outline: none !important;
    border-color: var(--border-color) !important;
    box-shadow: 0 0 0 2px var(--border-color), 0 4px 16px rgba(0,0,0,0.4) !important;
}

textarea::placeholder, input::placeholder {
    color: var(--text-tertiary) !important;
}

/* Buttons */
button {
    background: transparent !important;
    border: none !important;
    color: var(--text-secondary) !important;
    font-weight: 500 !important;
    border-radius: 0.5rem !important;
    padding: 0.75rem 1rem !important;
    transition: all 0.2s ease !important;
    cursor: pointer !important;
}

button:hover {
    background: var(--bg-tertiary) !important;
    color: var(--text-primary) !important;
}

button[variant="primary"] {
    background: var(--accent) !important;
    color: white !important;
    font-weight: 600 !important;
}

button[variant="primary"]:hover {
    background: #16a068 !important;
}

/* Send Button - Circular Icon Style */
.send-btn {
    position: absolute !important;
    right: 0.5rem !important;
    bottom: 0.5rem !important;
    width: 36px !important;
    height: 36px !important;
    border-radius: 50% !important;
    background: var(--text-primary) !important;
    color: var(--bg-primary) !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    padding: 0 !important;
}

.send-btn:hover {
    background: var(--text-secondary) !important;
}

/* Examples Grid */
.examples-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 0.75rem;
    max-width: 700px;
    margin: 2rem auto;
}

.example-btn {
    background: var(--bg-tertiary) !important;
    border: 1px solid var(--border-color) !important;
    border-radius: 0.75rem !important;
    padding: 1rem !important;
    text-align: left !important;
    color: var(--text-secondary) !important;
    font-size: 0.9rem !important;
    line-height: 1.4 !important;
    transition: all 0.2s ease !important;
}

.example-btn:hover {
    background: var(--bg-secondary) !important;
    border-color: var(--text-tertiary) !important;
    color: var(--text-primary) !important;
}

/* Settings Accordion */
.accordion {
    background: var(--bg-secondary) !important;
    border: 1px solid var(--border-color) !important;
    border-radius: 0.75rem !important;
    margin: 1rem 0 !important;
    max-width: 700px !important;
}

.accordion summary {
    color: var(--text-secondary) !important;
    padding: 1rem !important;
    cursor: pointer !important;
}

/* Sliders */
input[type="range"] {
    accent-color: var(--accent) !important;
}

.slider-container {
    background: var(--bg-tertiary) !important;
    border-radius: 0.5rem !important;
    padding: 1rem !important;
}

/* Labels */
label {
    color: var(--text-secondary) !important;
    font-size: 0.9rem !important;
    font-weight: 500 !important;
}

/* Scrollbar */
::-webkit-scrollbar {
    width: 8px;
    height: 8px;
}

::-webkit-scrollbar-track {
    background: var(--bg-primary);
}

::-webkit-scrollbar-thumb {
    background: var(--bg-tertiary);
    border-radius: 4px;
}

::-webkit-scrollbar-thumb:hover {
    background: var(--border-color);
}

/* Status Indicator */
.status-indicator {
    position: fixed;
    top: 1rem;
    right: 1rem;
    font-size: 1.5rem;
    z-index: 1000;
}

/* Hide Gradio Branding */
.gradio-container .footer {
    display: none !important;
}

footer {
    display: none !important;
}

/* Markdown in responses */
.markdown-body {
    color: var(--text-primary) !important;
}

.markdown-body p {
    margin: 0.75rem 0 !important;
    line-height: 1.6 !important;
}

.markdown-body code {
    background: var(--bg-tertiary) !important;
    color: var(--accent) !important;
    padding: 0.2rem 0.4rem !important;
    border-radius: 0.25rem !important;
    font-size: 0.9em !important;
}

.markdown-body pre {
    background: var(--bg-tertiary) !important;
    border: 1px solid var(--border-color) !important;
    border-radius: 0.5rem !important;
    padding: 1rem !important;
    overflow-x: auto !important;
}

/* Mobile Responsive */
@media (max-width: 768px) {
    .examples-grid {
        grid-template-columns: 1fr;
    }

    .input-container {
        width: 95%;
        bottom: 1rem;
    }

    .empty-state {
        font-size: 1.5rem;
    }
}
"""

# Build ChatGPT-Style Interface
with gr.Blocks(
    title="Market Research Assistant",
    css=custom_css,
    theme=gr.themes.Base(
        primary_hue="emerald",
        neutral_hue="slate",
    )
) as demo:

    # Status Indicator
    with gr.Row(elem_classes="status-indicator"):
        status = gr.Textbox(
            value=check_backend_health(),
            show_label=False,
            container=False,
            interactive=False
        )

    # Main Chat Area
    with gr.Column():
        chatbot = gr.Chatbot(
            elem_id="chatbot",
            show_label=False,
            height=600,
            show_copy_button=True
        )

    # Input Section - Fixed at bottom
    with gr.Row(elem_classes="input-container"):
        with gr.Column(scale=1):
            msg = gr.Textbox(
                placeholder="Ask anything...",
                show_label=False,
                container=False,
                lines=1,
                max_lines=5
            )

    with gr.Row():
        with gr.Column(scale=1):
            submit_btn = gr.Button("Send ↑", variant="primary", size="sm")
            clear_btn = gr.Button("Clear", variant="secondary", size="sm")

    # Examples
    with gr.Row(elem_classes="examples-grid"):
        gr.Examples(
            examples=EXAMPLES,
            inputs=msg,
            label="",
            examples_per_page=4
        )

    # Settings
    with gr.Accordion("⚙️ Settings", open=False, elem_classes="accordion"):
        with gr.Row():
            top_k_slider = gr.Slider(
                minimum=1,
                maximum=10,
                value=5,
                step=1,
                label="Number of sources",
                info="More sources = broader context"
            )
            similarity_slider = gr.Slider(
                minimum=0.0,
                maximum=1.0,
                value=0.05,
                step=0.05,
                label="Relevance threshold",
                info="Lower = more results"
            )

    # Event Handlers
    def respond(message, history, top_k, min_similarity):
        """Handle user message and get response."""
        response = chat(message, history, top_k, min_similarity)
        history.append((message, response))
        return "", history

    msg.submit(
        respond,
        inputs=[msg, chatbot, top_k_slider, similarity_slider],
        outputs=[msg, chatbot]
    )

    submit_btn.click(
        respond,
        inputs=[msg, chatbot, top_k_slider, similarity_slider],
        outputs=[msg, chatbot]
    )

    clear_btn.click(lambda: [], None, chatbot, queue=False)


if __name__ == "__main__":
    demo.launch(
        server_name="0.0.0.0",
        server_port=7860,
        share=False,
        show_error=True
    )
