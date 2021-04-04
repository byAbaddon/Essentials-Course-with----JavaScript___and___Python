dispenser = int(input())
queue_list = []

while True:
    current = input()
    if current == 'Start':
        break
    queue_list.append(current)


while True:
    token = input()
    if token == 'End':
        print(dispenser, 'liters left')
        break
    if len(token) <= 5:
        water = int(token)
        if dispenser >= water:
            dispenser -= water
            print(queue_list.pop(0), 'got water')
        else:
            goto_last_on_queue = queue_list.pop(0)
            print(goto_last_on_queue, 'must wait')
            queue_list.append(goto_last_on_queue)
    else:
        add_water = token.split(' ')[1]
        dispenser += int(add_water)




'''
2
Peter
Amy
Start
2
refill 1
1
End
#Peter got water
#Amy got water
#0 liters left
'''