'''Fuel gauges indicate, often with fractions, just how much fuel is in a tank. For instance 1/4 indicates that a tank is 25% full, 1/2 indicates that a tank is 50% full, and 3/4 indicates that a tank is 75% full.

In a file called fuel.py, implement a program that prompts the user for a fraction, formatted as X/Y, wherein each of X and Y is an integer, and then outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank. If, though, 1% or less remains, output E instead to indicate that the tank is essentially empty. And if 99% or more remains, output F instead to indicate that the tank is essentially full.

If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again. (It is not necessary for Y to be 4.) Be sure to catch any exceptions like ValueError or ZeroDivisionError.'''

def main():
    value = get_fraction('Fraction: ')
    if value <= 0.01:
        print('E')
    elif value >= 0.99:
        print('F')
    else:
        print(f'{value:.0%}')

def get_fraction(prompt):
    while True:
        try:
            value = input(prompt)
            split = value.split('/')
            list = []
            for num in split:
                list.append(int(num))
            if list[0] > list[1]:
                raise ValueError
        except (ValueError, ZeroDivisionError):
            pass
        else:
            fraction = list[0] / list[1]
            return fraction

main()