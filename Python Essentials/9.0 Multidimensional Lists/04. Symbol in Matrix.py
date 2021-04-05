matrix_size = int(input())
matrix = [' '.join(input()).split() for i in range(matrix_size)]
symbol = input()

for r in range(len(matrix)):
    for c in range(len(matrix)):
        if matrix[r][c] == symbol:
            print(f'({r}, {c})')
            exit()

print(symbol, 'does not occur in the matrix')


'''
3
ABC
DEF
X!@
!
#(2, 1)
'''