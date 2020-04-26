def separator():
    print("-" * 30)

def print_menu():
    separator()
    print('Welcome to PyCalc')
    separator()

    print('[1] - Add')
    print('[2] - Substract')

    def sum(num1, num2):
        return num1 + num2

opc = ''
while(opc != 'x'):
    print_menu()
    opc = input('Please select an option: ')
    print('user choose: ' + opc)

    num1 = float(input('First number: '))
    num2 = float(input('Second number: '))

    if(opc == 1):
        res = sum(num1, num2)
        print("Result: " + str(res))

print("Byte byte!")
