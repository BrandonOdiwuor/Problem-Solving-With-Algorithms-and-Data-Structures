class UnorderedLinkedList:

	# ------------------------------ Nested Node class ------------------------------
	class Node:
		def __init__(self, data):		# Initializes Node fields
			self.data = data					# The item to be stored in the list
			self.next = None					# Reference to the next node

		def get_data(self):
			return self.data

		def set_data(self, new_data):
			self.data = new_data

		def get_next(self):
			return self.next

		def set_next(self, next_node):
			self.next = next_node

	# ------------------------------ Unordered Linked list methods ------------------------------
	def __init__(self):
		'''Creates an empty linked list.'''
		self.head = None
		self.tail = None
		self.size = 0

	def __len__(self):
		'''Returns the number of items in the linked list.'''
		return self.size

	def is_empty(self):
		'''Returns True if the list is empty.'''
		return self.size == 0

	def add(self, item):
		'''Adds a new Item to the head linked list.'''
		if self.size == 0:
			temp_node = self.Node(item)
			temp_node.set_next(self.head)
			self.tail = temp_node
			self.head = temp_node
		else:
			temp_node = self.Node(item)
			temp_node.set_next(self.head)
			self.head = temp_node
		self.size = self.size + 1

	def search(self, item):
		'''Searches for an item within the sinlgly linked list. 
			Returns True if the item is found.
		'''
		current_node = self.head
		found = False
		while current_node != None and not(found):
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
		item_found = None
		while current_node != None:
			if current_node.get_data() == item:
				previous_node.set_next(current_node.get_next())
				item_found = item
				self.size = self.size - 1	
			previous_node = current_node	
			current_node = current_node.get_next()
		return item_found

	def append(self, item):
		'''Adds a new Item to the end(tail) of the list.'''
		new_node = self.Node(item)
		self.tail.set_next(new_node)
		self.tail = self.tail.get_next()
		self.size =self.size + 1

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


