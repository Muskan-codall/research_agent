import ollama


def generate_notes(topic):

    prompt = f"""
    Generate short and easy-to-understand study notes on the following topic:

    {topic}
    """

    response = ollama.chat(
        model="gemma3b:1b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]