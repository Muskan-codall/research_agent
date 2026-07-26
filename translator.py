import ollama

def translate(text, language):

    prompt = f"""
    Translate the following text into {language}.

    Text:
    {text}
    """

    response = ollama.chat(
        model="gemma3",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]