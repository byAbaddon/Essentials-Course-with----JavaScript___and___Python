string = input()
stack_list = []

for index in range(len(string)):
    if string[index] == '(':
        stack_list.append(index)
    elif string[index] == ')':
        end_index = index + 1
        print(string[stack_list.pop():end_index])



'''
1 + (2 - (2 + 3) * 4 / (3 + 1)) * 5
'''