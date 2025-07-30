import unittest
from set_for_life import loadSetForLife
from lottery_class import Lottery, Draw_Type, NumberOutOfRangeError, ListLenMismatchError

class TestSetForLife(unittest.TestCase):
    def setUp(self):
        self.test_1 = Lottery(Draw_Type.SFL)
        self.test_1.main_numbers = ["1", "2", "3", "4", "5"]
        self.test_1.special_numbers = ["10"]

    def test_main_num_len(self):
        # length of 6 - exceeding length
        self.test_1.main_numbers = ["1", "2", "3", "4", "5", "6"]
        with self.assertRaises(ListLenMismatchError):
            loadSetForLife(self.test_1)
        # length of 3 - insufficient length
        self.test_1.main_numbers = ["1", "2", "3"]
        with self.assertRaises(ListLenMismatchError):
            loadSetForLife(self.test_1)
        # blank array
        self.test_1.main_numbers = []
        with self.assertRaises(ListLenMismatchError):
            loadSetForLife(self.test_1)
        # correct length
        self.test_1.main_numbers = ["1", "2", "3", "4", "5"]
        output = loadSetForLife(self.test_1)
        assert output["main_numbers"].item() == "1,2,3,4,5"

    def test_main_num_oor(self):
        # number below 1
        self.test_1.main_numbers = ["0", "10", "12", "30", "47"]
        with self.assertRaises(NumberOutOfRangeError):
            loadSetForLife(self.test_1)
        # number above 47
        self.test_1.main_numbers = ["1", "10", "12", "30", "48"]
        with self.assertRaises(NumberOutOfRangeError):
            loadSetForLife(self.test_1)
        # negative value
        self.test_1.main_numbers = ["1", "10", "-12", "30", "47"]
        with self.assertRaises(NumberOutOfRangeError):
            loadSetForLife(self.test_1)
        # correct range
        self.test_1.main_numbers = ["1", "10", "12", "30", "47"]
        output = loadSetForLife(self.test_1)
        assert output["main_numbers"].item() == "1,10,12,30,47"

    def test_special_num_len(self):
        # length of 2 - exceeding length
        self.test_1.special_numbers = ["1", "2"]
        with self.assertRaises(ListLenMismatchError):
            loadSetForLife(self.test_1)
        # blank array
        self.test_1.special_numbers = []
        with self.assertRaises(ListLenMismatchError):
            loadSetForLife(self.test_1)
        # correct length
        self.test_1.special_numbers = ["10"]
        output = loadSetForLife(self.test_1)
        assert output["life_ball"].item() == "10"

    def test_special_num_oor(self):
        # number below 1
        self.test_1.special_numbers = ["0"]
        with self.assertRaises(NumberOutOfRangeError):
            loadSetForLife(self.test_1)
        # number above 10
        self.test_1.special_numbers = ["11"]
        with self.assertRaises(NumberOutOfRangeError):
            loadSetForLife(self.test_1)
        # negative value
        self.test_1.special_numbers = ["-10"]
        with self.assertRaises(NumberOutOfRangeError):
            loadSetForLife(self.test_1)
        # correct range
        self.test_1.special_numbers = ["10"]
        output = loadSetForLife(self.test_1)
        assert output["life_ball"].item() == "10"