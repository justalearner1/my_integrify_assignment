list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Print item in index 4 using bracket notation
print(list[4])
# Print item in index 5 using negative [-1] index
print(list[-4])
# Print every second item from the list
print(list[0::2])
# Print items from 3rd to 5th
print(list[3:5])

given_data = {
    'foo': {'name': 'Foo', 'lastname': 'Fooer'},
    'bar': {'name': 'Bar', 'lastname': 'Baer'},
    'Baz': None
}
# Print all the keys
print(given_data)
# Print `bar`s `name` and lastname in format "Firstname is [NAME], and lastname is [LASTNAME]". Hint: Use string formatting & placeholders
variable_1 = given_data['bar']['name']
variable_2 = given_data['bar']['lastname']
print(f'First name is {variable_1} and last name is {variable_2}.')
# Loop over all keys and print the name as mentioned in the previous step IF the keys value is not empy.


# 3. Create a function named `summer` which takes two parameters: `a` and `b`
def summer(a, b):
    return a + b


# Make the function return sum of the parameters. Note: Do NOT modify the original parameters
print(summer(3, 5))
# Refactor the function to have default values to parameters
# Refactor the function to have `**kwargs` and if alternate parameter `negatove` is `True` return the value as a negative sum.


# 4. Given a list `['python', 'and', 'data', 'science', 'is', 'awesome']`
# Create a new list from the given list using list comprehension and include item only if it's length is greater than 5
# Create a dict from the given list using comprehension where list index is the key and value is the actual value
# Add item to the dict where the key is the next integer and value is "!"


# 5. Create a function which takes a list-type parameter and returns a new list containing only integers from the parameter list in an descending order. e.g. if the function receives parameter `['x', -0.1, 'foo', True, 'bar', 10, 1.1, '8', 5, None, 12]`, it should return `[12, 10, 5]`. Note: Do not modify the original parameter and use list comprehension.
