row, col = input().split(', ')
matrix = [[int(col) for col in input().split(', ')] for _ in range(int(row))]
print(sum([sum(row) for row in matrix]))
print(matrix)


'''
3, 6
7, 1, 3, 3, 2, 1
1, 3, 9, 8, 5, 6
4, 6, 7, 9, 1, 0
'''