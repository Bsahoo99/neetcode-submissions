class Account:
    def __init__(self, name: str, balance : int):
        self.title = name
        self._balance = balance
    
    def get_balance(self) -> int:
        return self._balance

    def _some_protected_method(self) -> None:
        print(f"Balance: ${self._balance}")

    def display_balance(self) -> None:
        self._some_protected_method()

# Do not modify the code below this line
account = Account("John", 1000)
account.display_balance()
