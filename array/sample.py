###################################################################################################
# Find the lowest value in an array
###################################################################################################

""" my_array = [7, 12, 9, 4, 11]
minVal = my_array[0]

for num in my_array:

    if num < minVal:
        minVal = num
    
print(minVal) """

###################################################################################################
# Implement bubble sort algorithm on an array - Ascending
###################################################################################################

""" my_array = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(my_array)

for i in range(n-1):
    for j in range(n-1-i):

        if my_array[j] > my_array [j+1]:

            my_array[j], my_array[j+1] = my_array[j+1], my_array[j]

print(my_array) """

###################################################################################################
# Implement bubble sort algorithm on an array - Descending
###################################################################################################

""" my_array = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(my_array)

for i in range(n-1):
    for j in range(n-1-i):

        if my_array[j] < my_array [j+1]:

            my_array[j], my_array[j+1] = my_array[j+1], my_array[j]

print(my_array) """

###################################################################################################
# Improvement on bubble sort algorithm on an array - Ascending
###################################################################################################

""" my_array = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(my_array)

for i in range(n-1):

    for j in range(n-1-i):

        swapped = False

        if my_array[j] > my_array [j+1]:

            my_array[j], my_array[j+1] = my_array[j+1], my_array[j]

            swapped = True
    
    if not swapped:
        break

print(my_array)  """

###################################################################################################
# Implement selection sort algorithm on an array - Ascending
###################################################################################################

""" my_array = [64, 34, 25, 5, 22, 11, 90, 12]

n = len(my_array)

for i in range(n-1):

    min_index = i

    for j in range(i+1, n):

        if my_array[j] < my_array[min_index]:
            min_index = j
    
    min_value = my_array.pop(min_index)
    my_array.insert(i, min_value)

print(my_array) """

###################################################################################################
# Implement selection sort algorithm on an array - Descending
###################################################################################################

""" my_array = [64, 34, 25, 5, 22, 11, 90, 12]

n = len(my_array)

for i in range(n-1):

    min_index = i

    for j in range(i+1, n):

        if my_array[j] > my_array[min_index]:
            min_index = j
    
    min_value = my_array.pop(min_index)
    my_array.insert(i, min_value)

print(my_array) """

###################################################################################################
# Improvement on selection sort algorithm on an array - Ascending
###################################################################################################

""" my_array = [64, 34, 25, 5, 22, 11, 90, 12]

n = len(my_array)

for i in range(n-1):

    min_index = i

    for j in range(i+1, n):

        if my_array[j] < my_array[min_index]:
            min_index = j
    
    my_array[i], my_array[min_index] = my_array[min_index], my_array[i]

print(my_array) """