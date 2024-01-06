# check_module.py
def check_amount():
    while True:
        check_consistency_input = input("How many times will you be receiving a paycheck for the current month? (Enter a number from 0 to 5): ")
        try:
            check_consistency = int(check_consistency_input)
            if 0 <= check_consistency <= 5:
                break  # Break out of the loop if the input is valid
            else:
                print("Please enter a number between 0 and 5.")
        except ValueError:
            print("Please enter a valid integer.")

    checks_data = []  # List to store data for each check

    for i in range(check_consistency):
        while True:
            check_input = input(f"Enter the amount for check {i + 1}: ")
            try:
                check_amount = float(check_input)
                split_50 = round(check_amount * 0.50, 2)
                split_30 = round(check_amount * 0.30, 2)
                split_20 = round(check_amount * 0.20, 2)
                checks_data.append((check_amount, split_50, split_30, split_20))
                break  # Break out of the loop if the input is valid
            except ValueError:
                print("Please enter a valid number for the check amount.")

        if i < check_consistency - 1:
            next_check = input("Have you received the next check? (yes/no): ").lower()
            if next_check == "no":
                break  # Finish the program if the user hasn't received the next check

    return checks_data, check_consistency
