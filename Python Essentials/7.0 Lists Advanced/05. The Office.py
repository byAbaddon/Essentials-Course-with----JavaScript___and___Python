employee_list = [int(x) for x in input().split()]
factor = int(input())

employee_list = list(map(lambda x: x * factor, employee_list))
average_factor = sum(employee_list) / len(employee_list)
happy_list = list(filter(lambda x: x >= average_factor, employee_list))

if len(happy_list) >= len(employee_list) / 2:
    print(f'Score: {len(happy_list)}/{len(employee_list)}. Employees are happy!')
else:
    print(f'Score: {len(happy_list)}/{len(employee_list)}. Employees are not happy!')



'''
1 2 3 4 2 1
3
#Score 2/6. Employees are not happy!
'''