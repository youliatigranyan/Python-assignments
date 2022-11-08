import cmath
import re

def calc_math_expression(num1,operator,num2):
    if num2 == 0:
        return "Error"
    elif operator == "+":
        result=num1+num2
    elif operator == "-":
        result=num1-num2
    elif operator == "*":
        result=num1*num2
    elif operator == ":":
        result=num1/num2
    else:
        return None  #If we're getting an illegal input for this function, return None

    match operator:
        case ("+"):
            print("plus")
        case ("-"):
            print("minus")
        case ("*"):
            print("multipication")
        case (":"):
            print("division")

    return result



# it gets a single string, splits to parameters, and sends it to the previous function
def calc_math_expression_from_str(str_input):
    inp = str_input.split(" ")
    return calc_math_expression(num1=float(inp[0]),operator=inp[1],num2=float(inp[2]))


#test
print(calc_math_expression_from_str("10 : 2"))
print(calc_math_expression_from_str("10 : -2"))
print(calc_math_expression_from_str("-10 : -2"))
print(calc_math_expression_from_str("-10 : 2"))
print(calc_math_expression_from_str("10 + 2"))
print(calc_math_expression_from_str("100 - 39.3"))
print(calc_math_expression_from_str("5 : 2"))
print(calc_math_expression_from_str("5 : 0"))
print(calc_math_expression_from_str("10 333 2"))
print(calc_math_expression_from_str("10 ^ 2"))


def find_largest_and_smallest_numbers(number1=0.0, number2=0.0, number3=0.0):
    #max
    #number1 > number2 ? (number1 > number3 ? number1 : number3) : (number2 < number3 ? number2 : number3)

    # min
    # number1 < number2 ? (number1 < number3 ? number1 : number3) : (number2 < number3 ? number2 : number3)

    if (number1 >= number2) and (number1>=number3):
        largestNumber = number1
    elif(number2 >= number1) and (number2 >= number3):
        largestNumber= number2
    elif (number3 >= number1) and (number3 >= number2):
        largestNumber = number3

    if (number1 <= number2) and (number1 <= number3):
        smallestNumber = number1
    elif (number2 <= number1) and (number2 <= number3):
        smallestNumber = number2
    elif (number3 <= number1) and (number3 <= number2):
        smallestNumber = number3

    min_max = (largestNumber, smallestNumber)
    return min_max

print(find_largest_and_smallest_numbers(5, 1, 10))
print(find_largest_and_smallest_numbers(2.5, 2.5, 7))
print(find_largest_and_smallest_numbers(7, 2.5, 2.5))
print(find_largest_and_smallest_numbers(-5, -5, -5))
print(find_largest_and_smallest_numbers(10, -1, 10))
print(find_largest_and_smallest_numbers(-2, 5, -2))
print(find_largest_and_smallest_numbers(3, 20, -2))
print(find_largest_and_smallest_numbers(7, 10, 0))
print(find_largest_and_smallest_numbers(10, 7, 0))
print(find_largest_and_smallest_numbers(0, 10.01, 10))


def quadratic_equation_solver(a, b, c):
    d=pow(b,2)-(4*a*c)

    x1 = (-b-cmath.sqrt(d)/(2*a))
    x2 = (-b +cmath.sqrt(d)/(2 * a))

    if (x1) and (x2):
        return (x1,x2)

    elif (x1) and (not(x2)):
        return (x1,None)

    elif (not(x1)) and (not(x2)):
        return (None,None)


# def quadratic_equation_solver_from_user_input(str_input):
#     quad = str_input.split(" ")
#     return quadratic_equation_solver(a=int(quad[0]),b=int(quad[1]),c=int(quad[2]))



def is_not_valid_input(user_str_input):
    if not len(user_str_input.split()) != 3:
        return "Too few variables, please enter 3 variables for the equation: "
    elif not re.match("^[0-9 -.]+$", user_str_input):
        return "Only numbers and spaces allowed, please enter 3 variables for the equation: "
    elif user_str_input.startswith("0"):
        return "First variable can't be 0, please enter 3 variables for the equation: "
    return False


def quadratic_equation_solver_from_user_input():
    user_str_input = input(
        "Please enter 3 variables for the equation in the \"a b c\" format: ")
    flag = True
    while flag:
        result = is_not_valid_input(user_str_input)
        if not result:
            flag = False
        else:
            user_str_input = input(result)

    variables = user_str_input.split()
    a = float(variables[0])
    b = float(variables[1])
    c = float(variables[2])
    return quadratic_equation_solver(a, b, c)



print(quadratic_equation_solver(1, 1.5, -1))
print(quadratic_equation_solver(1, -8, 16))
print(quadratic_equation_solver(1, -2, 34.5))
print(quadratic_equation_solver(4, -12, 9))




def temp_checker(min_temp, temp_1, temp_2, temp_3):
    # This function returns True if and only if 2 or more days that are warmer than the threshold
    temperature = (temp_1,temp_2,temp_3)
    days = 0
    for t in temperature:
        if t > min_temp:
            days +=1

    if days >=2:
        return True
    else:
        return False




print(temp_checker(26, 38, 90, 20))
print(temp_checker(10, 10, 10, 10))
print(temp_checker(10, 11, 10, 11))
print(temp_checker(-1, -9, 0, 1))
print(temp_checker(0, 90, 0, 1))
