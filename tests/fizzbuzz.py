class FizzBuzz:

  FIZZ_BUZZ = 'FizzBuzz'
  FIZZ      = 'Fizz'
  BUZZ      = 'Buzz'  

  lista = []

  def __init__(self, min = 1, max = 101):
    self.lista = range(min, max)

  def isFizz(self, number):
    return number % 3 == 0 and number % 5 != 0

  def isBuzz(self, number):
    return number % 5 == 0 and number % 3 != 0

  def isFizzBuzz(self, number):
    return number % 5 == 0 and number % 3 == 0  

  def numberToText(self, number):
    if self.isFizz(number):
      return self.FIZZ
    elif self.isBuzz(number):
      return self.BUZZ
    elif self.isFizzBuzz(number):
      return self.FIZZ_BUZZ