
warhammer = open("Practice.txt", "a")
warhammer.write("\nWarhammer is great! I like Space Marines!")
warhammer.close()

# The above will append to the file in question.
# Nothing will show in the console, check actual text file!
# Make sure to use escape chars.
'''
If you replace the 'a' with a 'w' (write), it will overwrite the whole file
and only add the what you have written

'''

# Writing a NEW file

warhammer = open("Warhammer2.txt", "w")
warhammer.write("I hope they come out with Warhammer 2!")

# You can write other files besides .txt, such as HTML.