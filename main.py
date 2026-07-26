from tkinter import *
from calculator import calculate
from gemma_chat import ask_gemma
from notes_generator import generate_notes
from code_explainer import explain_code
from code_explainer import is_code
# from reminder_system import reminder
# from todo import add_task
# from translator import translate
root = Tk()

l1 =Label(text="you")
l1.pack()
t1 =Entry()
t1.pack()
l3 =Text()
l3.pack()



def show():
    user_input = t1.get()
    notes_keywords = [
                "notes",
                "note",
                "study material",
                "study notes",
                "short notes",
                "summary",
                "summarize",
                "summarise",
                "revision notes",
                "revision",
                "explanation",
                "explain",
                "material"
                ]
    if user_input.lower() == "exit":
        break
    
             
    elif any(op in user_input for op in ["+", "-", "*", "/", "%", "^", "(", ")"]):
    
        l3.config(text="\nAgent:\n")
        l3.config(text=calculate(user_input))
    
    
    elif any(keyword in user_input.lower() for keyword in notes_keywords):
        response = generate_notes(user_input)
        l3.config(text= response)
    elif is_code(user_input):
    
            l3.config(text="\nCode detected.")

            l3.config(text="\nPaste your complete code.")
            l3.config(text="Type END when finished.\n")

            code_lines = []

            while True:

                line = input()

                if line.upper() == "END":
                    break

                code_lines.append(line)

            code = "\n".join(code_lines)

            l3.config(text="\nAgent :\n")

            l3.config(text=explain_code(code))


    else:
        reply = ask_gemma(user_input)
        l3.config(text="\nGemma :", reply)

           

Button(text="enter",command=show).pack()
mainloop()