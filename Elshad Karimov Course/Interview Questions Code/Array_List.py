# Credits to Elshad Karimov from Udemy Course
## https://www.udemy.com/course/data-structures-and-algorithms-bootcamp-in-python/

### Finding the missing number in an integer list of 1 to n

list_missing = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
#list_test = list(range(1, 100+1))

def find_missing_number(mylist):
    """
    This line is intended for documentation.
    """
    list_total = max(mylist) * (max(mylist) + 1) / 2
    list_user = sum(mylist)
    print(list_total - list_user)

print('Step 1 - Finding the missing number in an integer list of 1 to n')
find_missing_number(list_missing)

### Finding the pairs in an integer list of 1 to n

list_pairs = [1, 2, 3, 2, 3, 4, 5, 6]

def find_pairs(mylist, target):
    """
    This line is intended for documentation.
    """
    for i in range(len(mylist)):
        for j in range(i+1, len(mylist)):
            if mylist[i] == mylist[j]:
                continue
            elif mylist[i] + mylist[j] == target:
                print(i, j)
print('Step 2 - Finding the pairs in an integer list of 1 to n')
find_pairs(list_pairs, 12)

### Check if an array contains a number in Python

import numpy as np

array_number = np.array([1, 2, 3, 2, 3, 4, 5, 6])

def find_number(myarray, find):
    for i in range(len(myarray)):
        if myarray[i] == find:
            print(i)

print('Step 3 - Check if an array contains a number in Python')
check_number(array_number, 2)