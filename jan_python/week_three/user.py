## Create a User class
    # users should have first names, last names, emails and passwords
    # users should be able to "say hello"

class Account:
    def __init__(self):
        self.balance = 0
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        self.balance -= amount
        return self

class User:
    def __init__(self, first, last, email, password):
        self.first=first
        self.last=last
        self.email=email
        self.password=password
        self.account=Account()
    def say_hello(self):
        print(f"{self.first} {self.last} says hello")
        return self
    def change_name(self, new_name):
        self.first=new_name
        return self
    def wrestling_move(self, move_name, target):
        print(f"{self.first} did move {move_name} to {target.first}")
        return self
    
first_user=User("Dwayne", "Johnson", "rock@wwe.com", "whatscookin")
# print(first_user)
second_user=User("Rey", "Mysterio", "rey@wwe.com", "luchador")
# print(first_user)

print(first_user.wrestling_move("slam", second_user))

# first_user.change_name("The Rock")
# second_user.say_hello().say_hello().say_hello().say_hello()

# print(first_user.account.deposit(100000))
# print(first_user.account.balance)
