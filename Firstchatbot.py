
# ------------------------------
# Gemini Chatbot - Beginner Friendly
# ------------------------------

import google.generativeai as genai

# 1️⃣ Configure your Google Gemini API key
# Replace "YOUR_API_KEY" with your actual API key from Google AI Studio
genai.configure(api_key="YOUR_API_KEY")
# 2️⃣ Load free-tier model
model = model = genai.GenerativeModel("models/gemini-2.5-flash")

print("Welcome to Gemini chatbot! Type 'exit' to quit.\n")

# Simple chat loop
while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    # Send a single string to Gemini
    prompt = f"You are a helpful assistant. User says: {user_input}"

    try:
        response = model.generate_content(prompt)
        bot_reply = response.text.strip()
        print("Bot:", bot_reply)

    except Exception as e:
        print("Error communicating with Gemini API:", e)
        print("Make sure your API key is correct and you have free quota left.")


  