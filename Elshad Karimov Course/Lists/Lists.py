# Credits to Elshad Karimov from Udemy Course
## https://www.udemy.com/course/data-structures-and-algorithms-bootcamp-in-python/

# Working with lists in Python

## List in python is a built-in data structure, which means that it comes with the standard Python library.

# Basic List Creation

print('Step 1 - List of integers')

integer_list = [1, 2, 3, 4, 5]
print(integer_list)

print('Step 2 - List of Strings')
string_list = ['I', 'Love', 'Python', 'Lists', '\0x/']
print(string_list)

print('Step 3 - List of Mixed Data')
mixed_list = ['I', 2, 2.5, 'Lists']
print(mixed_list)

print('Step 4 - Nested List')
nested_list = [1, 2, 3, [4, 5]]
print(nested_list)

print('Step 5 - Nested Mixed List')
nested_mixed_list = [1, 2.5, 3, ['Python', 5]]
print(nested_mixed_list)

print('Step 6 - Empty List')
empty_list = []
print(empty_list)

print('Step 7 - Accessing elements of a list')
shopping_list = ['Milk', 'Cheese', 'Butter']
print(shopping_list[0])

print('Step 7.1 - Accessing elements of a list that does not exist')
## If the elements is not available in the index, then and error occur

class Integer(Exception):
    def __init__(self, message):
        super().__init__(message)

message = 'The index must be integer'

def error_out_of_range(my_list, index):
    if int(index) == index:
        raise Integer(message)
    else:
        try:
            my_list[index]
        except LookupError:
            print(f'The index is out of range. The list range starts in 0 until ' + str(len(my_list) - 1))
        except TypeError:
            print('Ops, there is something weird in your typing')
        else:
            print(f'The element in the {index+1} position is '+str(my_list[index]))

error_out_of_range(shopping_list, 2.5)

print('Step 7.2 - Use in operator to search elements inside the list')
## If the elements is not available in the list, then False boolean occur
#print('Vegan' in shopping_list)