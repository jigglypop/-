import re
text = "문의사항이 있으면 032-232-3245 으로 연락주시기 바랍니다"

# r = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
r = re.compile(r'\d{3}-\d{3}-\d{4}')
obj = r.search(text)
phone = obj.group()
print(phone)
