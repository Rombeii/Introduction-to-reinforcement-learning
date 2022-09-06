# https://www.freecodecamp.org/news/python-code-examples-sample-script-coding-tutorial-for-beginners/#-variable-definitions-in-python
import numpy as np
import  matplotlib.pyplot as plt
def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    #Printing
    print("Hello world")

    # Variables
    # < var_name > = < value >
    # Basic variable
    my_age = 24
    my_name = "Tamás"
    pi = 3.14
    boolean = True

    # Lists
    colors = ["blue", "green", "red"]
    numbers = [1, 2, 3, 4, 5]

    # Data types
    print(type(my_age))
    print(type(my_name))
    print(type(pi))
    print(type(boolean))
    print(type(colors))

    # Strings
    single_quotes = 'test1'
    double_quotes = "test2"
    print(single_quotes)
    print(double_quotes)

    double_quotes = "I'm Tamás"
    #double_quotes = 'I'm Tamás'

    # Indexing strings
    print(double_quotes[0])
    print(double_quotes[-1])
    print(double_quotes[4:9])
    print(double_quotes[4:])
    #print(double_quotes[100])

    #Lists in depth
    mixed_list = [1, "2", "test", '123', boolean]
    nested_list = [[1, 2, 3], [4, 5, 6]]
    print(numbers)
    print(nested_list)
    print(nested_list[0])
    print(nested_list[0][2])
    nested_list[0][2] = 10
    print(nested_list)

    colors.append("black")
    print(colors)
    colors.remove("red")
    print(colors)
    print(len(colors))

    print("black" in colors)

    # Dictionaries
    directions = {1: "Move Left", 2: "Move Right", 3: "Move Up", 4: "Move Down"}
    days = {"Monday": 1, "Tuesday": 2}
    print(directions[1])
    print(directions.get(1))
    print(days["Monday"])
    directions[1] = "Left"
    print(directions)
    print(directions.keys())
    print(directions.values())
    directions[5] = "Stay"
    print(directions)

    # Operators
    a = 5 + 2
    b = 5 - 2
    c = 5 * 2
    d = 5 / 2
    e = 5 ** 2
    f = 5 % 2

    # Comparison operators
    a = 1 > 2
    b = 1 < 2
    b = 1 <= 2
    c = 1 == 2
    e = 1 != 2
    f = 1 < 2 and 2 > 4 or 4 > 2

    # Conditions
    if my_age < 25:
        print("I'm young")
    else:
        print("I'm old")

    if my_age < 3:
        print("I'm an infant")
    elif my_age < 25:
        print("I'm young")
    else:
        print("I'm old")

    # For loop
    for i in range(5):
        print(i)

    for color in colors:
        print(color)

    for key in directions:
        print(key)
        print(directions[key])

    # While loop
    x = 10
    while x < 15:
        print(x)
        x += 1

    # Functions

    def print_hello_world():
        print("Hello world")

    def print_type(variable):
        print(type(variable))


    def get_rectangle_area(length, width):
        return length * width

    print_type("test")

    print(get_rectangle_area(10, 40))

    # Numpy
    a = np.array([2, 3, 4])
    print(a.dtype)

    b = np.array([1.2, 3.5, 5.1])
    print(a.dtype)

    c = np.array([[1, 2, 3], [4, 5, 6]])
    print(c)

    d = np.zeros((3, 4))
    print(d)

    e = np.ones((2, 10))
    print(e)
    print(c.max())
    print(c.sum())

    # Matplotlib
    plt.plot([1, 2, 3, 4])
    plt.ylabel('some numbers')
    plt.show()

    plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'rx')
    plt.axis([0, 6, 0, 20])
    plt.show()

    x = np.linspace(0, 100, 30)
    y = np.linspace(20, 200, 30)

    plt.plot(x, y, 'o')
    plt.show()