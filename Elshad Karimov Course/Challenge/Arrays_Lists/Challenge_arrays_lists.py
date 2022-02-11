# Credits to Elshad Karimov from Udemy Course
# https://www.udemy.com/course/data-structures-and-algorithms-bootcamp-in-python/

import numpy as np


print('Part 1 - Middle function')

part_1_list = [1, 2, 3, 4]

print('My solution')


def middle(lst):
    second = lst[1]
    last_but_one = lst[len(lst)-2]
    return [second, last_but_one]


print(middle(part_1_list))

print('Elshad\'s solution')


def middle_2(lst):
    new = lst[1:]
    del new[-1]
    return new


print(middle_2(part_1_list))


print('Part 2 - 2d Lists')

part_2_2d_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print('My first was not so brilliant')
print(part_2_2d_list[0][0] + part_2_2d_list[1][1] + part_2_2d_list[2][2])

print('Some Google searching, look how nice the solution')
# Credits to Rodrigo Carneiro
# https://stackoverflow.com/questions/20447210/get-diagonal-without-using-numpy/20447298


def sum_diagonal(lst):
    diagonal = [lst[i][i] for i in range(0, len(lst))]
    return sum(diagonal)


print(sum_diagonal(part_2_2d_list))


def sum_counter_diagonal(lst):
    counter_diagonal = [lst[i][~i] for i in range(0, len(lst))]
    return sum(counter_diagonal)


print(sum_counter_diagonal(part_2_2d_list))

print('Elshad\'s solution')

def sumDiagonal(a):
    sum = 0
    for i in range(len(a)):
        sum += a[i][i]
    return sum


print(sumDiagonal(part_2_2d_list))

print('Part 3 - Best Scores')

part_3_best_scores_list = [84, 85, 86, 87, 85, 90, 85, 83, 23, 45, 84, 1, 2, 0]

print("Adapted from https://www.geeksforgeeks.org/python-ways-to-remove-duplicates-from-list/")
def FirstSecond(givenList):
    """[summary]

    Args:
        givenList ([type]): [description]
    """
    temp_list = []
    for my_number in givenList:
        if my_number not in temp_list:
            temp_list.append(my_number)
            temp_list.sort(reverse=True)
    first = temp_list[0]
    second = temp_list[1]
    return (first, second)
    
print(FirstSecond(part_3_best_scores_list))

print("Another solution")
def FirstSecond_2(givenList):
    test_list = list(set(part_3_best_scores_list))
    test_list.sort(reverse=True)
    first = test_list[0]
    second = test_list[1]
    return (first, second)

print(FirstSecond_2(part_3_best_scores_list))

print("Part 4 - Missing Number")

part_4_missing_number = [1, 2, 3, 4, 6]
part_4_array_missing_number = np.array([1, 2, 3, 4, 6])

def find_missing_number(mylist, listcount):
    """
    This line is intended for documentation.
    """
    list_total = max(mylist) * (max(mylist) + 1) / 2
    list_user = sum(mylist)
    print(list_total - list_user)

find_missing_number(part_4_array_missing_number, 6)

print("Part 5 - Removing Duplicates")

part_5_remove_duplicates = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]

def removeDuplicates(myList):
    # TODO
    tempList = []
    for element in myList:
        # print(element)
        if element not in tempList:
            tempList.append(element)
    return tempList

print(removeDuplicates(part_5_remove_duplicates))

print("Part 6 - Finding pairs that the sum is equal to a given number")

part_6_find_pairs = [2, 4, 3, 5, 6, -2, 4, 7, 8, 9]

def pairSum(myList, sum):
    # TODO
    tempList = []
    for element in range(len(myList)):
        for nextElement in range(element + 1, len(myList)):
            sumofpairs = myList[element] + myList[nextElement] 
            if sumofpairs == sum:
                pairs = str(myList[element]) + "+" + str(myList[nextElement])
                tempList.append(pairs)
    return tempList

print(pairSum(part_6_find_pairs, 7))
