#.................................................................SCIENTIFIC Calculator...........................................................................
import math

module1 = """
    Choose an Operation to proceed: 
    1 or +: Addition         
    2 or -: Substraction       
    3 or *: Multiplication   
    4 or /: Division 
    5 or %: Modulas         
    6 or exp: Exponent
    7 or sqrt: Squareroot       
    8 or t: Trigonometry   
    9 or d:degree 
    10 or r:radian   
    11 or e: exit()
    -> """

module2 = """
    Supported Operations: sin, cos, tan, cot, cosec, sec
    Format: sin(angle), cos(angle), tan(angle),radians,degrees
    Note:- Angle to be input in terms of radians
    -> """

def operation():
    op = input(module1)
    return op


def process(equation):
    if equation[:3] == 'sin': equation = equation.replace('sin', 'math.sin')
    elif equation[:3] == 'cos': equation = equation.replace('cos', 'math.cos')
    elif equation[:3] == 'tan': equation = equation.replace('tan', 'math.tan')
    elif equation[:3] == 'rad': equation =equation.replace('rad', 'math.radian')
    elif equation[:3] == 'deg': equation =equation.replace('deg','math.degree')
    return equation
#    if equation[:3] == 'sin': equation.replace('sin', math.sin)


#Supported Operations
lis= ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '+']

op = operation()

while True:
    if op=='1' or op=='+':
        print(eval(input('Number 1: ')+'+'+input('Number 2: ')))
        op = operation()
    elif op=='2' or op=='-':
        print(eval(input('Number 1: ')+'-'+input('Number 2: ')))
        op = operation()
    elif op=='3' or op=='*':
        print(eval(input('Number 1: ')+'*'+input('Number 2: ')))
        op = operation()
    elif op=='4' or op=='/':
        print(eval(input('Number 1: ')+'/'+input('Number 2: ')))
        op = operation()
    elif op=='5' or op=='%':
        print(eval(input('Dividend: ')+'%'+input('Divisor: ')))
        op = operation()
    elif op=='6' or op=='exp':
        print(eval(input('Number : ')+'**'+input('Exponent: ')))
        op = operation()
    elif op == '7' or op=='sqrt':
        print(eval(input('Number : ') + '**0.5'))
        op = operation()
    elif op == '8' or op=='t':
         x = input("Choose 'sin', 'cos' or 'tan': ")
         y = math.radians(int(input("Enter angle: ")))
         if x == 'sin':
            print(f"sin({math.ceil(math.degrees(y))}) = {math.sin(y)}")
            if x == 'cos':
                print(f"cos({math.ceil(math.degrees(y))}) = {math.cos(y)}")
            if x == 'tan':
                print(f"tan({math.ceil(math.degrees(y))}) = {math.tan(y)}")
            op = operation()
        
    elif op == '9' or op=='d':
        print(math.degrees(eval(input("Enter number in radian: "))))
    elif op == '10' or op=='r':
        print(math.radians(eval(input("Enter number in degree: "))))
    elif op == 'e' or op=='11':
        exit()
    else:
        print("Choose Correct Option.")
        op = operation()

#.............................................................SCIENTIFIC CALCULATOR.........................................................................