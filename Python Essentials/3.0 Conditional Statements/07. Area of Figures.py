def area_of_figures(figure):
    num_a = float(input())
    num_b = 0
    if figure == 'rectangle' or figure == 'triangle':
        num_b = float(input())

    switch = {
        'square': num_a * num_a,
        'rectangle': num_a * num_b,
        'circle':  num_a * num_a * 3.14159,
        'triangle': num_a * num_b / 2,
    }
          
    return  f'{switch[figure]:.3f}'


print(area_of_figures(input()))

