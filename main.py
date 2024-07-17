MAX_LINES = 3


def deposit():
    #Constantly ask for deposit until deposit requirements are satisfied (is a number, then converts string to int and deposit larger than 0 then breaks)
    while True:
        amount = input("What would you like to deposit? $")
        #if isinstance(amount, str) == True:
            #amount = amount.replace('.', '')

        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a valid number.")

    return amount

def get_number_of_lines():
    while True:
        lines = input(f"Enter the number of lines to bet on (1-{MAX_LINES})? ")
        

        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines")
        else:
            print("Please enter a valid number.")

    return lines


def main(): 
    balance = deposit()
    lines = get_number_of_lines()
    print(balance, lines)





main()