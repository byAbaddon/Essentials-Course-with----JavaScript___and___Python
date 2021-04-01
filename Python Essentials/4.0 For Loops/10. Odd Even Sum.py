loop = int(input())
num_list = [int(input()) for _ in range(loop)]
even_sum = sum(num_list[1::2])
odd_sum = sum(num_list[0::2])

print(f'Yes\nSum = {even_sum}' if even_sum == odd_sum else f'No\nDiff = {abs(even_sum - odd_sum)}')


'''
4
10
50
60
20
#Yes
#Sum = 70
'''