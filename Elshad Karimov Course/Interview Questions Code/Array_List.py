# Credits to Elshad Karimov from Udemy Course
## https://www.udemy.com/course/data-structures-and-algorithms-bootcamp-in-python/

### Finding the missing number in an integer list of 1 to n

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

### Finding the pairs in an integer list of 1 to n

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

### Check if an array contains a number in Python

import numpy as np

array_number = np.array([1, 2, 3, 2, 3, 4, 5, 6])


def find_number(myarray, find):
    for i in range(len(myarray)):
        if myarray[i] == find:
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