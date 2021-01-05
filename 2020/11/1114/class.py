class Add:
    def __init__(self):
        self.var = "hello"

    def add(self, *args):
        print(self.var)
        return sum(args)


add = Add()
print(add.add(1, 2, 3, 4, 5))
