print("Welcome to the SkyBerryBot!")
name = input("What is your name?")
print(f"Welcome {name}! How can I help you today?\n")
while True:
    print("Please choose from the following options:\n1. Track my order\n2. Report a late / missing order\n3. Update delivery instructions\n4. Exit the chat")
    choice = input("Enter the number of your choice: ")

    if choice == "1":
        order = input("Please enter your order number (e.g., A123): ")
        print(f"Checking order {order}... 🚗 \nYour order is currently OUT FOR DELIVERY. Estimated arrival: 15-25 minutes. \n")

    elif choice == "2":
        order = input("Please enter your order number (e.g., A123): ")
        minutes = input("How many minutes passed since you ordered?")
        print(f"Okay, checking order {order}. \nWe're sorry your food hasn't arrived yet!🍕 \nWould you like to: \n  a) Re-deliver\n  b) Get a refund\n  c) Get store credit")
        choice2 = input("Enter a, b or c: ")
        if choice2 == "a":
            print("✅ A new delivery has been requested!")
        elif choice2 == "b":
            print("💳 Refund will be processed in 3-5 business days.") 
        else:
            print("🎟️ Store credit has been added yo your account.")
        print()  

    elif choice == "3":
        note = input("Enter new delivery note (e.g., 'Leave at door'): ")
        print(f"Got it! We'll tell your driver: {note}\n")

    elif choice == "4":
        print(f"Goodbye {name}! Have a nice meal!👋")
        break
    else:
        print("Invalid choice. Please enter 1, 2, 3 or 4.\n")