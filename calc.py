result=0
num1=int(input("num1: "))
operator=str(input("operator "))
num2 = int(input("num2: "))

def calc_math_expression(num1,operator,num2):
    if operator == "+":
        result=num1+num2
    elif operator == "-":
        result=num1-num2
    elif operator == "*":
        result=num1*num2
    elif operator == ":":
        result=num1/num2
    return result

print(calc_math_expression(num1,operator,num2))
