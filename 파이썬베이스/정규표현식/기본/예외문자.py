import re
text = 'We just received $10.00 for cookies.'
# string = re.findall('\$[0-9]+\.[0-9]+', text)
string = re.findall(r'\$[0-9.]+', text)
print(string)
