import string
def solution(msg):
    msg_lower = list(msg.lower())
    answer = []
    lower = ['1'] +  list(string.ascii_lowercase)
    i = 0
    while i < len(msg_lower):
        temp = []
        w = ''
        for j in range(i,len(msg_lower)):
            w += msg_lower[j]
            temp.append(w)
            j += 1
        for j in range(len(temp)-1,-1,-1):
            if temp[j] in lower:
                lower.append(w)
                answer.append(lower.index(temp[j]))
                i += j+1
                break
            else:
                w = temp[j]
    return answer


solution('ABABABABABABABAB')