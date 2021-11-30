# Credits to Renan Moura Ferreira on https://www.freecodecamp.org/news/python-string-manipulation-handbook/
# String manipulation using built-in functions

print('Step 1 - text basics')
print()
# A string or str can be defined like this:

# Using quotes
my_name_single = 'Felipe Vaz'
my_name_double = "Felipe Vaz"

# Explicitly defining

my_name_explicitly = str("Felipe Vaz")

# Testing types

print(f'{my_name_single}, data type: {type(my_name_single)}.')
print(f'{my_name_double}, data type: {type(my_name_double)}.')
print(f'{my_name_explicitly}, data type: {type(my_name_explicitly)}.')

print()

print('Step 2 - text concatenation')

# Plus sign "+" is the operator used in order to concatenate strings

my_first_name = "Felipe"
my_middle_name = "Vidor"
my_surname = "Vaz"

my_name = my_first_name + " " + my_middle_name + " " + my_surname

print(my_name)

print()

print('Step 3 - char selection')

char = my_name[0]
print(char)

print()

print('Step 3.1 - char traversing')


def traverse_name(name):
    for i in range(len(name)):
        print(name[i])


traverse_name(my_name)

print('Step 3.2 - char traversing WOW')


# OMG we can use "char" in the place of "i"

def traverse_name_wow(name):
    for char in name:
        print(char)


traverse_name_wow(my_first_name)

print()

print('Step 4 - the size of a string')

print(len(my_name))

print()

print('Step 5 - replace part of a string')

my_name_replace = my_name.replace("Felipe", "João")

print(my_name_replace)

print()

print('Step 6 - count character in a string')

# Case-sensitive
# Why in the world count "" in a word with 16 chars returns 17??
print(my_name.count(""))

print()

print('Step 7 - repeating a string')

repeat_per = 4

print(my_first_name * repeat_per)

print()

print('Step 8 - splitting a string using whitespaces')

# the default for split method is a whitespace as delimiter
my_name_splitting = my_name.split()

print(my_name_splitting)


def traverse_my_name_splitting(name):
    for word in name:
        print(word)


traverse_my_name_splitting(my_name_splitting)

print()

print('Step 9 - splitting a string using different arguments as delimiters')

my_phone_number = str("53999999999")
my_mobile_brand = str("Apple")

my_csv_fake_row = my_first_name + \
                  ";" + my_middle_name + \
                  ";" + my_surname + \
                  ";" + my_phone_number + \
                  ";" + my_mobile_brand

print(my_csv_fake_row)

my_csv_fake_row_splitting = my_csv_fake_row.split(";")

for data in my_csv_fake_row_splitting:
    print(data)
    print(my_csv_fake_row_splitting[3])

print()

# String manipulation using re library and its functions

print('Step 10 - removing all whitespaces in a string using regular expressions')

my_string_with_whitespaces = "  " + my_first_name + \
                             "    " + my_middle_name + \
                             "  " + my_surname + \
                             " " + my_phone_number + \
                             "    " + my_mobile_brand + "  "

import re

# Credits for https://www.freecodecamp.org/news/python-string-manipulation-handbook/, thank you \0/
# Notice that the \s represents not only space ' ', but also form feed \f, line feed \n, carriage return \r, tab \t,
# and vertical tab \v. # In summary, \s = [ \f\n\r\t\v]. # The + symbol is called a quantifier and is read as 'one or
# more'. This means that it will consider, in this case, one or more white spaces since it is positioned right after
# the \s.

my_string_without_whitespaces = re.sub(r'\s+', '', my_string_with_whitespaces)

print(my_string_with_whitespaces)
print(my_string_without_whitespaces)

print()

print('Step 11 - handling multiline strings')

# it is possible to instead of using double quotes use single quotes for multiline string handling
my_long_text = """This is my long text,

and its usage is related with multiline strings.

I am doing this for string manipulation studies purpose."""

print(my_long_text)

print()
# it is possible to instead of using double/single quotes use parentheses for multiline string handling, but
# we need to add \n in the place that will have the line changing

my_long_text_with_parentheses = ("This is my long text, \n\n"
                                 "and its usage is related with multiline strings. \n\n"
                                 "I am doing this for string manipulation studies purpose.\n\n")

print(my_long_text_with_parentheses)

# another option: it is possible to instead of using the examples above adding backslashes \ and remove the parentheses

print()

print('Step 12 - removing spaces and chars from the beginning of a string')

# removing spaces from beginning
print(my_string_with_whitespaces)
print(my_string_with_whitespaces.lstrip())

print()

# removing specified chars from beginning

print(my_string_without_whitespaces)

my_string_without_some_char = my_string_without_whitespaces.lstrip("F")
print(my_string_without_some_char)

# it is possible to instead of using the lstrip() method get rstrip() for removing spaces and chars
# from the end of string
# Also, using just strip() method removes spaces and chars from both sides of a string

print()

print('Step 13 - Make a whole string lowercase and uppercase and use title case')

print(my_name)
print(f'This is my name lowercase {my_name.lower()}')
print(f'This is my name uppercase {my_name.upper()}')

my_name_lower = my_name.lower()

print(f'This is my name lowercase {my_name_lower} for title() method')
print(f'This is my name title case {my_name_lower.title()}')

print()

print('Step 14 - Swapping case from a string')

print(my_name.swapcase())
print(my_name_lower.swapcase())

print()

print('Step 15 - Checking if a string is empty')

my_empty_string = ''
my_non_empty_string = my_name


def is_string_empty(my_string):
    if not my_string:
        print('My string is empty')
    elif my_string:
        print('My string is not empty')


is_string_empty(my_non_empty_string)

print()

print('Step 16 - Right/Left-justify a string')

# Why is not possible to see the results using less than 10 number_of_chars?

number_of_chars = 32
string_char = '$'

my_first_name_right_justified = my_first_name.rjust(number_of_chars)
my_first_name_right_justified_crazy = my_first_name.rjust(number_of_chars, string_char)
my_first_name_left_justified = my_first_name.ljust(number_of_chars)
my_first_name_left_justified_crazy = my_first_name.ljust(number_of_chars, string_char)

print(my_first_name_right_justified)
print(my_first_name_right_justified_crazy + ' (my money name version...jejejeje)')
print(my_first_name_left_justified)
print(my_first_name_left_justified_crazy)







