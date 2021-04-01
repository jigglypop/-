import re


text2 = "Pinging hog.forta.com [12.159.46.200]\
    with 32 bytes of data:"

# 방법 2
print(
    re.search("(((25[0-5])|(2[0-4]\d)|(1\d{2})|(\d{1,2}))\.){3}((25[0-5])|(2[0-4]\d)|(1\d{2})|(\d{1,2}))", text2).group())
