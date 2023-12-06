'''Even so, in a file called lines.py, implement a program that expects exactly one command-line argument, the name (or path) of a Python file, and outputs the number of lines of code in that file, excluding comments and blank lines. If the user does not specify exactly one command-line argument, or if the specified file’s name does not end in .py, or if the specified file does not exist, the program should instead exit via sys.exit.'''
import sys

def main():
    filename = get_valid_python_filename()
    output = count_lines(filename)
    print(output)


def get_valid_python_filename():
    # Checks there's only one command-line argument
    if  len(sys.argv) == 2:
        #Makes sure that it is a python file
        if sys.argv[1].endswith(".py"):
            return sys.argv[1].lstrip()
        else:
            sys.exit("Not a Python file")

    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

    else:
        sys.exit("Too many command-line arguments")



def count_lines(filename):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()

            non_empty_lines = [line.strip() for line in lines if line.strip() and not line.strip().startswith("#")]

            return len(non_empty_lines)
        
    except FileNotFoundError:
        sys.exit("File does not exist")



if __name__ == "__main__":
    main()
