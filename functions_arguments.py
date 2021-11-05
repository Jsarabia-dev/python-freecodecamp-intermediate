print("==== Arguments and parameters ====")


def print_name(name):  # name is the parameter
    print(name)


print_name('Alex')  # 'Alex' is the argument

print("==== Positional and keyword arguments ====")


def foo(a, b, c):
    print(a, b, c)


# positional arguments
foo(1, 2, 3)

# keyword arguments
foo(a=1, b=2, c=3)
foo(c=3, b=2, a=1)  # Note that the order is not important here

# mix of both
foo(1, b=2, c=3)

# This is not allowed:
# foo(1, b=2, 3) # positional argument after keyword argument
# foo(1, b=2, a=3) # multiple values for argument 'a'


print("==== Default arguments ====")


def foo(a, b, c, d=4):
    print(a, b, c, d)


foo(1, 2, 3, 4)
foo(1, b=2, c=3, d=100)

# not allowed: default arguments must be at the end
# def foo(a, b=2, c, d=4):
#     print(a, b, c, d)

print("==== Variable-length arguments (*args and **kwargs) ====")


def foo(a, b, *args, **kwargs):
    print(a, b)
    for arg in args:
        print(arg)
    for kwarg in kwargs:
        print(kwarg, kwargs[kwarg])


# 3, 4, 5 are combined into args
# six and seven are combined into kwargs
foo(1, 2, 3, 4, 5, six=6, seven=7)
print()

# omitting of args or kwargs is also possible
foo(1, 2, three=3)

print("==== Forced keyword arguments ====")


def foo(a, b, *, c, d):
    print(a, b, c, d)


foo(1, 2, c=3, d=4)

# not allowed:
# foo(1, 2, 3, 4)

print("==== arguments after variable-length arguments must be keyword arguments ====")


def foo(*args, last):
    for arg in args:
        print(arg)
    print(last)


foo(8, 9, 10, last=50)

print("==== Unpacking into agruments ====")


def foo(a, b, c):
    print(a, b, c)


# list/tuple unpacking, length must match
my_list = [4, 5, 6]  # or tuple
foo(*my_list)

# dict unpacking, keys and length must match
my_dict = {'a': 1, 'b': 2, 'c': 3}  # Must match name param
foo(**my_dict)

# my_dict = {'a': 1, 'b': 2, 'd': 3} # not possible since wrong keyword

print("==== Local vs global variables ====")


def foo1():
    x = number  # global variable can only be accessed here
    print('number in function:', x)


number = 0
foo1()


# modifying the global variable
def foo2():
    global number  # global variable can now be accessed and modified
    number = 3


print('number before foo2(): ', number)
foo2()  # modifies the global variable
print('number after foo2(): ', number)

print("==== Parameter passing ====")

print(" == immutable objects -> no change == ")


def foo(x):
    x = 5  # x += 5 also no effect since x is immutable and a new variable must be created


var = 10
print('var before foo():', var)
foo(var)
print('var after foo():', var)

print(" == mutable objects -> change == ")


def foo(a_list):
    a_list.append(4)


my_list = [1, 2, 3]
print('my_list before foo():', my_list)
foo(my_list)
print('my_list after foo():', my_list)
