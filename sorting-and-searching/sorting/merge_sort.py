def merge_sort(lst):
  '''
  Sorts a list in ascending order accoring to Merger Sort algorithm

  Time Complexity O(n log n)
  '''

  if len(lst) >= 2:
    middpoint = len(lst) // 2
    right_half = lst[middpoint:]
    left_half = lst[:middpoint]

    merge_sort(right_half)
    merge_sort(left_half)
    lst = merge(right_half, left_half, lst)

    return lst



def merge(rh,lh, m_lst):
  i, j, k = 0, 0, 0

  while i < len(rh) and j < len(lh):
    if rh[i] < lh[j]:
      m_lst[k] = rh[i]
      k, i = k + 1, i + 1
    else:
      m_lst[k] = lh[j]
      k, j = k + 1, j + 1

  while i < len(rh):
    m_lst[k] = rh[i]
    k, i = k + 1, i + 1

  while j < len(lh):
    m_lst[k] = lh[j]
    k, j = k + 1, j + 1

  return m_lst

def main():
  assert(merge_sort([54, 26, 93, 17, 77, 31, 44, 55, 20]) == [17, 20, 26, 31, 44, 54, 55, 77, 93])
  assert(merge_sort([5, 1, 4, 6, 3, 8, 7, 2]) == [1, 2, 3, 4, 5, 6, 7, 8])
  print('Test Pass')

if __name__ == '__main__':
  main()
