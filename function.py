# Functions Without Parameters

a=int(input("Enter a number: "))
b=int(input("Enter another number: "))

def add():
    print("The sum is:", a + b)
def subtract():
    print("The difference is:", a - b)
def multiply():
    print("The product is:", a * b)
def divide():
    if b != 0:
        print("The quotient is:", a / b)
    else:
        print("Error: Division by zero is not allowed.")

add()
subtract()
multiply()
divide()

# Functions With Parameters


