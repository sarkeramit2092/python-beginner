#tuples

'''
In Python, a tuple is a collection data type that is similar to a list. 
However, unlike lists, tuples are immutable, 
meaning their elements cannot be modified or changed after the tuple is created. 
Tuples are defined using parentheses ().
'''
# Attempting to modify a tuple will result in an error
# Uncommenting the line below would raise a TypeError

# Creating a tuple
my_tuple = (1, 2, 3, 'apple', 'banana')

# Accessing elements in a tuple
print("First element:", my_tuple[0])   # Output: 1
print("Last element:", my_tuple[-1])   # Output: 'banana'

# Slicing a tuple
print("Slice:", my_tuple[2:4])         # Output: (3, 'apple')

# Tuple with a single element
single_element_tuple = (42,)
print("Single-element tuple:", single_element_tuple)   # Output: (42,)

# Nested tuple
nested_tuple = (1, (2, 3), 'four')
print("Nested tuple:", nested_tuple)   # Output: (1, (2, 3), 'four')

# Tuple unpacking
a, b, c, *rest = my_tuple
print("Unpacking:", a, b, c, rest)     # Output: 1 2 3 ['apple', 'banana']

# Creating a tuple
coordinates = (3, 4)

# Tuple unpacking
x, y = coordinates

# Displaying the unpacked values
print("x:", x)  # Output: 3
print("y:", y)  # Output: 4

# Creating a nested tuple
person = ("John", 30, ("New York", "USA"))

# Tuple unpacking
name, age, (city, country) = person

# Displaying the unpacked values
print("Name:", name)       # Output: John
print("Age:", age)         # Output: 30
print("City:", city)       # Output: New York
print("Country:", country) # Output: USA

# Creating a tuple
grades = (95, 87, 91, 78, 94)

# Tuple unpacking with *
first, *rest, last = grades

# Displaying the unpacked values
print("First grade:", first)  # Output: 95
print("Middle grades:", rest)  # Output: [87, 91, 78]
print("Last grade:", last)    # Output: 94
