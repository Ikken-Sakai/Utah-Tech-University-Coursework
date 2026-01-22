import time
import Student2

class AgeHolder:
	def __init__(self):
		self.mAge = 0

def AddAges(s, data):
	data.mAge += int(s.getage())

class Node:
	def __init__(self, item, next):
		self.mItem = item
		self.mNext = next

class UUC:
	def __init__(self):
		self.mFirst = None

	def Traverse(self, callback, data):
		current = self.mFirst
		while current:
			callback(current.mItem, data)
			current = current.mNext

	def Size(self):
		count = 0
		current = self.mFirst
		while current:
			count += 1
			current = current.mNext
		return count

	def Exists(self, item):
		current = self.mFirst
		while current != None:
			if current.mItem.getssn() == item.getssn():
				return True
			current = current.mNext
		return False

	def Delete(self, item):
		if not self.Exists(item):
			return False
		if self.mFirst.mItem == item:
			self.mFirst = self.mFirst.mNext
			return True
		current = self.mFirst
		while not current.mNext.mItem == item:
			current = current.mNext
		current.mNext = current.mNext.mNext
		return True

	def Retrive(self, item):
		if not self.Exists(item):
			return None
		current = self.mFirst
		while not current.mItem.getssn() == item.getssn():
			current = current.mNext
		return current.mItem

	def Insert(self, item):
		if self.Exists(item):
			return False
		self.mFirst = Node(item, self.mFirst)
		return True

def main():
	t1 = time.time()
	f = open("FakeNames.txt", "r")
	allStudents = UUC()
	for line in f:
		fields = line.split()
		s = Student2.Student(fields[0], fields[1], fields[2], fields[3], fields[4])
		ok = allStudents.Insert(s)
		if not ok:
			print("Error", fields[0], fields[1], fields[2], fields[3], fields[4])

#Traverse
	data = AgeHolder()
	allStudents.Traverse(AddAges, data)
	print("Traverse: Average is ", data.mAge/allStudents.Size())
	f.close()
	t2 = time.time()
	print("Time is: ", t2 - t1)

#Delete
	t1 = time.time()
	f = open("DeleteNames.txt", "r")
	for line in f:
		ssn = line.strip()
		dummyStudent = Student2.Student("", "", ssn, "", "")
		ok = allStudents.Delete(dummyStudent)
		if not ok:
			print("Error")
	f.close()
	print("Deleted")
	t2 = time.time()
	print("Time is: ", t2 - t1)

#Retrieve
	t1 = time.time()
	totalage = 0
	totalcount = 0
	f = open("RetriveNames.txt", "r")
	for ssn in f:
		ssn = ssn.strip()
		realStudent = allStudents.Retrive(Student2.Student("","",ssn,"",""))
		if not realStudent:
			print("Error")
		else:
			totalage += int(realStudent.getage())
			totalcount += 1
	f.close()
	print("Retrive: Average in Retrieve", totalage/totalcount)
	t2 = time.time()
	print("Time is: ", t2 - t1)

main()
