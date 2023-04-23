import unittest

from shape import triangle


class TraingleTests(unittest.TestCase):

    def test_wrong_size(self):
        self.assertEqual( triangle.triangleType(1,2,6), "Invalid Triangle" )


if __name__ == '__main__':
    unittest.main()