# Credits to Elshad Karimov from Udemy Course
## https://www.udemy.com/course/data-structures-and-algorithms-bootcamp-in-python/

### Practicing arrays in Python

# calling library
from array import *

# 1 - Create an array and traverse
print('Step 1')
my_array = array('i', [1, 2, 3, 4, 5])


def traverseAnArray(array):
    """
    Space dedicated for documentation.
    """
    for i in array:
        print(i)

traverseAnArray(my_array)

# 2 - Access individual elements through indexes
print('Step 2')
def accessIndividualElements(array, index):
    """
    Space dedicated for documentation.
    """
    if index >= len(array) or index < 0:
        print('The index dos not exist')
    else:
        print(array[index])

accessIndividualElements(my_array, 3)

# 3 - Append value in an array using append() method
print('Step 3')
def appendValue(array, value):
    """
    Space dedicated for documentation.
    """
    array.append(value)  # time complexity O(1) space complexity O(1)
    return print(array)  # time complexity O(1) space complexity O(1)

appendValue(my_array, 5)

# 4 - Insert value in an array using insert() method
print('Step 4')
def insertValue(array, index, value):
    """
    Space dedicated for documentation.
    """
    array.insert(index, value)  # time and space complexity O(n)
    return print(array)  # time and space complexity O(1), getting rid of constant it becomes O(n)

insertValue(my_array, 5, 6)

# 5 - Extend the array using extend() method
print('Step 5')
def extendArray(oldArray, newArray, direction):
    """
    The direction parameter is 'l' (left) or 'r' (right).
    """
    assert direction == 'l' or direction == 'r', 'The direction is l (left) or r (right)'
    if direction == 'l':
        newArray.extend(oldArray)
        return print(newArray)
    elif direction == 'r':
        oldArray.extend(newArray)
        return print(oldArray)

my_array2 = array('i', [77, 88, 99, 10])
extendArray(my_array, my_array2, 'r')

# 6 - Extend the array using fromlist() method
print('Step 6')
my_list = [11, 12, 13]

extendArray(my_array, my_list, 'l')

# 7 - Remove a value from array using remove() method
print('Step 7')
def remove_value(array, value):
    """
    Space dedicated for documentation.
    """
    array.remove(value)
    return print(array)

remove_value(my_array, 1)

# 8 - Remove the last array value using pop() method
print('Step 8')
def remove_last_value(array, last_value):
    """
    Space dedicated for documentation.
    """
    array.pop()
    print(array)

remove_last_value(my_array, 5)

# 9 - Fetch any element through its index using index() method
print('Step 9')
print(my_array.index(3))

# 10 Reverse an array using reverse() method
print('Step 10')
print(my_array)
my_array.reverse()
print(my_array)

# 11 Get array buffer information using buffer_info() method
print('Step 11')
print(my_array.buffer_info())

# 12 Count the number of times an element occur in an array using count() method
print('Step 12')
my_array.append(1)
print(my_array.count(1))

# 13 Convert an array using tobytes() and frombytes() method
print('Step 13')
temp_string = my_array.tostring()
print(temp_string)
new_array_int = array('i')
new_array_int.frombytes(temp_string)
print(new_array_int)

# 14 Convert my_array to a python list using tolist() method
print('Step 14')
# print(my_array.tolist())

# 15 Append a string to the char array using fromstring() method
print('Step 15')
new_array_int = array('i')
new_array_int.frombytes(temp_string)
print(new_array_int)

# 16 SLice elements from an array
print('Step 16')
print(my_array[1:4])
print(my_array[:4])
print(my_array[1:])

print('hello world')