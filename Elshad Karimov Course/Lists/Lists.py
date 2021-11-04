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
        print(f'{type(e3)} :The index was typed as string and should be integer.')
    else:
        print(f'The element in the {index+1} position (index {index}) is '+str(my_list[index]))

error_out_of_range(shopping_list, 5)

print('Step 7.2 - Use in operator to search elements inside the list')
## If the elements is not available in the list, then False boolean occur
print('Vegan' in shopping_list)

print('Step 7.3 - Traverse a list')
# Time complexity is O(n) because it depends to the size of the list. Space complexity is O(1), because we do not need extra space.
for i in shopping_list:
    print(i)

for i in range(len(shopping_list)):
    shopping_list[i] = shopping_list[i]+"+"
    print(shopping_list[i])

print('Step 7.4 - Accessing elements in a list')
# Time and space complexity in this operation is O(1)
print(integer_list)
integer_list[4] = 22
print(integer_list)

print('Step 7.5 - Inserting elements in a list')
integer_list_step_74 = [1, 2, 3, 4, 5]
# To the beginning of the list

# To the any given place in the list
def insert_element(my_list, index, value):
    try:
        if len(my_list) < index:
            raise OutOfListIndex()
    except OutOfListIndex as e1:
        print(f'{type(e1)} :The index is out the list range.')
    else:
        print(my_list)
        my_list.insert(index, value)
        print(my_list)

print('To the any given place in the list. Time and space complexity is O(n).')
insert_element(integer_list_step_74, 5, 0)

# To the end of the list
print('To the end of the list. Time and space complexity is O(1).')
integer_list_step_74.append(0)
print(integer_list_step_74)

# Insert another list to the list
print('Insert another list to the list. Time and space complexity is O(n).')
new_integer_list = [11, 12, 13, 14]
integer_list_step_74.extend(new_integer_list)
print(integer_list_step_74)

print('Step 7.6 - Slice/Delete elements in a list')
print('Slicing')
print(integer_list)
print(integer_list[1:3])

print('Deleting using pop() method. If the element is not at the end, then the time complexity will be O(n).')
integer_list.pop(2) # using a parameter the time ans space complexity is O(n)
print(integer_list)
print('If any element is provided, then the pop() method deletes the last.')
integer_list.pop() # without any parameter the time ans space complexity is O(1)
print(integer_list)

print('Deleting using del() method.')
del integer_list[1] # O(n)
print(integer_list)

print('Deleting using remove() method is used for deletion of specific element.')
integer_list.remove(4) # O(n)
print(integer_list)

print('Step 7.7 - Searching elements in a list')
print('Using in operator')
def searching_in_list(my_list, value):
    try:
        if isinstance(value, int):
            raise IsString
    except IsString as e1:
        print(f'{type(e1)} :The value was typed as integer and should be string.')
    else:
        if value in my_list:
            print(f'The {value} you search is at the {my_list.index(value)} index.')
        else:
            print('The value does not exist in the given list')

searching_in_list(string_list, 'I')

print('Using linear search')
def searching_in_list_2(my_list, value):
    for i in my_list:
        if i == value:
            return print(f'The index of the value is {my_list.index(value)}.')
    return print('The value does not exist in the given list')

searching_in_list_2(string_list, 'Love')

