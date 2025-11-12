"""SkyBerryBot - A simple food delivery chatbot simulation.
This bot allows users to track orders, report issues, and update delivery instructions."""
import random, time
THRESHOLD_TIME = 30  # minutes

# ---Welcome message and user name input---
print("Welcome to the SkyBerryBot!") 
name = input("What is your name?").capitalize() 
print(f"Hey {name}! I'm here to make sure your food arrives hot and fresh!\n")

# ---Main interaction loop---
while True:
    print("Please choose from the following options:\n1. Track my order\n2. Report a late / missing order\n3. Update delivery instructions\n4. Exit the chat")
    choice = input("Enter the number of your choice: ")

    if choice == "1":
        # ---Track order status----
        order = input("Please enter your order number (e.g., A123): ").upper()
        statuses = [
           "Preparing your order 🍔 Estimated arrival: 15-25 minutes.", 
           "Order is being packed 📦 Estimated arrival: 10-15 minutes.", 
           "Out for delivery 🚗 Estimated arrival: 5-7 minutes.", 
           "Delivered ✅ Enjoy your meal!"
           ]
        status = random.choice(statuses)
        print(f"Checking order {order}... 🚗 ")
        time.sleep(2)
        print(f"{status}\n")

    elif choice == "2":

        # ---Get order number and time since order---
        order = input("Please enter your order number (e.g., A123): ").upper()
        minutes_raw = input("How many minutes passed since you ordered? ").strip()
        try:
           minutes = int(minutes_raw)
        except ValueError:
            print("Please enter a valid number (e.g., 25)\n")
            continue

        # ---Determine response based on time elapsed---
        if minutes < THRESHOLD_TIME:
            print(f"Your order {order} is still being prepared. Please allow more time for delivery. 🍔 \n")
            continue
        elif minutes == THRESHOLD_TIME:
            print(f"Your order {order} is almost there! Driver should arrive shortly. 🚗 \n")
            continue
        else:
            print(f"Okay, checking order {order}...")
            time.sleep(2)
            print(
               "We're sorry your food hasn't arrived yet! Your order was cancelled due to unforeseen circumstances.\n"
               "Would you like to:\n"
               "a) 🔁 Re-deliver the same items\n"
               "b) 💳 Full refund (3-5 business days)\n"
               "c) 🎟️ Store discount"
                )
               
            action = input("Please enter a, b, or c: ").lower()
            if action == "a": 
              print("✅ Re-delivery request submitted. Your food will arrive shortly!")
            elif action == "b": 
              print("✅ Refund initiated. You will receive your refund in 3-5 business days.")
            elif action == "c": 
              print("✅ Store credit has been applied to your account.")
            else:
              print("Invalid choice. Please enter a, b, or c.\n")
              continue

    # ---Update delivery instructions---
    elif choice == "3":
        note = input("Enter new delivery note (e.g., 'Leave at door'): ").strip()
        print(f"Got it! We'll tell your driver: {note}\n")

    # ---Exit chat---
    elif choice == "4":
        print(f"Thanks for chatting with me {name}! 🍟 Come back anytime!")
        break

    # ---Invalid choice handling---
    else:
        print("Invalid choice. Please enter 1, 2, 3 or 4.\n")