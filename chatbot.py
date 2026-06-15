print("Welcome to AI Chatbot")
print("Type 'bye' to exit the chat.\n")

while True:
    user = input("You: ").lower()

    if user in ["hi", "hello", "hey"]:
        print("Bot: Hello! Nice to meet you.")

    elif user == "how are you":
        print("Bot: I am fine. Thanks for asking!")

    elif user == "your name":
        print("Bot: My name is AI Chatbot.")

    elif user == "what is ai":
        print("Bot: AI stands for Artificial Intelligence.")

    elif user == "who made you":
        print("Bot: I was created using Python programming.")

    elif user == "what can you do":
        print("Bot: I can answer simple predefined questions.")

    elif user == "python":
        print("Bot: Python is a popular programming language used for AI and software development.")

    elif user == "course":
        print("Bot: I am learning Artificial Intelligence.")

    elif user == "college":
        print("Bot: Please enter your college name.")

    elif user == "help":
        print("Bot: You can ask me about AI, Python, greetings, my name, and more.")

    elif user == "good morning":
        print("Bot: Good Morning! Have a wonderful day.")

    elif user == "good afternoon":
        print("Bot: Good Afternoon!")

    elif user == "good evening":
        print("Bot: Good Evening!")

    elif user == "good night":
        print("Bot: Good Night! Sweet dreams.")

    elif user == "thank you":
        print("Bot: You're welcome!")

    elif user == "add":
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print("Bot: Sum =", num1 + num2)

    elif user == "multiply":
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print("Bot: Product =", num1 * num2)

    elif user == "bye":
        print("Bot: Goodbye! Have a nice day.")
        break

    else:
        print("Bot: Sorry, I don't understand that question.")