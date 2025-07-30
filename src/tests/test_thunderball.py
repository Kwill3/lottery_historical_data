import unittest
from thunderball import loadThunderball
from lottery_class import Lottery, Draw_Type, NumberOutOfRangeError, ListLenMismatchError

class TestThunderball(unittest.TestCase):
    def setUp(self):
        self.test_1 = Lottery(Draw_Type.THUNDERBALL)
        self.test_1.main_numbers = ["1", "2", "3", "4", "5"]
        self.test_1.special_numbers = ["14"]

    def test_main_num_len(self):
        # length of 6 - exceeding length
        self.test_1.main_numbers = ["1", "2", "3", "4", "5", "6"]
        with self.assertRaises(ListLenMismatchError):
            loadThunderball(self.test_1)
        # length of 3 - insufficient length
        self.test_1.main_numbers = ["1", "2", "3"]
        with self.assertRaises(ListLenMismatchError):
            loadThunderball(self.test_1)
        # blank array
        self.test_1.main_numbers = []
        with self.assertRaises(ListLenMismatchError):
            loadThunderball(self.test_1)
        # correct length
        self.test_1.main_numbers = ["1", "2", "3", "4", "5"]
        output = loadThunderball(self.test_1)
        assert output["main_numbers"].item() == "1,2,3,4,5"

    def test_main_num_oor(self):
        # number below 1
        self.test_1.main_numbers = ["0", "10", "12", "30", "39"]
        with self.assertRaises(NumberOutOfRangeError):
            loadThunderball(self.test_1)
        # number above 39
        self.test_1.main_numbers = ["1", "10", "12", "30", "40"]
        with self.assertRaises(NumberOutOfRangeError):
            loadThunderball(self.test_1)
        # negative value
        self.test_1.main_numbers = ["1", "10", "-12", "30", "39"]
        with self.assertRaises(NumberOutOfRangeError):
            loadThunderball(self.test_1)
        # correct range
        self.test_1.main_numbers = ["1", "10", "12", "30", "39"]
        output = loadThunderball(self.test_1)
        assert output["main_numbers"].item() == "1,10,12,30,39"

    def test_special_num_len(self):
        # length of 2 - exceeding length
        self.test_1.special_numbers = ["1", "2"]
        with self.assertRaises(ListLenMismatchError):
            loadThunderball(self.test_1)
        # blank array
        self.test_1.special_numbers = []
        with self.assertRaises(ListLenMismatchError):
            loadThunderball(self.test_1)
        # correct length
        self.test_1.special_numbers = ["10"]
        output = loadThunderball(self.test_1)
        assert output["thunderball"].item() == "10"

    def test_special_num_oor(self):
        # number below 1
        self.test_1.special_numbers = ["0"]
        with self.assertRaises(NumberOutOfRangeError):
            loadThunderball(self.test_1)
        # number above 14
        self.test_1.special_numbers = ["15"]
        with self.assertRaises(NumberOutOfRangeError):
            loadThunderball(self.test_1)
        # negative value
        self.test_1.special_numbers = ["-12"]
        with self.assertRaises(NumberOutOfRangeError):
            loadThunderball(self.test_1)
        # correct range
        self.test_1.special_numbers = ["12"]
        output = loadThunderball(self.test_1)
        assert output["thunderball"].item() == "12"