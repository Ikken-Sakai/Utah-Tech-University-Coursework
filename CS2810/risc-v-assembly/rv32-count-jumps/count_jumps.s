                .global count_jumps
                .text


				#a0 = array
				#a1 = size
				#a2 = count
				#a3	= curr_index
				#a4 = element

# int count_jumps(int *array, int size)
count_jumps:
				li		a2, 0		#count = 0
				mv		a3, a1		#curr_index = size
1:
				add		t0, a0, a3	#element = array[curr_index]	
				lb		t0, (t0)
				slli	t0, t0, 1
				add		t0, a3, t0
				lh		a4, (t0)
				mv		a3, a4		#curr_index = element
				li		t1, 1		#if curr_index == 1: goto 2f
				beq		a3, t1, 2f
				bgt		a3, a1, 3f	#if curr_index > size: goto 3f
				blez	a3, 3f		#if curr_index < 0: goto 3f
2:
				addi	a2, a2, 1	#count ++
				ble		a3, a1, 1b	#if curr_index <= size: goto 1b
3:
				mv		a1, a2
				ret
