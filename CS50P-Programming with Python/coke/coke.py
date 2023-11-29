amount_due = 50
print(f'Amount due: {amount_due}')

while amount_due > 0:
    #Ask user to enter coin
    coin = int(input("Insert coin: "))
    #Check that coin is valid
    if coin not in [25, 10, 5]:
        amount_due
    else:
        amount_due -= coin

    #Printing amount due
    if amount_due >0:
        print(f'Amount Due: {amount_due}')

    #Printing change
    if amount_due <= 0:
        change_owed = abs(amount_due)
        print(f'Change Owed: {change_owed}')
