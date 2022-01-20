# calculator - 1-addition, 2-subtraction, 3-multiplication, 4-division, 5-exit
# enter 2 numbers in terminal.

def select_operation():
    return int(input("1-Addition, 2-Subtraction, 3-Multiplication, 4-Division, 5-Exit : "))


def select_input():
    number1 = float(input("Enter first number : "))
    number2 = float(input("Enter second number : "))
    return number1, number2


def addition(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiple(n1, n2):
    return n1 * n2


def division(n1, n2):
    return n1 / n2


try:
    operation = select_operation()
    while operation != 5:
        if operation == 1:
            try:
                num1, num2 = select_input()
                print("Addition of 2 numbers is ", addition(num1, num2))
            except:
                print("the numbers are not valid")
        elif operation == 2:
            try:
                num1, num2 = select_input()
                print("Subtraction of 2 numbers is ", subtract(num1, num2))
            except:
                print("the numbers are not valid")
        elif operation == 3:
            try:
                num1, num2 = select_input()
                print("Multiplication of 2 numbers is ", multiple(num1, num2))
            except:
                print("the numbers are not valid")
        elif operation == 4:
            try:
                num1, num2 = select_input()
                try:
                    print("Division of 2 numbers is ", division(num1, num2))
                except:
                    print("Divide by 0 exception")
            except:
                print("The number is invalid")

        try:
            operation = select_operation()
        except:
            print("the option is not an integer value")
    else:
        print("We are exiting now!!! Bye!!!")
except:
    print("The entered option is not an integer value")
