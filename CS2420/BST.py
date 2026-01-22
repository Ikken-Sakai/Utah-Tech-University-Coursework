import bst
import time

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



def insertNames():
	t1 = time.time()
	with open("InsertNames.txt", 'r') as file:
		students = bst.UUC()
		failures = 0
		for line in file:
			data = line.split()
			student = Student(data[0], data[1], data[2], data[3], data[4])
			if not students.insert(student):
				failures +=1
		t2 = time.time()
		t = t2 - t1
		print("BST Insert")
		print("Time is" , t)
		print("Error: The SSN is the same as previous student:",data[2])
		print()
		return students
gTOTAL_AGE = 0

def addAges(s):
	global gTOTAL_AGE
	gTOTAL_AGE += int(s.getAge())

def deleteNames(students):
	t1 = time.time()
	with open("DeleteNames.txt", 'r') as file:
		success = 0
		failures = 0
		for line in file:
			data = line.strip()
			dummy_student = Student( 0, 0, data, 0, 0)
			if not students.delete(dummy_student):
				failures += 1
			else:
				success += 1
		t2 = time.time()
		t = t2 - t1
		print("Deleting")
		print("Time of deletion: ", t)
		print("successes: ", success)
		print("failures ", failures)
		print()

def retrieveNames(students):
	t1 = time.time()
	with open("RetriveNames.txt", 'r') as file:
		total_age = 0
		total_students = 0
		failures = 0
		for line in file:
			data = line.strip()
			dummy = Student(0,0,data,0,0)
			studentR = students.retrieve(dummy)
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
		print("success: ", total_students)
		print("failures: ", failures)
		print("avg age: ", avg_age)
		print()

def traverseNames(students):
	t1 = time.time()
	students.traverse(addAges)
	avg_age = gTOTAL_AGE / students.getSize()
	t2 = time.time()
	t = t2 - t1
	print("Traversing")
	print("Time of traversal: ", t)
	print("Avg Age: " , avg_age)
	print()

def print_items(item):
	print (item.mssn)

def main():
	students = insertNames()
	traverseNames(students)
	deleteNames(students)
	retrieveNames(students)

if __name__ == "__main__":
	main()
