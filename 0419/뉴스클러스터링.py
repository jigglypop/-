import re
from collections import Counter


pattern = re.compile('[a-z][a-z]')
    
def preprocessing(content):
    result = []
    for i in range(0, len(content)-1):
        two_letter = content[i:i+2]
        if pattern.search(two_letter):
            result.append(two_letter)
    print(result)
    return result
    

def solution(str1, str2):
    # 두 개의 문자열에 대해서 소문자로 처리
    str1 = str1.lower()
    str2 = str2.lower()
    
    if str1 == str2: # 일치한다면 유사도는 1
        return 65536
    
    str1 = preprocessing(str1)
    str2 = preprocessing(str2)
    
    counter_1 = Counter(str1)
    counter_2 = Counter(str2)
            
    intersections = counter_1 & counter_2 # 교집합
    intersections = sum(list(intersections.values()))
    
    unions = counter_1 | counter_2 # 합집합
    unions = sum(list(unions.values()))
    return int(intersections/unions * 65536)
