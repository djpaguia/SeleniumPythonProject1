# def func_name(parameter):
#     body

def printHello():
    print("Hello")


printHello()


def printHi(name="John"):
    print("Hi, " + name)


printHi("DJ")


def sum(a, b, c):
    print(a + b + c)


sum(10, 20, 30)


def returnSum(a, b):
    """this is a function to calculate a sum of two numbers"""
    return (a + b)


x = returnSum(10, 20)
print(x)

word_1 = "S$tarb#ucks@"


def remove_special_characters(word):
    char_array = list(word)
    if char_array.__contains__("$"):
        char_array.remove("$")
    if char_array.__contains__("#"):
        char_array.remove("#")
    if char_array.__contains__("@"):
        char_array.remove("@")
    if char_array.__contains__("$"):
        char_array.remove("$")
    if char_array.__contains__("%"):
        char_array.remove("%")
    if char_array.__contains__("^"):
        char_array.remove("^")
    if char_array.__contains__("&"):
        char_array.remove("&")
    if char_array.__contains__("*"):
        char_array.remove("*")
    if char_array.__contains__("("):
        char_array.remove("(")
    if char_array.__contains__(")"):
        char_array.remove(")")
    x = "".join(char_array)
    return x


print(word_1)
new_word = remove_special_characters(word_1)
print(new_word)
