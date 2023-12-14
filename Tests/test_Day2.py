from unittest import TestCase

from Days.Day2 import Day2


class TestDay1(TestCase):
    def test_task1(self):
        expected_value = str(58)
        actual_value = Day2('../Resources/Day2/test1').task1()
        self.assertEqual(expected_value, actual_value)

        expected_value = str(43)
        actual_value = Day2('../Resources/Day2/test2').task1()
        self.assertEqual(expected_value, actual_value)

    def test_task2(self):
        expected_value = str(34)
        actual_value = Day2('../Resources/Day2/test1').task2()
        self.assertEqual(expected_value, actual_value)

        expected_value = str(14)
        actual_value = Day2('../Resources/Day2/test2').task2()
        self.assertEqual(expected_value, actual_value)
