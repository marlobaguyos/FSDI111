def separator():
    print("-" * 30)

def print_menu():
    print('\n' * 5)
    separator()
    print('Welcome to PyCalc')
    separator()

    print('[1] - Add')
    print('[2] - Substract')
    print('[3] - Multiply')
    print('[4] - Divide')

    print('[x] - Close')

    separator()

def sum(num1, num2):
    return num1 + num2

def substract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    while num2 == 0:
        input('Devide by ZERO? Nope Try again: ')
    else:
        return num1 / num2

opc = ''
while(opc != 'x'):
    print_menu()
    opc = input('Please select an option: ')
    print('Selected: ' + opc)
    if(opc == 'x'):
        break # break = finish loop here and get out of the loop

    num1 = float(input('First number: '))
    num2 = float(input('Second number: '))

    if(opc == '1'):
        res = sum(num1, num2)
        print('Addition my good sir.')
        print("Result: " + str(res))
    elif(opc == '2'):
        print('You have selected Substraction my good sir.')
        print("Result: " + str(substract(num1, num2)))
    elif(opc == '3'):
        print('You have selected Multiplication my good sir.')
        print("Result: " + str(multiply(num1, num2)))
    elif(opc == '4'):
        print('You have selected Division my good sir.')
        print("Result: " + str(divide(num1, num2)))
            

    input("Press Enter to continue...")

print("Byte byte!")
