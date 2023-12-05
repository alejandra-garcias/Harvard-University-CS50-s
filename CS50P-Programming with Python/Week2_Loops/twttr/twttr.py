'''When texting or tweeting, it’s not uncommon to shorten words to save time or space, as by omitting vowels, much like Twitter was originally called twttr. In a file called twttr.py, implement a program that prompts the user for a str of text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.'''

#Asking user for word
input = input("Input: ")

#Iterating through vowels:

for char in input:
    if char in 'aeiouAEIOU':
        input = input.replace(char,'')

print(f'Output: {input} ')


