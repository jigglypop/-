def generator():
    for i in range(10):
        yield i


# def generator():
#     for i in range(10):
#         return i


for i in generator():
    print(i)
