                .global array_sum
                .text

# int array_sum(int *array, int count)
				#a0 = array
				#a1 = count
				#a3 = sum
				#a4 = predicate
				#a5 = array
				#a6 = i
array_sum:
				li		a3, 0		#sum = 0
				li		a6, 0		#i = 0
				jal		2f			#jump to 2f
1:				
									#if not predicate(array[i]) goto 3f
									#sum += array[i]
3:
				addi	a6, a6, 1	#i ++
2:
				blt		a6, a1, 1b	#if i < count: goto 1b
				mv		a0, a3		#return sum
                ret
