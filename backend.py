users ={}

def add_user(username, password, balance, BVN, Acctype='Adult'):
    new_user = User(username, password, balance, BVN, Acctype=Acctype)
    users[new_user.userID] = new_user
    
class User:
    def __init__(self, username, password, balance, BVN, userID=None, Acctype='Adult'):
        self.username = username
        self.password = password 
        self.balance = balance
        self.BVN = BVN
        self.userID = userID if userID is not None else self.generate_user_id()
        self.Acctype = Acctype

    def generate_user_id(self):
        import uuid
        return str(uuid.uuid4())

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def __repr__(self):
        return f"User (username={self.username}, balance={self.balance}, userID={self.userID})"
         
         
    class Admin:
        def __init__(self, admin_username, admin_password):
            self.admin_username = admin_username
            self.admin_password = admin_password

    def create_user(self, bank, username, password, balance=0.0, bvn=None):
        bank.add_user(User(username, password, balance, bvn))
        return f"User {username} created successfully."

    def delete_user(self, bank, username):
        if username in bank.users:
            del bank.users[username]
            return f"User {username} deleted successfully."
        return f"User {username} does not exist."
