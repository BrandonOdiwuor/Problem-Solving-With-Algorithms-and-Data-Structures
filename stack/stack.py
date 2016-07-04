class Stack:
  def __init__(self):
    self.stack_array = []

  def is_empty(self):
      '''
      Returns a boolean indicating if a Stack is empty

      Worst Case Compleixty O(1)
      '''
    return self.stack_array == []

  def push(self, item):
    '''
    Adds an element to the end of the Stack.

     Worst Case Complexity 0(1)
    '''
    self.stack_array.append(item)

  def peek(self):
    '''
    Returns the last element in the Stack

    Worst Case Complexity O(1)
    '''
    return self.stack_array[len(self.stack_array) - 1]

  def pop(self):
    '''
    Removes the last item from the Stack.

    Worst Case Complexity 0(1)
    '''
    return self.stack_array.pop()

  def size(self):
    '''
    Returns the size of the Stack.

    Worst Case Complexity O(1)
      '''
    return len(self.stack_array)
