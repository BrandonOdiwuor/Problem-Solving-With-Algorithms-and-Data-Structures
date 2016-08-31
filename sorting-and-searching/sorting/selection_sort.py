def selection_sort(lst):
  '''
  Sorts a list in ascending order according to Selection Sort algorithm

  Time Complexity O(N^2)
  '''

  for fill_position in range(len(lst)-1, 0, -1):
    position_of_max = 0
    for i in range(1, fill_position + 1):
      if lst[i] > lst[position_of_max]:
        position_of_max = i
    lst[position_of_max], lst[fill_position] = lst[fill_position], lst[position_of_max]

  return lst

def main():
  assert(selection_sort([54, 26, 93, 17, 77, 31, 44, 55, 20]) == [17, 20, 26, 31, 44, 54, 55, 77, 93])
  assert(selection_sort([5, 1, 4, 6, 3, 8, 7, 2]) == [1, 2, 3, 4, 5, 6, 7, 8])
  print('Test Pass')


if __name__ == '__main__':
  main()
