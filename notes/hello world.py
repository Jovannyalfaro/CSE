"""
print("hello world!!")

# this is a comment. This has no effect on the cod
# but this does allow me to do things. I can:
# 1. Make notes to myself
# 2. comment pieces of code that do not work
# 3. Make my code easier to read

print ("look at what happens here. is there any space?")
print ()
print()
print("there should be a couple blank lines here.")

# math
print(3 + 5)
print(5 - 2)
print(3 * 4)
print(6 / 2)

print("figure this out...")
print(6 // 2)
print(5 // 2)
print(9 // 4)

print("here is another one...")
print(6 % 2)
print(5 % 2)
print(11 % 4)  # modulus (remainder)

# powers
# what is 2^20?
print(2 ** 100)

# taking input
name = input ("what is your name?")
print ("hello %s." % name)

age = input ("how old are you? >_")
print("%s?!? you belong in a museum>" % age)
print()
print("%s is really old. They are %s years old." % (name, age))

# Variable Assignments
car_name = "Sneeze Mobile"
car_type = "Minivan"
car_cylinders = 16
car_miles_per_gallon = 0.01

print("I have a car called %s. It is a %s" % (car_name, car_type))


# Recasting
real_age = int(input("How old are you again?"))
hidden_age = real_age + 5
print("This is your real age: %d" % hidden_age)
"""

"""
This is a multi-line comment
Anything between the "s" is not run.
"""


# functions
def say_it():
    print("hello world!")


say_it()
say_it()
say_it()


# f(x) = 2x + 34
def f(x):
    print(2*x + 3)


f(1)
f(5)
f(5000)


# Distance Formula
def distance(x1, y1, x2, y2):
    dist = ((x1-x2)**2 + (y2-y1)**2)**(1/2)
    print(dist)


distance(0, 0, 3, 4)
distance(0, 0, 5, 12)


# Loops
for i in range(100000):  # This gives the numbers 0 through 4
    say_it()
for i in range(1000000):
    print(i + 1)

for i in range(5):
    f(i)









































# Equality statements
print(5 > 3)
print(5 >= 3)
print(3 == 3)
print(3 != 4)
"""
a = 3 # A is set to 3
a == 3 # is a equal to 3?
"""

