print("Welcome to the Elite101 Chatbot!")
name = input("What is your name?")
age = input("Hello" + name + ", how old are you?")
print(f"Welcome{name}! Oh to be{age} again! How can I help you today?\n")
while True:
    print("Please choose from the following options:\n1. Placeholder Option 1\n2. Placeholder Option 2\n3. Placeholder Option 3\n4. Exit the conversation")
    choice = input("Enter the number of your choice: ")
    if choice == "1":
        print("You selected Option 1.\n")
    elif choice == "2":
        print("You selected Option 2.\n")
    elif choice == "3":
        print("You selected Option 3.\n")
    elif choice == "4":
        print(f"Goodbye{name}! Have a great day!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, 3 or 4.\n")