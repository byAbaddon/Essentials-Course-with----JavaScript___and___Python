train_list = [0] * int(input())

for _ in range(100):
    token = [int(x) if x.isdigit() else x for x in input().split()]
    if token[0] == 'End':
        break

    if token[0] == 'add':
        people = train_list.pop()
        train_list.append(token[1] + people)
    elif token[0] == 'insert':
        people = train_list.pop(token[1])
        train_list.insert(token[1], token[2] + people)
    else:
        people = train_list.pop(token[1])
        train_list.insert(token[1], people - token[2])


print(train_list)



'''
3
add 20
insert 0 15
leave 0 5
End
#[10, 0, 20]
'''