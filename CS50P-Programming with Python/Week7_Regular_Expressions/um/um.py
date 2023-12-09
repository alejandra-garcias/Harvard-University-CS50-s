import re

def main():
    print(count(input("Text: ")))


def count(s):
    number_ums = 0
    find_ums = re.finditer(r'\bum\b', s, re.IGNORECASE)
    for match in find_ums:
        number_ums += 1
    return number_ums


if __name__ == "__main__":
    main()
