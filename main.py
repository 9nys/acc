class Account:
    def __init__(self, balance, account_holder):
        self.__balance = balance
        self._account_holder = account_holder

    def get_balance(self):
        return self.__balance


my_account = Account(1000, "John Doe")

print("Current balance:", my_account.get_balance())


print("Account holder:", my_account._account_holder)

