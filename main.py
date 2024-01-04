def check_amount():
    check_input = input("Enter the check amount: ")

    try:
        check_total = float(check_input)
        # Split check into percentages based on the 50/30/20 rule
        split_50 = round(check_total * 0.5, 2)
        split_30 = round(check_total * 0.3, 2)
        split_20 = round(check_total * 0.2, 2)
        return check_total, split_50, split_30, split_20
    except ValueError:
        print("Please enter a valid integer.")
        return None

def bills():
    bill_input = input("Enter total of bills for the month: ")
    try:
        bill_total = float(bill_input)
        return bill_total
    except ValueError:
        print("Please enter a valid integer.")
        return None

def input_transactions():
    while True:
        transaction_q = input("Do you want to add any transactions? (yes/no): ").lower()
        if transaction_q == 'yes':
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
        elif transaction_q == 'no':
            return None
        else:
            print("Please enter 'yes' or 'no'.")

def credit_card_debt():
    while True:
        credit_card_response = input("Do you have credit card debt? (yes/no): ").lower()
        if credit_card_response == 'yes':
            try:
                debt_amount = float(input("Enter the total credit card debt: "))
                return debt_amount
            except ValueError:
                print("Please enter a valid number for the debt amount.")
        elif credit_card_response == 'no':
            return 0
        else:
            print("Please enter 'yes' or 'no'.")

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

    total_credit_card_debt = credit_card_debt()
    print("Total credit card debt:", total_credit_card_debt)
else:
    print("Program crashed")