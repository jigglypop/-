def solution(cacheSize, cities):
    answer = 0
    cache_array = [' '] * cacheSize

    for city in cities:
        city_lowered = city.lower()
        if city_lowered in cache_array:
            answer = answer + 1
            cache_array.remove(city_lowered)
            cache_array.append(city_lowered)
        else:
            answer += 5
            cache_array.append(city_lowered)
            cache_array.pop(0)
    return answer