# import ollama

# def explain_code(code):

#     prompt = f"""
#     Explain the following Python code
#     in simple words.

#     {code}
#     """

#     response = ollama.chat(
#         model='gemma3:1b',
#         messages=[
#             {
#                 'role':'user',
#                 'content':prompt
#             }
#         ]
#     )

#     return response['message']['content']

import ollama


# Detect whether the user's input looks like source code.
def is_code(text):

    code_patterns = [

        # Python
        "def ",
        "import ",
        "print(",
        "class ",
        "return ",

        # C / C++
        "#include",
        "printf(",
        "scanf(",
        "cout",
        "cin",
        "using namespace",

        # Java
        "public class",
        "public static void main",
        "System.out.println",

        # JavaScript
        "function ",
        "console.log",
        "let ",
        "const ",
        "var ",

        # SQL
        "SELECT",
        "INSERT",
        "UPDATE",
        "DELETE",
        "CREATE TABLE",

        # HTML
        "<html>",
        "<body>",
        "<div>",
        "<head>",

        # Common symbols
        "{",
        "}",
        "()",
        ";",
        "[]",
        "return",
        "=>"
    ]

    count = 0

    for pattern in code_patterns:

        if pattern.lower() in text.lower():
            count += 1

    # Multi-line code generally contains '\n'
    if "\n" in text:
        count += 1

    return count >= 2


# Explain the code.
def explain_code(code):

    prompt = f"""

You are a Friendly Programming Tutor.

Your job is to explain source code in the easiest possible way.

IMPORTANT RULES:

1. Detect the programming language automatically.

2. Write the purpose of the code in only 1 or 2 lines.

3. Explain the code line by line OR group related lines together if required.

4. For EVERY explanation use the following format.


----------------------------------------------------

Programming Language:
<language name>

Purpose:
<1 or 2 lines>

----------------------------------------------------

For each line or group of lines:

Code:
<actual code>

Explanation:
<maximum 2 short lines>

Syntax Used:
- Mention the syntax.
- Explain what it does.

Real Life Example:
- Give a real life example whenever possible.

If no suitable example exists, write:
Not Applicable.

----------------------------------------------------


5. If libraries are imported, explain them separately.

6. If functions are used, explain them separately.

7. If variables are used, explain them separately.

8. Mention the expected output or behaviour of the program.

9. Mention any possible errors if present.

10. Give 2 or 3 short suggestions for improvement.

11. Never write lengthy paragraphs.

12. Keep explanations beginner friendly.

13. Use bullet points wherever possible.

14. Maximum explanation for one code block should be short and easy to understand.

15. Imagine that you are teaching a first-year college student.


Code to Explain:

{code}

"""

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