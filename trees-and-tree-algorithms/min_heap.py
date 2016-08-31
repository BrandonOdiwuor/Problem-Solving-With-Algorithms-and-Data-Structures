class BinaryHeap:
  '''
  A min heap Implementation of a BinaryHeap data structure
  '''

  def __init__(self):
    self.heap_list = [0]
    self.current_size = 0

  def insert(self, k):
    self.heap_list.append(k)
    self.current_size = self.current_size + 1
    self.__percolate_up(self.current_size)

  def find_min(self):
    '''
    Returns the smallest item in the heap

    Time Complexity O(1)
    '''
    return self.heap_list[i]

  def del_min(self):
    pass

  def build_heap(self, lst):
    pass

  def size(self):
    return self.current_size

  def is_empty(self):
    return return self.current_size  == 0

  def __percolate_up(self, i):
    while i > 0:
      if self.heap_list[i] < self.heap_list[i//2]:
        self.heap_list[i], self.heap_list[i//2] = self.heap_list[i//2], self.heap_list[i]
      i = i // 2
