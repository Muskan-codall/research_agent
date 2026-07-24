from calculator import calculate
from gemma_chat import ask_gemma


while True:
    operators =["+","-","*","/","%","**"]
    user_input = input("You : ").lower()

    if any (op in user_input for op in operators):
        print("calculate:",calculate(user_input))   
    else:
        reply = ask_gemma(user_input)
        print("\nGemma :", reply)
