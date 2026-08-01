'''
1. ATM Withdrawal 💳 (Easy)
Scenario

ব্যাংক অ্যাপ থেকে টাকা তোলা হচ্ছে।

Rules
User amount input দিবে।
যদি amount <= 0 হয় → raise ValueError
যদি amount balance (10000) এর বেশি হয় → raise ValueError
নাহলে টাকা withdraw হবে।

Example

Balance: 10000

Enter amount: 2000

Withdraw Successful
Remaining Balance: 8000

Invalid

Enter amount: -500

Invalid amount!
'''

#sollution
def atm_withdrawl(amount: int):
    try:
        if amount <= 0:
            raise ValueError
        elif amount > 10000:
            raise ValueError

        final_amount = 10000 - amount
        return (
            f"Withdraw Successful \n"
            f"Remaining Balance: {final_amount}"
        )
    except ValueError:
        return "Please give a valid input!"

print(atm_withdrawl(2000))
print(atm_withdrawl(-500))
print(atm_withdrawl(100000))

