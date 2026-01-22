import time
import bst
import hashtable

class Node:
	def __init__(seslf, item):
		self.item = item
		self.l = None
		self.r = None

class Student:
	def __init__(self, fn, ln, ssn, em, age):
		self.fname = fn
		self.lname = ln
		self.ssn = ssn
		self.email = em
		self.age = age

	def getfname(self):
		return self.fname

	def getlname(self):
		return self.lname

	def getssn(self):
		return self.ssn

	def getemail(self):
		return self.email

	def getage(self):
		return self.age

	def setfname(self, fname):
		self.fname = fname

	def setlname(self, lname):
		self.lname = lname

	def setssn(self, ssn):
		self.ssn = ssn
	
	def setemail(self, email):
		self.email = email

	def setage(self, age):
		self.age = age

	def __eq__(self,rhs):
		if self.ssn == rhs.ssn:
			return True
		else:
			return False

	def __lt__(self, rhs):
		if self.ssn < rhs.ssn:
			return True
		else:
			return False

	def __gt__(self, rhs):
		if self.ssn > rhs.ssn:
			return True
		else:
			return False

	def getAge(self):
		return self.age

	def __int__(self):
		return int(self.ssn.replace('-', ''))

def InsertNames():
	t1 = time.time()
	students = []
	f = open("FakeNames.txt","r")
	for i in f:
		i = i.split(" ")
		student = Student(i[0], i[1], i[2], i[3], i[4])
		student.setfname(i[0])
		student.setlname(i[1])
		student.setssn(i[2])
		student.setemail(i[3])
		student.setage(i[4])
		matched = False
		for s in students:
			if s.getssn() == student.getssn():
				matched = True
				break
		if matched == False:
			students.append(student)
	f.close()
	t2 = time.time()
	t = t2 - t1
	print("Time is : ", t)
	print()
	return students

def TraverseNames(students):
	t1 = time.time()
	current = 0
	counter = 0
	for i in students:
		age = int(i.getage())
		current += age
		counter += 1
	print("Average age is: ", current/counter)
	t2 = time.time()
	t = t2-t1
	print("Time is : ", t)
	print()

def DeleteNames(students):
	t1 = time.time()
	f = open("DeleteNames.txt", "r")
	for ssn in f:
		deleted = False
		ssn = ssn.strip()
		for i, student in enumerate(students):
			if ssn == student.getssn():
				students.pop(i)
				deleted = True
				break
		if not deleted:
			print("These SSN doesn't exist: ", ssn)

	print("Deleted the data in this file")
	t2 = time.time()
	t = t2-t1
	print("Time is: ", t)
	print()

def RetrieveNames(students):
	t1 = time.time()
	current = 0
	counter = 0
	counted = False
	f = open("RetriveNames.txt","r")
	for ssn in f:
		ssn = ssn.strip()
		for student in students:
			if ssn == student.getssn():
				age = int(student.getage())
				current += age
				counter += 1
				counted = True
				break
		if not counted:
			print("These SSN doesn't exist: ", ssn)
	print("Average age is: ", current/counter)
	t2 = time.time()
	t = t2-t1
	print("Time is : ", t)
	print()

#BSTInsert
def BSTInsertNames():
	t1 = time.time()
	with open("InsertNames.txt", 'r') as file:
		bststudents = bst.UUC()
		failures = 0
		for line in file:
			data = line.split()
			student = Student(data[0], data[1], data[2], data[3], data[4])
			if not students.bstinsert(student):
				failures +=1
		t2 = time.time()
		t = t2 - t1
		print("BST Insert")
		print("Time is" , t)
		print("Error: The SSN is the same as previous student:",data[2])
		print()
		return bststudents
gTOTAL_AGE = 0

def BSTAddAges(s):
	global gTOTAL_AGE
	gTOTAL_AGE += int(s.getAge())

