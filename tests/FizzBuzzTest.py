import unittest
from fizzbuzz import FizzBuzz

class FizzBuzzTest(unittest.TestCase):

  def setUp(self):
    self.fizzbuzz = FizzBuzz()

  def test_is_fizz(self):    
    self.assertTrue(self.fizzbuzz.isFizz(3))
    self.assertTrue(self.fizzbuzz.isFizz(9))
    self.assertFalse(self.fizzbuzz.isFizz(15))

  def test_is_buzz(self):
    self.assertTrue(self.fizzbuzz.isBuzz(5))
    self.assertTrue(self.fizzbuzz.isBuzz(10))
    self.assertFalse(self.fizzbuzz.isBuzz(15))

  def test_is_fizz_buzz(self):
    self.assertTrue(self.fizzbuzz.isFizzBuzz(15))
    self.assertTrue(self.fizzbuzz.isFizzBuzz(30))
    self.assertFalse(self.fizzbuzz.isFizzBuzz(9))

  def test_has_100_numbers(self, total = 100):
    self.assertEqual(total, len(self.fizzbuzz.lista))

  def test_number_to_Text(self):
    self.assertEqual(FizzBuzz.FIZZ, self.fizzbuzz.numberToText(3))
    self.assertEqual(FizzBuzz.BUZZ, self.fizzbuzz.numberToText(5))
    self.assertEqual(FizzBuzz.FIZZ_BUZZ, self.fizzbuzz.numberToText(15))    

if __name__ == '__main__':
  unittest.main()