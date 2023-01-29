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
    self.users[email] = user
    return user

  def get_user(self, email):
    return self.users.get(email, None)

  def deposit(self, email, amount):
      user = self.users[email]
      user.deposit(amount)
      return user

  def withdraw(self, email, amount):
      user = self.users[email]
      if user.balance < amount:
        raise ValueError('Insufficient funds')
      user.withdraw(amount)
      return user

  def send_money(self, sender, receiver, amount):
      sender_user = self.users[sender]
      receiver_user = self.users[receiver]

      if sender_user.balance < amount:
        raise ValueError('Insufficient funds')

      sender_user.withdraw(amount)
      receiver_user.deposit(amount)
      return sender_user, receiver_user

  def check_balance(self, userId):
      return users[userId].balance

app = P2PApp()