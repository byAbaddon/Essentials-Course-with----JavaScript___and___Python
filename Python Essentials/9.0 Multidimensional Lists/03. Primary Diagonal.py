matrix_size = int(input())
matrix = [[int(el) for el in input().split()] for _ in range(matrix_size)]
print(sum([matrix[i][i] for i in range(len(matrix))]))


'''
3
11 2 4
4 5 6
10 8 -12
#4
'''