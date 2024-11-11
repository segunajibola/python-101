i=0
while i < 5:
    i+=1
    print(f"{i}."+ "*"*i + "Loops are awesome" + "*"*i)
    
# Three Loop Questions:
#1. What do I want to repeat?
#  -> message
#2. What do I want to change each time?
#  -> stars
#3. How long should we repeat?
#  -> 5 times

# 1.*Loops are awesome*
# 2.**Loops are awesome**
# 3.***Loops are awesome***
# 4.****Loops are awesome*****
# 5.*****Loops are awesome*****

#Guessing game

print('Guessing game') 
# Guess the correct number in 3 guesses. If you don’t get it right after 3 guesses you lose the game. 
# Give user input box: 1. To capture guesses, 
# print(and input boxes) 1. If user wins 2. If user loses
# Tip:( remember you won’t see  print statements durng execution, so If you want to see prints during whle loop, then print to the input box

#Modification 1: number 1-100, tell user if guess is too high/low ,and let them have 5-10 guesses.
# Tip:( remember you won’t see  print statements during execution, so If you want to see prints during whle loop, print to the input box (This is specific to this platform)

# Three Loop Questions:
#1. What do I want to repeat?
#  -> guesses
#2. What do I want to change each time?
#  -> guess number and number of guesses
#3. How long should we repeat?
#  -> until user loses, runs out of guesses, or wins

num = 76
guess = 0
guess_limit=5
guess_number = 0
guess = int(input(f'Guess a number 1-100: '))
guess_number +=1
while guess_number < guess_limit:
    
    if guess != num:
        guess_number +=1
        if guess > num:
            guess = int(input(f'{guess} Too high - Guess again 1-100: '))
        else:
            guess = int(input(f'{guess} too low - Guess again 1-100: '))
    if guess == num:
        print(f'You Win! You Guessed it: {guess}')
        break
    
if guess != num:
    print(f'Sorry you lose! It was {num}')
    
    
# For loops
for letter in 'Norway':
    print(letter)
    
#N
#o
#r
#w
#a
#y

for furgle in range(8):
    print(furgle)
#0 to 7

for furgle in range(2,8):
    print(furgle)
#start from 2 to 7

for furgle in range(1,15,3):
    print(furgle)
#start from 1 to 15 in steps of 3. 1,4,7,10,13

for name in ['John','Terry','Eric','Michael','George']:
    print(name)
#John
#Terry
#Eric
#Micheal
#George

#OR

friends = ['John','Terry','Eric','Michael','George']
for friend in friends:
    print(friend) #or

print("For Loop done!")


for index in range(len(friends)):
   print(friends[index])

for friend in friends:
    if friend == 'Eric':
        print('Found' + friend + '!')
        break
    print(friend)   

#John
#Terry
#FoundEric!

friends = ['John','Terry','Eric']
for friend in friends:
    for number in [1,2,3]:
        print(friend, number)
        
#John 1
#John 2
#John 3

#Terry 1
#Terry 2
#Terry 3

#Eric 1
#Eric 2
#Eric 3

