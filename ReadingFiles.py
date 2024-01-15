# First you need to open the file with open()
# You then need to choose the mode - "r" is for read. "w" is write
# "a" is for append
# "r+" is read and write.

warhammer = open("Practice.txt", "r")

# You need to remember to close the file too. warhammer.close()

#warhammer.close()

# Check if you can read
#.readable() will return a bool value

print(warhammer.readable())

# Print contents to terminal
#print(warhammer.read())

# To read indivdual lines

print(warhammer.readline())

#.readlines() takes the file and puts it in a list
# Add [] to find specific line

print(warhammer.readlines())