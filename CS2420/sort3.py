import random
import math
import sys

class Counter:
	def __init__(self):
		self.compares = 0

def CreateRandomList(N):
	A=[]
	for i in range(N):
		r=random.randrange(0,N)
		A.append(r)
	return A

def MostlySorted(A):
	A = CreateRandomList(A)
	A.sort()
	A[0],A[-1] = A[-1],A[0]
	return A

def BubbleSort(A, c):
	done = False
	while not done:
		done = True
		for i in range(len(A)-1):
			c.compares += 1
			if A[i]>A[i+1]:
				A[i],A[i+1] = A[i+1],A[i]
				done = False
	return

def ShakerSort(A, c):
	done = False
	while not done:
		done = True
		for i in range(len(A)-1):
			c.compares += 1
			if A[i] > A[i+1]:
				A[i],A[i+1] = A[i+1],A[i]
				done = False
		for i in range(len(A)-1,0,-1):
			c.compares += 1
			if A[i] < A[i-1]:
				A[i-1],A[i] = A[i],A[i-1]
				done = False
	return

def CountingSort(A, c):
	F=[0]*len(A)
	for v in A:
		F[v]+=1
	k=0
	for i in range(len(F)):
		value=i
		count=F[i]
		for j in range(count):
			A[k]=value
			k+=1
	c.compares += len(A)
	return

def MergeSort(A, c):
	if len(A)<=1:
		return
	mid = len(A)//2
	L = A[:mid]
	R = A[mid:]
	MergeSort(L, c)
	MergeSort(R, c)
	i = 0
	j = 0
	k = 0
	while i<len(L) and j<len(R):
		c.compares += 1
		if L[i] < R[j]:
			A[k] = L[i]
			i+=1
		else:
			A[k] = L[i]
			j+=1
		k+=1
	while i < len(L):
		A[k] = L[i]
		i+=1
		k+=1
	while j < len(R):
		A[k] = R[j]
		j+=1
		k+=1
	return

def QuickSort(A, c,low,high):
	if high - low <= 0:
		return
	lmgt = low+1
	for i in range(low+1, high):
		c.compares += 1
		if A[i] < A[low]:
			A[i],A[lmgt] = A[lmgt],A[i]
			lmgt+=1
	A[low],A[lmgt-1] = A[lmgt-1],A[low]
	QuickSort(A,c, low,lmgt-1)
	QuickSort(A, c, lmgt,high)
	return

def ModQuickSort(A,c,  low, high):
	if high - low <= 0:
		return
	mid = (high + low)//2
	A[low],A[mid] = A[mid],A[low]
	lmgt = low+1
	for i in range(low+1, high):
		c.compares += 1
		if A[i] < A[low]:
			A[i],A[lmgt] = A[lmgt],A[i]
			lmgt+=1
	A[low],A[lmgt-1] = A[lmgt-1],A[low]
	ModQuickSort(A, c,low,lmgt-1)
	ModQuickSort(A,c,lmgt,high)
	return

def quick(a,c):
	QuickSort(a,c,0,len(a))

def modquick(a,c):
	ModQuickSort(a,c,0,len(a))

def main():
	sys.setrecursionlimit(5000)
	sorts = [BubbleSort, ShakerSort, CountingSort, MergeSort, quick, modquick]

	print(end="\t")
	for sort in sorts:
		print("%11s" % (sort.__name__), end=" ")
	print()
	for i in range(3,12):
		print(i, end="\t")
		for sort in sorts:
			a = CreateRandomList(2**i)
			c = Counter()
			sort(a,c)
			print("%11.2f" % (math.log(c.compares,2)), end=" ")
		print()

	print(end="\t")
	for sort in sorts:
		print("%11s" % (sort.__name__),end=" ")
	print()
	for i in range(3,12):
		print(i, end="\t")
		for sort in sorts:
			a = MostlySorted(2**i)
			c = Counter()
			sort(a,c)
			print("%11.2f" % (math.log(c.compares,2)), end=" ")
		print()

main()
