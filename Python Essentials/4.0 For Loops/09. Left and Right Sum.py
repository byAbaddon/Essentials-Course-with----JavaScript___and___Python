loop = int(input())
num_list = [int(input()) for _ in range(loop * 2)]
left_sum = sum(num_list[0:loop])
right_sum = sum(num_list[loop:])

print(f'Yes, sum = {left_sum}' if left_sum == right_sum else f'No, diff = {abs(left_sum - right_sum)}')


'''
2
10
90
60
40
#Yes, sum = 100
'''

