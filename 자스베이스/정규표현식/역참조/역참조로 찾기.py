import re


# text = "This is a block of of text,\nseveral words here are are\nrepeated, and and they\nshould not be."
text = "This is a block of of text, several words here are are repeated, and and theyshould not be."
# 방법 1
p = re.compile(r"[ ]+(\w+)[ ]+\1")
print(p.findall(text))
