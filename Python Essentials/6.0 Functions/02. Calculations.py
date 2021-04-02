def calc(command, n1, n2):
    result = 0
    if command == 'multiply':
        result = n1 * n2
    elif command == 'divide':
        result = n1 / n2
    elif command == 'add':
        result = n1 + n2
    else:
        result = n1 - n2

    return round(result)


print(calc(input(), int(input()), int(input())))


'''
divide
8
4
#2
'''