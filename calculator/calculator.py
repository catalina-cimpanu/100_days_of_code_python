def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2

operations = {"+": add, "-": subtract, "*": multiply, "/": divide}

def calculator():
    num1 = float(input("What's the first number? "))

    for operation in operations:
        print(operation)

    op_symbol = input("Pick an operation from the line above: ")

    calc_function = operations[op_symbol]
    num2 = float(input("What's the second number? "))

    answer = calc_function(num1, num2)
    print(f"{num1} {op_symbol} {num2} = {answer}")

    keep_on = input(f"Type 'y' to continue calculating with {answer}, type 'exit' if you want to exit, otherwise type anything else to start over with a new calculation: ")
    while keep_on == "y":
        op_symbol = input("Pick an operation: ")    
        calc_function = operations[op_symbol]

        num1 = answer
        num2 = float(input("What's the next number? "))
        answer = calc_function(num1, num2)
        print(f"{num1} {op_symbol} {num2} = {answer}")
        keep_on = input(f"Type 'y' to continue calculating with {answer}, type 'exit' if you want to exit, otherwise type anything else to start over with a new calculation:  ")
    if keep_on == "exit":
        return print("Exiting calculator")
    else:
        print("\nStarting over\n")
        calculator()

calculator()
print("Byeee!")
