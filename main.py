# Inbuilt module imports
import sys


# -----Global variables-----
num1 : float = 0
num2 : float = 0

# -----Main functions-----
def init():
    """
    This function handles initiation of this program.
    """    

    print("Add           : +\n")
    print("Subtract      : -\n")
    print("Multiply      : *\n")
    print("Divide        : /\n")
    print("Power         : ^\n")
    print("Remainder     : %\n")
    print("Terminate     : #\n")
    print("Reset         : $\n")

    # Get user's choice
    user_input = input("Enter choice (+,-,*,/,^,%,#,$) : ")

    # Choose operation
    choose_operations(user_input)


def choose_operations(user_input : str):
    """
    This function selects the operation according to the user input.

    Parameters:
        user_input (str): Input from the user
    """    
    if(user_input == "#"):
        print("Terminate!")
        sys.exit()
    else:
        if(user_input[-1] == "$"):
            init()
        else:
            if(user_input == "+"):
                get_numbers()
                add()
            elif(user_input == "-"):
                get_numbers()
                subtract()
            elif(user_input == "*"):
                get_numbers()
                multiply()
            elif(user_input == "/"):
                get_numbers()
                divide()
            elif(user_input == "^"):
                get_numbers()
                power()
            elif(user_input == "%"):
                get_numbers()
                remainder()
            else:
                print("Unrecognized operation!")


def get_numbers():
    """
    This function gets 2 numbers from the user.
    """ 

    global num1, num2

    num1 = input("Enter first number : ")
    num2 = input("Enter second number : ")


# -----Operator functions-----
def add():
    """
    This function provides the additon of 2 numbers.
    """ 

    if(num1 == 0):
        print("Enter first number!")
    elif(num2 == 0):
        print("Enter second number!")
    else:
        print(float(num1) + float(num2))
        init()


def subtract():
    """
    This function provides the subtraction of 2 numbers.
    """ 

    if(num1 == 0):
        print("Enter first number!")
    elif(num2 == 0):
        print("Enter second number!")
    else:
        print(float(num1) - float(num2))
        init()


def multiply():
    """
    This function provides the multiplication of 2 numbers.
    """ 
    
    if(num1 == 0):
        print("Enter first number!")
    elif(num2 == 0):
        print("Enter second number!")
    else:
        print(float(num1) * float(num2))
        init()


def divide():
    """
    This function provides the division of 2 numbers.
    """ 

    if(num1 == 0):
        print("Enter first number!")
    elif(num2 == 0):
        print("Enter second number!")
    else:
        print(float(num1) / float(num2))
        init()


def power():
    """
    This function provides the power of 2 numbers.
    """ 

    if(num1 == 0):
        print("Enter first number!")
    elif(num2 == 0):
        print("Enter second number!")
    else:
        print(float(num1) ** float(num2))
        init()


def remainder():
    """
    This function provides the remainder of 2 numbers.
    """ 

    if(num1 == 0):
        print("Enter first number!")
    elif(num2 == 0):
        print("Enter second number!")
    else:
        print(float(num1) % float(num2))
        init()


if __name__ == "__main__":
    init()