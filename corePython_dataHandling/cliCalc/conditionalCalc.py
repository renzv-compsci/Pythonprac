import math

def add (x,y):
    return x + y

def subtract (x,y):
    return x - y

def multiply (x,y):
    return x * y

def division (x,y):
    if y!= 0:
        return x / y

    else:
        return "Cannot be divided by zero"
    
def condiCalc():
    while True:
        print("Welcome to MiniCalc")
        print("\nSelect Operation")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5: EXIT")

        choice = input ("Enter choice here: ")

        if choice == '5':
                print("Good Bye")
                break

        if choice in ['1' , '2' , '3' , '4']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(f"Result: {add(num1,num2)}")

            elif choice == '2':
                print(f"Result: {subtract(num1,num2)}")

            elif choice == '3':
                print(f"Result: {multiply(num1,num2)}")

            elif choice == '4':
                print(f"Result: {division(num1,num2)}")

        
        else:
            print("Invalid Input")

if __name__ == "__main__":
    condiCalc()