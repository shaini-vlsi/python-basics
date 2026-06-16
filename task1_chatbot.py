def chatbot():
    print("🤖 Smart ChatBot")
    print("Type 'bye' to exit.\n")

    while True:
        user = input("You: ").lower().strip()

        if user in ["hello", "hi", "hey"]:
            print("Bot: Hello! Nice to meet you.")

        elif "name" in user:
            print("Bot: I am CodeAlpha Smart ChatBot.")

        elif "how are you" in user:
            print("Bot: I am doing great. Thanks for asking!")

        elif "course" in user:
            print("Bot: I can help with Python programming.")

        elif "time" in user:
            from datetime import datetime
            print("Bot: Current time is", datetime.now().strftime("%H:%M:%S"))

        elif user == "bye":
            print("Bot: Goodbye! Have a nice day.")
            break

        else:
          print("Bot: Sorry, I don't understand that.")

chatbot()
            print("Bot: Sorry, I don't understand that.")

chatbot()
