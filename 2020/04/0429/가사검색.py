import re


def make_match(query, words):
    count = 0
    for word in words:
        q = query.replace('?', '.')
        m = re.match(q, word)
        if m and len(q) == len(word):
            count += 1
    return count


def solution(words, queries):
    answer = []
    word = words[0]
    for query in queries:
        num = make_match(query, words)
        answer.append(num)
    return answer


print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], [
      "fro??", "????o", "fr???", "fro???", "pro?"]))
