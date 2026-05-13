def add(n1, n2):
    return n1 + n2
def subtract(n1,n2):
    return n1 - n2
def multiply(n1,n2):
    return n1 * n2
def divide(n1,n2):
    return n1 / n2

operations={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}
def calculate():
    num1 = float(input("Enter the first number:"))

    should_accumulate = True
    while should_accumulate:
        for symbol in operations:
            print(symbol)
        def choosing_symbol():
            global operation_symbol
            operation_symbol = input("choose an operation ('+','-','*','/'):")
            if operation_symbol != "+" and operation_symbol != "-" and operation_symbol != "*" and operation_symbol != "/":
                print("enter a valid symbol")
                choosing_symbol()
        choosing_symbol()
        num2 = float(input("Enter the second number:"))
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        repeat = input(f"type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
        if repeat == 'y':
            num1 = answer
        else:
            should_accumulate = False
            calculate()
calculate()




