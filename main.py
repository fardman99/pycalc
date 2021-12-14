from smath import *
x = 0.0
y = 0.0
z = ""
def math1():
    global x
    try: x = float(input("Enter a number: "))
    except ValueError:
        print("Invalid input.")
        math1()

def op():
    global z
    z = input("Enter an operator: ")
    if z not in ["+", "-", "*", "/"]:
        print("Invalid input.")
        op()

def math2():
    global y
    try: y = float(input("Enter a number: "))
    except ValueError:
        print("Invalid input.")
        math2()
    
math1()
op()
math2()
if z == "+":
    print(add(x, y))
elif z == "-":
    print(sub(x, y))
elif z == "*":
    print(mul(x, y))
elif z == "/":
    print(div(x, y))