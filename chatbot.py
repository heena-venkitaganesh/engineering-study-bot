import google.generativeai as genai

genai.configure(api_key="Insert your API key")

model = genai.GenerativeModel("gemini-2.5-flash")

print("📚 Engineering Study Buddy")
print("Type 'exit' to quit")

while True:
    user_input = input("\nYou: ")

    if user_input.lower() == "exit":
        print("Bot: Goodbye!")
        break

    prompt = f"""
You are an Engineering Study Buddy.

Help engineering students understand concepts clearly.

Rules:
- Explain in simple language.
- Give practical examples.
- Include formulas when needed.
- Be suitable for undergraduate engineering students.

Question:
{user_input}
"""

    try:
        response = model.generate_content(prompt)

        print("\nBot:")
        print(response.text)

    except Exception as e:
        print("Error:", e)
