# SkyBerryBot 🍓🤖  
A simple and interactive **food delivery chatbot simulation** built in Python.  
This bot allows users to **track orders**, **report late or missing orders**, and **update delivery instructions**.

---

## 🚀 Features
✔ Track your order status (preparing, packing, out-for-delivery, delivered)  
✔ Report a late or missing order  
✔ Automated responses based on wait time  
✔ Re-delivery, refund, or store credit options  
✔ Update delivery notes for the driver  
✔ Clean user interaction loop  
✔ Randomized responses for realism  

---

## 🧠 How It Works
The chatbot runs in the terminal and guides the user through several menu options:

### **1️⃣ Track My Order**
- User enters an order number  
- Bot randomly picks a status (preparing/packing/delivery/delivered)  
- Simulates loading using `time.sleep()`  

### **2️⃣ Report a Late / Missing Order**
- User enters order number + minutes since ordering  
- If minutes < THRESHOLD_TIME → “still preparing” message  
- If minutes == THRESHOLD_TIME → “almost there” message  
- If minutes > THRESHOLD_TIME → user chooses:
  - 🔁 Re-delivery  
  - 💳 Refund  
  - 🎟️ Store credit  

### **3️⃣ Update Delivery Instructions**
- User enters a new delivery note  
- Bot confirms the update  

### **4️⃣ Exit**
- Chatbot ends with a friendly goodbye message  

---

## 🛠 Technologies Used
- **Python 3**
- `random` — to generate order statuses  
- `time` — for timing delays  
- Terminal-based user input  

---

## 📌 Code Snippet (Main Logic)

```python
print("Welcome to the SkyBerryBot!")
name = input("What is your name?").capitalize()
print(f"Hey {name}! I'm here to make sure your food arrives hot and fresh!\n")

while True:
    print("Please choose from the following options:\n1. Track my order\n2. Report a late / missing order\n3. Update delivery instructions\n4. Exit the chat")
    choice = input("Enter the number of your choice: ")
