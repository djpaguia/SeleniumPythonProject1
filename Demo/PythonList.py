# There are 4 Collection data types in Python
# List | Tuple | Set | Dictionary

# List         -   []      - ordered | indexed | changeable | duplicates
# Tuple        -   ()      - ordered | indexed | unchangeable | duplicates
# Set          -   {}      - unordered | unindexed | no duplicates
# Dictionary   -   {K:V}   - unordered | indexed | changeable | no duplicates

my_list = ["Tokyo", "London", "New York"]
print(my_list)
print(my_list[2])

my_list[2] = "New Delhi"
print(my_list)

for val in my_list:
    print(val)

print(len(my_list))

my_list.append("Boston")
print(my_list)

my_list.insert(2, "Durham")
print(my_list)

my_list.remove("Tokyo")
print(my_list)

my_list.pop(1)
print(my_list)

del my_list[1]
print(my_list)

my_list.clear()
print(my_list)

fruits = ["apples", "oranges", "cherries"]
print(fruits)
fruits.reverse()
print(fruits)

my_list_2 = ["apples", 1, 2, 3.0]
my_list_3 = ["apples", [1, 2, 3], ['a', 'b', 'c']]             # Nested List
print(my_list_3)
print(my_list_3[1][1])



