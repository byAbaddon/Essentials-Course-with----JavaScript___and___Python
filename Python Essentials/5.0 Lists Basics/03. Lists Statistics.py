num_list = [int(input()) for _ in range(int(input()))]
positive = [el for el in num_list if el >= 0]
negative = [el for el in num_list if el < 0]
print(f'{positive}\n{negative}\nCount of positives: {len(positive)}. Sum of negatives: {sum(negative)}')


'''
5
10
3
2
-15
-4
#[10, 3, 2]
#[-15, -4]
'''