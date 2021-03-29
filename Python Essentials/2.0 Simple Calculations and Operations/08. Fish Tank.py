long, width, height, percent = [float(input()) for _ in range(4)]
size = long * width * height * 0.001
pr = percent * 0.01
print(f'{size * (1 - pr):.3f}')

 
'''
85
75
47
17
#248.689
'''
