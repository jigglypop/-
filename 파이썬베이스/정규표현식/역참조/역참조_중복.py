import re
text = "1121112"
print(re.findall(r"(\w)\1+|\w", text))
