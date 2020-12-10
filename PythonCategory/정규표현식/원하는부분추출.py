import re
text = "From chlgmltn101@naver.com Sat Jan  5 09:14:16 2019"
# 1. \S 공백 아닌 문자 찾기
string1 = re.findall('\S+@\S+', text)
# 2. 소괄호
string2 = re.findall('From (\S+@\S+)', text)

# 이메일 호스트 출력
string3 = re.findall('@([^ ]+)', text)
print(string1)
print(string2)
print(string3)
