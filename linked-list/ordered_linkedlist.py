class OrderedLinkedList:

  # ------------------------------ Nested Node class ------------------------------
  class Node:
    def __init__(self, data):    # Initializes Node fields
      self.data = data           # The item to be stored in the list
      self.next = None           # Reference to the next node

    def get_data(self):
      return self.data

    def set_data(self, new_data):
      self.data = new_data

    def get_next(self):
      return self.next

    def set_next(self, next_node):
      self.next = next_node

  # ------------------------- Ordered Linked list methods -------------------------
  def __init__(self):
    '''Creates an empty linked list.'''
    self.head = None
    self.size = 0

  def __len__(self):
    '''Returns the number of items in the linked list.'''
    return self.size

  def is_empty(self):
    '''Returns True if the list is empty.'''
    return self.size == 0

  def add(self, item):
    '''Adds a new Item to the list while maintaing the order.'''
    current = self.head
    previous = None
    stop = False
    while current != None and not(stop):
      if current.get_data() > item:
        stop = True
      else:
        previous = current
        current = current.get_next()

    temp = self.Node(item)
    if previous == None:
      temp.set_next(self.head)
      self.head = temp
      self.size = self.size + 1
    else:
      temp.set_next(current)
      previous.set_next(temp)
      self.size = self.size + 1

  def search(self, item):
    '''Searches for an item within the sinlgly linked list. 
      Returns True if the item is found.
    '''
    current_node = self.head
    found = False
    while not(found) and current_node != None:
      if current_node.get_data() == item:
        found = True
      current_node = current_node.get_next() 
    return found

  def remove(self, item):
    '''Removes and returns an item from the linked list.
      Returns False if item is not found.
    '''
    current_node = self.head
    previous_node = None
    item_found = False
    while current_node != None:
      if current_node.get_data() == item:
        previous_node.set_next(current_node.get_next())
        item_found = item
        self.size = self.size - 1	
      previous_node = current_node	
      current_node = current_node.get_next()
    return item_found


  def __str__(self):
    '''Used to print the list.'''
    linkedlist_string = '['
    current_node = self.head
    while current_node != None:
      if current_node == self.head:
        linkedlist_string = linkedlist_string + repr(current_node.get_data())
      else:
        linkedlist_string = linkedlist_string + ' , ' + repr(current_node.get_data())
      current_node = current_node.get_next()
    linkedlist_string = linkedlist_string + ']'	
    return linkedlist_string

  def __getitem__(self, key):
    ''' Alows indexing'''
    current_node = self.head
    for i in range(key):
      current_node = current_node.get_next()
    return current_node.get_data()

  def __setitem__(self, key, value):
    ''' Allows indexing assignment'''
    current_node = self.head
    for i in range(key):
      current_node = current_node.get_next()
    current_node.set_data(value)
      


