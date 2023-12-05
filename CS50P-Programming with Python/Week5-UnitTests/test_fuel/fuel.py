def main():
    fraction = input("Fraction: ")
    fraction_converted = convert(fraction)
    output = gauge(fraction_converted)
    print(output)

def convert(fraction):
    while True:
        try:
            x,y = fraction.split("/")
            int_x = int(x)
            int_y = int(y)
            new_value = int_x / int_y
            if new_value <=1:
                percent = int(new_value*100)
                return percent
            else:
                fraction = input("Fraction: ")
                pass
        except(ValueError,ZeroDivisionError):
            raise


def gauge(percentage):
    if percentage <=1:
        return "E"
    elif percentage>=99:
        return "F"
    else:
        return str(percentage)+"%"


if __name__ == "__main__":
    main()


