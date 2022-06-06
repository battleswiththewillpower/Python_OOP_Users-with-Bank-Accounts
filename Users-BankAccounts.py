class BankAccount:
    #don't change anything in this class
    bank_name ="Big Bank Roll"
    all_accounts = []
    def __init__(self, interest_rate, balance):
        #self.name = name
        self.interest_rate = interest_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    def add_deposit(self, amount):
        self.balance += amount
        #self.display_account()
        return self

    def make_withdraw(self,amount):
        
        if amount > self.balance:
            self.balance -= 5
            print("Insufficient funds: Charging a $5 fee")
        else: 
            self.balance -= amount
        return self

    def display_account(self):
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
# increases the account balance by the current balance * the interest rate (as long as the balance is positive)
        if self.balance > 0:
            self.balance = self.balance + self.balance * self.interest_rate
        return self

    """@classmethod
    def all_balances(cls):
        sum = 0
        for account in cls.all_accounts:
            sum += account.balance
            print(f"The account total is ${sum}")
        return sum"""


class User:
#Update the User class __init__ method
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
        #self.email = email
        #self.birthdate = birthdate
        self.account = BankAccount(0.04, 0)
        # self.account = {
        #     "checking": BankAccount(.01, 0),
        #     "savings": BankAccount(.04, 0)
        #     }

#Update the User class make_deposit method
    def deposit(self, amount):
        self.account.add_deposit(amount)
        return self

    def withdrawl(self, amount):
        self.account.make_withdraw(amount)
        return self

    def display_user_balance(self):
        #my setup might be wrong. ask about it
        print(f"User: {self.first_name} {self.last_name}, Balance: ${self.account.balance}")
        self.account.display_account()
        return self

#SENSEI BONUS: Allow a user to have multiple accounts; update methods so the user 
# has to specify which account they are withdrawing or depositing to
    """def transfer_money(self, amount, account, checkings, savings):
        self.account[account].make_withdraw(amount)
        checkings.account[savings].add_deposit(amount)
        return self"""

user_1 = User("Ashley", "Battles")
user_2 = User("Mars", "Ayanna")

user_1.deposit(7222).display_user_balance()
user_2.deposit(2777).display_user_balance()
print()

"""user_1.deposit(7222, "checking").deposit(1000, "saving").display_user_balance()
#user_2.deposit(2777).display_user_balance()
print()"""


    
