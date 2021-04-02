def shop(item_kind, count ):
    items_dict = {'coffee': 1.50, 'water': 1.00, 'coke': 1.40, 'snacks': 2.00}
    return f'{(items_dict[item_kind] * count):.2f}'


print(shop(input(), int(input())))



'''
water
5
#5.00
'''