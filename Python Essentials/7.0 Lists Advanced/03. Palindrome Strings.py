strings = input().split(' ')
search_word = input()

palindrome_list = []

for word in strings:
    if word == word[::-1]:
        palindrome_list.append(word)

print(f'{palindrome_list}\nFound palindrome {palindrome_list.count(search_word)} times')



'''
wow father mom wow shirt stats
wow
#['wow', 'mom', 'wow', 'stats']
#Found palindrome 2 times
'''