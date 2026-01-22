import time
import UUC
from student import Student

class AgeHolder:
	def __init__(self):
		self.mAge = 0

	def addAges(s, data):
		data.mAge += int(s.getage())

def main():
	t1 = time.time()
	f = open("FakeNames.txt","r")
	allStudents = UUC.UUC()
	for line in f:
		fields = line.split()
		s = Student(fields[0], fields[1], fields[2], fields[3]. fields[4])
		ok = allStudents.Insert(s)

		if not ok:
			print("Error", fields[0], fields[1], fields[2]. fields[3], fields[4])
		#Traverse
		data = AgeHolder()
		allStudents.Traverse(addAges(data))
		print("average is ", data.mAge/allStudents.size())

	f.close()
	t2 = time.time()
	print("Time is: ", t2-t1)


main()
