# Credits to Elshad Karimov from Udemy Course
# https://www.udemy.com/course/data-structures-and-algorithms-bootcamp-in-python/

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