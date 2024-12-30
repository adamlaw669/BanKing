import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
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
    
    style = ttk.Style()
    style.configure("TButton", font=('Arial', 12), padding=10)
    style.configure("TLabel", font=('Arial', 16))
    
    frame = ttk.Frame(root, padding="20") 
    frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
    
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    frame.grid_rowconfigure(0, weight=1)
    frame.grid_columnconfigure(0, weight=1)
    
    ttk.Label(frame, text="BanKing", style = 'TLabel').grid(row=0, column=0, columnspan=2, pady=10)
    ttk.Button(frame,  text="Signup", command=lambda: SignupWindow(root), style = 'TButton').grid(row =1, column = 0, columnspan=2, pady = 10, sticky=(tk.W, tk.E))
    ttk.Button(frame,  text="Login", command=lambda: Login_window(root), style = 'TButton').grid(row =2, column = 0, columnspan=2, pady = 10, sticky=(tk.W, tk.E))
    ttk.Button(frame,  text="Exit", command=root.quit, style = 'TButton').grid(row =3, column = 0, columnspan=2, pady = 10, sticky=(tk.W, tk.E))

 
class SignupWindow:
    def __init__(self, root):
        self.root = root  
        self.is_open = False  # Track dropdown state
        self.selected_choice = "Normal"  
        
        
        frame = ttk.Frame(root, padding="10")
        frame.grid(row=0, column=0, sticky=(tk.N, tk.S, tk.E, tk.W))

        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        ttk.Label(frame, text="Enter your full name:", style='TLabel').grid(row=0, column=0, pady=10, sticky=tk.W)
        self.full_name_entry = ttk.Entry(frame)
        self.full_name_entry.grid(row=0, column=1, pady=10, sticky=(tk.W, tk.E))

        ttk.Label(frame, text="Enter your username:", style='TLabel').grid(row=1, column=0, pady=10, sticky=tk.W)
        self.username_entry = ttk.Entry(frame)
        self.username_entry.grid(row=1, column=1, pady=10, sticky=(tk.W, tk.E))

        ttk.Label(frame, text="Enter your email:", style='TLabel').grid(row=2, column=0, pady=10, sticky=tk.W)
        self.email_entry = ttk.Entry(frame)
        self.email_entry.grid(row=2, column=1, pady=10, sticky=(tk.W, tk.E))

        ttk.Label(frame, text="Enter a password:", style='TLabel').grid(row=3, column=0, pady=10, sticky=tk.W)
        self.password_entry = ttk.Entry(frame, show="*")
        self.password_entry.grid(row=3, column=1, pady=10, sticky=(tk.W, tk.E))

        ttk.Label(frame, text="Confirm password:", style='TLabel').grid(row=4, column=0, pady=10, sticky=tk.W)
        self.confirm_password_entry = ttk.Entry(frame, show="*")
        self.confirm_password_entry.grid(row=4, column=1, pady=10, sticky=(tk.W, tk.E))

        self.toggle_button = ttk.Button(frame, text="Choose account type", command=self.toggle_dropdown)
        self.toggle_button.grid(row=5, column=0, columnspan=2, pady=10)

        self.options_frame = ttk.Frame(frame)
        self.create_option_buttons()

        self.selected_label = ttk.Label(frame, text=f"Selected account type: {self.selected_choice}")
        self.selected_label.grid(row=6, column=0, columnspan=2, pady=10)

        ttk.Button(frame, text="Signup", command=self.signup, style='TButton').grid(row=7, column=0, pady=10, sticky=(tk.W, tk.E))
        ttk.Button(frame, text="Back", command=lambda: show_main_menu(root), style='TButton').grid(row=7, column=1, pady=10, sticky=(tk.W, tk.E))

        root.bind('<Return>', self.signup)

    def create_option_buttons(self):
        options = ["Normal", "Student"]
        for option in options:
            btn = ttk.Button(self.options_frame, text=option, command=lambda opt=option: self.select_option(opt))
            btn.grid(sticky=(tk.W, tk.E))

    def toggle_dropdown(self):
        if not self.is_open:
            self.options_frame.grid(row=8, column=0, columnspan=2, sticky=(tk.W, tk.E)) 
            self.is_open = True
        else:
            self.options_frame.grid_forget()
            self.is_open = False

    def select_option(self, option):
        self.selected_choice = option
        self.selected_label.config(text=f"Selected account type: {self.selected_choice}")  # Update label
        self.toggle_dropdown()

    def signup(self, event=None):
        username = self.username_entry.get()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()
        full_name = self.full_name_entry.get() 
        email = self.email_entry.get()
        acctype = self.selected_choice

        if password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match!")
            return

        if bank.Users.signup(username, full_name, password, email, acctype):
            messagebox.showinfo("Success", "Signup successful!")
            show_main_menu(self.root)
        else:
            messagebox.showerror("Error", "Signup failed. Username may already be taken.")
        


