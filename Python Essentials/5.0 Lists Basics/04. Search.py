loop = int(input())
word = input()
strings_list = [input() for _ in range(loop)]
filter_list = [x for x in strings_list if word in x]
print(f'{strings_list}\n{filter_list}')


'''
3
SoftUni
I study at SoftUni
I walk to work
I learn Python at SoftUni
#['I study at SoftUni', 'I walk to work', 'I learn Python at SoftUni']
#['I study at SoftUni', 'I learn Python at SoftUni']
'''