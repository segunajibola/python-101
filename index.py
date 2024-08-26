# strings "Segun" '2'
# integers 1, 2, 3, 4
# floats 2.3
# boolean true or false

a="it's"
b='it\'s' # escaping characters b = 'it's'
print('Welcome to Python 101!')
failed_subjects=2
passed_subjects='3'
name='John'
print('Dear Mrs Badger')
print('Your son ' + name + ' is failing ' + str(failed_subjects) + ' and passing ' + passed_subjects + ' subjects.')
print(type('hello'), type(1), type(passed_subjects)) # str, int, str
print(False) # False
print(type(1.64)) # int
print(type(True)) # bool

a = int(1)        # a will be 1
b = int(2.5)      # b will be 2
c = int("3")      # c will be 3
# c1 = int("3.4") give error
c2 = int(float("3.4"))   # c2 will be 3
d = float(1)      # d will be 1.0
e = float(2.5)    # e will be 2.5
f = float("3")    # f will be 3.0
g = float("4.23") # g will be 4.23
h = str("80s")    # h will be '80s'
i = str(22)       # i will be '22'
j = str(3.01)     # j will be '3.01'

print([a,b,c,c2,d,e,f,g,h,i,j])


print("/// Calculations")
a=6
b=2
print('Addition : ', a + b)
print('Subtraction : ', a - b)
print('Multiplication : ', a * b)
print('Division (float) : ', a / b)
print('Division (floor) : ', a // b)
print('Modulus : ', a % b)
print('Exponent : ', a ** b)


print("/// Strings operation")

msg='welcome to it\'s Python 101: Strings'
print(msg, msg) # welcome to it's Python 101: Strings welcome to it's Python 101: Strings
print(msg.upper()) # WELCOME TO IT'S PYTHON 101: STRINGS
print(msg.lower()) # welcome to it's python 101: strings
print(msg.capitalize()) # Welcome to it's python 101: strings
print(msg.title()) # Welcome To It'S Python 101: Strings

word = "Python101 is good"
print(len(word)) # 17
print("word count", word.count('o')) # word count 3

# slicing

print(word[0], word[3]) # P h
print(word[-1], word[-4]) # d g
print(word[2:], word[3:7], word[:8]) # thon101 is good, hon1, Python10

msg1='welcome to Python 101: Strings'
msg2=msg1[18]+' '+msg1[:8]+msg1[25:29]+msg1[7:11]+msg1[13]+msg1[12]+msg1[2]+msg1[1]+msg1[-5]  
print(msg2.title())
print(msg2[::-1].title()) # write string from the back
msg3="""Dear Terry,,
You must cut down the mightiest 
tree in the forest with…
a herring! <3"""
print(msg3) # break string in multiple lines

print("/// Find & Replace")
print(msg1.find('w'))
print(msg1.replace('Python','C')) # strings are immutable, this won't change the real string
print(msg1) # msg1 is still 'welcome to Python 101: Strings''welcome to Python 101: Strings'
msg1=msg1.replace('Python','C') # string will now change
print(msg1) # # msg1 is now 'welcome to C 101: Strings''welcome to Python 101: Strings'

print('C' in msg1) # return True because C is in msg1
print('C' not in msg1) # return False because C is in msg1

name='TERRY'
color = 'RED'
print('[' + name + '] loves the color ' + color.lower() + '!') # [TERRY] loves the color red!
print(f'[{name.capitalize()}] loves the color {color.lower()}!') # [Terry] loves the color red!

# if num1 is 3 and num2 is 4
# num1=input('Enter a digit: ') # takes the result as string
# num2=input('Enter a second number:') # takes the result as string
# answer=float(num1)+float(num2) # answer = 7.0
# print(int(answer)) # returns 7

# name = input('Enter your name: ')
# distance_km = input('Enter distance in km: ')
# distance_mi = float(distance_km)/1.609
# print(f'Hi {name.title()}! {distance_km}km is equivalent to {round(distance_mi,1)} miles.')

# LISTS

# how to create empty lists
empty_list = []
empyt_list = list()

friends = ['John','Michael','Terry','Eric','Graham']

print(friends) # ['John','Michael','Terry','Eric','Graham']
print(friends[1],friends[4]) # Michael Graham
print(friends[:4]) # ['John', 'Micheal', 'Terry', 'Eric']
print(len(friends)) # 5
print(friends[:]) # ['John', 'Michael', 'Terry', 'Eric', 'Graham']
print(friends.count('Eric')) # occurence of Eric which is 1 
print(friends.index('Eric')) # index of Eric which is 3
friends.sort()
print(friends) # ['Eric', 'Graham', 'John', 'Michael', 'Terry']
friends.sort(reverse=True)
print(friends) # ['Terry', 'Michael', 'John', 'Graham', 'Eric']

cars = [911,130,328,535,740,308]
cars.sort()
print(cars) # [130, 308, 328, 535, 740, 911]
print(min(cars)) # 130
print(max(cars)) # 911
print(sum(cars)) # 2952

friends.append('TerryG') 
print(friends) # ['Terry', 'Michael', 'John', 'Graham', 'Eric', 'TerryG']
friends.insert(1,'TerryG') 
print(friends) # ['Terry', 'TerryG', 'Michael', 'John', 'Graham', 'Eric', 'TerryG'] 
friends[2]='TerryG' # replace Michael with TerryG
print(friends) # ['Terry', 'TerryG', 'TerryG', 'John', 'Graham', 'Eric', 'TerryG']
friends.extend(cars) 
print(friends) # ['Terry', 'TerryG', 'TerryG', 'John', 'Graham', 'Eric', 'TerryG', 911, 130, 328, 535, 740, 308]

friends.remove('Terry')
print(friends) # ['TerryG', 'TerryG', 'John', 'Graham', 'Eric', 'TerryG', 130, 308, 328, 535, 740, 911]
popped = friends.pop()
print(popped) # 911
print(friends) # ['TerryG', 'TerryG', 'John', 'Graham', 'Eric', 'TerryG', 130, 308, 328, 535, 740]
friends.pop(2)
print(friends) # ['TerryG', 'TerryG', 'Graham', 'Eric', 'TerryG', 130, 308, 328, 535, 740]
friends.pop(-1)
print(friends) # ['TerryG', 'TerryG', 'Graham', 'Eric', 'TerryG', 130, 308, 328, 535]
del friends[2] # del friends without [2] deletes friends entirely, very powerful, use carefully
print(friends) # ['TerryG', 'TerryG', 'Eric', 'TerryG', 130, 308, 328, 535]

# friends.clear()
# print(friends) # []

# how to copy lists
new_friends1 = friends[:]
new_friends2 = friends.copy()
new_friends3 = list(friends)

print('copied', new_friends1, new_friends2, new_friends3)

sales_w1 = [7,3,42,19,15,35,9]
sales_w2 = [12,4,26,10,7,28]
sales = []
# new_day = input('Enter #of lemonades for new day: ')
# sales_w2.append(int(new_day)) # adds new_day value as integer into sales_w2 list
sales_w2.append(int(5)) # adds new_day value as integer into sales_w2 list

# 1 Way to join two lists together
# sales.extend(sales_w1)
# sales.extend(sales_w2)

# Another Way to join two lists together - better way
sales = sales_w1 + sales_w2

# 1 way to get minimum and maximum value in sales list 
# sales.sort()
# worst_day_prof = sales[0] * 1.5
# best_day_prof = sales[-1] * 1.5

# Another way to get minimum and maximum value in sales list - better way
worst_day_prof = min(sales) * 1.5
best_day_prof = max(sales) * 1.5

print(f'Worst day profit:$ {worst_day_prof}')
print(f'Best day profit:$ {best_day_prof}')
print(f'Combined profit:$ {worst_day_prof + best_day_prof}')

csv = 'Eric,John,Michael,Terry,Graham'
print(csv.split(',')) # ['Eric', 'John', 'Michael', 'Terry', 'Graham']


msg_new ='Welcome  to  Python  101: Split and Join'
friends_list = ['Eric','John','Michael','Terry','Graham']
print(''.join(friends_list)) # EricJohnMichaelTerryGraham

print('split mgs', msg_new.split()) # ['Welcome', 'to', 'Python',  '101:', 'Split', 'and', 'Join']

print(''.join(msg_new.split())) # join all msg_new # WelcometoPython101:SplitandJoin
print(msg_new.replace(' ', '')) # replace all spaces in msg_new with 'nothing' # WelcometoPython101:SplitandJoin

# Tuples  - faster Lists you can't change, use () can't use append, split etc...

#  how to create empty Tuple
empty_tuple = ()
empty_tuple = tuple()

friends_tuple = ('John','Michael','Terry','Eric','Graham')
print(friends_tuple[2]) # Terry
print(friends_tuple[2:4]) # ('Terry','Eric')

# Set - use {}, unordered, remove deplicates, very fast

# how to create empty Set
empty_set = {} # this is wrong, this is a dictionary
empty_set = {'John', 'Michael'} # this is correct
empty_set = set()

friends_set = {'John','Michael','Terry','Eric','Graham','Eric'}
print(friends_set) # {'John','Michael','Terry','Eric','Graham'} last Eric not shown - no duplicates

my_friends_set = {'Reg','Loretta','Colin','Eric','Graham'}
print(friends_set.intersection(my_friends_set)) # names that exist in both -- {'Eric', 'Graham'}
print(friends_set.difference(my_friends_set)) # names that exist in friends_set but not in my_friends_set -- {'John', 'Michael', 'Terry'}
print(friends_set.difference(my_friends_set)) # all names in both set without duplicates -- {'John', 'Michael', 'Terry', 'Eric', 'Graham', 'Reg', 'Loretta', 'Colin'}

#Sets - Exercise

friends = {'John','Michael','Terry','Eric','Graham'}
my_friends = {'Reg','Loretta','Colin','John','Graham'}
cars =['900','420','V70','911','996','V90','911','911','S','328','900']

#1. Check if ‘Eric’ and ‘John’ exist in friends
print('Eric' in friends and 'John' in friends) # True

#2. combine or add the two sets

print(friends.union(my_friends)) # {'John', 'Michael', 'Terry', 'Eric', 'Graham', 'Reg', 'Loretta', 'Colin'}
print(friends | my_friends)      # {'John', 'Michael', 'Terry', 'Eric', 'Graham', 'Reg', 'Loretta', 'Colin'}

#3. Find names that are in both sets
print(friends.intersection(my_friends)) # {'John', 'Graham'}
print(friends & my_friends)             # {'John', 'Graham'}

#4. find names that are ONLY in friends
print(friends.difference(my_friends))   # {'Michael', 'Terry', 'Eric'}
print(friends - my_friends)             # {'Michael', 'Terry', 'Eric'}

#5. find names that are ONLY in my_friends
print(my_friends.difference(friends))   # {'Reg', 'Loretta', 'Colin'}
print(my_friends - friends)             # {'Reg', 'Loretta', 'Colin'}

#6. Show only the names who only appear in one of the lists
print(my_friends.symmetric_difference(friends)) # {'Reg', 'Loretta', 'Colin', 'Michael', 'Terry', 'Eric'}
print(my_friends ^ friends)                     # {'Reg', 'Loretta', 'Colin', 'Michael', 'Terry', 'Eric'}

#7. Create a new cars-list without duplicates
cars_no_dupl_set = set(cars)
print(cars_no_dupl_set)         # {'900', '420', 'V70', '911', '996', 'V90', 'S', '328'}

#8. Convert the cars-set back to a list
cars_no_dupl_list = list(set(cars)) 
print(cars_no_dupl_list)        # ['900', '420', 'V70', '911', '996', 'V90', 'S', '328']











