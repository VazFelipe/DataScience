# Credits to Elshad Karimov from Udemy Course
## https://www.udemy.com/course/data-structures-and-algorithms-bootcamp-in-python/

### Practicing Two Dimensional Arrays in Python

import numpy as np

oneDimArray = np.array([1,2,3,4])
print(oneDimArray)
twoDimArray = np.array([[11,15,10,6], [10,14,11,5], [12,17,12,8], [15,18,14,9]]) # O(mxn)
print(twoDimArray[0][2])

# inserting values in a two dimensional array

# using array method
print('Step 1 - using array method')
newTwoDimArray = np.insert(twoDimArray, 0, [[1,2,3,4]], axis=0) # 1 col, 0 row
print(newTwoDimArray)

# using append method
print('Step 2 - using append method')
newTwoDimArray_2 = np.append(twoDimArray, [[1,2,3,4]], axis=0) # 1 col, 0 row
print(newTwoDimArray_2)

# access elements in two dimensional array
print('Step 3 - accessing elements from a two dimensional array')
def access_elements(array, row_index, col_index):
    """
    Time and space complexity is constant O(1)
    """
    assert int(row_index) == row_index and int(col_index) == col_index, 'The row and col index has to be integers'
    if row_index >= len(array) or col_index >= len(array[0]): # >= because the index starts from 0 ## len(array[0]) return column number, otherwise row number
        return print(f"The max dimension of your array is {len(array)} rows and {len(array[0])} cols, starting from 0 index")
    return print(array[row_index][col_index])

access_elements(newTwoDimArray_2, 2, 3)

# Array traversal from a two dimensional array
print('Step 4 - Array traversal from a two dimensional array')

def traverse_two_dim_array(array):
    try:
        len(array[0])
    except:
        print(f"The array must be multidimensional. Your array has {len(array)} rows, where are the columns?")
    else:
        for i in range(len(array)):
            for j in range(len(array[0])):
                print(array[i][j])

traverse_two_dim_array(oneDimArray)
