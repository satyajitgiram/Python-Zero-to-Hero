# capitalize

s = 'Krishna'
s2 = 'Uß'
r = s.capitalize() # first capital and remaining all small
# print(r)

r = s.casefold() # convert special char like beta ß to lower -> works on unicode
# print(r)

r = s.lower()
# print(r)

r = s.center(13, '_') # this will center by second char
# print(r)

r = s.count('z') 
# count require 1 parameter 
# print(r)

r = s.encode('utf-8') 
# print(type(r))
# print(r)

r = s.endswith('na') # check weather is avail or not end string -> return bool
# print(r)

s2 = 'hare \tkrishna'
r = s2.expandtabs(45) # increase tab width within the string.
# print(r)

r = s.find('K') # return position of starting index if not find return -1 it is case sensitive
# print(r)

s2 = 'The value of x is {0} and y is {1}'
r = s2.format(23, 54) # goes result respectively
# print(r)

# customization string formating
point = {'x':4,'y':-5}
# print('{x} {y}'.format(**point))

s2 = 'The value of x is {x} and value of y is {y}'
r = s2.format_map(point) # map keys into string
# print(r)

r = s.index('K') # return index if not found throw value error
# print(r)

s2 = 'Lasd230'
s3 = '$-Lksd34' # this is not alpha numeric
r = s2.isalnum() # alphabets and number only check return bool
# print(r)

s2 = 'name'
r = s2.isalpha()
# print(r)

s2 = '1234.09' # this is not decimal 
s2 = '234'
r = s2.isdecimal()
# print(r)

s2 = '\u00B2'
r = s2.isdigit() # it is similar isdecimal but it support unicode also
# print(r)

r = s2.isidentifier() # verify if it is support variable naming
# print(r)

s = 'hare 2krishna'
r = s.islower() # check only char
# print(r)

s2 = '1235'
r = s2.isnumeric()
# print(r)

s2 = '```: \n )b #1'
r = s2.isprintable()
# print(r)

s2 = 'LLSLD1'
r = s2.isupper() # check only char
# print(r)

s2 = ' ' # one space 
r = s2.isspace()  # check only space
# print(r)

s2 = 'Hari Bol'
r = s2.istitle() # check if each char is capital or not
# print(r)

s2 = 'satis is'
r = ' '.join('my_name') # join to each char first str
# print(r)

r = s2.ljust(20, '_') # left side alignment of string
# print(r)

r = s2.rjust(20, '_') # right side alignment of string
# print(r)

r = s2.lower()
# print(r)

x = '   strif   '
r = x.lstrip() # left side white sapce removed
# print(r)

x = '   some str   '
r = x.rstrip() # right side white sapce removed
# print(r)

s = 'radha rani'
r = s.maketrans('a', 'k') # translate char _> charecter lever replacements
# print(s.translate(r)) # use this[ replace all char]

# r = s.replace('radha', 'krishna') # replace str with new one
r = s.replace('a', 'k') # replace str with new one
# print(r)

x = 'hare krishna'
r = x.partition(' ') # particiate by input str
# print(r)

r = x.rfind('h') # if two found take right one
# print(r)

r = x.rindex('a') # if two found take right one
# print(r)

r = x.rpartition('a') # if two found take right one and partiation
# print(r)

x = 'moonlight sunlight'
r = x.split(' ') # split into parts
# print(r)

x = 'c:/home/deskop/newfolder/myfile/py\nthoncoursee/abc'
r = x.rsplit('/', 2)  # split uses right side max split size
# print(r)

r = x.splitlines() # if fount \n then split
# print(r)

r = x.startswith('c') # check start char if present or not
# print(r)

r = x.swapcase() # change case if upper then lower vice versa
# print(r)

x = ' a n  sdflk  '
r = x.strip()
# print(r)

x = '12'
r = x.zfill(3) # zero fill
# print(r)

