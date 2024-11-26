import tkinter as tk
from tkinter import messagebox
import bank  # Assuming bank.py contains your original bank-related code

current_user = None


def clear_window(root):
    """Clears the window content."""
    for widget in root.winfo_children():
        widget.destroy()


def show_main_menu(root):
    """Show the main menu for Signup/Login."""
    clear_window(root)

    tk.Label(root, text="=== Bank System ===", font=("Arial", 16)).pack(pady=20)
    tk.Button(root, text="Signup", command=lambda: signup_window(root)).pack(pady=10)
    tk.Button(root, text="Login", command=lambda: login_window(root)).pack(pady=10)
    tk.Button(root, text="Exit", command=root.quit).pack(pady=10)


def signup_window(root):
    """Show the signup window."""
    clear_window(root)

    tk.Label(root, text="Enter a username:").pack(pady=10)
    username_entry = tk.Entry(root)
    username_entry.pack(pady=10)
    tk.Label(root, text="Enter a password:").pack(pady=10)
    password_entry = tk.Entry(root, show="*")
    password_entry.pack(pady=10)
    tk.Label(root, text="Confirm password:").pack(pady=10)
    confirm_password_entry = tk.Entry(root, show="*")
    confirm_password_entry.pack(pady=10)

    def signup():
        username = username_entry.get()
        password = password_entry.get()
        confirm_password = confirm_password_entry.get()

        # Handle user signup logic here (similar to your original code)
        if username in bank.users:
            messagebox.showerror("Error", "Username already exists!")
            return

        if password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match!")
            return

        # You would want to capture the email, bvn, account type here like your original code
        bank.users[username] = {
            "password": password,
            "email": "email@example.com",
            "bvn": "1234567890",
            "account_type": "Normal",
            "balance": 0.00,
        }

        messagebox.showinfo("Success", f"Account created successfully for {username}!")
        show_main_menu(root)

    tk.Button(root, text="Sign Up", command=signup).pack(pady=10)
    tk.Button(root, text="Back", command=lambda: show_main_menu(root)).pack(pady=10)


def login_window(root):
    """Show the login window."""
    clear_window(root)

    tk.Label(root, text="Enter username:").pack(pady=10)
    username_entry = tk.Entry(root)
    username_entry.pack(pady=10)
    tk.Label(root, text="Enter password:").pack(pady=10)
    password_entry = tk.Entry(root, show="*")
    password_entry.pack(pady=10)

    def login():
        username = username_entry.get()
        password = password_entry.get()

        if username in bank.users and bank.users[username]["password"] == password:
            global current_user
            current_user = username
            walp_menu(root, current_user)
        else:
            messagebox.showerror("Error", "Invalid username or password!")

    tk.Button(root, text="Login", command=login).pack(pady=10)
    tk.Button(root, text="Back", command=lambda: show_main_menu(root)).pack(pady=10)


def walp_menu(root, username):
    """WALP Menu where users can interact with various features."""
    clear_window(root)

    tk.Label(root, text=f"Welcome, {username}", font=("Arial", 16)).pack(pady=20)

    # Show home balance and options
    tk.Button(root, text="Home Balance", command=lambda: home_balance(root, username)).pack(pady=10)
    tk.Button(root, text="Card", command=lambda: get_card(root)).pack(pady=10)
    tk.Button(root, text="Send Money", command=lambda: send_money(root, username)).pack(pady=10)
    tk.Button(root, text="Request Money", command=lambda: request_money(root, username)).pack(pady=10)
    tk.Button(root, text="Exit", command=lambda: show_main_menu(root)).pack(pady=10)


def home_balance(root, username):
    """Show the home balance and transaction options."""
    clear_window(root)

    account_balance = bank.users[username]["balance"]
    tk.Label(root, text=f"Your Balance: ${account_balance:.2f}", font=("Arial", 16)).pack(pady=20)

    tk.Button(root, text="Add Cash", command=lambda: add_cash(root, username)).pack(pady=10)
    tk.Button(root, text="Cash Out", command=lambda: cash_out(root, username)).pack(pady=10)
    tk.Button(root, text="Buy Bitcoin", command=lambda: buy_bitcoin(root, username)).pack(pady=10)
    tk.Button(root, text="Buy Stock", command=lambda: buy_stock(root, username)).pack(pady=10)
    tk.Button(root, text="Back", command=lambda: walp_menu(root, username)).pack(pady=10)


def add_cash(root, username):
    """Add cash to the account."""
    clear_window(root)

    tk.Label(root, text="Enter amount to add:").pack(pady=10)
    amount_entry = tk.Entry(root)
    amount_entry.pack(pady=10)

    def confirm_add_cash():
        amount = amount_entry.get()
        try:
            amount = float(amount)
            if amount > 0:
                bank.users[username]["balance"] += amount
                messagebox.showinfo("Success", f"${amount:.2f} added to your account.")
                home_balance(root, username)
            else:
                messagebox.showerror("Error", "Invalid amount.")
        except ValueError:
            messagebox.showerror("Error", "Invalid amount.")

    tk.Button(root, text="Add Cash", command=confirm_add_cash).pack(pady=10)
    tk.Button(root, text="Back", command=lambda: home_balance(root, username)).pack(pady=10)


