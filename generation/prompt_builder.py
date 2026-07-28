from app.retrieval.search import SearchResult

SYSTEM_PROMPT = """
You are a helpful assistant.
Use only the provided context.
Don't make up answers.
If the answer isn't present, say you don't know.    
"""


def build_messages(question: str, search_results: list[SearchResult]):
    context = [result.text for result in search_results]

    context_text = "\n\n".join(context)

    user_prompt = f"""
        Context:

        {context_text}

        Question:

        {question}
    """
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_prompt},
    ]
    return messages
