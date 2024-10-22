# Arrays

- The global variable is used when you want to modify a global variable from inside the function.
  - It is not used inside loops.

# Bubble Sort

- If n is the length of the array:
  - Outer loop: for i in range(n-1)
  - Inner loop: for j in range(n-i-1)
- It is possible to reverse an array by doing my_array[::-1]

- Starting from the left, it compares each consecutive numbers and then moves the bigger number to the right. If the first time it went "n" positions tot he right, next time it will go "n-1" positions.
# Selection Sort

- If n is the length of the array:
  - Outer loop: for i in range(n-1)
  - min_index = i
  - Inner loop: for j in range(i+1, n)

- Find the smallest element in the entire list. Swap it with the first unsorted element. Move to the second element. Find the smallest element in the sub list that has all the numbers except for the first element. Move it to the second of the previous list or the first position of the sub list. repeat for the third element.

# Insertion Sort

- If n is the length of the array:
  - Outer loop: for i in range(1, n)
  - insert_index = i
  - Inner loop: for j in range(i-1, -1, -1)

- It assumes the first element is sorted.
- It takes out number "n". It compares "n" to all the values before it. If there is a number greater than "n", it inserts the "n" in the place of that number.
