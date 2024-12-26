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
        
        style = ttk.Style()
        style.configure("TButton", font=('Arial', 12), padding=10)
        style.configure("TLabel", font=('Arial', 16))
        
        frame = ttk.Frame(root, padding="20") 
        frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(0, weight=1)
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)

        self.root = root

        ttk.Label(frame, text="Enter a username:", style='TLabel').grid(row=0, column=0, columnspan=2, pady=20)
        self.username_entry = ttk.Entry(frame)
        self.username_entry.grid(row=1, column=0, columnspan=2, pady=10, sticky=(tk.W, tk.E))

        ttk.Label(frame, text="Enter a password:", style='TLabel').grid(row=2, column=0, columnspan=2, pady=10)
        self.password_entry = ttk.Entry(frame, show="*")
        self.password_entry.grid(row=3, column=0, columnspan=2, pady=10, sticky=(tk.W, tk.E))

        ttk.Label(frame, text="Confirm password:", style='TLabel').grid(row=4, column=0, columnspan=2, pady=10)
        self.confirm_password_entry = ttk.Entry(frame, show="*")
        self.confirm_password_entry.grid(row=5, column=0, columnspan=2, pady=10, sticky=(tk.W, tk.E))

        ttk.Button(frame, text="Signup", command=self.signup, style='TButton').grid(row=6, column=0, columnspan=2, pady=10, sticky=(tk.W, tk.E))
        ttk.Button(frame, text="Back", command=lambda: show_main_menu(root), style='TButton').grid(row=7, column=0, columnspan=2, pady=10, sticky=(tk.W, tk.E))

    def signup(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()

        if password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match!")
            return

        if bank.Users.signup(username, password):
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
    root.geometry("400x500")
    
    bank.load_users_from_csv()

    show_main_menu(root)

    root.mainloop()



