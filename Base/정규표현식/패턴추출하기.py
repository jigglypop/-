import re
text = "My favorite numbers are 19 and 43 and 123455"
num = re.findall('[0-9]+', text)
string = re.findall('[aeiou]+', text)
print(num)
print(string)
