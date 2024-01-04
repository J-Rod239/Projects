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

    check_input = input("Enter the check amount: ")
    try:
        check_total = float(check_input)
        # Split check into percentages based on the 50/30/20 rule
        split_50 = round(check_total * 0.5, 2)
        split_30 = round(check_total * 0.3, 2)
        split_20 = round(check_total * 0.2, 2)
        return check_total, split_50, split_30, split_20, check_consistency
    except ValueError:
        print("Please enter a valid number for the check amount.")
        return None