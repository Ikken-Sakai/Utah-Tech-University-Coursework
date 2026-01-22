                .global _start
                .equ    sys_exit, 93

                .data
array1:         .4byte  1
array2:         .4byte  -1
array3:         .4byte  -1, -1, -1
array4:         .4byte  0, 2, -3, -1, 2, -1, -5, 0, 0, -4
array5:         .4byte  20, 9, 9, 9, 9, 9, 9, 9, 9, 9
                .4byte  -10, -10, -10, -10, -10, -10, -10, -10, -10, -10
msg_testing:    .asciz  "\nTesting with the array: "
msg_comma:      .asciz  ", "
msg_newline:    .asciz  "\n"
msg_expected:   .asciz  "\nExpecting return value of:  "
msg_actual:     .asciz  "\nGot actual return value of: "

                .text
_start:
				.option	push
				.option norelax
				la		gp, __global_pointer$
				.option pop

                # test the function with each of the arrays above
                la      a0, array1
                li      a1, 1
                li      a2, 1
                call    run_test

                la      a0, array2
                li      a1, 1
                li      a2, 1
                call    run_test

                la      a0, array3
                li      a1, 3
                li      a2, 3
                call    run_test

                la      a0, array4
                li      a1, 10
                li      a2, 7
                call    run_test

                la      a0, array5
                li      a1, 20
                li      a2, 20
                call    run_test

                li      a0, 0
                li      a7, sys_exit
                ecall


run_test:
                addi    sp, sp, -24
                sw      ra, 20(sp)
                sw      s3, 12(sp)
                sw      s2, 8(sp)
                sw      s1, 4(sp)
                sw      s0, 0(sp)

                mv      s0, a0
                mv      s1, a1
                mv      s2, a2

                la      a0, msg_testing
                call    puts

                li      s3, 0
1:
                beqz    s3, 2f
                la      a0, msg_comma
                call    puts
2:
                slli    t0, s3, 2
                add     t0, s0, t0
                lw      a0, (t0)
                call    print_n
                addi    s3, s3, 1
                blt     s3, s1, 1b

                la      a0, msg_expected
                call    puts
                mv      a0, s2
                call    print_n
                la      a0, msg_actual
                call    puts

                mv      a0, s0
                mv      a1, s1
                la      a4, count_jumps
                call    call_function
                call    print_n
                la      a0, msg_newline
                call    puts

                lw      ra, 20(sp)
                lw      s3, 12(sp)
                lw      s2, 8(sp)
                lw      s1, 4(sp)
                lw      s0, 0(sp)
                addi    sp, sp, 24
                ret
