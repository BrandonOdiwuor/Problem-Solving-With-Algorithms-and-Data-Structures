def insertion_sort(lst):
  '''
  Sorts a list in ascending order according to Insertion Sort algorithm
  
  Time Complexity O(N^2)
  '''
  for index in range(1, len(lst)):
    item = lst[index]
    i = index
    while i > 0 and item < lst[i - 1]:
      lst[i] = lst[i - 1]
      i = i - 1
    lst[i] = item

  return lst

def main():
  assert(insertion_sort([54, 26, 93, 17, 77, 31, 44, 55, 20]) == [17, 20, 26, 31, 44, 54, 55, 77, 93])
  assert(insertion_sort([5, 1, 4, 6, 3, 8, 7, 2]) == [1, 2, 3, 4, 5, 6, 7, 8])
  print('Test Pass')


if __name__ == '__main__':
  main()
