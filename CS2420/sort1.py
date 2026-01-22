import random

def CreateRandomList(N):
	A=[]
	for i in range(N):
		r=random.randrange(0,N)
		A.append(r)
	return A

def BubbleSort(A):
	movingthings = True
	while movingthings:
		movingthings = False
		for i in range(len(A)-1):
			if A[i]>A[i+1]:
				A[i],A[i+1] = A[i+1],A[i]
				movingthings = True
	return

def ShakerSort(A):
	movingthings = True
	while movingthings:
		movingthings = False
		for i in range(len(A)-1):
			if A[i] > A[i+1]:
				A[i],A[i+1] = A[i+1],A[i]
				movingthings = True
		for i in range(len(A)-1,0,-1):
			if A[i] < A[i-1]:
				A[i-1],A[i] = A[i],A[i-1]
				movingthings = True
	return

def CountingSort(A):
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
	return

def MergeSort(A):
	if len(A)<=1:
		return
	mid = len(A)//2
	L = A[:mid]
	R = A[mid:]
	MergeSort(L)
	MergeSort(R)
	i = 0
	j = 0
	k = 0
	while i<len(L) and j<len(R):
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

def QuickSort(A,low,high):
	if high - low <= 0:
		return
	lmgt = low+1
	for i in range(low+1, high):
		if A[i] < A[low]:
			A[i],A[lmgt] = A[lmgt],A[i]
			lmgt+=1
	A[low],A[lmgt-1] = A[lmgt-1],A[low]
	QuickSort(A,low,lmgt-1)
	QuickSort(A,lmgt,high)
	return

def ModQuickSort(A, low, high):
	if high - low <= 0:
		return
	mid = (high + low)//2
	A[low],A[mid] = A[mid],A[low]
	lmgt = low+1
	for i in range(low+1, high):
		if A[i] < A[low]:
			A[i],A[lmgt] = A[lmgt],A[i]
			lmgt+=1
	A[low],A[lmgt-1] = A[lmgt-1],A[low]
	ModQuickSort(A,low,lmgt-1)
	ModQuickSort(A,lmgt,high)
	return

def main():
	N = 10
	A = CreateRandomList(N)
	B = A[:]
	B.sort()

	print(A)

	BubbleSort(A)
	if B != A:
		print(A, "Error in BubbleSort")
	else:
		print("Bubble", A)

	ShakerSort(A)
	if B != A:
		print(A, "Error in ShakerSort")
	else:
		print("Shaker", A)

	CountingSort(A)
	if B != A:
		print(A, "Error in CountingSort")
	else:
		print("Counting", A)

	MergeSort(A)
	if B != A:
		print(A, "Error in MergeSort")
	else:
		print("Merge", A)

	QuickSort(A, 0, len(A)-1)
	if B != A:
		print(A, "Error in QuickSort")
	else:
		print("Quick", A)

	ModQuickSort(A, 0, len(A)-1)
	if B != A:
		print(A, "Error in ModQuickSort")
	else:
		print("Mod", A)


main()
