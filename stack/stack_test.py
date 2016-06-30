import stack

# Provided simple test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


def main():
  my_stack = stack.Stack()

  test(my_stack.is_empty(), True)
  my_stack.push(1)
  test(my_stack.peek(), 1)
  my_stack.push('Second Item')
  my_stack.push(True)
  test(my_stack.size(), 3)
  test(my_stack.pop(), True)
  test(my_stack.size(), 2)

if __name__ == '__main__':
  main()
