# Updated Basic Calculator

num1 = float(input("Enter the first number\nFirst Number: "))
num2 = float(input("Enter the second number\nSecond Number: "))
operator = input("Select any of the operator (+, -, *, /): ")

if operator == "+":
    print("The sum of ", num1, "and", num2, "is", num1+num2)
elif operator == "-":
    print("The difference of ", num1, "and", num2, "is", num1-num2)
elif operator == "*":
    print("The multiplication of ", num1, "and", num2, "is", num1*num2)
elif operator == "/":
    print("The division of ", num1, "and", num2, "is", num1/num2)
else:
    print("INVALID INPUT(PLEASE RECHECK THE NUMBER AND THE OPERATOR YOU TYPE)")