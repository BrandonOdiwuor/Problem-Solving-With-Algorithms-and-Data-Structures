def bubble_sort(lst):
  '''
  Sorts a list in ascending order according to Bubble Sort algorithm

  Time Complexity O(N^2)
  '''
  for pass_num in range(len(lst) - 1, 0, -1):

    lst_not_sorted = True
    i = 0

    while i < pass_num and lst_not_sorted:
      lst_sorted = False
      if lst[i] > lst[i + 1]:
        lst_sorted = True
        lst[i], lst[i + 1] = lst[i+1], lst[i]
      i = i + 1

  return lst


def main():
  assert(bubble_sort([54, 26, 93, 17, 77, 31, 44, 55, 20]) == [17, 20, 26, 31, 44, 54, 55, 77, 93])
  assert(bubble_sort([5, 1, 4, 6, 3, 8, 7, 2]) == [1, 2, 3, 4, 5, 6, 7, 8])
  print('Test Pass')

if __name__ == '__main__':
  main()
