class load_number:

    def __init__(self, path) -> None:
        self.path = path
    
    def load(self):
        f = open(self.path, "r")
        y = []
        for value in f:
            y.append(value.rstrip("\n"))
        f.close()
        return y

# result = load_number("number/8.txt")
# x = result.load()
# print(x)