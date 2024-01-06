import sys

def debt_data():
    while True:
        check_debt = input("Do you have credit card debt? (yes/no): ").lower()
        if check_debt == "yes":
            debt_question = input("How much do you owe in total?: ")
            debt_total = debt_question
            return debt_total
        elif check_debt == "no":
            print("Congrats on not having any debt!")
            sys.exit("Program terminated.")