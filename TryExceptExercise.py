'''
Try and except are used for catching errors in your code.
If the criteria is met, you will be okay, if something (in this case a string
is input, instead of the program crashing, it will throw this error.)
'''
try:
   # value = 10 / 0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Bad input")

# You always want to except for specific errors.