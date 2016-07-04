def gcd(m, n):
  while m % n != 0:
    old_m = m
    old_n = n

    m = old_n
    n = old_m % old_n
  return n

class Fraction:
  def __init__(self, top, bottom):
    self.num = top
    self.den = bottom
  
  def show(self):
    print(self.num, '/', self.den)

  def __str__(self):
    return str(self.num) + '/' + str(self.den)

  def __add__(self, other_fraction):
    my_num = self.num * other_fraction.den + self.den * other_fraction.num
    my_den = self.den * other_fraction.den
    common = gcd(my_num, my_den)
    return Fraction(my_num//common, my_den//common)

  def __sub__(self, other_fraction):
    my_num = self.num * other_fraction.den - self.den * other_fraction.num
    my_den = self.den * other_fraction.den
    common = gcd(my_num, my_den)
    return Fraction(my_num//common, my_den//common)

  def __mul__(self, other):
    my_num = self.num * other.num 
    my_den = self.den * other.den
    common = gcd(my_num, my_den)
    return Fraction(my_num//common, my_den//common)

  def __truediv__(self, other):
    my_num = self.num * other.den 
    my_den = self.den * other.num
    common = gcd(my_num, my_den)
    return Fraction(my_num//common, my_den//common)

  def __eq__(self, other):
    first_num = self.num * other.den
    last_num = self.num * other.den
    return first_num == last_num
  
  def __lt__(self, other):
    return (self.num/self.den) < (other.num/other.den)

  def __gt__(self, other):
    return (self.num/self.den) > (other.num/other.den)

  def get_num(self):
    return self.num

  def get_den(self):
    return self.den


def main():
  my_fraction = Fraction(3,5)
  f2 = Fraction(2,5)
  f3 = my_fraction + f2
  f4 = Fraction(3,5)
  f5 = my_fraction - f2
  f6 = Fraction(1,3)
  f7 = Fraction(3,1)
  #my_fraction.show()
  print(my_fraction)
  print(f3)
  print(f4 == my_fraction)
  print(f2 < my_fraction)
  print(f5)
  print(f6 * my_fraction)
  print(my_fraction / f7)


if __name__ == '__main__':
  main()
