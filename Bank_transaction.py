class BankTransaction:

    def __init__(self,balance):
        self.balance = balance
        print("Initial Balance :", self.get_balance())

    def credit(self,amount):
        self.balance += amount
        print("Amount Credited : ", amount)
        print("New Balance :", self.get_balance())

    def debit(self,amount):
        if amount > self.balance:
            print("Insufficient Balance")
        else:
            self.balance -= amount
            print("Amount Debited : ", amount)
            print("New Balance :", self.get_balance())

    def get_balance(self):
        return self.balance
    
Customer1 = BankTransaction(10000)
Customer1.credit(500)
Customer1.debit(200)
