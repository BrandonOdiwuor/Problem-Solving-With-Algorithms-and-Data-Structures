class Deque:
	def __init__(self):
		self.deque_list = []

	def size(self):
		return len(self.deque_list)

	def is_empty(self):
		return self.deque_list == []

	def add_front(self, item):
		self.deque_list.insert(0, item)

	def add_rear(self, item):
		self.deque_list.append(item)

	def remove_front(self):
		return self.deque_list.pop(0)

	def remove_rear(self):
		return self.deque_list.pop()
