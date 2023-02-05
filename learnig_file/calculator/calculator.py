# from art import logo
def add(n1, n2):
    return n1 + n2
def sub(n1, n2):
    return n1 - n2
def mul(n1, n2):
    return n1 * n2
def div(n1, n2):
    return n1 / n2

calculate = {"+": add, "-": sub, "*": mul, "/": div}
def calculator():
    # print(logo)
    num1 = int(input("Enter the 1st number:"))

    for i in calculate:
        print(i)

    should_continue = True

    while should_continue:
                    
        symbol = input("Enter the another operation: ")
        num2 = int(input("Enter the next number: "))
        first_ans = calculate[symbol](num1, num2)

        print(f"{num1} {symbol} {num2} = {first_ans}")

        next = input("Type 'y' to continue or 'n' to new calculation: ").lower()

        if next == 'y':
            num1 = first_ans
        else:
            should_continue = False
            calculator()
calculator()