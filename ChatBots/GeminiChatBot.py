import google.generativeai as genai
API_KEY = "ENTER-YOUR-API-KEY"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-2.5-flash")
chat = model.start_chat()
print("Welcome to Gemini Chat-Bot !!!")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    response = chat.send_message(user_input)
    print("Gemini : ",response.text)

