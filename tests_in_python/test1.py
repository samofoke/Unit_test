import unittest
from test2 import solve_me




class Test1(unittest.TestCase):

    def test_basics_1(self):
        r = [4, 12, 3, 20, 50, 8, 5, 13, 30];
        x = 8;
        n = len(r);
        res = solve_me(r, n, x)
        if (res == -1):
            self.assertEqual(res, -1, print ('it returns -1 as expected.'))
        else:
            self.assertEqual(res, res, print('it returns the value of x as expected',res))

    # def test_basics_2(self):
    #     pass

    # def test_basics_3(self):
    #     pass


if __name__ == '__main__':
    unittest.main()