#data for testing
current_balance = 1000
user_transactions = [5000, -1200, -500, -800, 2000, -1500]

def display_result(func_value, display_text:str):
    return f"{display_text}: {func_value}"


def total_deposited(transactions:list):
    if not transactions: return
    total_deposists = 0
    for transaction in transactions:
        if transaction >= 0: total_deposists += transaction
    return total_deposists


def total_withdrawls_method_1(transactions:list):
    if not transactions: return
    total_withdrawls = 0
    for transaction in transactions:
        if transaction < 0:
           transac_to_str = str(transaction).replace('-', '') #convert to string and replace - with ''
           total_withdrawls += int(transac_to_str) #convreting updated string to int and adding to varibale
    return total_withdrawls


def total_withdrawls_method_2(transactions:list):
    if not transactions: return
    total_withdrawls = 0
    for transaction in transactions:
        if transaction < 0:
           total_withdrawls += (0 - (transaction)) #convert to positive
    return total_withdrawls


def show_final_balance(total_deposited, total_withdrawls, balance):
    final_balance = (total_deposited + balance) - total_withdrawls
    if final_balance >= 0: return final_balance
    else: return "Sorry you have unsufficient balance!"


def largest_withdrawl(transactions:list):
    if not transactions: return
    withdrawls = []
    
    for transaction in transactions:
        if transaction < 0: withdrawls.append((0 - (transaction)))

    largest_withdraw = withdrawls[0]

    for withdraw in withdrawls:
        if withdraw > largest_withdraw:
            largest_withdraw = withdraw

    return largest_withdraw


def largest_deposit(transactions:list):
    if not transactions: return
    largest_deposit_value = transactions[0]
    for transaction in transactions:
        if transaction > 0 and transaction > largest_deposit_value:
            largest_deposit_value = transaction
    if largest_deposit_value >= 0: return largest_deposit_value

#testing
#1.total deposits
total_deposists = total_deposited(user_transactions)
print(display_result(total_deposists, display_text="Total diposists"))

#2.total withdrawls method 1
total_withdrawls_1 = total_withdrawls_method_1(user_transactions)
print(display_result(total_withdrawls_1, display_text="Total withdrawls"))

#3.total withdrawls method 2
total_withdrawls_2 = total_withdrawls_method_2(user_transactions)
print(display_result(total_withdrawls_2, display_text="Total withdrawls"))

#4.showing final balance
print(display_result(show_final_balance(total_deposists, total_withdrawls_1, current_balance,), display_text="Final balance"))

#5.largest deposit
largest_deposit_is = largest_deposit(user_transactions)
print(display_result(largest_deposit_is, display_text="Largest deposit"))

#6.largest withdraw
largest_withdraw_value = largest_withdrawl(user_transactions)
print(display_result(largest_withdraw_value, display_text="Largest withdraw"))



