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

    def testdate(self):
        datedif = task.retdate([1, 1, 2004], [1, 18, 2004])
        self.assertEqual(datedif, 17)
        datedif = task.retdate([5, 15, 2004], [1, 4, 2020])
        self.assertEqual(datedif, 5713)


if __name__ == '__main__':
    unittest.main()
