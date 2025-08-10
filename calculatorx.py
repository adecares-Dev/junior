# welcome to simple calculator program
# we are going to add, subtract. multiply ,and divide two numbers like a pro!
# we are using 'float' to make sure our number can have decimal number too. Good right?

# step 1: Ask the user to input the first number
num1 = float(input("Enter the first number:"))

# step 2: Ask the user to input the second number
num2 = float(input("Enter the second number:"))

# step 3: user are going to carry out this operation
operation = input("Enter the operation(+,-,*,/)")

# step 4: perform the calculation
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 == 0:
        print("Error: Division by zero is not allowed")
 
    result = num1 / num2
else:
    print("Error: Invalid operation. please use +,-,*./.")
    
# step %: Display the result
print(f"{num1} {operation} {num2} = {result}")    

