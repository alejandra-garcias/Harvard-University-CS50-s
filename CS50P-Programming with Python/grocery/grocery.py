grocery= {

}

while True:
    try:
        item = input().upper()
        if item in grocery:
            grocery[item] += 1
        else:
            grocery[item] = 1

    except EOFError:
        for key, value in sorted(grocery.items()):
            print(f'{value} {key}')
        break

