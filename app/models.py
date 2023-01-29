import uuid
class User:
    def __init__(self, userId, name, email, balance=0):
        self.userId = userId
        self.name = name
        self.email = email
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

class P2PApp:
  def __init__(self):
    self.users = {}
  

  def add_user(self, name, email):
    userId = str(uuid.uuid4())
    user = User(userId, name, email)
    self.users[userId] = user
    return user

  def get_user(self, userId):
    return self.users.get(userId, None)

  def deposit(self, userId, amount):
      user = self.users[userId]
      user.deposit(amount)
      return user

  def withdraw(self, userId, amount):
      user = users[userId]
      user.withdraw(amount)
      return user

  def send_money(self, sender, receiver, amount):
      sender_user = self.users[sender]
      receiver_user = self.users[receiver]
      sender_user.withdraw(amount)
      receiver_user.deposit(amount)
      return sender_user, receiver_user

  def check_balance(self, userId):
      return users[userId].balance

app = P2PApp()