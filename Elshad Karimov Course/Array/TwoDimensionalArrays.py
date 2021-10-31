# Credits to Elshad Karimov from Udemy Course
## https://www.udemy.com/course/data-structures-and-algorithms-bootcamp-in-python/

### Practicing Two Dimensional Arrays in Python

import numpy as np

oneDimArray = np.array([1, 2, 3, 4])
print(oneDimArray)
twoDimArray = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]])  # O(mxn)
print(twoDimArray[0][2])

# inserting values in a two dimensional array

# using array method
print('Step 1 - using array method')
newTwoDimArray = np.insert(twoDimArray, 0, [[1, 2, 3, 4]], axis=0)  # 1 col, 0 row
print(newTwoDimArray)

# using append method
print('Step 2 - using append method')
newTwoDimArray_2 = np.append(twoDimArray, [[1, 2, 3, 4]], axis=0)  # 1 col, 0 row
print(newTwoDimArray_2)

# access elements in two dimensional array
print('Step 3 - accessing elements from a two dimensional array')


def access_elements(array, row_index, col_index):
    """
    Time and space complexity is constant O(1)
    """
    assert int(row_index) == row_index and int(col_index) == col_index, 'The row and col index has to be integers'
    if row_index >= len(array) or col_index >= len(
            array[0]):  # >= because the index starts from 0 ## len(array[0]) return column number, otherwise row number
        return print(
            f"The max dimension of your array is {len(array)} rows and {len(array[0])} cols, starting from 0 index")
    return print(array[row_index][col_index])


access_elements(newTwoDimArray_2, 2, 3)

# Array traversal from a two dimensional array
print('Step 4 - Array traversal from a two dimensional array')


def traverse_two_dim_array(array):
    """
    Space dedicated for documentation.
    Time complexity O(n^2)
    Space complexity O(1)
    """
    try:
        len(array[0])  # Time Complexity O(1) constant
    except:
        print(
            f"The array must be multidimensional. Your array has {len(array)} rows, where are the columns?")  # Time and Space Complexity O(1) constant
    else:
        for i in range(
                len(array)):  # Time Complexity O(mn) because it has nested loops and needed to look for every row
            for j in range(len(array[0])):  # Time Complexity O(n) because it has to look for n columns
                print(array[i][j])  # Time Complexity O(1) constant


traverse_two_dim_array(twoDimArray)

# Searching an element from a two dimensional array
print('Step 5 - Searching an element from a two dimensional array')


def search_two_dim_array(array, value):
    """
    Space dedicated for documentation.
    Time complexity O(n^2)
    Space complexity O(1)
    """
    try:
        len(array[0])  # Time complexity is O(1) constant
    except:
        print(
            f"The array must be multidimensional. Your array has {len(array)} rows. Where are the columns?")  # Time complexity is O(1) constant
    else:
        for i in range(
                len(array)):  # the search starting from rows ## Time Complexity O(mn) because it has nested loops and needed to look for every row
            for j in range(len(array[
                                   0])):  # then looking through columns ## Time Complexity O(n) because it has to look for n columns
                if value == array[i][j]:  # Time complexity is O(1)
                    return print('Starting from zero index, the first occurrence of value is located at row ' + str(
                        i) + " and column " + str(j))
        return print('The value was not found')


search_two_dim_array(twoDimArray, 13)
print(twoDimArray)

# Deleting row or column from a two dimensional array
print('Step 6 - Deleting row or column from a two dimensional array')


def delete_row_col_two_dim_array(array, index, row_or_col):
    """
    Space for documentation.
    Did not resolve the assert for index as an integer type.
    """
    assert int(index) == index, "The index must be positive integer"
    try:
        len(array[0])
    except:
        print(f"The array must be multidimensional. Your array has {len(array)} rows. Where are the columns?")
    else:
        if row_or_col == 'r':
            temp = array
            print(np.delete(temp, index, axis=0))
        elif row_or_col == 'c':
            temp = array
            print(np.delete(temp, index, axis=1))
        else:
            print('The row_or_col must be r for row or c for column')


delete_row_col_two_dim_array(twoDimArray, 3, 'c')
print(twoDimArray)


