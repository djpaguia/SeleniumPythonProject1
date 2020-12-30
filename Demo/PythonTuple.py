# There are 4 Collection data types in Python
# List | Tuple | Set | Dictionary

# List         -   []      - ordered | indexed | changeable | duplicates
# Tuple        -   ()      - ordered | indexed | unchangeable | duplicates
# Set          -   {}      - unordered | unindexed | no duplicates
# Dictionary   -   {K:V}   - unordered | indexed | changeable | no duplicates

my_tuple = ("Apples", "Oranges", "Grapes")
print(my_tuple)
print(my_tuple[1])
print(my_tuple[-1])
print(my_tuple[0:3])     # starting from index 0, prints 3 elements inside the tuple

for val in my_tuple:
    print(val)

#my_tuple[3]    = "Cherry"
#del my_tuple[2]

print(len(my_tuple))

my_tuple_2 = ("Banana", (1, 2, 3), ["Tokyo", "New Delhi"])
print(my_tuple_2)
print(my_tuple_2[2][1])

my_tuple_2[2][1] = "New York"
print(my_tuple_2)

print("Banana" in my_tuple_2)   # True
print("Cherry" in my_tuple_2)   # False

