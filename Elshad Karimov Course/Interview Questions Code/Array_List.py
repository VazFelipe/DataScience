# Credits to Elshad Karimov from Udemy Course
# https://www.udemy.com/course/data-structures-and-algorithms-bootcamp-in-python/

# Finding the missing number in an integer list of 1 to n

import numpy as np

list_missing = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
                29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54,
                55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
                81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]


# list_test = list(range(1, 100+1))

def find_missing_number(mylist):
    """
    This line is intended for documentation.
    """
    list_total = max(mylist) * (max(mylist) + 1) / 2
    list_user = sum(mylist)
    print(list_total - list_user)


print('Step 1 - Finding the missing number in an integer list of 1 to n')
find_missing_number(list_missing)

# Finding the pairs in an integer list of 1 to n

list_pairs = [1, 2, 3, 2, 3, 4, 5, 6]


def find_pairs(mylist, target):
    """
    This line is intended for documentation.
    """
    for i in range(len(mylist)):
        for j in range(i + 1, len(mylist)):
            if mylist[i] == mylist[j]:
                continue
            elif mylist[i] + mylist[j] == target:
                print(i, j)


print('Step 2 - Finding the pairs in an integer list of 1 to n')
find_pairs(list_pairs, 12)

# Check if an array contains a number in Python

array_number = np.array([1, 2, 3, 2, 3, 4, 5, 6])


def find_number(my_array, find):
    for i in range(len(my_array)):
        if my_array[i] == find:
            print(i)


print('Step 3 - Check if an array contains a number in Python')
find_number(array_number, 2)

print('Step Extra - Checking is an year is Leap Year')
# fill in an year in the list, in this case, 2001 is not a leap year and 2000 is a leap year

list_year = [2000, 2001, 2004]


# full leap year's test list [1900, 2000, 2004, 2008, 2012, 2016, 2020, 2024, 2028, 2032, 2036, 2040, 2044, 2048]


def find_leap_year(my_list):
    """
    This line is intended for documentation.
    """
    cond1 = 4
    cond2 = 100
    cond3 = 400

    for i in range(0, len(list_year)):
        div_year_cond1 = (list_year[i] / cond1)
        div_year_cond2 = (list_year[i] / cond2)
        div_year_cond3 = (list_year[i] / cond3)
        verify_year_cond1 = int(div_year_cond1) == div_year_cond1
        verify_year_cond2 = int(div_year_cond2) != div_year_cond2
        verify_year_cond3 = int(div_year_cond3) == div_year_cond3
        if verify_year_cond1 and verify_year_cond2:
            print(f'{list_year[i]} is a leap year')
        elif verify_year_cond1 and verify_year_cond3:
            print(f'{list_year[i]} is a leap year')
        else:
            print(f'{list_year[i]} is not a leap year')


find_leap_year(list_year)

print('Step 4 - Finding a maximum product of two integers in the array where all elements are positive')

array_step_4 = np.array([1, 20, 30, 44, 5, 56, 57, 8, 9, 10, 31, 12, 13, 14, 35, 16, 27, 58, 19, 21])


def find_max_product(my_array):
    max_product = 0
    for i in range(len(my_array)):
        for j in range(i + 1, len(my_array)):
            if my_array[i] * my_array[j] > max_product:
                max_product = my_array[i] * my_array[j]
                my_array_pairs = str(my_array[i]) + " and " + str(my_array[j]) + " (" + str(my_array[i]) + " * " + str(
                    my_array[j]) + " = " + str(max_product) + ")"
    print(f'The maximum product of two integers in the array is {max_product}.')
    print(f'The pairs that generates the maximum product is {my_array_pairs}.')


find_max_product(array_step_4)

print('Step 5 - Checking is a list has unique values and return True or False')

list_step_5 = [1, 20, 30, 44, 5, 56, 57, 8, 9, 10, 31, 12, 13, 14, 35, 16, 27, 58, 19, 21]


def is_unique(my_list):
    """
    This space is intended for documentation.
    """
    list_temp = []
    for i in my_list:
        if i in list_temp:
            print(i)
            return False
        else:
            list_temp.append(i)
    return True


is_unique(list_step_5)


print('Step 6 - Checking if two lists are permutation of each other')

list_1 = [1, 3, 2]
list_2 = [2, 1, 3]


def permutation(list1, list2):
    if len(list1) != len(list2):
        return False
    list1.sort()
    list2.sort()
    if list1 == list2:
        for i in range(0, len(list1)):
            print(list1[i], list2[i])
        return True
    else:
        for i in range(0, len(list1)):
            print(list1[i], list2[i])
        return False


print(permutation(list_1, list_2))


print('Step 7 - Rotating a matrix in an array')
# This is one hard to do, so a tried to explain it step by step

# creating an 3 x 3 matrix
array_rotating = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# printing the matrix for better understanding about its shape
print(array_rotating)

# setting n to the number of rows in the matrix
n = len(array_rotating)

# getting all the parameters inside the function and displaying it
# printing n
print('n')
print(n)

# printing n divided by 2 and returning a whole number
print('n//2')
print(n//2)

# printing range of n divided by 2
print('range(n//2)')
print(range(n//2))

# printing n minus layer minus 1
print('n - layer - 1')
print(n - (n//2) - 1)


# creating a function
def rotate_matrix(matrix):
    n = len(matrix)
    for layer in range(n//2):
        first = layer
        last = n - layer - 1
        for i in range(first, last):
            # saving the top element
            top = matrix[layer][i]
            # moving left element to the top
            matrix[layer][i] = matrix[-i-1][layer]
            # moving bottom element to the left
            matrix[-i-1][layer] = matrix[-layer-1][-i-1]
            # moving right element to the bottom
            matrix[-layer-1][-i-1] = matrix[i][-layer-1]
            # moving top element to the right
            matrix[i][-layer-1] = top
    return print(matrix)

rotate_matrix(array_rotating)