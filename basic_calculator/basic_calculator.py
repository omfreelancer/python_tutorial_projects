operator = input("Chose an operator (+ - * /): ")

num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2st number: "))

if operator == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {round(result,3)}")
elif operator == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {round(result,3)}")
elif operator == "*":
    result = num1 * num2
    print(f"{num1} - {num2} = {round(result,3)}")
elif operator == "/":
    result = num1 / num2
    print(f"{num1} / {num2} = {round(result,3)}")
else:
    print(f"'{operator}' is not valid operator")