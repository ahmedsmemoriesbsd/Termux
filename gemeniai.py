import requests
import json

# 🔐 Your Gemini API Key 👇🏻👇🏻👇🏻 (Generate from Google's AI Studio)
API_KEY = "PASTE_YOUR_API_KEY_HERE"

# 🌐 Gemini Endpoint
URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"

# 🧠 Headers
HEADERS = {
    "Content-Type": "application/json"
}

print("🔹 Chat with Gemini (Type 'exit' to stop) 🔹\n")

while True:
    user_input = input("You: ")  # 🎤 Taking user input

    if user_input.lower() in ["exit", "quit"]:  # ✌️ Exit condition
        print("👋 Exiting chat...")
        break

    data = {
        "contents": [{
            "parts": [{"text": user_input}]
        }]
    }

    # 🚀 Sending the request
    response = requests.post(URL, headers=HEADERS, data=json.dumps(data))

    # ✅ Handling response
    if response.status_code == 200:
        result = response.json()
        try:
            bot_response = result["candidates"][0]["content"]["parts"][0]["text"]
            print(f"Gemini: {bot_response}\n")
        except (KeyError, IndexError):
            print("❌ Error: Unexpected response format.\n")
    else:
        print(f"❌ API Error: {response.status_code} - {response.text}\n")
