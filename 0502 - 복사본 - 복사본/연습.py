import re
p = re.compile('[^a-z]')
lst = 'ab@cde#f'
r = re.split(p, lst)
print(r)
