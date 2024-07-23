num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))


print("choose an operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. multiplication (*)")
print("4. Division (/)")


operation = input("Enter the operation (+, -, *, /): ")
if operation == '+':
   result = num1 + num2
   print(result)
elif operation == '-':
   result = num1 - num2
   print(result)
elif operation == '*':
   result = num1 * num2
   print(result)
elif operation == '/':
   result = num1 / num2
   print(result)
else:
   print("invalid operations")

