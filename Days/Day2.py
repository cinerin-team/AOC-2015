from Utilities.read_file_to_string_array import read_to_array


class Day2:
    arr = []

    def __init__(self, file):
        self.arr.clear()
        self.arr = read_to_array(file)

    def task1(self):
        result = 0
        for element in self.arr:
            nums = element.split("x")
            x = int(nums[0])
            y = int(nums[1])
            z = int(nums[2])

            result += x * y * 2 + x * z * 2 + z * y * 2 + min(x * y, x * z, y * z)

        return str(result)

    def task2(self):
        result = 0
        for element in self.arr:
            nums = element.split("x")
            x = int(nums[0])
            y = int(nums[1])
            z = int(nums[2])

            ab = self.ket_minimum(x, y, z)

            result += ab[0] * 2 + ab[1] * 2 + x * y * z

        return str(result)

    def ket_minimum(self, x, y, z):
        maxim = max(x, y, z)
        if x == maxim:
            result = (y, z)
        elif y == maxim:
            result = (x, z)
        else:
            result = (x, y)

        return result
