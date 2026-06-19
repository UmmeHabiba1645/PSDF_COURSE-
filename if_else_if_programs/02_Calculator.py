num1 = float(input('Enter first num: '))
num2 = float(input('Enter second number: '))
op = input('Enter Operator (+, -, *, /, %): ')

if op == '+':
    print ("Result = ",num1 + num2)
elif op == "-":
    print ("Result = ",num1 - num2)
elif op == "*":
    print ("Result = ",num1 * num2)
elif op == "/":
    print ("Result = ",num1 / num2)
elif op == "%":
    print ("Result : ",num1 % num2)
else:
    print ("Invalid Operator")
