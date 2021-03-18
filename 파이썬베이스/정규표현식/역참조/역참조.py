import re


text = " <body>\n<h1>Welcome to my Homepage</h1>\nContent is divided into two sections:<br/>\n<h2>SQL</h2>\nInformation about SQL.\n<h2>RegEx</h2>\nInformation about Regular Expressions.\n</body>"

# 방법 1
print(re.findall(r"<[hH]1>.*<\/[hH]1>", text))
# 방법 2
print(re.findall(r"<[hH][1-6]>.*<\/[hH][1-6]>", text))
# 역참조
print(re.findall(r"<[hH]([1-6])>.*<\/[hH]\1>", text))
