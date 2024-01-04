from transactions_module import input_transactions
from check_module import check_amount
from billings_module import bills

def credit_card_debt(check_total, split_20):
    while True:
        credit_card_response = input("Do you have credit card debt? (yes/no): ").lower()
        if credit_card_response == 'yes':
            try:
                debt_amount = float(input("Enter the total credit card debt: "))
                set_aside = round(split_20, 2)
                print(f"To pay off credit card debt, you should set aside: ${set_aside}")
                return debt_amount, set_aside
            except ValueError:
                print("Please enter a valid number for the debt amount.")
        elif credit_card_response == 'no':
            return 0, 0
        else:
            print("Please enter 'yes' or 'no'.")

# Perform check_amount first
check_result = check_amount()
bills_info = bills()
print("Bills Information:", bills_info)

if check_result is not None:
    check_total, split_50, split_30, split_20, check_consistency = check_result

    # Perform operations from billings_module
    remaining_amount = round(check_total - bills(), 2)
    print("Remaining amount after bills:", remaining_amount)
    print("50% Split:", split_50)
    print("30% Split:", split_30)
    print("20% Split:", split_20)

    transactions_result = input_transactions()

    if transactions_result is not None:
        total_spent = sum(transactions_result)
        remaining_amount -= total_spent
        print("Remaining amount after transactions:", remaining_amount)

    total_credit_card_debt, set_aside = credit_card_debt(check_total, split_20)
    print("Total credit card debt:", total_credit_card_debt)
else:
    print("Program crashed")