import re


text = "Send personal email to ben@forta.com or ben.forta@forta.com. For questions about a book use support@forta.com. \
Feel free to send unsolicited email to spam@forta.com (wouldn't it be nice if it were that simple, huh?)."

# 방법 1
print(re.findall(r"\w+@\w+\.\w+", text))
# 방법 1
print(re.findall(r"[\w.]+@[\w.]+\.\w+", text))
