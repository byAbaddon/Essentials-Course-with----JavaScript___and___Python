string = input()
sums = 0
letters_dict = {'a': 1, 'e': 2, 'i': 3, 'o': 4, 'u': 5}

for l in string:
    if l in letters_dict:
        sums += letters_dict[l]

print(sums)

#hello
