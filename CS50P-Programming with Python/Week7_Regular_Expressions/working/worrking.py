import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    time = re.search(r'^([0-9]+):?([0-5][0-9])? (AM|PM) to ([0-9]+):?([0-5][0-9])? (AM|PM)$', s)

    if time:
        if int(time.group(1)) | int(time.group(4)) > 12 or int(time.group(2)) | int(time.group(5)) >= 60:
            raise ValueError

        else:

            if (time.group(3)) == 'PM'and (time.group(6)) == 'PM':
                connverted_1 = str(int(time.group(1)) + 12)
                connverted_2 = str(int(time.group(4)) + 12)
                return f'{connverted_1}:{time.group(2)} to {connverted_2}:{time.group(5)}'

            elif (time.group(6)) == 'PM':
                connverted_2 = str(int(time.group(4)) + 12)
                return f'{time.group(1)}:{time.group(2)} to {connverted_2}:{time.group(5)}'
            elif (time.group(3)) == 'PM':
                connverted_1 = str(int(time.group(1)) + 12)
                return f'{connverted_1}:{time.group(2)} to {time.group(4)}:{time.group(5)}'
            else:
                return f"{time.group(1)}:{time.group(2)} to {time.group(4)}:{time.group(5)}"









if __name__ == "__main__":
        main()

