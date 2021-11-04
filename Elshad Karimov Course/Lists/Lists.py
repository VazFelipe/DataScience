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

class Error(Exception):
    """
    Base class for other exceptions.
    """
    pass

class NotInteger(Error):
    """
    Raised when the value is not an integer and was typed as float.
    """
    pass

class OutOfListIndex(Error):
    """
    Raised when the index is out the list range.
    """
    pass

class IsString(Error):
    """
    Raised when the index is typed as string and should be integer.
    """
    pass

def error_out_of_range(my_list, index):
    try:
        if isinstance(index, str):
            raise IsString()
        elif len(my_list) < index:
            raise OutOfListIndex()
        elif int(index) != index:
            raise NotInteger()
    except NotInteger as e1:
        print(f'{type(e1)} :The value is not an integer and was typed as float.')
    except OutOfListIndex as e2:
        print(f'{type(e2)} :The index is out the list range.')
    except IsString as e3:
        print(f'{type(e3)} :The index is typed as string and should be integer.')
    else:
        print(f'The element in the {index+1} position (index {index}) is '+str(my_list[index]))

error_out_of_range(shopping_list, 2)

print('Step 7.2 - Use in operator to search elements inside the list')
## If the elements is not available in the list, then False boolean occur
print('Vegan' in shopping_list)