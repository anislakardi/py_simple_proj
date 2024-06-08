a = float(input("enter the first number : "))
b = float(input("enter the second number : "))
op = input("enter the operator: ")

if op == '*':
  result = a*b
  print(f"a * b = {result}")
elif op == '+':
  result = a+b
  print(f"a + b = {result}")
elif op == '-':
  result = a-b
  print(f"a - b = {result}")
elif op == '/':
  result = a/b
  print(f"a / b = {result}")
else:
  print("invalid operation")