import ollama

def generate_notes(topic):

    prompt = f"""
    Generate short study notes on:

    {topic}
    """

    response = ollama.chat(
        model='gemma3:1b',
        messages=[
            {
                'role':'user',
                'content':prompt
            }
        ]
    )

    return response['message']['content']