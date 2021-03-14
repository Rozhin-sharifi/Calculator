import math

op = input()

if op == "sqrt" or op == "sin" or op == "cos" or op == "tan" or op == "fct":
    a = float(input())
else:
    a = float(input())
    b = float(input())

if op == "+":
    result = a+b
elif op == "-":
    result = a-b
elif op == "*":
    result = a*b
elif op == "/":
    if b == 0:
        result = "Cannot divide by zero!"
    else:
        result = a/b
elif op == "^":
    result = a**b
elif op == "log":
    result = math.log(a, b)
elif op == "sqrt":
    result = math.sqrt(a)
elif op == "sin":
    d = a*math.pi/180
    result = math.sin(d)
elif op == "cos":
    d = a*math.pi/180
    result = math.cos(d)
elif op == "tan":
    d = a*math.pi/180
    result = math.tan(d)
elif op == "cot":
    d = a*math.pi/180
    result = 1/math.tan(d)
elif op == "fct":
    factorial = 1
    if a < 0:
        print("Sorry, factorial does not exist for negative numbers")
    elif a == 0:
        print("The factorial of 0 is 1")
    else:
        a = int(a)
        for i in range(1, a + 1):
            factorial = factorial*i
            result = factorial
else:
    result = "Error! operator not found"
print(result)
