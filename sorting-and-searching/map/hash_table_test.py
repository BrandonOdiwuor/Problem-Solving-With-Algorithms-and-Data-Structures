import hash_table


def main():
  h = hash_table.HashTable()

  # The number of items in an empty hash_table
  test(len(h), 0)

  # Adding a key value pair to the hash table
  h.put(3, 'Brandon')
  h.put(6, 'Odiwuor')

  # The number of items in a hash_table with two items
  test(len(h), 2)

  # Testign the __contains__(self, key) method
  test(3 in h, True)
  test(5 in h, False)

  # Getting a value from the hash_table using a key
  test(h.get(6), 'Odiwuor')
  test(h[3], 'Brandon')

  # Changing a values a ssociated with a particular key
  h[3] = 'Baker'
  test(h[3], 'Baker')

  # Deleting a key-value pair from the hash_table
  del h[6]
  test(len(h), 1)


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
