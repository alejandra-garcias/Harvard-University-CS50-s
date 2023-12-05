
def main():
    word = input("Input: ")
    output = shorten(word)
    print(f'Output: {output} ')



def shorten(word):
    for char in word:
        if char in 'aeiouAEIOU':
            word = word.replace(char,'')
    return word


if __name__ == "__main__":
    main()
