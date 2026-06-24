class BankAccount:
    def __init__(self,balance):
        self.__balance=balance
  
    def deposit(self,amount):
        self.__balance+=amount
        self.__balance=1000


    def show_balance(self):
        print("balance_is:",self.__balance)


c=BankAccount(2000)
c.show_balance()
c.deposit(3000)
c.show_balance()
print(c.__balance)