def BSTDeleteNames(bststudents):
	t1 = time.time()
	with open("DeleteNames.txt", 'r') as file:
		success = 0
		failures = 0
		for line in file:
			data = line.strip()
			dummy_student = Student( 0, 0, data, 0, 0)
			if not bststudents.bstdelete(dummy_student):
				print("These SSN doesn't exist: ", ssn)
			else:
				success += 1
		t2 = time.time()
		t = t2 - t1
		print("BST Deleting")
		print("Time of deletion: ", t)
		print()

def BSTRetrieveNames(bststudents):
	t1 = time.time()
	with open("RetriveNames.txt", 'r') as file:
		total_age = 0
		total_students = 0
		failures = 0
		for line in file:
			data = line.strip()
			dummy = Student(0,0,data,0,0)
			studentR = bststudents.bstretrieve(dummy)
			if studentR is None:
				failures += 1
			else:
				total_age += int(studentR.age)
				total_students +=1
		avg_age = total_age / total_students
		t2 = time.time()
		t = t2 - t1
		print("Retrieving:")
		print("time of retrieval: ", t)
		print("avg age: ", avg_age)
		print()

def BSTTraverseNames(bststudents):
	t1 = time.time()
	bststudents.bsttraverse(BSTAddAges)
	avg_age = gTOTAL_AGE / bststudents.getSize()
	t2 = time.time()
	t = t2 - t1
	print("Traversing")
	print("Time of traversal: ", t)
	print("Avg Age: " , avg_age)
	print()

def print_items(item):
	print (item.ssn)

#Hash
def HASHInsertNames():
	t1 = time.time()
	with open("fakenames.txt", 'r') as file:
		hashstudents = hashtable.UUC(3000000)
		failures = 0
		for line in file:
			data = line.split()
			student = Student(data[0], data[1], data[2], data[3], data[4])
			if hashstudents.hashinsert(student) == False:
				failures +=1
		t2 = time.time()
		t = t2 - t1
		print("Hash Inserting")
		print("time of insertion: " , t)
		print("Successes: ", hashstudents.getSize())
		print("Error: The SSN is the same as previous student:",data[2])
		print()
		return hashstudents
gTOTAL_AGE = 0

def HASHAddAges(s):
	global gTOTAL_AGE
	gTOTAL_AGE += int(s.getAge())

def HASHDeleteNames(hashstudents):
	t1 = time.time()
	with open("deletenames.txt", 'r') as file:
		t1 = time.time()
		success = 0
		failures = 0
		for line in file:
			data = line.strip()
			dummy_student = Student( 0, 0, data, 0, 0)
			if hashstudents.hashdelete(dummy_student) == False:
				failures += 1
			else:
				success += 1
		t2 = time.time()
		t = t2 - t1
		print("Hash Deleting")
		print("Time of deletion: ", t)
		print()

def HASHRetrieveNames(hashstudents):
	t1 = time.time()
	with open("retrievenames.txt", 'r') as file:
		total_age = 0
		total_students = 0
		failures = 0
		for line in file:
			data = line.strip()
			dummy = Student(0,0,data,0,0)
			studentR = hashstudents.hashretrieve(dummy)
			if studentR:
				total_age += int(studentR.getAge())
				total_students +=1
			else:
				failures += 1
		avg_age = total_age / total_students
		t2 = time.time()
		t = t2 - t1
		print("Hash Retrieving:")
		print("time of retrieval: ", time)
		print("avg age: ", avg_age)
		print()

def HASHTraverseNames(hashstudents):
	t1 = time.time()
	hashstudents.hashtraverse(HASHAddAges)
	avg_age = gTOTAL_AGE / hashstudents.getSize()
	t2 = time.time()
	t = t2 - t1
	print("Hash Traversing")
	print("Time of traversal: ", t)
	print("Avg Age: " , avg_age)
	print()

def main():
	students = InsertNames()
	TraverseNames(students)
	DeleteNames(students)
	RetrieveNames(students)
	students = BSTInsertNames
	BSTTraverseNames(students)
	BSTDeleteNames(students)
	BSTRetrieveNames(students)
	students = HASHInsertNames()
	HASHTraverseNames(students)
	HASHDeleteNames(students)
	HASHRetrieveNames(students)

if __name__ == "__main__":
	main()
main()
