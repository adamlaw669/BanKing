import tkinter as tk
from tkinter import messagebox
import bank  

current_user = None

def clear_window(root):
    """Clears the window content."""
    for widget in root.winfo_children():
        widget.destroy()

def show_main_menu(root):
    """Show the main menu for Signup/Login."""
    clear_window(root)
    tk.Label(root, text="BanKing", font=("Arial", 16)).pack(pady=20)
    tk.Button(root, text="Signup", command=lambda: SignupWindow(root)).pack(pady=10)
    tk.Button(root, text="Login", command=lambda: Login_window(root)).pack(pady=10)
    tk.Button(root, text="Exit", command=root.quit).pack(pady=10)

class AnimatedDropdown:
    def __init__(self, master, options, default_choice="Normal"):
        self.master = master
        self.options = options
        self.is_open = False
        self.selected_choice = default_choice

        # Button to toggle dropdown
        self.toggle_button = tk.Button(master, text="Choose account type", command=self.toggle_dropdown)
        self.toggle_button.pack(pady=10)

        # Frame to hold options
        self.options_frame = tk.Frame(master)
        self.create_option_buttons()

        # Label to display the selected option
        self.selected_label = tk.Label(master, text=f"Selected account type: {self.selected_choice}")
        self.selected_label.pack(pady=10)

    def create_option_buttons(self):
        for option in self.options:
            btn = tk.Button(self.options_frame, text=option, command=lambda opt=option: self.select_option(opt))
            btn.pack(fill='x')

    def toggle_dropdown(self):
        if not self.is_open:
            self.options_frame.pack()  # Show the frame
            self.is_open = True
        else:
            self.options_frame.pack_forget()  # Hide the frame
            self.is_open = False

    def select_option(self, option):
        self.selected_choice = option
        self.selected_label.config(text=f"Selected account type: {self.selected_choice}")  # Update label
        self.toggle_dropdown()  # Close dropdown after selection

class SignupWindow:
    def __init__(self, root):
        """Show the signup window."""
        clear_window(root)
        self.root = root

        tk.Label(root, text="Enter a username:").pack(pady=10)
        self.username_entry = tk.Entry(root)
        self.username_entry.pack(pady=10)

        tk.Label(root, text="Enter your fullname: ").pack(pady=10)
        self.fullname_entry = tk.Entry(root)
        self.fullname_entry.pack(pady=10)

        tk.Label(root, text="Enter a password:").pack(pady=10)
        self.password_entry = tk.Entry(root, show="*")
        self.password_entry.pack(pady=10)

        tk.Label(root, text="Confirm password:").pack(pady=10)
        self.confirm_password_entry = tk.Entry(root, show="*")
        self.confirm_password_entry.pack(pady=10)

        tk.Label(root, text="Enter your email:").pack(pady=10)
        self.email_entry = tk.Entry(root)
        self.email_entry.pack(pady=10)

        tk.Label(root, text="Choose account type:").pack(pady=10)
        self.account_types = ["Student", "Normal", "Business"]
        self.animated_dropdown = AnimatedDropdown(root, self.account_types)

        tk.Button(root, text="Sign Up", command=self.signup).pack(pady=10)
        tk.Button(root, text="Back ", command=lambda: show_main_menu(root)).pack(pady=10)

    def signup(self):
        if not bank.username_check(self.username_entry.get()):
            messagebox.showerror('Error', 'Invalid username')
            show_main_menu(self.root)
            return
        else:
            bank.Users(username=self.username_entry.get(), 
                        full_name=self.fullname_entry.get(), 
                        password=self.password_entry.get(), 
                        email=self.email_entry.get(), 
                        acctype=self.animated_dropdown.selected_choice)
            messagebox.showinfo('Account created successfully')
            show_main_menu(self.root)



class Login_window():
    
    def __init__(self, root):
        """Show the login window."""
        clear_window(root)
        self.root = root
        
        tk.Label(root, text="Enter username:").pack(pady=10)
        self.username_entry = tk.Entry(root)
        self.username_entry.pack(pady=10)
        
        tk.Label(root, text="Enter password:").pack(pady=10)
        self.password_entry = tk.Entry(root, show="*")
        self.password_entry.pack(pady=10)
        
        def login():
            username = self.username_entry.get()
            password = self.password_entry.get()
            
            if bank.Users.login(username,password):
                global current_user
                current_user = username
                messagebox.showinfo('Login Succesful')
                menu(root, current_user)
            else:
                messagebox.showerror("Could not log you in !")

        tk.Button(root, text="Login", command=login).pack(pady=10)
        tk.Button(root, text="Back", command=lambda: show_main_menu(root)).pack(pady=10)
        
        
    
    
    
    
    
    
    


def menu(root, username):
    """Menu where users can interact with various features."""
    clear_window(root)

    tk.Label(root, text=f"Welcome, {current_user}", font=("Arial", 16)).pack(pady=20)

    # Show home balance and options
    tk.Button(root, text="Home Balance", command=lambda: home_balance(root, username)).pack(pady=10)
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
    root.title("BanKing")
    root.geometry("400x500")
    
    bank.load_users_from_csv()

    show_main_menu(root)

    root.mainloop()



