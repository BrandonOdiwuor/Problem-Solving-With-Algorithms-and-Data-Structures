def to_string(num, base):
  ''' The function recursively converts an integer to a string of any base between 2 and 16'''
  lookup = '0123456789ABCDE'

  if num < base:
    ''' Base case'''
    return lookup[num]
  else:
    ''' recursive case'''
    return to_string(num // base, base) + lookup[num % base]

def main():
  test(to_string(10, 2), '1010')
  test(to_string(976, 10), '976')
  test(to_string(12, 16), 'C')


def test(got, expected):
  ''' Test function that takes what a function(got) returns and compares it wich expected output'''
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


if __name__ == '__main__':
  main()
