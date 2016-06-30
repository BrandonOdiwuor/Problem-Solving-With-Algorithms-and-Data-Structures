class Stack:
  def __init__(self):
    self.stack_array = []
 
  def is_empty(self):
    return self.stack_array == []

  def push(self, item):
    self.stack_array.append(item)

  def peek(self):
    return self.stack_array[len(self.stack_array) - 1]

  def pop(self):
    return self.stack_array.pop()

  def size(self):
    return len(self.stack_array)
