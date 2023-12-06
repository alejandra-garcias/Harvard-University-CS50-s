'''In a file called scourgify.py, implement a program that:

Expects the user to provide two command-line arguments:
the name of an existing CSV file to read as input, whose columns are assumed to be, in order, name and house, and
the name of a new CSV to write as output, whose columns should be, in order, first, last, and house.
Converts that input to that output, splitting each name into a first name and last name. Assume that each student will have both a first name and last name.
If the user does not provide exactly two command-line arguments, or if the first cannot be read, the program should exit via sys.exit with an error message.'''

import sys
import csv


def main():
    before,after = get_valid_csv_filenames()
    rewriting_lines(before, after)



def get_valid_csv_filenames():
    # Checks there's only one command-line argument
    if  len(sys.argv) == 3:
        #Makes sure that it is a python file
        if sys.argv[1].endswith(".csv") and sys.argv[2].endswith(".csv"):
            return sys.argv[1].lstrip(), sys.argv[2].lstrip()
        else:
            sys.exit("Not a CSV file")

    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    else:
        sys.exit("Too many command-line arguments")



def rewriting_lines(before, after):
    try:
        with open(before, 'r') as file_before, open(after, 'w', newline='') as file_after:
            # Inicializar DictWriter para escribir en el archivo 'after'
            fieldnames = ['first', 'last', 'house']
            csv_writer = csv.DictWriter(file_after, fieldnames=fieldnames)

            # Escribir la línea de encabezado en el archivo 'after'
            csv_writer.writeheader()

            # Ignorar la primera línea en el archivo 'before'
            next(file_before)

            # Procesar cada línea del archivo 'before' y escribir en 'after'
            for line in file_before:
                row = line.rstrip().split('",')
                full_name = row[0].strip('"')
                last_name, first_name = map(str.strip, full_name.split(','))
                last_name = last_name.rstrip(',')
                first_name = first_name.lstrip()
                new_line = {'first': first_name, 'last': last_name, 'house': row[1]}
                csv_writer.writerow(new_line)
    except FileNotFoundError:
        sys.exit("File does not exist")



if __name__ == "__main__":
    main()
