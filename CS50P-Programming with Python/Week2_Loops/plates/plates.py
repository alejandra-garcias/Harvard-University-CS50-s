'''In Massachusetts, home to Harvard University, it’s possible to request a vanity license plate for your car, with your choice of letters and numbers instead of random ones. Among the requirements, though, are:

“All vanity plates must start with at least two letters.”
“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
“Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
“No periods, spaces, or punctuation marks are allowed.”
In plates.py, implement a program that prompts the user for a vanity plate and then output Valid if meets all of the requirements or Invalid if it does not. Assume that any letters in the user’s input will be uppercase. Structure your program per the below, wherein is_valid returns True if s meets all requirements and False if it does not. Assume that s will be a str. You’re welcome to implement additional functions for is_valid to call (e.g., one function per requirement).'''

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    #Restricciones de tamaño
    if 2 <= len(s) <= 6:
        #Invalidar si se usa simbolo
        for c in s:
            if c in['.',' ','!','?']:
                return False
        #Validar si todos son letras
        if s.isalpha():
            return True
        #Validar que al menos los primeros 2 caracteres son letras
        elif s[0:2].isalpha():
            #Comprobar que los digitos estan al final de la placa
            idx = -1
            while idx >= -len(s) and s[idx].isdigit():
                idx -= 1

            if 1 <= len(s[idx + 1:]) <= 4 and s[idx + 1:].isdigit() and s[idx + 1] != '0':
                return True



    return False

main()
