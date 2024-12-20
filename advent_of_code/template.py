import unittest

data = """
"""


def parse(data: str):
    return data


def solve1():
    pass


def solve2():
    pass


class Tests(unittest.TestCase):
    def test_parse(self):
        self.assertEqual(parse(""), None)

    def test_solve1(self):
        self.assertEqual(solve1(), None)

    def test_solve2(self):
        self.assertEqual(solve2(), None)


if __name__ == "__main__":
    print(solve1())
    print(solve2())
    unittest.main()
