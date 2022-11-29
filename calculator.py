# defining the Operators 
# Addition
def add(x,y):
    return x + y

# Substraction
def subtract(x,y):
    return x - y

# Multiplication
def multiply(x,y):
    return x * y

# Division
def divide(x,y):
    return x / y

# Selecting the desired operation 
print("Select operation.")
print("a.Add")
print("b.Subtract")
print("c.Multiply")
print("d.Divide")
# Processing the operation
while True:
    choice = input("Enter your choice(a/b/c/d): ")
    if choice in ('a', 'b', 'c', 'd'):
        number1 = float(input("Enter first number: "))
        number2 = float(input("Enter second number: "))
        if choice == 'a':
           print(number1, "+", number2, "=", add(number1, number2))
        elif choice == 'b':
           print(number1, "-", number2, "=", subtract(number1, number2))
        elif choice == 'c':
           print(number1, "*", number2, "=", multiply(number1, number2))
        elif choice == 'd':
           print(number1, "/", number2, "=", divide(number1, number2))
        break
    else:
         print("Invalid operator")
