import re


def compare(p, word):
    p_split = p.replace(".", '[.](1-3)')
    ptr = '[' + "|".join(p_split) + ']'
    print(re.findall("A[A-Z]{1,2}[A-Z]{1,2}C", word))
    # print(re.findall("[^A|B|C]", "ABCDC"))

compare("A.C", "ABCDC")