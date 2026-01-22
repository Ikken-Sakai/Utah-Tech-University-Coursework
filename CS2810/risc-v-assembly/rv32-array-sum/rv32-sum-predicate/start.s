                .global _start, threshold
                .equ    stdout, 1
                .equ    sys_write, 64
                .equ    sys_exit, 93
                .include "lib/macros.si"

                .data
                # each element is stored as a 32-bit value
test_array_1:   .4byte  5
                .equ    test_len_1, 1
test_array_2:   .4byte  2, 13, 16, 24, 5, 7, 11, 10, 6, 13
                .equ    test_len_2, 10

threshold:      .8byte  0
newline:        .ascii  "\n"
                .equ    newline_len, (. - newline)

                .text
_start:
                # test the function with the arrays above
                # using various threshold values
                la      a0, test_array_1
                li      a1, test_len_1
                li      t0, 10
                la      t1, threshold
                sw      t0, (t1)
                la      a4, array_sum
                call    call_function
                call    print_n
                print   newline

                la      a0, test_array_1
                li      a1, test_len_1
                li      t0, 0
                la      t1, threshold
                sw      t0, (t1)
                la      a4, array_sum
                call    call_function
                call    print_n
                print   newline

                la      a0, test_array_1
                li      a1, test_len_1
                li      t0, 5
                la      t1, threshold
                sw      t0, (t1)
                la      a4, array_sum
                call    call_function
                call    print_n
                print   newline

                la      a0, test_array_1
                li      a1, test_len_1
                li      t0, 6
                la      t1, threshold
                sw      t0, (t1)
                la      a4, array_sum
                call    call_function
                call    print_n
                print   newline

                la      a0, test_array_2
                li      a1, test_len_2
                li      t0, 0
                la      t1, threshold
                sw      t0, (t1)
                la      a4, array_sum
                call    call_function
                call    print_n
                print   newline

                la      a0, test_array_2
                li      a1, test_len_2
                li      t0, 2
                la      t1, threshold
                sw      t0, (t1)
                la      a4, array_sum
                call    call_function
                call    print_n
                print   newline

                la      a0, test_array_2
                li      a1, test_len_2
                li      t0, 3
                la      t1, threshold
                sw      t0, (t1)
                la      a4, array_sum
                call    call_function
                call    print_n
                print   newline

                la      a0, test_array_2
                li      a1, test_len_2
                li      t0, 10
                la      t1, threshold
                sw      t0, (t1)
                la      a4, array_sum
                call    call_function
                call    print_n
                print   newline

                la      a0, test_array_2
                li      a1, test_len_2
                li      t0, 13
                la      t1, threshold
                sw      t0, (t1)
                la      a4, array_sum
                call    call_function
                call    print_n
                print   newline

                la      a0, test_array_2
                li      a1, test_len_2
                li      t0, 14
                la      t1, threshold
                sw      t0, (t1)
                la      a4, array_sum
                call    call_function
                call    print_n
                print   newline

                # call the exit system call
                li      a0, 0
                li      a7, sys_exit
                ecall
