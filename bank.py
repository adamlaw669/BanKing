import csv

users = {}

csv_file = 'user_db.csv'

def save_users_to_csv():
    with open(csv_file, 'a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["username", "password", "email", "bvn", "account_type", "balance"])
        #writer.writeheader()
        for username, user_data in users.items():
            writer.writerow({"username": username, **user_data})

def load_users_from_csv():
    try:
        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)
            if reader.fieldnames != ["username", "password", "email", "bvn", "account_type"]:
                print("CSV file has incorrect headers. Please fix the file.")
                return
            for row in reader:
                users[row['username']] = {
                    "password": row["password"],
                    "email": row["email"],
                    "bvn": row["bvn"],
                    "account_type": row["account_type"],
                    "balance": float(row["balance"])
                }
    except FileNotFoundError:
        print("CSV file not found. Starting with an empty database.")
    except Exception as e:
        print(f"An error occurred while loading users: {e}")


def signup():
    print("=== Signup ===")
    
    username = input("Enter a username: ")
    if username in users:
        print("Username already exists! Try a different one.")
        return
    
    while True:
        password = input("Enter a password: ")
        confirm_password = input("Confirm your password: ")
        if password == confirm_password:
            break
        else:
            print("Passwords do not match. Try again.")
    
    email_address = input("Enter a valid email address: ")
    if any(user['email'] == email_address for user in users.values()):
        print("Email address already exists! Try a different one.")
        return
    
    bvn = input("Enter your BVN: ")
    if any(user['bvn'] == bvn for user in users.values()):
        print("BVN already exists in an account! Try a different one.")
        return
    
    print("Choose account type:")
    print("1. Student account")
    print("2. Normal account")
    print("3. Business account")
    
    while True:
        try:
            choice = int(input("Enter your preferred choice: "))
            if choice in [1, 2, 3]:
                account_type = ["Student", "Normal", "Business"][choice - 1]
                print(f"You've successfully created your {account_type} account.")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    
    users[username] = {
        "password": password,
        "email": email_address,
        "bvn": bvn,
        "account_type": account_type,
        "balance": 0.00
    }
    save_users_to_csv()
    print(f"Account created successfully! You can now log in, {username}.")


def login():
    print("=== Login ===")
    username = input("Enter your username: ")
    
    if username in users:
        password = input("Enter your password: ")
        if users[username]["password"] == password:
            print(f"Login successful! Welcome back, {username}.")
            walp_menu(username)
        else:
            print("Incorrect password.")
    else:
        print("Username not found! Please sign up first.")


def walp_menu(username):
    
    while True:
        print("\n=== WALP Menu ===")
        print("1. Home Balance")
        print("2. Card")
        print("3. Send Money")
        print("4. Request Money")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        user_data = users[username]
        account_balance = user_data["balance"]

        if choice == "1":
            home_balance(username)
        elif choice == "2":
            get_card()
        elif choice == "3":
            account_balance = send_money(username, account_balance)
        elif choice == "4":
            account_balance = request_money(username, account_balance)
        elif choice == "5":
            print("Exiting WALP menu. Thank you!")
            break
        else:
            print("Invalid option. Please try again.")


