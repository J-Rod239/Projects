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