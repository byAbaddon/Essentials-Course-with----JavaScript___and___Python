row, col = input().split(', ')
matrix = [[int(col) for col in input().split()] for _ in range(int(row))]
[print(sum([row[i] for row in matrix])) for i in range(0, len(matrix[0]))]

'''
3, 6
7 1 3 3 2 1
1 3 9 8 5 6
4 6 7 9 1 0
'''