print("Hello World...")

# Variables are case-sensitive. No need to to declare the data type (ex: In Java, int x = 5; String y = "Automation";)
# In variable naming, use letters (a-z), underscore, numbers(0-9)
x = 5
y = "Automation"
print(x)
print(y)

print("Hello " + y)

x = 10
y = 20
print(x+y)

# Syntax
# Identations are important for loops. Statements, ex: if statement, are ended with a colon (:)
if 10 > 5:
    print("10 is greater than 5")

# Functions - use the keyword def (ex: In Java, public static int sum(a,b){})
def sum(a,b):
    print(a+b)

x = sum(20,30)

x = 10
y = 2.5
z = 4j

print(type(x))
print(type(y))
print(type(z))

# Casting
x = int(2)    # 2
y = int(2.5)  # 2
z = float(1)  # 1.0
p = str(10)   # 10

print(x)
print(y)
print(z)
print(p)

# String

x = "Hello World..."
print(x)
print(x[1])
print(x[6:11])
print(len(x))
print(x.lower())
print(x.upper())
x = "    Hello World...   "
print(x)
print(x.strip())
print(x.replace("e","a").replace("H","J").strip())
x = "   Hello,World...   "
print(x.split(","))

print("Enter your name: ")
x = input()
print("Hello, " + x)


