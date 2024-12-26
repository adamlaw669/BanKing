import csv
import uuid
import re
import os
from datetime import datetime

user_db = {}
transactions_db = {}

csv_file = '/Users/mac/Documents/Bank/BanKing/tkinter stuff/user_db.csv'
csv_file_tr = '/Users/mac/Documents/Bank/BanKing/tkinter stuff/transaction_db.csv'


def save_users_to_csv():
    with open(csv_file, 'a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["Username", 'Full_name',"Password", 'ID', "email", "Type", "Balance"])  #extrasaction= 'ignore')
        #writer.writeheader()
        for username, user_data in user_db.items():
            writer.writerow({"Username": username, **user_data})

def load_users_from_csv():
    global user_db
    try:
        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)
            print(f"Field names: {reader.fieldnames}")  
            if reader.fieldnames != ["Username", 'Full_name', "Password", "ID", 'email', 'Type', "Balance"]:
                print("Field names do not match expected names.")  
                return
            for row in reader:
                user_db[row['Username']] = {
                    "Password": row["Password"],
                    "email": row["email"],
                    "ID": row["ID"],
                    "Type": row["Type"],
                    "Balance": float(row["Balance"]),
                    'Full_name': row['Full_name'],
                    'Username': row['Username']
                }
            print(f"Loaded users: {user_db}")  
    except FileNotFoundError:
        print("CSV file not found.")  
        return
    except Exception as e:
        print(f"An error occurred: {e}")  
        
    
    
def save_transactions_csv():
        file_exists = os.path.isfile(csv_file_tr)
        
        with open(csv_file_tr, 'a+', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["id",
                                                      'sender',
                                                      "receiver",
                                                      'amount',
                                                      "type",
                                                      "timestamp"])
            if not file_exists:
                writer.writeheader()
            
            for sender, user_data in transactions_db.items():
                writer.writerow({"sender": sender, **user_data})

def load_transactions_from_csv():
    try:
        with open(csv_file_tr, 'r') as file:
            reader = csv.DictReader(file)
            if reader.fieldnames != ["id",
                                   'sender',
                                   "receiver",
                                   'amount',
                                    "type",
                                  "timestamp"]:
                return
            for row in reader:
                transactions_db[row['sender']] = {
                    "id": row["id"],
                    "sender": row["sender"],
                    "receiver": row["receiver"],
                    "type": row["type"],
                    "timestamp": row["timestamp"],
                    'amount': row['amount'],
                }
    except FileNotFoundError:
        return
    except Exception as e:
        print(f"An error occurred: {e}")    
    
    
    
    
def generate_uuid():
    return str(uuid.uuid4())
def username_check(username):
    pattern = r"^[a-zA-Z0-9_]{3,20}$"
    if username not in user_db:
        return True
    if re.search(pattern, username):
        return True
    else: return False
    
    
def track_transaction(sender, receiver, amount, transaction_type):
    id = str(uuid.uuid4())
    transactions_db[id] = {
        'id': id,
        'sender': sender,
        'receiver': receiver,
        'amount': amount,
        'type': transaction_type,
        'timestamp': datetime.now().isoformat()
    }
    
    save_transactions_csv()

class Users:
    def __init__(self, username='none', 
                 full_name='John Doe',
                 email='johndoe@gmail.com', 
                 password=0000, 
                 id= None, 
                 acctype='Normal', 
                 balance=0.00) -> None:
        
        self.username = username
        self.full_name = full_name
        self.id = id or generate_uuid()
        self.type = acctype
        self.balance = balance
        self.password = password
        self.email = email
        
        self.add_user_to_db()
        
    def add_user_to_db(self):
        user_db[self.username] = {
            "Username": self.username,
            'Full_name': self.full_name,
            'ID' : self.id,
            "Balance": self.balance,
            "Type": self.type,
            'Password': self.password,
            'email': self.email
        }
        
        save_users_to_csv()
    

        
    @classmethod
    def login(cls, username, password):
        user_info = user_db.get(username)  # Retrieve user info from the database
        print(f"Attempting to log in user: {username}") 
        print(user_db)# Debugging line
        if user_info:
            print(f"User  found: {user_info}")  # Debugging line
            if user_info['Password'] == str(password):  # Check password
                print(f"Login successful for user: {username}")  # Debugging line
                track_transaction(sender=username, receiver=None, amount=None, transaction_type='Login')
                return True  # Login successful
            else:
                print("Incorrect password.")  # Debugging line
        else:
            print("User  not found.")  # Debugging line
        return False  # Login failed
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            user_db[self.username]['Balance'] = self.balance
            track_transaction(sender=self, 
                              receiver=self,
                              amount = amount,
                              transaction_type= 'Deposit')
            return True
        return False
        
    @classmethod    
    def transfer(cls,sender_username, receiver_username, amount):
        if receiver_username in user_db and sender_username in user_db:
            if amount > 0 and user_db[sender_username]['Balance'] >= amount:
                user_db[sender_username]['Balance'] -= amount
                user_db[receiver_username]['Balance'] += amount
                save_users_to_csv()
                track_transaction(sender=sender_username, 
                                  receiver= receiver_username,
                                  amount = amount,
                                  transaction_type= 'Transfer')
                return True
        return False
        
    def balance_check(self):
        track_transaction(sender=self, receiver=self, amount = self.balance, transaction_type= 'Balance Check')
        return self.balance
        
    