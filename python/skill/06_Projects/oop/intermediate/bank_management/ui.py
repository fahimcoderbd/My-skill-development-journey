from main import Customer


def print_menu() -> None:
    """Show the console choices."""
    print("\n===== Bank Management Console =====")
    print("1. Create account")
    print("2. Deposit money")
    print("3. Withdraw money")
    print("4. Transfer money")
    print("5. Show accounts")
    print("6. Show transaction history")
    print("7. Show total balance")
    print("8. Exit")


def read_amount(prompt: str) -> float:
    """Read a valid numeric amount from the user."""
    while True:
        try:
            return float(input(prompt).strip())
        except ValueError:
            print("Please enter a valid numeric amount.")


def run_ui(customer: Customer)-> None :
    """Start the simple terminal-based UI loop."""
    print(f"\nWelcome, {customer.name}!")

    while True:
        print_menu()
        choice = input("Choose an option: ").strip()

        try:
            if choice == "1":
                account_number = input("Enter account number: ").strip()
                customer.create_account(account_number)
                print("Account created successfully.")

            elif choice == "2":
                account_number = input("Enter account number: ").strip()
                amount = read_amount("Enter deposit amount: ")
                customer.deposit(account_number, amount)
                print("Deposit completed.")

            elif choice == "3":
                account_number = input("Enter account number: ").strip()
                amount = read_amount("Enter withdrawal amount: ")
                customer.withdraw(account_number, amount)
                print("Withdrawal completed.")

            elif choice == "4":
                from_account = input("Enter source account number: ").strip()
                to_account = input("Enter destination account number: ").strip()
                amount = read_amount("Enter transfer amount: ")
                customer.transfer(from_account, to_account, amount)
                print("Transfer completed.")

            elif choice == "5":
                customer.show_accounts()

            elif choice == "6":
                account_number = input("Enter account number: ").strip()
                customer.show_transaction_history(account_number)

            elif choice == "7":
                print(f"Total balance: {customer.total_balance():.2f}")

            elif choice == "8":
                print("Goodbye!")
                break

            else:
                print("Invalid option. Please select a number from 1 to 8.")

        except ValueError as error:
            print(f"Error: {error}")
        except Exception as error:
            print(f"Unexpected error: {error}")


if __name__ == "__main__":
    customer_name = input("Enter customer name: ").strip() or "Guest Customer"
    run_ui(Customer(customer_name))
