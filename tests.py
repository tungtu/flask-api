import unittest

class TestSimple(unittest.TestCase):

    def test_sum_1_plus_1_equal_2(self):
        self.assertEqual(1 + 1, 2)

    def test_sum_2_plus_2_equal_4(self):
        self.assertEqual(2 + 2, 4)
        
    def test_sum_2_plus_3_equal_5(self):
        self.assertEqual(2 + 3, 5)        

if __name__ == '__main__':
    unittest.main()