class Login_window():
    
    def __init__(self, root):
        """Show the login window."""
        clear_window(root)
        self.root = root
        
        style = ttk.Style()
        style.configure("TButton", font=('Arial', 12), padding=10)
        style.configure("TLabel", font=('Arial', 16))
        
        frame = ttk.Frame(root, padding="20") 
        frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(0, weight=1)
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)
        
        ttk.Label(frame, text="Enter username:", style='TLabel').grid(row= 0, column =0, columnspan=2, pady=10)
        self.username_entry = ttk.Entry(frame)
        self.username_entry.grid(row=1, column=0, pady=10, sticky=(tk.W, tk.E))
        
        ttk.Label(frame, text="Enter password:", style='TLabel').grid(row = 2, column=0, pady=10)
        self.password_entry = ttk.Entry(frame, show="*")
        self.password_entry.grid(row=3,column=0, pady=10, sticky=(tk.W, tk.E))
        
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

        ttk.Button(frame, text="Login", command=login, style='TButton').grid(row = 4, column=0, pady=10)
        ttk.Button(frame, text="Back", command=lambda: show_main_menu(root), style='TButton').grid(row =5, column=0, pady=10)
        root.bind('<Return>', login)
        
    
    
    
    
    
    
    


def menu(root, username):
    """Menu where users can interact with various features."""
    clear_window(root)
    
    style = ttk.Style()
    style.configure("TButton", font=('Arial', 12), padding=10)
    style.configure("TLabel", font=('Arial', 16))

    frame = ttk.Frame(root, padding="20")
    frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
    
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    frame.grid_rowconfigure(0, weight=1)
    frame.grid_columnconfigure(0, weight=1)

    ttk.Label(frame, text=f"Welcome, {username}", style='TLabel').grid(row=0, column=0, columnspan=2, pady=20)

    ttk.Button(frame, text="Home Balance", command=lambda: home_balance(root, username), style='TButton').grid(row=1, column=0, columnspan=2, pady=10, sticky=(tk.W, tk.E))
    ttk.Button(frame, text="Send Money", command=lambda: transfer(root, username), style='TButton').grid(row=2, column=0, columnspan=2, pady=10, sticky=(tk.W, tk.E))
    #ttk.Button(frame, text="Request Money", command=lambda: request_money(root,username)).grid(row=3, column=0, columnspan=2, pady=10, sticky=(tk.W, tk.E))
    ttk.Button(frame, text="Exit", command=lambda: show_main_menu(root), style ='TButton').grid(row=4, column=0, columnspan=2, pady=10, sticky=(tk.W, tk.E))



def home_balance(root, username):
    """Show the home balance and transaction options."""
    clear_window(root)
    
    style = ttk.Style()
    style.configure("TButton", font=('Arial', 12), padding=10)
    style.configure("TLabel", font=('Arial', 16))

    frame = ttk.Frame(root, padding="20")
    frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
    
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    frame.grid_rowconfigure(0, weight=1)
    frame.grid_columnconfigure(0, weight=1)

    welcome_message = f"Welcome, {username}!"
    ttk.Label(frame, text=welcome_message, style='TLabel').grid(row=0, column=0, columnspan=2, pady=10)

    account_balance = bank.user_db[username]['Balance']
    ttk.Label(frame, text=f"Your Balance: ${account_balance:.2f}", style='TLabel').grid(row=1, column=0, columnspan=2, pady=20)

    ttk.Button(frame, text="Transfer", command=lambda: transfer(root, username)).grid(row=2, column=0, columnspan=1, pady=10, sticky=(tk.W, tk.E))
    ttk.Button(frame, text="Back", command=lambda: menu(root, username)).grid(row=2, column=1, columnspan=2, pady=10, sticky=(tk.W, tk.E))




def transfer(root, username):
    """Send money to another user."""
    clear_window(root)
    
    style = ttk.Style()
    style.configure('TButton', font=('Arial', 12), padding=10)
    style.configure('TLabel', font=('Arial', 16))
    
    frame = ttk.Frame(root, padding="20")
    frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
    
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    frame.grid_rowconfigure(0, weight=1)
    frame.grid_columnconfigure(0, weight=1)

    ttk.Label(frame, text="Transfer Money", style='TLabel').grid(row=0, column=0, columnspan=2, pady=20)
    ttk.Label(frame, text="Enter recipient's username:", style='TLabel').grid(row=1, column=0, pady=10, sticky=tk.W)
    recipient_entry = ttk.Entry(frame)
    recipient_entry.grid(row=1, column=1, pady=10, sticky=(tk.W, tk.E))

    ttk.Label(frame, text="Enter amount to send:", style='TLabel').grid(row=2, column=0, pady=10, sticky=tk.W)
    amount_entry = ttk.Entry(frame)
    amount_entry.grid(row=2, column=1, pady=10, sticky=(tk.W, tk.E))

    def confirm_send_money():
        recipient = recipient_entry.get()
        try:
            amount = float(amount_entry.get())
        except ValueError:
            messagebox.showinfo('Error', 'Invalid amount')
            return

        if bank.Users.transfer(username, recipient, amount):
            messagebox.showinfo('Transfer successful', f'Successfully transferred ${amount:.2f} to {recipient}.')
            home_balance(root, username)
        else:
            messagebox.showinfo('Error', 'Transfer failed')

    ttk.Button(frame, text="Complete transfer", command=confirm_send_money).grid(row=3, column=0, columnspan=1, pady=10, sticky=(tk.W, tk.E))
    ttk.Button(frame, text="Back", command=lambda: home_balance(root, username)).grid(row=3, column=1, columnspan=2, pady=10, sticky=(tk.W, tk.E))
    
    

# Main function to start the app
if __name__ == "__main__":
    root = ThemedTk(theme='arc')
    root.title("BanKing")
    root.geometry("400x600")
    
    bank.load_users_from_csv()

    show_main_menu(root)

    root.mainloop()



