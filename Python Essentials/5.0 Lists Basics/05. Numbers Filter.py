num_list = [int(input()) for _ in range(int(input()))]
command = input()


def calc(type_command):
    switch_command = {
            'even': list(filter(lambda x: not x & 1, num_list)),
            'odd': list(filter(lambda x: x & 1, num_list)),
            'negative': list(filter(lambda x: x < 0, num_list)),
            'positive': list(filter(lambda x: x >= 0, num_list)),
            }

    return switch_command.get(type_command)


print(calc(command))



'''
5
33
19
-2
18
998
even
#[-2, 18, 998]
'''