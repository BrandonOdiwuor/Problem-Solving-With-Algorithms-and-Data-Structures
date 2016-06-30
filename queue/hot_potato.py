import queue

def hot_potato(list_of_names, num):
  q = queue.Queue()

  for name in list_of_names:
    q.enqueue(name)

  while q.size() > 1:
    for i in range(num):
      q.enqueue(q.dequeue())
    q.dequeue()

  return q.dequeue()

def main():
  test(hot_potato(['Brandon', 'Wayne', 'Odiwuor', 'Backer', 'Otieno', 'Glen', 'McRenny'], 7), 'Backer')

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
