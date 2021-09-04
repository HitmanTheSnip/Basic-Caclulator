# Basic Calculator

number1 = float(input("Enter the first number\nFirst Number: "))
number2 = float(input("Enter the second number\nSecond Number: "))
op = input("Select the operator (+, -, *, /): ")

if op == "+":
	print(number1 + number2)
elif op == "-":
	print(number1 - number2)
elif op == "*":
	print(number1 * number2)
elif op == "/":
	print(number1 / number2)

else:
	print("Invalid Input")