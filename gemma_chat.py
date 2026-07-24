import ollama

def ask_gemma(prompt):

    response = ollama.chat(
        model="gemma3:1b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]


question = input("You : ")

print(ask_gemma(question))