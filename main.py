def check_amount():
    check_input = input("Enter the check amount: ")

    try:
        check_total = int(check_input)
        # Split check into percentages based on the 50/30/20 rule
        split_50 = check_total * 0.5
        split_30 = check_total * 0.3
        split_20 = check_total * 0.2
        return check_total, split_50, split_30, split_20
    except ValueError:
        print("Please enter a valid integer.")
        return None

def bills():
    bill_input = input("Enter total of bills for the month: ")
    try:
        bill_total = int(bill_input)
        return bill_total
    except ValueError:
        print("Please enter a valid integer.")
        return None

def input_transactions():
    try:
        num_transactions = int(input("Enter the number of transactions: "))
        transactions = []
        for i in range(num_transactions):
            transaction_amount = float(input(f"Enter amount for transaction {i + 1}: "))
            transactions.append(transaction_amount)
        return transactions
    except ValueError:
        print("Please enter a valid integer for the number of transactions and valid floats for transaction amounts.")
        return None

check_result = check_amount()
bills_result = bills()

if check_result is not None and bills_result is not None:
    check_total, split_50, split_30, split_20 = check_result
    remaining_amount = check_total - bills_result
    print("Remaining amount after bills:", remaining_amount)
    print("50% Split:", split_50)
    print("30% Split:", split_30)
    print("20% Split:", split_20)

    transactions_result = input_transactions()

    if transactions_result is not None:
        total_spent = sum(transactions_result)
        remaining_amount -= total_spent
        print("Remaining amount after transactions:", remaining_amount)
else:
    print("Program crashed")