import math

print("Welcome to MiniCalc")


print("Choose your operation")
print("1: Addition")
print("2: Subtraction")
print("3: Multiplcation")
print("4: Division")


choice = input ("Enter your choice here: ")


x = input ("Enter your first number: ")
y = input ("Enter your second number: ")

x= float(x)
y= float(y)

if choice == '1': 
    result = x + y

elif choice == '2':
    result = x - y

elif choice == '3':
    result = x * y

elif choice == '4':
    result = x/y

else:
    print("Invalid input")

print(f"Answer {result}")


