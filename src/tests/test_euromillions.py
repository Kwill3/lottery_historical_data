import unittest
from euromillions import loadEuromillions
from lottery_class import Lottery, Draw_Type, NumberOutOfRangeError, ListLenMismatchError

class TestThunderball(unittest.TestCase):
    def setUp(self):
        self.test_1 = Lottery(Draw_Type.EUROMILLIONS)
        self.test_1.main_numbers = ["1", "2", "3", "4", "5"]
        self.test_1.special_numbers = ["9", "11"]

    def test_main_num_len(self):
        # length of 6 - exceeding length
        self.test_1.main_numbers = ["1", "2", "3", "4", "5", "6"]
        with self.assertRaises(ListLenMismatchError):
            loadEuromillions(self.test_1)
        # length of 3 - insufficient length
        self.test_1.main_numbers = ["1", "2", "3"]
        with self.assertRaises(ListLenMismatchError):
            loadEuromillions(self.test_1)
        # blank array
        self.test_1.main_numbers = []
        with self.assertRaises(ListLenMismatchError):
            loadEuromillions(self.test_1)
        # correct length
        self.test_1.main_numbers = ["1", "2", "3", "4", "5"]
        output = loadEuromillions(self.test_1)
        assert output["main_numbers"].item() == "1,2,3,4,5"

    def test_main_num_oor(self):
        # number below 1
        self.test_1.main_numbers = ["0", "10", "12", "30", "50"]
        with self.assertRaises(NumberOutOfRangeError):
            loadEuromillions(self.test_1)
        # number above 50
        self.test_1.main_numbers = ["1", "10", "12", "30", "51"]
        with self.assertRaises(NumberOutOfRangeError):
            loadEuromillions(self.test_1)
        # negative value
        self.test_1.main_numbers = ["1", "10", "-12", "30", "50"]
        with self.assertRaises(NumberOutOfRangeError):
            loadEuromillions(self.test_1)
        # correct range
        self.test_1.main_numbers = ["1", "10", "12", "30", "50"]
        output = loadEuromillions(self.test_1)
        assert output["main_numbers"].item() == "1,10,12,30,50"

    def test_special_num_len(self):
        # length of 3 - exceeding length
        self.test_1.special_numbers = ["1", "2", "3"]
        with self.assertRaises(ListLenMismatchError):
            loadEuromillions(self.test_1)
        # length of 1 - insufficient length
        self.test_1.special_numbers = ["1"]
        with self.assertRaises(ListLenMismatchError):
            loadEuromillions(self.test_1)
        # blank array
        self.test_1.special_numbers = []
        with self.assertRaises(ListLenMismatchError):
            loadEuromillions(self.test_1)
        # correct length
        self.test_1.special_numbers = ["1", "10"]
        output = loadEuromillions(self.test_1)
        assert output["lucky_stars"].item() == "1,10"

    def test_special_num_oor(self):
        # number below 1
        self.test_1.special_numbers = ["0", "10"]
        with self.assertRaises(NumberOutOfRangeError):
            loadEuromillions(self.test_1)
        # number above 14
        self.test_1.special_numbers = ["10", "15"]
        with self.assertRaises(NumberOutOfRangeError):
            loadEuromillions(self.test_1)
        # negative value
        self.test_1.special_numbers = ["10", "-12"]
        with self.assertRaises(NumberOutOfRangeError):
            loadEuromillions(self.test_1)
        # correct range
        self.test_1.special_numbers = ["10", "12"]
        output = loadEuromillions(self.test_1)
        assert output["lucky_stars"].item() == "10,12"