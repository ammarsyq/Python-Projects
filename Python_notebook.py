#video 1 list, set, dictionary
daily_pints = {1,2,3,23}
type(daily_pints)

wifes_daily_pints_log = {3,5,4,6,1,2}

print(wifes_daily_pints_log ^ daily_pints)

dict_cream = {'name': 'Ammar', 'weekly intake': 5}

print(dict_cream)

#video 2 comparison operator

10 == 10
10 == 50

x = 'vanilla'
y = 'chocolate'

x == y

10 < 10
10 <= 10
20 >= 10

(10 == 10) and (20 == 20)
(10 == 10) or (10 == 20)

#video 3 if, elif, else

if 25 < 10:
    print('hell yea')
elif 25 < 20:
    print('yea')
else:
    print('bro cmon')

#video 4 for loops

integers = [1,2,3,4,5]
for num in integers:
    print('yea')


integers = [1,2,3,4,5]
for a in integers:
    print(a+a)

flavors = ['vanilla', 'chocolate', 'cnc']
toppings = ['sprinks', 'choco chips']
for one in flavors:
    for two in toppings:
        print(one, 'topped with', two)


#video 5 while loops

number = 0
while number < 10:
    print(number)
    number = number + 1


number = 0
while number < 10:
    print(number)
    if number == 3:
        break
    number = number + 1

number = 0
while number <= 10:
    print(number)
    if number == 3:
        continue
    number = number + 1
else:
    print('done')


number = 0
while number <= 10:
    number = number + 1
    if number == 3:
        continue
    print(number)
else:
    print('done')

#video 6 functions

def first():
    print('we did it')

first()

def number_sq(num):
    print(num**2)

number_sq(5)

def number_sq(num, pw):
    print(num**pw)

number_sq(5, 3)

def number_args(*num):
    print(num[0]*num[2])

number_args(5,7,5,5)

def number_sq(num, pw):
    print(num**pw)

number_sq(num = 2, pw = 3)

def num_kwarg(**number):
    print('my num is: ' + number['int'])

num_kwarg(int = '2309')

#video 7 coverting data typ

a = 7
b = '8'

d = int(b)

c = a+d
c

ls = [1,2,3]
type(ls)

tpl = tuple(ls)
type(tpl)