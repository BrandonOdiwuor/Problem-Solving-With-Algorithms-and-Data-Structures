class Queue:
  def __init__(self):
    self.queue_list = []

  def is_empty(self):
    return self.queue_list == []

  def size(self):
    return len(self.queue_list)

  def enqueue(self, item):
    self.queue_list.insert(0, item)

  def dequeue(self):
    return self.queue_list.pop()
