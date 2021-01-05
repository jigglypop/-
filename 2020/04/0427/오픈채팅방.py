def solution(record):
    print(record)
    id_dict = dict()
    recode_split = []
    for r in record:
        recode_split.append(r.split(' '))
    for recode in recode_split:
        if recode[0] == 'Enter':
            id_dict[recode[1]] = recode[2]
        if recode[0] == 'Change':
            id_dict[recode[1]] = recode[2]
    answer = []

    for recode in recode_split:
        if recode[0] == 'Enter':
            word = id_dict[recode[1]] + "님이 들어왔습니다."
            answer.append(word)
        elif recode[0] == 'Leave':
            word = id_dict[recode[1]] + "님이 나갔습니다."
            answer.append(word)
    return answer


solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo",
          "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"])
