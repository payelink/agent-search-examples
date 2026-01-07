from langchain.tools import tool


@tool
def summarize_text(text: str, style: str | None = None) -> str:
    """
    Use this tool to summarize a block of text.

    Args:
        text: The raw notes or text to summarize.
        style: Optional style hint (e.g., "bullets", "paragraph", "executive summary").

    Returns:
        A concise summary of the provided text, respecting the requested style when possible.
    """
    # This is a simple passthrough; the LLM instructions in the system prompt
    # control how the summary is produced. The tool exists to make the
    # summarization action explicit to the agent.
    header = "Summary"
    if style:
        header += f" ({style})"
    return f"{header}:\n\n{text}"


@tool
def extract_action_items(text: str) -> list[str]:
    """
    Extract action items from a block of notes.

    Args:
        text: The raw notes or meeting transcript.

    Returns:
        A list of action items as short, imperative sentences.
    """
    # In a real implementation, you might apply more structured parsing.
    # For now, this acts as a placeholder that can be improved later.
    # The LLM will decide how to call this tool based on the system prompt.
    # Here, we simply return an empty list to avoid hallucinating concrete tasks.
    return []


