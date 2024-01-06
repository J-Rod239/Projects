from transactions_module import input_transactions
from check_module import check_amount
from credit_debt import debt_data

check_result = check_amount()

if check_result is not None:
    checks_data, check_consistency = check_result

    for i, check_data in enumerate(checks_data):
        check_amount, split_50, split_30, split_20 = check_data
        print(f"Details for check {i + 1}:")
        print(f"Check Amount: {check_amount}")
        print(f"50% Split: {split_50}")
        print(f"30% Split: {split_30}")
        print(f"20% Split: {split_20}")

    transactions_result = input_transactions()

    if transactions_result is not None:
        remaining_amount = sum(check_amount for check_amount, _, _, _ in checks_data)
        total_spent = sum(transactions_result)

        # Subtract total spent from remaining_amount
        remaining_amount -= total_spent

        print("Remaining amount after transactions:", remaining_amount)
        
    else:
        print("Program crashed")
else:
    debt_function = debt_data()
    set_aside = check_amount * .2
    print(set_aside)