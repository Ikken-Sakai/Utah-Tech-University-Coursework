                .global calc_pencil, get_used, clear_used
                .text

				#a0 = board
				#a1 = group
				#a2 = used
				#a3 = group_index
				#a4 = element
				#a5 = count
				#a6 = position

# get_used(board, group) -> used
get_used:
 				li		a2, 0		#used = 0
				li		a3, 0		#group_index = 0
1:				add		t0, a1, a3	#board_index = group[group_index]
				lb		t0, (t0)	
				slli	t0, t0, 1					
				add		t0, a0, t0
				lh		a4, (t0)
				li      a5, 0		#count = 0
				li		a6, 1		#position = 1

2:				li		t1, 1		#mask = 1 << position
				sll		t1, t1, a6
				and		t2, a4, t1	#temp = element & mask
				beqz	t2, 3f		#if temp is non-zero:
				addi	a5, a5, 1	#count += 1

3:				addi	a6, a6, 1	#position++
				li		t3, 9
				ble		a6, t3, 2b	#if position <= 9: goto 2b
				li		t4, 1
				bne		a5, t4, 4f	#if count != 1: goto 4f
				or		a2, a2, a4

4:				addi	a3, a3, 1	#group_index++
				li		t3, 9
				blt		a3, t3, 1b	#if group_index < 9: goto 1b
				mv		a0, a2
				ret					#return used

# clear_used(board, group, used)
clear_used:
				not		a2, a2		#used = ~used(flip the bits) 
				li		t5, 0		#change_made = 0
				li		a3, 0		#group_index = 0

1:				add		t0, a1, a3	#board_index = group[group_index]
				lb		t0, (t0)	
				slli	t0, t0, 1					
				add		t0, a0, t0	#element = board[board_index]
				lh		a4, (t0)
				li      a5, 0		#count = 0
				li		a6, 1		#position = 1

2:				li		t1, 1		#mask = 1 << position
				sll		t1, t1, a6
				and		t2, a4, t1	#temp = element & mask
				beqz	t2, 3f		#if temp is non-zero:
				addi	a5, a5, 1	#count += 1									

3:				addi	a6, a6, 1	#position++
				li		t3, 9
				ble		a6, t3, 2b	#if position <= 9: goto 2b
				li		t4, 1
				bne		a5, t4, 4f	#if count != 1: goto 4f
				j		5f			#goto 5f

4:				and		t6, a4, a2	#new_element = element & used
				sh		t6, (t0)
				beq		t6, a4, 5f	#if new_element == element: goto 5f
				li		t5, 1		#change_made = 1

5:				addi	a3, a3, 1	#group_index++
				li		t3, 9
				blt		a3, t3, 1b	#if group_index < 9: goto 1b
				mv		a0, t5
				ret					#return change_made

# calc_pencil(board, table)
calc_pencil:
				addi 	sp, sp, -16
				sw 		s0, 0(sp) 				
				li		a2, 0		#changed = 0
				li		a3, 0		#group_start = 0
1:
				add		a1, a1, a2	#sum = table + group_start
				add		t0, a0, t0
				hw		a0, (t0)
				call	get_used
				call	clear_used
				beqz	a1, 2f
				li		a3, 1
2;
				li		t1, 27
				li		t2, 9
				MUL		t3, t1, t2
				blt		a3, t3, 1b
				mv		a0, a3
                ret
