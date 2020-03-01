import unittest
import task


class TestCase(unittest.TestCase):

    def test1(self):
        expected = "success"
        self.assertEqual(expected, task.firstrun())

    def test2(self):
        expected = "failure"
        self.assertNotEqual(expected, task.firstrun())

    def testarea(self):
        area = task.retarea(2)
        self.assertEqual(12.57, area)
        area = task.retarea(4)
        self.assertEqual(50.27, area)

    def testlist(self):
        liststr = task.retlist([0, 1, 2, 3, 4, 5])
        self.assertEqual(liststr, (0, 5))
        liststr = task.retlist([17, 4, 30, 11])
        self.assertEqual(liststr, (17, 11))


if __name__ == '__main__':
    unittest.main()
