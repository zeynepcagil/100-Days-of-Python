
def add(a,b):
    return a+b
def substract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b

def calculator():
    
    operations ={ "+" : add , "-": substract ,"*" : multiply , "/" :divide }
    f_numb= float(input("What's the first number?: "))

    should_accumulate=True
    while should_accumulate:
        for symbol in operations:
            print(symbol)
        op_symbol=input("Pick an operation: ")
        s_numb= float(input("What's the next number?: "))
        answer=operations[op_symbol](f_numb,s_numb)
        print(f"{f_numb} {op_symbol} {s_numb} = {answer}")

        is_continue = input(f" Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
        if is_continue=="y":
            f_numb=answer
        if is_continue=="n":
            should_accumulate=False
            calculator()

calculator()