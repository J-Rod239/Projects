def calculate_time_to_pay_off(debt_total, monthly_payment):
    remaining_debt = float(debt_total)
    months = 0

    while remaining_debt > 0:
        remaining_debt -= monthly_payment
        if remaining_debt < 0:
            remaining_debt = 0  # Ensure debt doesn't go negative
        months += 1

    return months

def debt_data(check_amount):
    while True:
        check_debt = input("Do you have credit card debt? (yes/no): ").lower()
        if check_debt == "yes":
            debt_question = input("How much do you owe in total?: ")
            debt_total = float(debt_question)
            
            # Calculate time to pay off assuming the entire debt gets paid off every month
            set_aside_percentage = 0.2
            monthly_payment = check_amount * set_aside_percentage
            
            months_to_pay_off = calculate_time_to_pay_off(debt_total, monthly_payment)
            
            print(f"It will take approximately {months_to_pay_off} months to pay off the credit card debt.")
            
            return debt_total
        elif check_debt == "no":
            print("Congrats on not having any debt!")
            return 0  # Returning 0 as default value when there is no debt
        else:
            print("You must answer only yes or no.")