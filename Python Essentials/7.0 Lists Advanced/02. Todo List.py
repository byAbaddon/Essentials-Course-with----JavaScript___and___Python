item_dict = {}

while True:
    command = input()
    if command == 'End':
        break
    key, val = command.split("-")
    item_dict[int(key)] = val


sort_dict = dict(sorted(item_dict.items(), key=lambda x:  x[0]))
print(list(sort_dict.values()))




'''
2-Walk the dog
1-Drink coffee
6-Dinner
5-Work
End
#['Drink coffee', 'Walk the dog', 'Work', 'Dinner']
'''