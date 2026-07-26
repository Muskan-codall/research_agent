import ollama

def summarize(text):

    prompt = f"Summarize this:\n{text}"

    response = ollama.chat(
        model='gemma3:1b',
        messages=[{'role':'user',
                   'content':prompt}]
    )

    return response['message']['content']