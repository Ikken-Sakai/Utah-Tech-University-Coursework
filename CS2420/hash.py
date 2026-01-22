import hashtable
import sys
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

	def __int__(self):
		return int(self.ssn.replace('-', ''))

def insertNames():
	t1 = time.time()
	with open("InsertNames.txt", 'r') as file:
		students = hashtable.UUC(3000000)
		failures = 0
		for line in file:
			data = line.split()
			student = Student(data[0], data[1], data[2], data[3], data[4])
			if students.hashinsert(student) == False:
				failures +=1
		t2 = time.time()
		t = t2 - t1
		print("Inserting")
		print("time of insertion: " , t)
		print("Successes: ", students.hashgetSize())
		print("Error: The SSN is the same as previous student:",data[2])
		print()
		return students
gTOTAL_AGE = 0

def addAges(s):
	global gTOTAL_AGE
	gTOTAL_AGE += int(s.getAge())

def deleteNames(students):
	t1 = time.time()
	with open("deletenames.txt", 'r') as file:
		t1 = time.time()
		success = 0
		failures = 0
		for line in file:
			data = line.strip()
			dummy_student = Student( 0, 0, data, 0, 0)
			if students.hashdelete(dummy_student) == False:
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
	with open("RetrieveNames.txt", 'r') as file:
		total_age = 0
		total_students = 0
		failures = 0
		for line in file:
			data = line.strip()
			dummy = Student(0,0,data,0,0)
			studentR = students.hashretrieve(dummy)
			if studentR:
				total_age += int(studentR.getAge())
				total_students +=1
			else:
				failures += 1
		avg_age = total_age / total_students
		t2 = time.time()
		t = t2 - t1
		print("Retrieving:")
		print("time of retrieval: ", time)
		print("success: ", total_students)
		print("failures: ", failures)
		print("avg age: ", avg_age)
		print()

def traverseNames(students):
	t1 = time.time()
	students.hashtraverse(addAges)
	avg_age = gTOTAL_AGE / students.hashgetSize()
	t2 = time.time()
	t = t2 - t1
	print("Traversing")
	print("Time of traversal: ", t)
	print("Avg Age: " , avg_age)
	print()

def main():
	students = insertNames()
	traverseNames(students)
	deleteNames(students)
	retrieveNames(students)

if __name__ == "__main__":
	main()
