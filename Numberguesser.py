# This number guess game is completely free to use.
import random
secret = random.randrange(1, 100)

guesses = 0
guessleft = 7

print('I\'m thinking of a number between 1 and 100. Can you guess which? You\'ll have ' + str(guessleft) + ' chances:')
while guesses < 7:
    userguess = int(input())
    guesses += 1
    guessleft -= 1
    
    if userguess < secret:
        print('Too low, you have ' + str(guessleft) + ' tries left!')
    if userguess > secret:
        print('Too high, you have ' + str(guessleft) + ' tries left!')
    if userguess == secret:
        break
if userguess == secret:
    print('You got it! You won this round in ' + str(guesses) + ' tries :^)')
else:
    print('You ran out of guesses this round. Call me to play again some time :P')