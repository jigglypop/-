import re


text = "This offer is not available to customers living in <b>AK</b> and <b>HI</b>"

# 방법 1
print(re.findall(r"<[Bb]>.*<\/[Bb]>", text))
# 게으른 수량자
print(re.findall(r"<[Bb]>.*?<\/[Bb]>", text))
