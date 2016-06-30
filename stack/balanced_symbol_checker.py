import stack

def balanced_symbol_checker(symbol_string):
  thestack = stack.Stack()
  is_balanced = True

  for i in range(len(symbol_string)):
    if symbol_string[i] in ['(', '[', '{']:
      thestack.push(symbol_string[i])
    else:
      if thestack.is_empty():
        is_balanced = False
      else:
        top = thestack.pop()
        is_balanced = checker(top, symbol_string[i])

  if not(thestack.is_empty()):
    is_balanced = False
  
  return is_balanced


def checker(opening_symbol, closing_symbol):
  opening_symbols = ['(', '[', '{']
  closing_symbols = [')', ']', '}']
  return opening_symbols.index(opening_symbol) == closing_symbols.index(closing_symbol)


# Provided simple test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))

def main():
  test(balanced_symbol_checker('{}'), True)
  test(balanced_symbol_checker('()'), True)
  test(balanced_symbol_checker('[]'), True)
  test(balanced_symbol_checker('((([]))'), False)
  test(balanced_symbol_checker('{((({}[])))}'), True)
  test(balanced_symbol_checker('(()()(()))'), True)
  test(balanced_symbol_checker('[()]'), True)
  test(balanced_symbol_checker('({()})'), True)

if __name__ == '__main__':
  main()
