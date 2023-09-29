import requests



response = requests.get("https://randomuser.me/api")
print(response.json())




gender = response.json()["results"][0]["gender"]
print(gender)

title = response.json()['results'][0]["name"]['title']
print(title)

location = response.json()['results'][0]["location"]["postcode"]
print(location)
name = response.json()['results'][0]["name"]["first"]
print(name)
name = response.json()['results'][0]["name"]["last"]
print(name)
login = response.json()['results'][0]["login"]["username"]
print(login)


#Emiliano Padilla
# Unique Elements:

# Given a list of integers, return a set containing only the unique integers.
# python
# Copy code
# example_input = [1, 2, 2, 3, 4, 4, 4]
# # Your code
# # Expected Output: {1, 2, 3, 4}
# Set Operations:
example_input = [1, 2, 2, 3, 4, 4, 4]
unique_elements = set(example_input)
my_list = {1, 2, 2, 3, 4, 4, 4}
print(my_list)
# Given two sets, perform the following operations:
# Union
# Intersection
# Difference (Set 1 - Set 2)
# Symmetric Difference
# Is Subset?:
my_set = {1, 2, 2, 3, 4, 4, 4}
my_set2 = {3, 4, 5, 6, 7}
my_set_3 = (my_set | my_set2)
print(my_set_3)
#or
print(my_set.union(my_set2))
print(my_set.intersection(my_set2))
print(my_set.difference(my_set2))


# Given two sets, check if the first set is a subset of the second set.
# Remove Duplicates:
def remove_duplicates(my_set):
    return ''.join(sorted(set(my_set)))

remove_duplicates(my_set)

def isThis_subset(my_set, my_set2):
    return my_set.issubset(my_set2)
print(isThis_subset(my_set, my_set2))
