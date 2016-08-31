def sequential_search(a_list, item):
  '''
  Returns a boolean indicating if the item is in a list

  Time Complexity O(N)
  '''
  found = False

  for i in a_list:
    if i == item:
      found = True

  return found

def test():
  ''' Test cases fot the function sequential_search(a_list, item) '''

  assert(sequential_search([1, 4, 5, 7, 3, 9, 12], 3)) == True
  assert(sequential_search([2, 4, 1, 6, 9, 3, 25], 5)) == False
  return 'Test Pass'

print(test())
