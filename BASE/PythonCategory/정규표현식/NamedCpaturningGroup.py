import re
text = "문의사항이 있으면 032-232-3245 으로 연락주시기 바랍니다"


r = re.compile(r'(?P<area>\d{3})-(?P<num>\d{3}-\d{4})')
obj = r.search(text)
area = obj.group("area")
num = obj.group("num")
print(area)
print(num)
