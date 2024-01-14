# Working with functions

# the def keyword

def say_hi():
    print("Hello user!")

#calling the function

say_hi()

#parameters

def say_bye(name):
    print("Bye " + name)
say_bye("pat")

# Return Statements

def cube_num(num):
    num * num * num
#this returns None - no return value
print(cube_num(4))

def square_num(num):
    return num * num

print(square_num(6))
