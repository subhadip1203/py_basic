import unittest
import cal

class testCal(unittest.TestCase) :
    
    def test_add(self):
        result = cal.add(1,2)
        self.assertEqual(result,3)

if __name__ == "__main__":
    unittest.main()

