import re


# def front_back(word):
#     front_set = set()
#     front_set = set()
#     for i in range(1, len(word)+1):
#         print(word[:i])
a = 'abcde'

p = re.compile('ab...')
m = p.match(a)

# front_back('abcde')
if m:
    print('Match found: ', m.group())
else:
    print('No match')
