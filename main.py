import logo


def addi(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1-n2


def div(n1, n2):
    return n1 / n2


def multiply(n1, n2):
    return n1 * n2


operations = {
    "+": addi,
    "-": subtract,
    "/": div,
    "*": multiply
}


def calculator():
    print(logo.logo)
    num1 = float(input("What's the first number? : "))

    for key in operations:
        print(key)

    loop = True
    while loop:
        operations_key = input("Pick an operation: ")
        num2 = float(input("What's the next number? : "))
        final_operation = operations[operations_key]
        answer = final_operation(num1, num2)
        print(f"{num1} {operations_key} {num2} = {answer}")
        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start new calc: ") == "y":
            num1 = answer
        else:
            loop = False
            calculator()


calculator()