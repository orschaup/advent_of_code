import unittest

data = """
"""


def parse(data: str):
    return data


def solve1():
    pass


def solve2():
    pass


testData = """
"""


class Tests(unittest.TestCase):
    def test_solve1(self):
        self.assertEqual(solve1(*parse(testData)), None)

    def test_solve2(self):
        self.assertEqual(solve2(*parse(testData)), None)


if __name__ == "__main__":
    print(solve1())
    print(solve2())
    unittest.main()
