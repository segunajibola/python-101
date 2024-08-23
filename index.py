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
print(msg, mgs) # welcome to it's Python 101: Strings welcome to it's Python 101: Strings
print(msg.upper()) # WELCOME TO IT'S PYTHON 101: STRINGS
print(msg.lower()) # welcome to it's python 101: strings
print(msg.capitalize()) # Welcome to it's python 101: strings
print(msg.title()) # Welcome To It'S Python 101: Strings