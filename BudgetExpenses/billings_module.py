def bills():
    while True:
        try:
            num_bills = int(input("Enter the total number of bills for the month: "))
            if num_bills <= 0:
                print("Please enter a positive number.")
                continue

            bill_info_list = []
            for _ in range(num_bills):
                while True:
                    try:
                        bill_total = float(input("Enter the total amount of the bill: "))
                        bill_type_input = input("Enter the type of bill (1 for regular bill, 2 for subscription): ")
                        bill_type = int(bill_type_input)

                        if bill_type in [1, 2]:
                            bill_info_list.append((bill_total, bill_type))
                            break
                        else:
                            print("Please enter either 1 for a regular bill or 2 for a subscription.")
                    except ValueError:
                        print("Please enter valid numbers.")

            return bill_info_list
        except ValueError:
            print("Please enter a valid number for the total number of bills.")