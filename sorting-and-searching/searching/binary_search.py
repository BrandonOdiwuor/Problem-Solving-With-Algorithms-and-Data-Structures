def binary_search(a_list, item, first=0, last=None):
  '''
  Returns a boolean indicating if the item is in a list

  Time Complexity O(log n)
  '''
  last = last or len(a_list)

  midpoint = (first + last) // 2

  if first > last:
    return False
  else:
    if a_list[midpoint] == item:
      return True
    else:
      if item < a_list[midpoint]:
        return binary_search(a_list, item, first, midpoint - 1)
      else:
  	    return binary_search(a_list, item, midpoint + 1, last)

def test():
  lst = [1, 2, 8, 13, 17, 19, 32, 42]
  assert binary_search(lst, 13) == True
  assert binary_search(lst, 0) == False
  return 'Test Pass'

print(test())
