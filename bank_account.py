class BankAccount:


    def __init__(self, balance):
        if balance < 0:
            raise ValueError ('Balance has to be possitive')
        self.balance = balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError ('Amount has to be possitive')
        if self.balance - amount < 0:
            raise ValueError('Balance has to be possitive')

        return self.balance - amount


    def deposite(self, amount):
        if amount <= 0:
            raise ValueError ('Amount has to be possitive')
        return self.balance + amount

one = BankAccount(6000)
two = BankAccount(200)
print('Stan konta', one.balance)
print('Wpłacam 200', one.deposite(200))
print('Wypłacam 3000', one.withdraw(3000))