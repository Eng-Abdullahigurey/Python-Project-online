dress = ["Printed lawn suit", "T-shirt", "short", "Check shirt"]
stock = [1000, 250, 500, 450]
price = [5000, 1000, 2000, 2300]

print("Welcome 🛍😄")

while True:
    passChoice = int(input("1 for new account 🔐 \n2 for Login 🔑: "))
    
    if passChoice == 1:
        # create new account
        with open("userspass.txt", "a+") as file:
            file.seek(0)
            while True:
                username = input("Please enter username 😀: ")
                if username not in file.read():
                    break
                else:
                    print("Username has already taken ❌❗")
            password = input("Please enter password 🔑: ")
            file.write(username + "," + password + "\n")
    
    result = True
    while result:
        username = input("Please enter username 😀: ")
        password = input("Please enter password 🔑: ")
        with open("userspass.txt", "r") as fin:
            for line in fin:
                uname, pword = line.strip().split(",")
                if username == uname and password == pword:
                    print("✅ Valid password and username 👏")
                    result = False
                    break
            else:
                print("❌ Invalid Password or Username 😥\nTry again ⤴")

    # Shopping cart logic
    cart = []
    quantity = []
    totalBill = 0

    while True:
        action = int(input("\n1 for adding new item to cart 🛒\n2 for removing item from cart 🧾\n3 for checkout 💳: "))
        
        if action == 1:
            print("\nAvailable Items:")
            for i in range(len(dress)):
                print(f"{i+1}. {dress[i]} - Rs.{price[i]} (Stock: {stock[i]})")
            
            choice = int(input("Enter item number to add to cart: ")) - 1
            if 0 <= choice < len(dress):
                qty = int(input("Enter quantity: "))
                if qty <= stock[choice]:
                    cart.append(dress[choice])
                    quantity.append(qty)
                    totalBill += qty * price[choice]
                    stock[choice] -= qty
                    print(f"✅ {qty} x {dress[choice]} added to cart.")
                else:
                    print("❌ Not enough stock available.")
            else:
                print("❌ Invalid item selection.")
        
        elif action == 2:
            if not cart:
                print("🛒 Cart is empty!")
                continue
            print("\nItems in Cart:")
            for i in range(len(cart)):
                print(f"{i+1}. {cart[i]} - Qty: {quantity[i]}")
            remove_index = int(input("Enter item number to remove: ")) - 1
            if 0 <= remove_index < len(cart):
                totalBill -= quantity[remove_index] * price[dress.index(cart[remove_index])]
                stock[dress.index(cart[remove_index])] += quantity[remove_index]
                print(f"❌ Removed {cart[remove_index]} from cart.")
                cart.pop(remove_index)
                quantity.pop(remove_index)
            else:
                print("❌ Invalid index.")

        elif action == 3:
            print("\n🧾 Checkout Summary:")
            for i in range(len(cart)):
                print(f"{cart[i]} x {quantity[i]} = Rs.{quantity[i] * price[dress.index(cart[i])]}")
            print(f"Total Bill = Rs.{totalBill}")
            print("✅ Thank you for shopping with us! 🛍")
            break
        
        else:
            print("❌ Invalid action.")
    
    break  # End outermost while loop after checkout
