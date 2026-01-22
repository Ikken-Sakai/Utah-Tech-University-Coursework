                .global array_max
                .text
				
				#a0: array
				#a1: count
				#a2: i
				#a3: max
				#a4: elt

# int array_max(int *array, int count)
array_max:
				lw		a3, (a0) 		#max = array[0]
				li 		a2, 1			#i = 1
				j 		2f				#jump tp 2f
1:				slli 	t0, a2, 2		#intelt = array[i]
				add 	t0, a0, t0
				lw		a4, (t0)
				ble		a4, a3, 3f		#if (elt <= max) goto 3
				mv		a3, a4			#max = elt	
3:				addi 	a2, a2, 1		#i++
2:				blt 	a2, a1, 1b		#if (i < count) goto 1
				mv 		a0, a3			#return max
				ret	
