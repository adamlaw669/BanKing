users = {
    "adam": {"password": "1234", "balance": 5000.0},
    "jane_doe": {"password": "qwerty", "balance": 3000.0},
}

def login(username, password):
    if username in users and users[username]["password"] == password:
        return True
    return False

def check_balance(username):
    return users[username]["balance"]


def deposit(username, amount):
    users[username]["balance"] += amount
    return users[username]["balance"]

def withdraw(username, amount):
    if users[username]["balance"] >= amount:
        users[username]["balance"] -= amount
        return True
    return False