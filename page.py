import tkinter as tk
import backend


current_user = None

# Create root window
root = tk.Tk(screenName=None, baseName=None, className='Tk', useTk=True, sync=False, use=None)
root.title("BanKing")
root.geometry("1000x500")


def login():
    global current_user
    username = username_entry.get()
    password = password_entry.get()
    if backend.login(username, password):
        current_user = username
        open_main_menu()
    else:
        tk.Label(root, text="Invalid login credentials!", fg="red").pack()



def open_main_menu():
    
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text= f"Welcome, {current_user}", font=("Arial", 16)).pack(pady=20)
    tk.Button(root, text="Deposit", command=deposit).pack(pady=5)
    tk.Button(root, text="Withdraw", command=withdraw).pack(pady=5)
    tk.Button(root, text="Balance Check", command=balance_check).pack(pady=5)
    tk.Button(root, text="Logout", command=logout).pack(pady=5)






def deposit():
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Deposit Amount", font=("Arial", 16)).pack(pady=20)
    amount_entry = tk.Entry(root)
    amount_entry.pack()
    tk.Button(root, text="Submit", command=lambda: perform_deposit(amount_entry.get())).pack(pady=10)
    tk.Button(root, text="Back", command=open_main_menu).pack(pady=5)

def perform_deposit(amount):
    try:
        amount = float(amount)
        if amount <= 0:
            tk.Label(root, text="Enter a valid amount!", fg="red").pack()
            return

        backend.deposit(current_user, amount)
        tk.Label(root, text="Deposit Successful!", fg="green").pack()

    except ValueError:
        tk.Label(root, text="Invalid input. Please enter a number.", fg="red").pack()

    
    
    
def withdraw():
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Withdraw Amount", font=("Arial", 16)).pack(pady=20)
    amount_entry = tk.Entry(root)
    amount_entry.pack()
    tk.Button(root, text="Submit", command=lambda: perform_withdrawal(amount_entry.get())).pack(pady=10)
    tk.Button(root, text="Back", command=open_main_menu).pack(pady=5)
    
def perform_withdrawal(amount):
    try:
        amount = float(amount)  
        if amount <= 0:
            tk.Label(root, text="Enter a valid amount!", fg="red").pack()
            return

        success = backend.withdraw(current_user, amount)  
        if success:
            tk.Label(root, text="Withdrawal Successful!", fg="green").pack()
        else:
            tk.Label(root, text="Insufficient Balance!", fg="red").pack()

    except ValueError:
        tk.Label(root, text="Invalid input. Please enter a number.", fg="red").pack()
        
        
        
        
def balance_check():
    for widget in root.winfo_children():
        widget.destroy()

    balance = backend.check_balance(current_user)  
    tk.Label(root, text=f"Your Balance: ${balance:.2f}", font=("Arial", 16)).pack(pady=20)
    tk.Button(root, text="Back", command=open_main_menu).pack(pady=5)


    
def logout():
    global current_user
    current_user = None
    for widget in root.winfo_children():
        widget.destroy()

    display_login_screen()


def display_login_screen():
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Login to your account", font=("Arial", 16)).pack(pady=20)
    tk.Label(root, text="Username:").pack()

    global username_entry
    username_entry = tk.Entry(root)
    username_entry.pack()

    tk.Label(root, text="Password:").pack()

    global password_entry
    password_entry = tk.Entry(root, show="*")
    password_entry.pack()

    tk.Button(root, text="Login", command= login).pack(pady=10)

    
    
    
username_entry = tk.Entry(root)
password_entry = tk.Entry(root, show="*")

display_login_screen()

root.mainloop()

