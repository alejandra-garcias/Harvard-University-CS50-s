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
