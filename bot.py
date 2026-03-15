print("AI Bot started. Type 'exit' to quit.")

while True:
    user = input("You: ")

    if user.lower() == "exit":
        print("Bot: Goodbye!")
        break

    responses = {
        "hello": "Hello! How can I help?",
        "name": "I am a simple AI bot created in Python.",
        "how are you": "I am running perfectly."
    }

    answered = False

    for key in responses:
        if key in user.lower():
            print("Bot:", responses[key])
            answered = True
            break

    if not answered:
        print("Bot: I don't understand yet.")