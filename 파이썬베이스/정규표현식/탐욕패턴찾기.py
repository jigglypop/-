import re

text = "From: Using the: character"
string1 = re.findall('^F.+:', text)
string2 = re.findall('^F.+?:', text)

print(string1)
print(string2)
