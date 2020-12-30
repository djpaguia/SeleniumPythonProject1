# There are 4 Collection data types in Python
# List | Tuple | Set | Dictionary

# List         -   []      - ordered | indexed | changeable | duplicates
# Tuple        -   ()      - ordered | indexed | unchangeable | duplicates
# Set          -   {}      - unordered | unindexed | no duplicates
# Dictionary   -   {K:V}   - unordered | indexed | changeable | no duplicates

my_dict = {
    "class" : "animal",
    "name"  : "giraffe",
    "age"   : 10
}

print(my_dict)
print(my_dict["name"])           # Prints value of the key = "name"
print(my_dict.get("name"))       # Prints value of the key = "name"
print(my_dict.values())          # Prints all Values

for x in my_dict:
    print(x)                     # Prints all Keys.

for x in my_dict:
    print(my_dict[x])            # Prints all Values.

for x,y in my_dict.items():      # Prints all keys and values
    print(x, y)

my_dict["name"] = "elephant"     # Updates value of existing Key
print(my_dict)

my_dict["color"] = "grey"        # Adds a new key and value since the key is previously non-existent.
print(my_dict)

my_dict.pop("color")             # Removes key "color" and its value from the Dictionary
print(my_dict)

my_dict.popitem()                # Removes last item from the dictionary.
print(my_dict)

del my_dict["class"]
print(my_dict)

my_dict.clear()
print(my_dict)

del my_dict

