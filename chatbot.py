# Simple Rule-Based Chatbot
def chatbot():
    print("🤖 Chatbot: Hello! I'm your assistant. Type 'bye' to end the chat.")

    while True:
        user_input = input("You: ").lower()

        if user_input == "hello":
            print("Chatbot: Hi! How can I help you today?")
        elif user_input == "how are you":
            print("Chatbot: I'm just a program, but I'm doing great!")
        elif user_input == "what is your name":
            print("Chatbot: I'm PyBot, your chatbot assistant.")
        elif user_input == "bye":
            print("Chatbot: Goodbye! Have a nice day. 😊")
            break
        else:
            print("Chatbot: Sorry, I don't understand that.")

# Run the chatbot
chatbot()
