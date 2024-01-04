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