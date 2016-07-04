class Queue:
  def __init__(self):
    self.queue_list = []

  def is_empty(self):
      '''
      Returns a boolean indicating if the Queue is empty

      Wost Case Complexity O(1)
      '''
    return self.queue_list == []

  def size(self):
      '''
      Returns the size of the Queue

      Worst Case Complexity O(1)
      '''
    return len(self.queue_list)

  def enqueue(self, item):
      '''
      Adds an adds and element to the end of the Queue

      Worst Case Complexity O(1)
      '''
    self.queue_list.insert(0, item)

  def dequeue(self):
      '''
      Removes the firt item from the Queue

      Wost Case Complexity O(1)
      '''
    return self.queue_list.pop()
