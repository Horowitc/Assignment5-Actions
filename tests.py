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


if __name__ == '__main__':
    unittest.main()
