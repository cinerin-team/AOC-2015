class Day1:
    str = ""

    def __init__(self, file):
        with open(file) as f:
            for line in f.readlines():
                self.str += line[:-1]

    def task1(self):
        result = 0
        for letter in self.str:
            if letter == "(":
                result += 1
            else:
                result -= 1
        return str(result)

    def task2(self):
        result = 0
        for letter in range(len(self.str)):
            if self.str[letter] == "(":
                result += 1
            else:
                result -= 1
            if result < 0:
                return str(letter + 1)
