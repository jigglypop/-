import re
text = "Hello, my name is Ben&nbsp;Forta, and I am\
    the author of multiple books on SQL (including\
     MySQL, Oracle PL/SQL, and SQL Server T-SQL),\
    Regular&nbsp;&nbsp;Expressions, and other subjects."

# 실패
print(re.search('&nbsp;{2,}', text))
# 성공
print(re.search('(&nbsp;){2,}', text).group())


text2 = "Pinging hog.forta.com [12.159.46.200]\
    with 32 bytes of data:"

# 방법 1
print(re.search("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", text2).group())
# 방법 2
print(re.search("(\d{1,3}\.){3}\d{1,3}", text2).group())


text3 = "ID: 042\
    SEX: M\
    DOB: 1967-08-17\
    Status: Active"

# 실패
print(re.search("19|20\d{2}", text3).group())
# 성공
print(re.search("(19|20)\d{2}", text3).group())
