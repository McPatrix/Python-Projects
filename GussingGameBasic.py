# Secret word

secret_word = "Python"
# Other vars

guess = " "
guess_count = 0
guess_limit = 3
out_of_guesses = False

# While loop until guessed. 
while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Guess a word ")
        guess_count += 1
    else:
        out_of_guesses == True
        
if out_of_guesses:
    print("LOSER!")
else:
    print("Winner!!")