class BankAccount:
    def __init__(self, account_number: str):
        self.account_number = account_number
        self.balance = 0.0
        self.transactions = []

    def validate_amount(self, amount: float):
        if amount <= 0:
            raise ValueError("Amount must be greater than 0.")

    def deposit(self, amount: float) -> str:
        """Add money to the account."""
        self.validate_amount(amount)
        self.balance += amount
        self.transactions.append(f"Deposited {amount}")
        return (
            f"{amount} added to your balance successfully! \n"
            f"Current balance: {self.balance}"
        )

    def withdraw(self, amount: float) -> str:
        """Remove money from the account."""
        self.validate_amount(amount)
        if self.balance < amount:
            raise ValueError("Insufficient balance.")
        self.balance -= amount
        self.transactions.append(f"Withdrew {amount}")
        return (
            f"{amount} withdrawn from your balance successfully! \n"
            f"Current balance: {self.balance}"
        )

    def transfer(self, amount: float, destination: "BankAccount") -> str:
        """Send money to another account."""
        self.validate_amount(amount)
        if self.balance < amount:
            raise ValueError("Insufficient balance.")
        self.balance -= amount
        destination.balance += amount
        self.transactions.append(f"Transferred {amount} to {destination.account_number}")
        destination.transactions.append(
            f"Received {amount} from {self.account_number}"
        )
        return (
            f"{amount} transferred successfully! \n"
            f"Current balance: {self.balance}"
        )

class Customer:
    """Represents a bank customer."""

    def __init__(self, name: str):
        self.name = name
        self.accounts: list[BankAccount] = []

    def create_account(self, account_number: str) -> str:
        """Create a new bank account."""

        for account in self.accounts:
            if account.account_number == account_number:
                raise ValueError("Account number already exists.")

        account = BankAccount(account_number)
        self.accounts.append(account)

        return f"Account {account_number} created successfully."

    def find_account(self, account_number: str) -> BankAccount:
        """Helper method to find an account."""

        for account in self.accounts:
            if account.account_number == account_number:
                return account

        raise ValueError("Account not found.")

    def deposit(self, account_number: str, amount: float) -> str:
        account = self.find_account(account_number)
        return account.deposit(amount)

    def withdraw(self, account_number: str, amount: float) -> str:
        account = self.find_account(account_number)
        return account.withdraw(amount)

    def transfer(
        self,
        from_account: str,
        to_account: str,
        amount: float
    ) -> str:

        sender = self.find_account(from_account)
        receiver = self.find_account(to_account)

        return sender.transfer(amount, receiver)

    def show_accounts(self) -> None:
        print(f"\nCustomer: {self.name}")

        for account in self.accounts:
            print(
                f"Account: {account.account_number}"
                f" | Balance: {account.balance}"
            )

    def show_transaction_history(self, account_number: str) -> None:
        account = self.find_account(account_number)

        print(f"\nTransaction History ({account_number})")

        if not account.transactions:
            print("No transactions found.")
            return

        for transaction in account.transactions:
            print("-", transaction)

    def total_balance(self) -> float:
        total = 0

        for account in self.accounts:
            total += account.balance

        return total