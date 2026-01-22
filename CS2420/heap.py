# a priorityQueue using a heap as it's implentation


class priorityQueue():


	def __init__(self):
		self.mItems = []
		self.mLength = 0

	def enqueue(self, node):
		self.mItems.append(node)
		self.mLength += 1
		# bubble up
		child = len(self.mItems) - 1
		parent = (child - 1) // 2
		while child > 0 and self.mItems[child][1] < self.mItems[parent][1]:
			self.mItems[child], self.mItems[parent] = self.mItems[parent], self.mItems[child]
			child = parent
			parent = (child - 1) // 2

	def dequeue(self):
		if len(self.mItems) == 0:
			return None
		if len(self.mItems) == 1:
			self.mLength -= 1
			return self.mItems.pop()
		
		priority = self.mItems[0]
		self.mItems[0] = self.mItems.pop()
		self.mLength -= 1
		
		# bubble down
		parent = 0
		while True:
			childL = parent * 2 + 1
			childR = parent * 2 + 2
			smallest = parent
			
			if childL < len(self.mItems) and self.mItems[childL][1] < self.mItems[smallest][1]:
				smallest = childL
			if childR < len(self.mItems) and self.mItems[childR][1] < self.mItems[smallest][1]:
				smallest = childR
			
			if smallest == parent:
				break
			
			self.mItems[parent], self.mItems[smallest] = self.mItems[smallest], self.mItems[parent]
			parent = smallest
		
		return priority

	def isEmpty(self):
		if len(self.mItems) == 0:
			return True
		else:
			return False

	def getSize(self):
		return self.mLength
