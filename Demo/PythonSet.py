# There are 4 Collection data types in Python
# List | Tuple | Set | Dictionary

# List         -   []      - ordered | indexed | changeable | duplicates
# Tuple        -   ()      - ordered | indexed | unchangeable | duplicates
# Set          -   {}      - unordered | unindexed | no duplicates
# Dictionary   -   {K:V}   - unordered | indexed | changeable | no duplicates

my_set = {"Chalk", "Duster", "Board"}
print(my_set)
# print(my_set[1])   # cannot use this in Set because it is unindexed. But you can use a  for loop

for x in my_set:
    print(x)

print("Chalk" in my_set)  # True

my_set.add("Pen")
print(my_set)

my_set.update(["Pencil", "Eraser"])
print(my_set)

print(len(my_set))

my_set.remove("Pencil")   # Once an element is removed, it will throw an exception if you try to remove it again.
print(my_set)

my_set.discard("Pen")     # If an element is discarded, it will NOT throw an exception if you try to discard it again.
print(my_set)

my_set.pop()   # Randomly deletes an element within a set
print(my_set)

del my_set     # Deletes a set.

my_set_2 = {"Apples", 1, 2, (3, 4, 5)}
print(my_set_2)

my_list = [1,2,3]
print(my_list)

my_set_3 = set(my_list)     # Converts List to a Set.
print(my_set_3)

# UNION | INTERSECTION | DIFF| SYMMETRIC DIFF

A = {'A', 'B', 1, 2, 3}
B = {'B', 'C', 3, 4, 5}

print(A.union(B))                 # Prints values that are present in A or B.
print(A | B)                      # Pipe symbol "|" is similar to Union.

print(A.intersection(B))          # Prints values that are both present to A and B
print(A & B)                      # And symbol "&" is similar to Intersection.

print(A.difference(B))            # Prints values that are present in A but not in B
print(A - B)                      # Minus symbol "-" is similar to Difference.

print(A.symmetric_difference(B))  # Prints values that are unique to both A and B. Common elements are not printed.
print(A ^ B)                      # Cap symbol "^" is similar to Symmetric Difference.


