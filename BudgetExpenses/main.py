from transactions_module import input_transactions
from check_module import check_amount
from credit_debt import debt_data, calculate_time_to_pay_off
from billings_module import bills
import sys

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
        total_bills = bills()

        # Subtract total spent from remaining_amount
        remaining_amount -= (total_spent + total_bills)

        print(f"Remaining amount after transactions:", remaining_amount)
        debt_function = debt_data()
        set_aside = check_amount * .2
        print("You should use the 20%: $", set_aside, " from your current check")
        sys.exit()
        
    else:
        total_bills = bills()
        remaining_amount = sum(check_amount for check_amount, _, _, _ in checks_data) - total_bills

        print(f"Remaining amount after bills: {remaining_amount}")
        debt_total = debt_data(remaining_amount)
        set_aside_percentage = 0.2
        monthly_payment = remaining_amount * set_aside_percentage
        months_to_pay_off = calculate_time_to_pay_off(debt_total, monthly_payment)        
        print(f"You should use {set_aside_percentage * 100}%: ${monthly_payment} each month to pay off your credit card debt in approximately {months_to_pay_off} months.")
        

