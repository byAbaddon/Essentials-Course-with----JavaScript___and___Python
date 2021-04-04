queue_list = []

while True:
    current = input()
    if current == 'End':
        break

    if current != 'Paid':
        queue_list.append(current)
    else:
        print('\n'.join(queue_list))
        queue_list = []


print(len(queue_list), 'people remaining.')


'''
Anna
Emma
Alexander
End
#3 people remaining.
'''