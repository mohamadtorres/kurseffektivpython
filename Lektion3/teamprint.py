from collections import abc

def calculate_salary():
    return 100

def calculate_whatever():
    #beräkning
    print("Calculate a lot of shit!")
    x = 200
    print("Done Calculating!")
    return x

def print_dekorator (func):
    print("Start function: " ,func)
    func()
    print("Ending")


salary = print_dekorator(calculate_salary)
whatever = print_dekorator(calculate_whatever)