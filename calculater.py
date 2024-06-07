'''first_number = eval(input("enter the first number:"))
operator = input("Enter the operator ( + - * % ):")
second_number = eval(input("Enter the second number:"))
if operator == "+":
    sum = first_number+second_number
    print(sum)
elif operator == "-":
    diff  = first_number-second_number
    print(diff)
elif operator == "*":
    mul = first_number* second_number
    print(mul)
elif operator == "%":
    div = first_number% second_number
    print(div)
else:
    print("you chose invalid operator")'''
from math import *
import symtable as sp
import sympy as sp
from sympy import symbols, diff,integrate
def add_value(values):
    first_number = eval(input("Enter the first number:"))
    operator = input("Enter the operator (+):")
    second_number = eval(input("Enter the second number:"))
    sum = first_number+second_number
    print(sum)
                        
def sub_value(values):
    first_number = eval(input("Enter the first number:"))
    operator = input("Enter the operator (-):")
    second_number = eval(input("Enter the second number:"))
    diff = first_number-second_number
    print(diff)
def mul_value(values):
    first_number = eval(input("Enter the first number:"))
    operator = input("Enter the operator (*):")
    second_number = eval(input("Enter the second number:"))
    mul= first_number*second_number
    print(mul)
def div_value(values):
    first_number = eval(input("Enter the first number:"))
    operator = input("Enter the operator (/):")
    second_number = eval(input("Enter the second number:"))
    divide= first_number/second_number
    print(divide)
def dot_value(values):
    first_number = int(input("Enter the first number:"))
    operator = input("Enter the operator (.):")
    second_number = int(input("Enter the second number:"))
    dot = float(f'{first_number}.{second_number}')
    print(dot)
def cos_value(values):
    x = eval(input("Enter the value of x:"))
    print(cos(x))
def sin_value(values):
    x = eval(input("Enter the value of x:"))
    print(sin(x))
def tan_value(values):
    x = eval(input("Enter the value of x:"))
    print(tan(x))
def log_value(values):
    x = eval(input("Enter the value of x:"))
    print(log(x))
def complex_value(values):
    a = eval(input("Enter the first number:"))
    b = eval(input("Enter the second number:"))
    print(complex(a,b))
def add_complex_value(values):
    real1 = eval(input("Enter the first real value:"))
    img1 = eval(input("Enter the first imaginary value:"))
    real2 = eval(input("Enter the second real value:"))
    img2 = eval(input("Enter the second imaginary value:"))
    complex1 = complex(real1,img1)
    complex2 = complex(real2,img2)
    add_complex = complex1+complex2
    print(add_complex)
def sub_complex_value(values):
    real1 = eval(input("Enter the first real value:"))
    img1 = eval(input("Enter the first imaginary value:"))
    real2 = eval(input("Enter the second real value:"))
    img2 = eval(input("Enter the second imaginary value:"))
    complex1 = complex(real1,img1)
    complex2 = complex(real2,img2)
    sub_complex = complex1-complex2
    print(sub_complex)
def mul_complex_value(values):
    real1 = eval(input("Enter the first real value:"))
    img1 = eval(input("Enter the first imaginary value:"))
    real2 = eval(input("Enter the second real value:"))
    img2 = eval(input("Enter the second imaginary value:"))
    complex1 = complex(real1,img1)
    complex2 = complex(real2,img2)
    mul_complex = complex1*complex2
    print(mul_complex)
def div_complex_value(values):
    real1 = eval(input("Enter the first real value:"))
    img1 = eval(input("Enter the first imaginary value:"))
    real2 = eval(input("Enter the second real value:"))
    img2 = eval(input("Enter the second imaginary value:"))
    complex1 = complex(real1,img1)
    complex2 = complex(real2,img2)
    add_complex = complex1+complex2
    print(add_complex)
def degree_to_radian(values):
    degree = eval(input("Enter the any degree value:"))
    radian = degree * (pi /180)
    print(radian)
def radian_to_degree(values):
    radian = eval(input("Enter the any degree value:"))
    degree = radian * (180/pi)
    print(degree)
def power(values):
    x = eval(input("Enter the base value:"))
    y = eval(input("Enter the power value:"))
    power = x**y
    print(power)
def baselog(values):
    x = eval(input("Enter the value of x:"))
    basex = log10(x)
    print(basex)
def derivative(values):
   x = symbols('x')
   fxn = input("Entee the any function:")
   fxn_derivative =diff(fxn,x)
   print(fxn_derivative)
def trigonometric_function(values):
    x = symbols('x')
    tfxn = input("Entee the any trigonometric function:")
    tfxn_derivative = diff(tfxn,x)
    print(tfxn_derivative)
def  al_fxn_integration(values):
   x = symbols('x')
   ifxn = input("Enter the any function:")
   ifxn_integration=integrate(ifxn,)
   print(ifxn_integration)

values =[]
while True:
    print("\n scientific calculater")
    print("1) add two number")
    print("2) subtract two number:")
    print("3) multiply two number:")
    print('4) divide two number:')
    print('5) dot the value')
    print('6) cosx value')
    print('7) sinx value')
    print('8) tanx value')
    print('9) logx value')
    print('10) complex value')
    print('11) add complex value')
    print('12) substract complex value')
    print('13) multiply complex value')
    print('14) division complex value')
    print('15) Degree to radian conversion value')
    print('16) Radian to degree conversion value')
    print('17) power value')
    print('18) logx value')
    print('19) derivate of simple polynomial function ')
    print('20) derivate of trigonometric function ')
    print('21) integration of all type of function')

    print('9) Exit the calculater app')

    choice = input("Enter the choice:")
    match choice:
        case '1':
            add_value(values)
        case '2':
            sub_value(values)
        case '3':
            mul_value(values)
        case '4':
            div_value(values)
        case '5':
            dot_value(values)
        case '6':
            cos_value(values)
        case '7':
            sin_value(values)
        case '8':
            tan_value(values)
        case '9':
            log_value(values)
        case '10':
           complex_value(values)
        case '11':
            add_complex_value(values)
        case '12':
           sub_complex_value(values)
        case '13':
            mul_complex_value(values)
        case '14':
            div_complex_value(values)
        case '15':
            degree_to_radian(values)
        case '16':
            radian_to_degree(values)
        case '17':
            power(values)
        case '18':
            baselog(values)
        case '19':
            derivative(values)
        case '20':
            trigonometric_function(values)
        case '21':
            al_fxn_integration(values)
       

        case _:
            break

'''first_number = eval(input("enter the first number:"))
operator = input("Enter the operator ( + - * % ):")
second_number = eval(input("Enter the second number:"))
if operator == "+":
    sum = first_number+second_number
    print(sum)
elif operator == "-":
    diff  = first_number-second_number
    print(diff)
elif operator == "*":
    mul = first_number* second_number
    print(mul)
elif operator == "%":
    div = first_number% second_number
    print(div)
else:
    print("you chose invalid operator")'''

