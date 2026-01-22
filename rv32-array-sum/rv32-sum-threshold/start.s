                .global _start
                .equ    stdout, 1
                .equ    sys_write, 64
                .equ    sys_exit, 93
                .include "lib/macros.si"


                .data

                # each element is stored as a 32-bit value
                .balign 4
test_array_1:   .4byte  5
                .equ    test_len_1, 1
test_array_2:   .4byte  2, 13, 16, 24, 5, 7, 11, 10, 6, 13
                .equ    test_len_2, 10
test_array_3:   .4byte  2, 13, 16, 10000, 24, 5, 7, 11, 10, 6, 13
                .equ    test_len_3, 11

newline:        .ascii  "\n"
                .equ    newline_len, (. - newline)

                .text
                # test the function with the arrays above
_start:
                la      a0, test_array_1
                li      a1, test_len_1
                li      a2, 10
                la      a4, array_sum
                call    call_function
                call    print_n
                print   newline

                la      a0, test_array_1
                li      a1, test_len_1
                li      a2, 0
                la      a4, array_sum
                call    call_function
                call    print_n
                print   newline

                la      a0, test_array_1
                li      a1, test_len_1
                li      a2, 5
                la      a4, array_sum
                call    call_function
                call    print_n
                print   newline

                la      a0, test_array_1
                li      a1, test_len_1
                li      a2, 6
                la      a4, array_sum
                call    call_function
                call    print_n
                print   newline

                la      a0, test_array_2
                li      a1, test_len_2
                li      a2, 0
                la      a4, array_sum
                call    call_function
                call    print_n
                print   newline

                la      a0, test_array_2
                li      a1, test_len_2
                li      a2, 2
                la      a4, array_sum
                call    call_function
                call    print_n
                print   newline

                la      a0, test_array_2
                li      a1, test_len_2
                li      a2, 3
                la      a4, array_sum
                call    call_function
                call    print_n
                print   newline

                la      a0, test_array_2
                li      a1, test_len_2
                li      a2, 10
                la      a4, array_sum
                call    call_function
                call    print_n
                print   newline

                la      a0, test_array_2
                li      a1, test_len_2
                li      a2, 13
                la      a4, array_sum
                call    call_function
                call    print_n
                print   newline

                la      a0, test_array_2
                li      a1, test_len_2
                li      a2, 14
                la      a4, array_sum
                call    call_function
                call    print_n
                print   newline

                la      a0, test_array_3
                li      a1, test_len_3
                li      a2, 0
                la      a4, array_sum
                call    call_function
                call    print_n
                print   newline

                li      a0, 0
                li      a7, sys_exit
                ecall
