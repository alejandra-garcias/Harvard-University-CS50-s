
#Asking user for word
input = input("Input: ")

#Iterating through vowels:

for char in input:
    if char in 'aeiouAEIOU':
        input = input.replace(char,'')

print(f'Output: {input} ')