def cash_out(root, username):
    """Cash out from the account."""
    clear_window(root)

    tk.Label(root, text="Enter amount to cash out:").pack(pady=10)
    amount_entry = tk.Entry(root)
    amount_entry.pack(pady=10)

    def confirm_cash_out():
        amount = amount_entry.get()
        try:
            amount = float(amount)
            if amount <= bank.users[username]["balance"] and amount > 0:
                bank.users[username]["balance"] -= amount
                messagebox.showinfo("Success", f"${amount:.2f} cashed out from your account.")
                home_balance(root, username)
            else:
                messagebox.showerror("Error", "Insufficient funds or invalid amount.")
        except ValueError:
            messagebox.showerror("Error", "Invalid amount.")

    tk.Button(root, text="Cash Out", command=confirm_cash_out).pack(pady=10)
    tk.Button(root, text="Back", command=lambda: home_balance(root, username)).pack(pady=10)


def buy_bitcoin(root, username):
    """Buy Bitcoin."""
    clear_window(root)

    tk.Label(root, text="Enter amount to buy Bitcoin:").pack(pady=10)
    amount_entry = tk.Entry(root)
    amount_entry.pack(pady=10)

    def confirm_buy_bitcoin():
        amount = amount_entry.get()
        try:
            amount = float(amount)
            if amount <= bank.users[username]["balance"] and amount > 0:
                bank.users[username]["balance"] -= amount
                messagebox.showinfo("Success", f"${amount:.2f} spent on Bitcoin.")
                home_balance(root, username)
            else:
                messagebox.showerror("Error", "Insufficient funds or invalid amount.")
        except ValueError:
            messagebox.showerror("Error", "Invalid amount.")

    tk.Button(root, text="Buy Bitcoin", command=confirm_buy_bitcoin).pack(pady=10)
    tk.Button(root, text="Back", command=lambda: home_balance(root, username)).pack(pady=10)


def buy_stock(root, username):
    """Buy stock."""
    clear_window(root)

    tk.Label(root, text="Enter amount to buy stock:").pack(pady=10)
    amount_entry = tk.Entry(root)
    amount_entry.pack(pady=10)

    def confirm_buy_stock():
        amount = amount_entry.get()
        try:
            amount = float(amount)
            if amount <= bank.users[username]["balance"] and amount > 0:
                bank.users[username]["balance"] -= amount
                messagebox.showinfo("Success", f"${amount:.2f} spent on stock.")
                home_balance(root, username)
            else:
                messagebox.showerror("Error", "Insufficient funds or invalid amount.")
        except ValueError:
            messagebox.showerror("Error", "Invalid amount.")

    tk.Button(root, text="Buy Stock", command=confirm_buy_stock).pack(pady=10)
    tk.Button(root, text="Back", command=lambda: home_balance(root, username)).pack(pady=10)


def send_money(root, username):
    """Send money to another user."""
    clear_window(root)

    tk.Label(root, text="Enter recipient's username:").pack(pady=10)
    recipient_entry

def send_money(root, username):
    """Send money to another user."""
    clear_window(root)

    tk.Label(root, text="Enter recipient's username:").pack(pady=10)
    recipient_entry = tk.Entry(root)
    recipient_entry.pack(pady=10)

    tk.Label(root, text="Enter amount to send:").pack(pady=10)
    amount_entry = tk.Entry(root)
    amount_entry.pack(pady=10)

    def confirm_send_money():
        recipient = recipient_entry.get()
        amount = amount_entry.get()

        try:
            amount = float(amount)
            if recipient in bank.users and amount <= bank.users[username]["balance"] and amount > 0:
                bank.users[username]["balance"] -= amount
                bank.users[recipient]["balance"] += amount
                messagebox.showinfo("Success", f"${amount:.2f} sent to {recipient}.")
                home_balance(root, username)
            else:
                messagebox.showerror("Error", "Invalid amount, recipient not found, or insufficient funds.")
        except ValueError:
            messagebox.showerror("Error", "Invalid amount.")

    tk.Button(root, text="Send Money", command=confirm_send_money).pack(pady=10)
    tk.Button(root, text="Back", command=lambda: walp_menu(root, username)).pack(pady=10)


def request_money(root, username):
    """Request money from another user."""
    clear_window(root)

    tk.Label(root, text="Enter sender's username:").pack(pady=10)
    sender_entry = tk.Entry(root)
    sender_entry.pack(pady=10)

    tk.Label(root, text="Enter amount to request:").pack(pady=10)
    amount_entry = tk.Entry(root)
    amount_entry.pack(pady=10)

    def confirm_request_money():
        sender = sender_entry.get()
        amount = amount_entry.get()

        try:
            amount = float(amount)
            if amount > 0:
                messagebox.showinfo("Request Sent", f"Request for ${amount:.2f} sent to {sender}.")
                home_balance(root, username)
            else:
                messagebox.showerror("Error", "Invalid amount.")
        except ValueError:
            messagebox.showerror("Error", "Invalid amount.")

    tk.Button(root, text="Request Money", command=confirm_request_money).pack(pady=10)
    tk.Button(root, text="Back", command=lambda: walp_menu(root, username)).pack(pady=10)


# Main function to start the app
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Banking System")
    root.geometry("400x500")

    show_main_menu(root)

    root.mainloop()

