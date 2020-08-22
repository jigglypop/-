def solution(files):
    answer = []
    files_lower = [s.lower() for s in files]
    idx = 0
    file_all = []
    for file in files_lower:
        file_split = []
        temp = []
        number = ''
        for i in range(len(file)):
            try:
                file_int = int(file[i])

                if len(temp) == 0:
                    number += file[i]
                    temp.append(i)
                elif i- temp[-1] == 1:
                    number += file[i]
                    temp.append(i)
            except:
                continue
        number = int(number)
        file_split.append(file[:temp[0]])
        file_split.append(number)
        file_split.append(idx)
        file_all.append(file_split)
        idx += 1
    file_sort = sorted(file_all, key = lambda x : (x[0], x[1], x[2]))
    file_index = [file[2] for file in file_sort]
    for i in file_index:
        answer.append(files[i])
    return answer

solution(["img12.png", "img10.png", "img02img3.png", "img1.png", "IMG01.GIF", "img2.JPG"])