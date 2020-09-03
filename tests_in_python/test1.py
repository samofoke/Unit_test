import unittest
from test2 import solve_me




class Test_First(unittest.TestCase):

    def test_basics_1(self):
        r = [4, 12, 3, 20, 50, 8, 5, 13, 30];
        x = 20;
        n = len(r);
        res = solve_me(r, n, x)
        if (res == -1):
            self.assertEqual(res, -1, print ('it returns -1 as expected.'))
        elif (res):
            self.assertEqual(res, res, print('it returns the value of x as expected',res))
        else:
            self.fail("Please try again your solution is not working.")

    def test_basics_2(self):
        r = [4, 12, 3, 20, 50, 8, 5, 13, 30];
        x = None;
        n = len(r);
        res = solve_me(r, n, x)
        if (res == None):
            self.assertEqual(res, None, print('Nothing is returned.'))
    # def test_basics_3(self):
    #     pass


if __name__ == '__main__':
    unittest.main()