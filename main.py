def check_amount():
    check_input = input("Enter the check amount: ")

    try:
        check_total = int(check_input)
        return check_total
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

check_result = check_amount()
bills_result = bills()

if check_result is not None and bills_result is not None:
    print("Remaining amount:", check_result - bills_result)
else:
    print("Program crashed")
    