kids_list = input().split()
index = int(input())

while len(kids_list) != 1:
    for i in range(1, index + 1):
        if i != index:
            out_in_queue = kids_list.pop(0)
            kids_list.append(out_in_queue)
        else:
            rm_kid = kids_list.pop(0)
            print('Removed', rm_kid)


print('Last is', kids_list[0])



'''
Tracy Emily Daniel
2
#Removed Emily
#Removed Tracy
#Last is Daniel
'''