def home_balance(username):
    while True:
        account_balance = users[username]["balance"]
        print(f"Account Balance: ${account_balance:.2f}")
        print("1. Add Cash                   2. Cash Out")
        print("3. Buy Bitcoin")
        print("4. Buy Stock")
        print("5. exit") 
        
        action = input("Choose an option: ")
        if action == "1":
            try:
                amount = float(input("Enter amount to add: "))
                account_balance += amount
                users[username]["balance"] = account_balance
                save_users_to_csv()
                print(f"Successfully added ${amount:.2f} to your account.")
            except ValueError:
                print("Invalid amount. Please enter a numeric value.")
        elif action == "2":
            amount = float(input("Enter amount to cash out: "))
            if amount <= account_balance:
                account_balance -= amount
                account_balance = users[username]["balance"]
                save_users_to_csv()
                print(f"Successfully cashed out ${amount:.2f}.")
            else:
                print("Insufficient funds.")
        elif action == "3":
            print("You chose to Buy Bitcoin.")
            buy_bitcoin = float(input("How much Bitcoin do you want to buy? "))
            if buy_bitcoin <= account_balance:
                account_balance -= buy_bitcoin
                account_balance = users[username]["balance"]
                save_users_to_csv()
                bitcoin_balance = buy_bitcoin / 100000
                print(f"You have successfully bought  ${buy_bitcoin:.2f} worth bitcoin.")
                print(f"Your current balance is ${account_balance:.2f}.")
                print(f"Your current bitcoin balance is {bitcoin_balance:.8f}BTC.")
                DO_YOU_WANT_TO_PERFORM_AN0THER_TRANSACATION = input("select an option between Y or y or N or n: ")
                if DO_YOU_WANT_TO_PERFORM_AN0THER_TRANSACATION == "Y" or DO_YOU_WANT_TO_PERFORM_AN0THER_TRANSACATION == "y":
                    continue
                else:
                    break

            else:
                print("Insufficient funds.")
        elif action == '4':
            print("You chose to Buy Stock.")
            buy_stock = float(input("How much Bitcoin do you want to buy? "))
            print("== chose your preferred currency ==")
            print("1. AUSD")
            print("2. NIG")
            print("3. JPN")
            print("4. SUD")

            currency = input("Select a currency (1-4): ")
            if currency == '1':
                amount = float(input("enter the amount: "))
                if amount <= account_balance:
                    account_balance -= amount
                    account_balance = users[username]["balance"]
                    save_users_to_csv()
                    AUSD = amount * 1.234
                    print(f"You have successfully bought ${amount:.2f} worth AUSD.")
                    print("You have successfully bought {AUSD:.8f}AUSD")
                    DO_YOU_WANT_TO_PERFORM_AN0THER_TRANSACATION = input("select an option between Y or y or N or n: ")
                    if DO_YOU_WANT_TO_PERFORM_AN0THER_TRANSACATION == "Y" or DO_YOU_WANT_TO_PERFORM_AN0THER_TRANSACATION == "y":
                        continue
                    else:
                        break
                else:
                    print("Insufficient funds.")   

            elif currency == '2':
                amount = float(input("enter the amount: "))
                if amount <= account_balance:
                    account_balance -= amount
                    account_balance = users[username]["balance"]
                    save_users_to_csv()  
                    NIG = amount * 1.356
                    print(f"You have successfully bought ${amount:.2f} worth NIG.")
                    print("You have successfully bought {NIG:.8f}NIG")
                    DO_YOU_WANT_TO_PERFORM_AN0THER_TRANSACATION = input("select an option between Y or y or N or n: ")
                    if DO_YOU_WANT_TO_PERFORM_AN0THER_TRANSACATION == "Y" or DO_YOU_WANT_TO_PERFORM_AN0THER_TRANSACATION == "y":
                        continue
                    else:
                        break
                else:
                    print("Insufficient funds.")

            elif currency == '3':
                amount = float(input("enter the amount: "))
                if amount <= account_balance:
                    account_balance -= amount
                    account_balance = users[username]["balance"]
                    save_users_to_csv() 
                    JPN = amount * 1.013
                    print(f"You have successfully bought ${amount:.2f} worth JPN.")
                    print("You have successfully bought {JPN:.8f}JPN")
                    DO_YOU_WANT_TO_PERFORM_AN0THER_TRANSACATION = input("select an option between Y or y or N or n: ")
                    if DO_YOU_WANT_TO_PERFORM_AN0THER_TRANSACATION == "Y" or DO_YOU_WANT_TO_PERFORM_AN0THER_TRANSACATION == "y":
                        continue
                    else:
                        break
                else:
                    print("Insufficient funds.")
                
            else:
                amount = float(input("enter the amount: "))
                if amount <= account_balance:
                    account_balance -= amount
                    account_balance = users[username]["balance"]
                    save_users_to_csv()  
                    SUD = amount * 0.650
                    print(f"You have successfully bought ${amount:.2f} worth SUD.")
                    print("You have successfully bought {SUD:.8f}SUD")
                    DO_YOU_WANT_TO_PERFORM_AN0THER_TRANSACATION = input("select an option between Y or y or N or n: ")
                    if DO_YOU_WANT_TO_PERFORM_AN0THER_TRANSACATION == "Y" or DO_YOU_WANT_TO_PERFORM_AN0THER_TRANSACATION == "y":
                        continue
                    else:
                        break
                else:
                    print("Insufficient funds.")
        elif action == '5':
            print("Existing to WALP menu......")
            break
        else:
            print("Invalid option.")

def get_card():
    choice = input("Do you want to get your free card? (Y/N): ").lower()
    if choice == 'y':
        address = input("Enter your home address: ")
        print(f"Your card will be delivered to {address} shortly.")
    elif choice == 'n':
        print("Thank you!")
    else:
        print("Invalid choice.")

def send_money(username, account_balance):
    amount = float(input("Enter amount to send: "))
    if amount <= account_balance:
        account_balance -= amount
        account_balance = users[username]["balance"]
        save_users_to_csv()
        receiver_name = input("Enter receiver name: ")
        print(f"Successfully sent ${amount:.2f} to {receiver_name}.")
    else:
        print("Insufficient funds.")
    return account_balance

def request_money(username, account_balance):
    amount = float(input("Enter amount to request: "))
    account_balance += amount
    account_balance = users[username]["balance"]
    save_users_to_csv() 
    requester_name = input("Enter requester name: ")
    print(f"Successfully requested ${amount:.2f} from {requester_name}.")
    return account_balance


def main():
    load_users_from_csv()
    while True:
        print("\n=== Bank System ===")
        print("1. Signup")
        print("2. Login")
        print("3. Exit")
        
        choice = input("Choose an option: ")
        if choice == "1":
            signup()
        elif choice == "2":
            login()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")
main()
