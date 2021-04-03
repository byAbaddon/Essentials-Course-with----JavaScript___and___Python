num_list = [int(x) for x in input().split(', ')]
print([i for i in range(len(num_list)) if not num_list[i] & 1])



'''
3, 2, 1, 5, 8
#[1, 4]
'''