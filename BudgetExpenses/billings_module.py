def bills():
    check_bill = input("Do you have any bills? (yes/no): ").lower()
    
    if check_bill == "yes":
        try:
            bill_total = float(input("Enter the total amount of your bills for this month: "))
            return bill_total
        except ValueError:
            print("Invalid input. Please enter a valid numerical value for the bill total.")
            return bills()  # Recursive call to allow the user to try again
        
    elif check_bill == "no":
        print("No bill total has been reported.")
        return 0  # Returning 0 as default value when there are no bills
    
    else:
        print("You must answer only yes or no.")
        return bills()  # Recursive call to allow the user to try again
