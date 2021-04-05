row, col = input().split(', ')
matrix = [[int(col) for col in input().split(', ')] for _ in range(int(row))]
save_big_square = ''
big_square_sum = 0

for r in range(len(matrix) - 1):
    for c in range(len(matrix[r]) - 1):
        current_square = matrix[r][c] + matrix[r][c + 1] + matrix[r + 1][c] + matrix[r + 1][c + 1]
        if current_square > big_square_sum:
            big_square_sum = current_square
            save_big_square = f'{matrix[r][c]} {matrix[r][c + 1]}\n{matrix[r + 1][c]} {matrix[r + 1][c + 1]}'

print(save_big_square)
print(big_square_sum)


'''
3, 6
7, 1, 3, 3, 2, 1
1, 3, 9, 8, 5, 6
4, 6, 7, 9, 1, 0
#9 8
#7 9
#33
'''