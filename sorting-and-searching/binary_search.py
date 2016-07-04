def binary_search(a_list, item, first, last):
  '''
  Returns a boolean indicating if the item is in a list

  Time Complexity O(log n)
  '''
  midpoint = (first + last) // 2

  if len(a_list) == 0:
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
  lst = [2, 4, 6, 8, 13, 15, 17, 20, 25, 40]
  assert binary_search(lst, 15, 0, len(lst) - 1) == True
  #assert binary_search(lst, 7) == False
  return 'Test Pass'

print(test())  

  