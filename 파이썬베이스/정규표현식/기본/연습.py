import re
text = "문의사항이 있으면 032-232-3245 으로 연락주시기 바랍니다"

counts = text.count(r'[0-9]+')
print(counts)
print(re.search('(?<=<p>)\w+(?=</p>)', 'Kakao <p>ryan</p> keep a straight face.').group())