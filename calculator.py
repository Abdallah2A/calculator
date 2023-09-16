# Define functions for basic arithmetic operations

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def divide(num1, num2):
    if num2 == 0:
        raise ValueError("Cannot divide by zero")
    return num1 / num2

def multiply(num1, num2):
    return num1 * num2

# Function to perform calculations based on provided numbers and operators
def calculate(numbers, operators):
    while len(numbers) != 1:
        for o in operators:
            index = operators.index(o)
            if o == "*":
                numbers[index] = multiply(numbers[index], numbers[index+1])
                numbers.remove(numbers[index+1])
                operators.remove(operators[index])
            
            elif o == "/":
                numbers[index] = divide(numbers[index], numbers[index+1])
                numbers.remove(numbers[index+1])
                operators.remove(operators[index])
            
            elif o == "+":
                numbers[index] = add(numbers[index], numbers[index+1])
                numbers.remove(numbers[index+1])
                operators.remove(operators[index])
            
            elif o == "-":
                numbers[index] = subtract(numbers[index], numbers[index+1])
                numbers.remove(numbers[index+1])
                operators.remove(operators[index])
    return numbers[0]

# Initialize lists to store numbers and operators
numbers = []
operators = []
end = True

# Input loop for user to enter numbers and operators
while end:
    try:
        num = input("\nEnter number: ")
        if num == "=":
            end = False
            continue
        num = float(num)
        operator = input("Enter Operator: ")
        if operator not in ['+', '-', '*', '/', '=']:
            raise ValueError("Invalid operator")
        operators.append(operator)
        numbers.append(num)
        for i in range(len(numbers)):
            if i < len(operators):
                print(f"{numbers[i]} {operators[i]}", end=" ")
        if operator == '=':
            end = False
            try:
                result = calculate(numbers, operators)
                print(f"\nResult: {result}")
            except Exception as e:
                print(f"Error: {e}")
    except ValueError as e:
        print(f"Error: {e}")