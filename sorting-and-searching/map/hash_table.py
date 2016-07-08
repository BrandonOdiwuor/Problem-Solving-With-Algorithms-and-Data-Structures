class HashTable:
  def __init__(self):
    self.size = 11
    self.slots = self.size * [None]
    self.data = self.size * [None]
    self.load_factor = 0

  def put(self, key, value):
    '''
    Adds a new key-values pair to the map
    '''
    hash_value = self.__hash_function(key, len(self.slots))

    if self.slots[hash_value] == None:
      self.slots[hash_value] = key
      self.data[hash_value] = value
      self.load_factor = self.load_factor + 1
    else:
      if self.slots[hash_value] == key:
        self.data[hash_value] = value
      else:
        next_slot = self.__rehash(hash_value, len(self.slots))

        while self.slots[next_slot] != None and self.slots[next_slot] != key:
          next_slot = self.__rehash(next_slot, len(self.slots))
        if self.slots[next_slot] == None:
          self.slots[next_slot] = key
          self.data[next_slot] = value
        else:
          self.data[next_slot] = value

  def get(self, key):
    '''
    Returns a value from the map associated with the key and None otherwise
    '''
    start_slot = self.__hash_function(key, len(self.slots))

    data = None
    found = False
    stop = False
    position = start_slot

    while self.slots[position] != None and not(found) and not (stop):
      if self.slots[position] == key:
        data =  self.data[position]
        found = True
      else:
        position = self.__rehash(position, len(self.slots))

        if position == start_slot:
          stop = True

    return data

  def __getitem__(self, key):
    return self.get(key)

  def __setitem__(self, key, value):
    self.put(key, value)

  def __contains__(self, key):
    '''
    Returns True if the key provided is in the map, False otherwise
    '''
    if self.get(key):
      return True
    else:
      return False

  def __len__(self):
    '''
    Returns the number of key-value pairs stored in the map

    Time Complexity O(1)
    '''

    return self.load_factor

  def __delitem__(self, key):
    '''
    Deletes a key-value pair from the map using the statement in the form:
      del map[key]
    '''
    if self.__contains__(key):
      index = self.slots.index(key)
      self.slots[index], self.data[index] = None, None
      self.load_factor = self.load_factor - 1

  def __hash_function(self, key, size):
    ''' Hash function implemented according to the remainder method '''
    return key % size

  def __rehash(self, old_hash, size):
    '''
    Rehash function using Linear Probing with a "plus 1" ,
    as a collision resolution technique
    '''
    return (old_hash + 1) % size
