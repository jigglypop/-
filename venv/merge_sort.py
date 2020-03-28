def merge(arr):
    # arr 크기가 1보다 작으면 그대로 리턴
    if len(arr) <= 1:
        return arr

    # arr를 low와 high로 나눈다. 그리고 각각 l,h를 놓는다.
    mid = len(arr) // 2

    # 재귀함수로 먼저 쪼개놓고 합치기 시작한다.
    low = merge(arr[:mid])
    high = merge(arr[mid:])
    buff = []
    l = h = 0

    # low나 high를 둘중 하나를 다 순회할 때까지 buff에 작은 순서대로 넣고 합친다.
    while l < len(low) and h < len(high):
        # 작은것 넣고 한칸씩 밀어준다.
        if low[l] < high[h]:
            buff.append(low[l])
            l += 1
        else:
            buff.append(high[h])
            h += 1

    # 남은것 합침
    buff += low[l:]
    buff += high[h:]
    return buff

arr = [1, 4, 3, 5, 2, 6, 8, 7, 9, 7]
print(merge(arr))