import queue

def main():
  my_queue = queue.Queue()
  test(my_queue.size(), 0)
  test(my_queue.is_empty(), True)
  my_queue.enqueue(1)
  my_queue.enqueue(True)
  my_queue.enqueue('Three')
  test(my_queue.is_empty(), False)
  test(my_queue.size(), 3)
  test(my_queue.dequeue(), 1)
  test(my_queue.size(), 2)

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
