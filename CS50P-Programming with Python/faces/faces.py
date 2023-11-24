def main():
    emoji = input("Type in ")
    convert(emoji)

def convert(emoji):
    x =(emoji).replace(":)","🙂").replace(":(","🙁")
    print(x)


main()
