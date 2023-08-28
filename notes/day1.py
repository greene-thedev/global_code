#importing stuff
import math

# Converting pi radian to degrees

rad = input("Please enter your value in rad: ")

def rad_to_deg(rad):
    cast_rad = int(rad)
    deg = (math.pi * cast_rad) / 180
    # print(round(deg, 2))
    return deg

# calling the function
result = rad_to_deg(56)
print(result)


########################################################################


def calculate(operation, num1, num2):
    operation = input('enter an operation in full ')
    num1 = int(input('enter the first number '))
    num2 = int(input('enter the second number '))

    # todo: master code below
    
    if operation == 'add':
        print(num1 + num2)
    elif operation == 'subtract':
        print(num1 - num2)
    elif operation == 'divide':
        print(num1 / num2)
    elif operation == 'multiply':
        print(num1 * num2)

    return 'keep that in mind'
    

print(calculate('add', 1,4))

# todo: delete if above is mastered.