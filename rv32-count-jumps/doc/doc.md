Write a RISC-V function with the following prototype:

    int count_jumps(int *array, int size)

`array` is the address of an array of 32-bit integers, and `size` is
the number of entries in the array (so the total memory used by the
array is `4 × size`), and all `int` values mean 32-bit integers.

The function should do the following:

*   Start at the last element in the array (it will have at least
    one element)

*   Load the element from the array and add it to the current index

*   If the index is outside the bounds of the array, stop

*   Return the total number of array indices visited

For example, if you were given the array with these 5 numbers:

    0, 0, 1, 2, -2

*   You would start with index 4 (the last valid index in the
    array).
*   You would load the value -2 from the array, and adding that to
    the index would give a new index of 2.
*   The element with index 2 is 1, so you would add that to the
    index, yielding 3.
*   The element at index 3 is 2, so you would add 2 to the index and
    get 5.
*   Index 5 is past the end of the array, so you would stop.

Since you loaded a total of 3 values (-2, 1, and 2), you would
return 3.

Note that you should stop when the index is off either end of the
array.

Write your code in the file `count_jumps.s`.
