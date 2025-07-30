import unittest
from lotto import loadLotto
from lottery_class import Lottery, Draw_Type, NumberOutOfRangeError, ListLenMismatchError, BonusNumberInMainError

class TestLotto(unittest.TestCase):
    def setUp(self):
        self.test_1 = Lottery(Draw_Type.LOTTO)
        self.test_1.main_numbers = ["1", "2", "3", "4", "5", "6"]
        self.test_1.special_numbers = ["14"]

    def test_main_num_len(self):
        # length of 7 - exceeding length
        self.test_1.main_numbers = ["1", "2", "3", "4", "5", "6", "7"]
        with self.assertRaises(ListLenMismatchError):
            loadLotto(self.test_1)
        # length of 3 - insufficient length
        self.test_1.main_numbers = ["1", "2", "3", "4", "5"]
        with self.assertRaises(ListLenMismatchError):
            loadLotto(self.test_1)
        # blank array
        self.test_1.main_numbers = []
        with self.assertRaises(ListLenMismatchError):
            loadLotto(self.test_1)
        # correct length
        self.test_1.main_numbers = ["1", "2", "3", "4", "5", "6"]
        output = loadLotto(self.test_1)
        assert output["main_numbers"].item() == "1,2,3,4,5,6"

    def test_main_num_oor(self):
        # number below 1
        self.test_1.main_numbers = ["0", "10", "22", "30", "40", "59"]
        with self.assertRaises(NumberOutOfRangeError):
            loadLotto(self.test_1)
        # number above 59
        self.test_1.main_numbers = ["1", "10", "22", "30", "40", "60"]
        with self.assertRaises(NumberOutOfRangeError):
            loadLotto(self.test_1)
        # negative value
        self.test_1.main_numbers = ["1", "10", "-22", "30", "40", "59"]
        with self.assertRaises(NumberOutOfRangeError):
            loadLotto(self.test_1)
        # correct range
        self.test_1.main_numbers = ["1", "10", "22", "30", "40", "59"]
        output = loadLotto(self.test_1)
        assert output["main_numbers"].item() == "1,10,22,30,40,59"

    def test_special_num_len(self):
        # length of 2 - exceeding length
        self.test_1.special_numbers = ["1", "2"]
        with self.assertRaises(ListLenMismatchError):
            loadLotto(self.test_1)
        # blank array
        self.test_1.special_numbers = []
        with self.assertRaises(ListLenMismatchError):
            loadLotto(self.test_1)
        # correct length
        self.test_1.special_numbers = ["8"]
        output = loadLotto(self.test_1)
        assert output["bonus_ball"].item() == "8"

    def test_special_num_oor(self):
        # number below 1
        self.test_1.special_numbers = ["0"]
        with self.assertRaises(NumberOutOfRangeError):
            loadLotto(self.test_1)
        # number above 59
        self.test_1.special_numbers = ["60"]
        with self.assertRaises(NumberOutOfRangeError):
            loadLotto(self.test_1)
        # negative value
        self.test_1.special_numbers = ["-12"]
        with self.assertRaises(NumberOutOfRangeError):
            loadLotto(self.test_1)
        # correct range
        self.test_1.special_numbers = ["9"]
        output = loadLotto(self.test_1)
        assert output["bonus_ball"].item() == "9"

    def test_bonus_in_main(self):
        # number 1 in main and bonus
        self.test_1.main_numbers = ["1", "2", "3", "4", "5", "6"]
        self.test_1.special_numbers = ["1"]
        with self.assertRaises(BonusNumberInMainError):
            loadLotto(self.test_1)