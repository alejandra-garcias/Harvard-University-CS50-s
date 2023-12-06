'''In a file called pizza.py, implement a program that expects exactly one command-line argument, the name (or path) of a CSV file in Pinocchio’s format, and outputs a table formatted as ASCII art using tabulate, a package on PyPI at pypi.org/project/tabulate. Format the table using the library’s grid format. If the user does not specify exactly one command-line argument, or if the specified file’s name does not end in .csv, or if the specified file does not exist, the program should instead exit via sys.exit.'''
import sys
import csv
from tabulate import tabulate

def main():
    filename = get_valid_csv_filename()
    output = display_csv(filename)
    print(output)


def get_valid_csv_filename():
    # Checks there's only one command-line argument
    if  len(sys.argv) == 2:
        #Makes sure that it is a python file
        if sys.argv[1].endswith(".csv"):
            return sys.argv[1].lstrip()
        else:
            sys.exit("Not a CSV file")

    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

    else:
        sys.exit("Too many command-line arguments")



def display_csv(filename):
    try:
        with open(filename) as file:
            reader = csv.reader(file)
            menu_list = [row for row in reader]
            print(tabulate(menu_list, headers="firstrow", tablefmt="grid").strip())
    except FileNotFoundError:
        sys.exit("File does not exist")



if __name__ == "__main__":
    main()
