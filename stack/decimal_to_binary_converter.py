import stack

#Divide by 2 algorithm
def convert(dec_number):
  rem_stack = stack.Stack()
  binary_string = ''

  while dec_number > 0:
    rem = dec_number % 2
    rem_stack.push(rem)
    dec_number = dec_number // 2

  while not rem_stack.is_empty():
    binary_string += str(rem_stack.pop())

  return binary_string

#Main function that calls the covert() function on the test() function
def main():
  test(convert(10), '1010')
  test(convert(5), '101')
  test(convert(233), '11101001')

# Provided simple test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))



if __name__ == '__main__':
  main()
