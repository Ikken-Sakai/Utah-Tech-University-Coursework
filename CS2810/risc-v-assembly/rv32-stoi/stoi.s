                .global stoi
                .text

				#a0 = string
				#a1 = n
				#a2 = c
				#a3 = is_negative
				
stoi:
                # your code goes here
                li		a1, 0		#n = 0
                li		a3, 0		#is_negative = 0
                					
1:									
				lw		t0, '-'		#if string == '-': goto 2f
				beq		a0, t0, 2f
				jal		3f			#jump to 3f
2:
				li		a3, 1		#is_negative = 1
				addi	a0, a0, 1	#string ++
3:
				mv		a2, a0		#c = string
4:
				lw		t1, '0'		#if c >= '0' && c <= '9': goto 5f
				lw		t2, '9'
				bge		a3, t1
				ble		a4, t2
				and		a3, a4, 5f
				jal		7f			#jump to 7f
5:
									#n = n * 10 + (c - '0')
				addi	a2, ao, 1	#c = string ++
6:
				lw		t3, '\0'	#if c != '\0': goto 4b
				bne		a2, t3, 4b
7:
				li		t4, 1		#if is_negative = 1: goto 9f
				
8:
									#return n = 0 - n
9:
									#return n
                ret
