import google.generativeai as genai

genai.configure(api_key="Enter your API key")

model = genai.GenerativeModel("gemini-2.5-flash")
chat_history = []

print("📚 Engineering Study Buddy")
print("Type 'exit' to quit")

while True:
    user_input = input("\nYou: ")

    if user_input.lower() == "exit":
        print("Bot: Goodbye!")
        break

    chat_history.append(f"User: {user_input}")

    prompt = f"""
You are an Engineering Study Buddy.

Conversation History:
{chr(10).join(chat_history)}

Answer the latest question clearly.
Use simple language.
Use examples when possible.
Suitable for undergraduate engineering students.
"""

    try:
        response = model.generate_content(prompt)

        print("\nBot:")
        print(response.text)

        chat_history.append(f"Bot: {response.text}")

    except Exception as e:
        print("Error:", e)
