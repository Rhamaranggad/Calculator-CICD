import unittest
import calculator

class TestCalculator(unittest.TestCase):
    
    def test_tambah(self):
        self.assertEqual(calculator.tambah(10, 5), 15)
        self.assertEqual(calculator.tambah(-1, 1), 0)
        self.assertEqual(calculator.tambah(-1, -1), -2)
    
    def test_kurang(self):
        self.assertEqual(calculator.kurang(10, 5), 5)
        self.assertEqual(calculator.kurang(-1, 1), -2)
        self.assertEqual(calculator.kurang(-1, -1), 0)
    
    def test_kali(self):
        self.assertEqual(calculator.kali(10, 5), 50)
        self.assertEqual(calculator.kali(-1, 1), -1)
        self.assertEqual(calculator.kali(-1, -1), 1)
    
    def test_bagi(self):
        self.assertEqual(calculator.bagi(10, 5), 2)
        self.assertEqual(calculator.bagi(-1, 1), -1)
        self.assertEqual(calculator.bagi(-1, -1), 1)
        self.assertRaises(ValueError, calculator.bagi, 10, 0)

if __name__ == '__main__':
    unittest.main()