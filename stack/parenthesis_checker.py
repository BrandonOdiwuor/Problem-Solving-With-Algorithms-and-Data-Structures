import stack

def parenthesis_checker(symbol_string):
  thestack = stack.Stack()
  is_balanced = True

  for i in range(len(symbol_string)):
    if symbol_string[i] == '(':
      thestack.push('(')
    else:
      if thestack.is_empty():
        is_balanced = False
      else:
        thestack.pop()
  if not(thestack.is_empty()):
    is_balanced = False
  
  return is_balanced


# Provided simple test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))

def main():
  test(parenthesis_checker('((())'), False)
  test(parenthesis_checker('((()))'), True)
  test(parenthesis_checker('(()()(()))'), True)
	test(parenthesis_checker('())'), False)

if __name__ == '__main__':
  main()
