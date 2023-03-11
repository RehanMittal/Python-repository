"""                                Unit -1 .                                   """

name = "rehan"
section = "koc36"
reg_no = 12221859
roll_no = 14
print("name:", name, "\t", "section:", section, "\t", "registration no.:", reg_no, "\t", "roll no.:", roll_no)

# This is python program comment. \n means new line, \t means tab space

name = "rehan"
section = "koc36"
reg_no = 12221859
roll_no = 14
print(" name:", name, "\n", "section:", section, "\n", "registration no.:", reg_no, "\n", "roll no.:", roll_no)

"""
Hello everyone this is docstring comment. two types of comment are single line and docstring.
comments do not nest ie ##
"""

print("hello world")
 
'''
welcome to keyword 
keep learning
'''
import keyword

print(keyword.kwlist)
"""
lets check if the word is keyword or not
"""
print(keyword.iskeyword("true"))
print(keyword.iskeyword("True"))
"""
                              LETS LEARN SOMETHING
THere are two interfaces for IDLE-IDLE SHEll (interactive environment)-REPL-Read evaluate print loop
and IDLE edition(python scripts) 
mobile apps cant be made from python, java is required for it
python is dynamic(no need to specify-int,float),portable,open source,easy to write and understand language.
Two types of errors are compiletime(typographical mistake)(syntax) and runntime(poor logic ex a/0
python is case sensitive programing language which means (age) and (Age)are two different identifiers  
Identifiers - cant be started with 0 to 9
includes- a to z;A to Z;0 to 9; only one special character that is underscore..._
a="hello"; here a is variable and also a identifier
keywords cant be used as identifier
35 keywords are there
python do not restrict length of identifier where as C do(31)
Variables are of 4 types-- string(words),number,float(fraction),boolean(true/false)
python2=32keywords
python3.5=33keywords(32+'nonlocal')
TYPES OF STATEMENTS--print,assignment(further classified into basic and augmented)
,selective,iterative,function declaration
"""
a, b, c = 5, 6, 7
print(a, b, c)
print(a)
print(b)
print(c)
print('a', 'b', 'c', sep='#')  # sep means seprate
print('a', 'b', 'c', sep='@')
print('a', 'b', 'c', sep='!')
"""

AUGMENTAL ASSIGNMENT
If a+=10 than it means a=a+10

"""
a = 5
a += 10
print(a)
a = 5
b = 10
a *= b
print(a, b)
"""
docstring comment should begin with capital letter and end with a full stop(period) (.)
a*=b means a=a*b which is 5*10=50
python is composed of multiple statements --comments,whitespace characters and tokens
IF WE ARE GIVEN age=21 THAN
age is reference variable to integer 21
21 is object which take some part of memory 
age is variable and 21 is value assigned to it
data types in python are --numbers,list,tuple,strings,dictioneryy,set
"""
a = b = c = d = "hello"
print(a, b, c, d)
print(id(a), id(b), id(c), id(d))
# this is an chained assignment ie a=b=c=d
# id stands to give identity of particular location
value1 = value2 = value3 = 'hello'
print(value1, value2, value3)
value1 = 99
value2 = "hello python"
value3 = "hello world"
print(value1, value2, value3)
"""
EXPRESSION consist of values(4+5=9 here 9 is value)
                    operand( 4 and 5)   
                    variables
                    and operators(+-*/)
                    instructions=statements
                    for ex a=10 is assigned statement
                           b=10 is assigned statement
                           print(a+b) a+b is expression and print(a+b) is statement
                           a=b*5+c ; b*5+c is expression 
 LETS SEE TYPE OF VARIABLE NOW                                               
"""
a = 345
b = 67.978
c = "hello"
d = [2, 3.9, "hello"]
print(type(a))
print(type(b))
print(type(c))
print(type(d))
"""
encoding --------ASCII codes                                     Unicode(Used in python)
(american standard code for information interchange)
A to Z
a to z                                                              used in python
0 to 9
use 8 bits for encoding                                         use 8 and 16 bits for encoding
previously 0 to 127                                                65 to 90-A to Z
now 0 to 255                                                       97 to 122-a to z  
sys  stands for system
python max encoding value is 1114111

ord  stands for ordinal
chr stands for character     
"""
import sys

print(sys.maxunicode)
print(ord("b"))
print(chr(65))
print(sys.getfilesystemencoding())
"""
 0 1 2 3 4 5 6
 W E L C O M E
-7-6-5-4-3-2-1
"""
str1 = "WELCOME"
print(str1)
print(str1[-1])
print(str1[2:4])
print(str1[4])
print(str1[2:6])
print(str1[2:])
print(str1[:4])
print(str1[-7:-1])
# Strings can be made in single quote,double quote,triple double quote.
a = 23
b = 21
c = a + b
print("sum of a:", a, "and b:", b, "is", c)
a, b, c, d, e = 1, 2, 3, 4, 5
f = a * b * c * d * e
print("product is:", f)
""""

LETS START WITH MATHEMATICAL CAALCULATIONS


"""
import math

radius = 5
area = math.pi * radius * radius  # can also use radius**2
print("Area:", area)
print("pi value:", math.pi)
"""
swapping values of 2 variables
"""
a, b = 10, 20
temp = a
a = b
b = temp
print(a, b)
'''
new method
'''
a, b = 10, 20
a = b
b = a
print(a, b)
"""
other way
"""
a, b = 10, 20
a = a + b  # a=30
b = a - b  # b=10
a = a - b  # a =20
print(a, b)
a, b = 10, 20
a = a * b  # a=200
b = a // b  # b=10
a = a // b  # a=20
print(a, b)
"""
input statements
"""
a = input("enter string value:")
print("string entered by you is:", a)
a = int(input("enter first number:"))
b = int(input("enter second number:"))
c = a + b
print("sum of numbers is:", c)
"""
string to float   float(_____) 
string to complex    complex(_____)
"""
a = int(input("Enter the celsius reading:"))
b = float(9 / 5) * a + 32
c = float(a) + 273
print("your fahrenheit reading is:", b, "and kelvin reading is:", c)

a = int(input("enter the radius of cylinder:"))
b = int(input("length of cylinder is:"))
c = math.pi * float(a ** 2 * b)
print("volume of cylinder given is:", c)

a = int(input("write feet reading:"))
b = float(a * 0.305)
print("reading in metres is:")

a = int(input("x2 coordinate:"))
b = int(input("x1 coordinate:"))
c = int(input("y2 coordinate:"))
d = int(input("y1 coordinate:"))
e = float((a - b) ** 2 + (c - d) ** 2) ** 1 / 2
print("distance between coordinates is:", e)
"""
here starts the class work
"""

import math

r, l = eval(input("Enter radius and length:"))  # eval func for more than 1 inputs
volume = math.pi * (r ** 2) * l
print("Volume is:", volume)
print("2+3")
print(eval("2+3"))
print(eval("3.4+5.6"))
x = 2
y = -x
print(x, y)
x = -2
y = -x
print(x, y)

a, b = eval(input("Enter the numbers :"))
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)

num = int(input("Enter 5 digit numbers:"))
digit5 = num % 10
num = num // 10
digit4 = num % 10
num = num // 10
digit3 = num % 10
num = num // 10
digit2 = num % 10
num = num // 10
digit1 = num % 10
print("sum of digits is:", digit1 + digit2 + digit3 + digit4 + digit5)


print(4 + 2 * 3 ** 2)


a = 5
b = 5
print(a < b)
print(a > b)
print(a <= b)
print(a >= b)
print(a != b)

age, membership = eval(input("Enter age and membership status"))
print(age >= 60 and membership == "prime")

import math

a, b = eval(input("radius and height of cylinder are:"))
c = math.pi * float(a ** 2 * b)
print("volume of cylinder is:", c)

a, b = eval(input("Enter the subtotal and the gratuity rate:"))
c = float(a * b) / 100
d = float(a + c)
print("your gratuity and total are:", c, d)

my_str = "Sambhavi is a good girl"
print(len(my_str))  # to find length

print("Hello", end='')
print("World")
"""
two types of data are homogeneous and hetrogeneous.
"""
age = int(input("enter age"))
if age >= 18:
    print("eligibe")
else:
    print("non eligible")

num = int(input("enter number:"))
print(num % 2 == 0)  # to check divisiblity by 2

num = int(input("enter num:"))
print(num % 5 == 0)  # use of double == is mandatory

# to check greatness of two numbers

num1, num2 = eval(input("enter two numbers:"))
print(num1 > num2)

num1, num2 = eval(input("enter two numbers:"))
if num1 > num2:
    print("true")
else:
    print("false")

# logical operator--

jee, twelth = eval(input("enter percentile and marks"))
print(jee >= 85 and twelth >= 60)

"""
--\ types of operators \ --
unioperant'--unary plus,unary minus,logical not,bitwise not
binaryoperant--arithmatic,relational,bitwise,logical,membership,identity
"""
'''
unary minus
'''
x = 4
y = -x
print(x, y)

''' unary plus'''

x = 4
y = x
print(x, y)
"""relational"""
a = int(input("enter age:"))
print(a >= 18)
"""  != is not equal to,,,,false means 0"""
"""logical operator---and,or,not"""
a = int(input("age"))
b = input("membership")
print(a >= 34 and b == "prime")  # and

"""
bitwise and,or(inclusive or),xor(exclusive or)
A B A&B A|B A^B
0 0 0   0   0
0 1 0   1   1
1 0 0   1   1
1 1 1   1   0

"""
x = 10  # 00001010
y = 2   # 00000010
print(x & y)

x = 15  # 00001111
y = 24
print(x | y)

x = 21
y = 46
print(x ^ y)  # XOR or exclusive or

"""
shift operations-- 2 cases 
case 1 n<<no_0f_bits -------5<<3 --5*2^3--shortcut
(left shift)5=00000101 convert to 00101000 makes 1*0+2*0+4*0+8+16*0+32=32+8=40
case 2 n>>no_of_bits -------9>>3 --9//2^3
(right shift)9=00001001 convert to 00000001 makes 1
"""
print(5 << 3)  # smaller than aya toh age wale hatao 3 hataooo
print(9 >> 3)  # greater than aya to piche wale hatao 3 hataoooo
''' bitwise not (~)
if n=5 --[-(n+1)]'''
n = 5
print(~n)

"""
membership
"""
x = "abcd"
print("a" in x)
print("y" in x)
print("a" not in x)
print("y" not in x)

x = str(input("enter string:"))
y = str(input("enter what u want to verify:"))
print(y in x)
"""identity--mutable(changable)-list,dictionry,set
             immutable-int,float,string,tuple,bool"""
x = 21
y = 21
z = 21
print(id(x), id(y), id(z))  # allsame

l1 = [1, 2, 3]
print(id(l1))
l1.append(4)
print(l1)  # mutable

x = "hello"
y = "hello"
print(x is y)

z = hex(id(x))
print(z)

n = 432
z1 = bin(n)
print(z1)

l1 = [1, 2, 3]
l2 = [1, 2, 3]
print(l1 is l2)  # false bcoz list is mutable using APPEND

x = 999
y = 999
print(x is y)  # older idle would show false against -5 to 256

"""
number system--
decimal--base10-0to9        0b                                 2| 7 |1     
binary--base2-0,1          bin                                 2| 3 |1
octal--base8-0to7           oct                                 | 1 |1
hexadecimal--base16--0to9 and a to f              hex           |   |       binary of 7 is 00000111

5==    00000101
       11111010====One's compliment         bitwise not---one's compliment operator(~)
       1=MOST SIGNIFICANT BIT==MSB
"""
x = 10
y = 10
print(id(x), id(y))  # same id

"""************formatting in python*********"""
name = "suresh"
print("hello,%s!" % name)  # String Modulo Operator--%

firstname = "suresh"
lastname = "kunmar"
print("%s,%s" % (firstname, lastname))

a = 10
b = 20
c = 3.45  # TYPES of ALIGNMENT--LEFT aligned and RIGHT aligned
str = "Hello"
print("%d,%d,%.2f,%s" % (a, b, c, str))

import math

r = float(input("enter radius"))
area = math.pi * r * r
print("area is:%.3f" % area)

x = 123
print("%d" % x)
print("%5d" % x)
print("%05d" % x)
print("%2d" % x)
print("%-5d" % x)
# mixed data--% type
a = 10
b = 20
c = 3.4678
str = "hello"
print("the value of a=%d,b=%d,c=%f and str=%s" % (a, b, c, str))  # here 3.4678 comes as 3.467800
# %precision type
a = 10
b = 20
c = 3.4678
str = "hello"
print("the value of a=%d,b=%d,c=%.2f and str=%s" % (a, b, c, str))  # .2f means to stop after 2 decimals

import math

r = int(input("radii:"))
area = math.pi * r ** 2
print("area is:%.3f" % area)

# %width type
x = 123
print("%d" % x)  # align left
print("%5d" % x)  # __123
print("%05d" % x)  # 00123 --%flag width type
print("%2d" % x)  # 123
print("%-5d" % x)  # 123

x = 123
y = 456
print("%-5d%d" % (x, y))
print("%d%5d" % (x, y))  # gives same result

x = 3.4567
print("%5.2f" % x)  # width=5(total 5 space)(1spacefrom start),precision=2(till 2 decimal places)
print("%05.2f" % x)
# with 2 decimal points and 5 leading spaces--2deciml point==45.28==5digits,,,,5digit+5spaces=10
x = 45.682354
print("%10.2f" % x)
# 2decimal point 1 leading space--
x = 45.682354
print("%06.2f" % x)
print("%-5.2f" % x)
print("%-05.2f" % x)  # no trailing 0 bcoz at a time only 1 flag can work
"""
width with string
"""
x = "hello"
print("%10s" % x)
print("%.2s" % x)
print("%10.2s" % x)
print("%-10.2s" % x)
print("%-10s" % x)
# tea with 5 white spaces on left
str = "teapot"
print("%8.3s" % str)

# 9.8216 upto 2 decimals and pad with 3 zeroes on left

x = 9.8216
print("%07.2f" % x)

"""hexa decimal octa values"""
a = 15
print("%x" % a)
print("%X" % a)
print("%o" % a)  # not zero ,o=octal
print("%d" % a)  # d=decimal

"""format function"""
a = 10
b = 20
print("a{},b{}".format(a, b))

print("a:{1},b:{0}".format(a, b))  # a at 0 position and b at 1 position
a = 10
b = 20
c = 30
print("{2},{0},{1}".format(a, b, c))  # a at 0,b at 1 , c at 2

x = 24.567385
print("%10.2f" % x)  # 5spaces+5digits

a = 10
b = 20
c = 30
print("value of a is {2},b is {0} and c is {1}".format(a, b, c))

print("{0} {1:d}".format("students", 18))  # 1 is a index
print("{0:10.4s}".format("everyone"))  # .5s=every,.2s=ev
print("{0:.5s}".format("everyone"))
# by defaultt letters gets aligned ---in string modulo--right
# in format tab--left

print("{0:10s} is the string".format('abc'))  # right aligned
print("{0:>10s} is the string".format('abc'))  # right aligned converted to left aligned,cant use (-) for alignment,use only<,>

print(3.14159)

print("{0:.2f}".format(3.14159))

print("{0:6.2f}".format(3.14159))  # 4chr,2leading spaces

# teapot with 3 whitespaces on left
print("{0:9s}".format("teapot"))

# 45 with 3 spaces on left
print("{0:5d}".format(45))

# print tea from string teapot
print("{0:.3s}".format("teapot"))  # cant use 1 in place of 0 ..whY?? -- bete index to dekhleee

# print 45.1245 upto 2 decimal places
print("{0:.2f}".format(45.1245))

print("{0:x}".format(15))
print("{0:X}".format(15))
print("{0:o}".format(15))
print("{0:b}".format(15))
print("{0:e}".format(1534566))  # 123e+06 means 123*10^6
print("{0:E}".format(1234567))

print(format("Hello", "10.2s"))  # left aligned
print(format("Hello", ">10.2s"))  # right aligned
print(format("Hello",45, "4d"))
print(format(123.5678, "7.2f"))

l1 = [1, 2, "one", "hi"]
print(l1[-2])  # lists are mutable and represented with[]
print(l1[1:3])  # list slicing                     """ one append can be used to add one digit only"""
print(l1 * 2)  # in sets , elements can be added but cant be updated,no duplicacy present
l1.append(9)  # ''' set is represented by {},,we can use set=set() to make set'''
print(l1)  # ''' dict is also used with{}'''
# tuples get freezed after taking input,bracket- ()
l1 = [2, 3, 4]  # tuples are converted to list to modify afterwards
l2 = [4, 5, 6]
print(l1 + l2)  # concatenation

n = int(input("how many times should list appear:"))
l3 = 123
print(l3 * n)  # repeating lists

l4 = [2, 4, 5, [8, 6, 7], 9, 0]
print(l4[3][1])  # nested list
# l1.insert(1,43)
l5 = [6, 7]  # mydict.update({"5":"five"})
print(l5)  # del mydict[4]--- delete function
l5[0] = 56  # mydict[4]="three"--Appending.,set.add(1),,s.union(1,2,3),,s.intersection(1,2,3),min(s),max(s),len()
print(l5)  # updating list,,,,56 come at place of 6

myset = {3, 4, 5, 6, 3, 2}  # print one digit only once
print(myset)

test = {}
print(type(test))

tuple1 = tuple()
print(tuple1)

mytuple = (3, 4, 5)  # need to put comma to make single element tuple otherwise it will be integer
print(mytuple)
print(mytuple[1])
print(mytuple[0])

mydict = {"TV": 25000, "LED": 45000, "Laptop": 70000}
print(mydict)

result = int(input(""), 2)
print(result)

# find the error
print("{:3d}{:d}".format(7,18))

'''
 dictioneriesssssss--are unordered andd represented as key,colon,value
key is mutable like roll no,,,give key to get value
key should be unique without duplicacy
index are immutable like registration no.
'''

mydict = dict()
print(type(mydict))

mydict = {}
print(type(mydict))

mydict = dict(Hyderabad=20, NewDelhi=40)
print(mydict)

mydict = {1: "one", 2: "two", 3: "three"}
print(mydict)
print(mydict[1])

d1 = {"TV": 65000, "car": 89000, "bike": 76000}
print(d1)
print(d1["TV"])


"""                           Unit-1 is OVER!!!!!                               """
"""                           Unit-2 is STARTED!!!                              """


# if statement

x = int(input("Enter value of x:"))
if x > 0:  # can use brackets like(x>0), use of : is necessary
    print("x is positive")  # put negative value and it wont work
    print("we are in block of if")
print("we are out of if and now in the program")


y = int(input("enter x:"))
if y % 2 == 0:  # arithmatic and comparison operator
    print("number is even")
else:
    print("number is odd")


z = int(input("enter age"))
if z >= 18:
    print("eligible")
else:
    print("non eligible")


# practice problems

n = int(input("enter num:"))
if n % 7 == 0:
    print("divisible by 7")
else:
    print("not divisible by 7")



a = 27
b = 27.0
if a == b:
    print("a and b are equal")
if a != b:
    print("a and b are unequal.")



marks = int(input("enter marks:"))
if marks > 75:
    print("User secured dstinnction.")
else:
    print("user did not secure distinction.")



balance = int(input("Enter balaance in your acount:"))
if (balance >= 1000):
    print("sufficient balance")
else:
    print("insufficient balance.")



# nested if else

p = int(input("enter value of x:"))
if p > 0:
    if p % 5 == 0:
        print("x is divisible by 5")
    else:
        print("x is not mulltiple of 5")
else:
    print("x is negative")


# admission application 12th prcntage,jee result

d = eval(input("enter 12th marks:"))
e = eval(input("enter jee percentile:"))
if d < 60:
    if e > 85:
        print("eligible")
    else:
        print("non eligible")
else:
    print("eligible")


# if-elif-else

x = int(input("x:"))
y = int(input("y:"))
if x < y:
    print(x, "is less than", y)
elif x > y:
    print(x, "is more than", y)
else:
    print(x, "and", y, "are equal.")


# chk no. is 0 or +ve or -ve
x = int(input("x:"))
if x == 0:
    print("number is 0")
elif x > 0:
    print("number is positive")
else:
    print("number is negative")


# take input to tell grade
score = int(input("score:"))
if score >= 90.0:
    grade = 'A'
elif score >= 80.0:
    grade = 'B'
elif score >= 70.0:
    grade = 'C'
elif score >= 60.0:
    grade = 'D'
else:
    grade = 'F'
    print(grade)


# find greatest among three numbers

x = int(input("x:"))
y = int(input("y:"))
z = int(input("z:"))
if x > y and y > z:
    print("x is greatest")
elif y > z and z > x:
    print("y is greatest")
elif x == y and y == z:
    print("all the numbers are equal.")
else:
    print("z is greatest")


# to check given no. is alphabet or digit

print("Enter 0 for exit")
ch = input("Enter any character: ")
if ch == 0:
    print("Enter 0 for a exit")
elif (ch >= 'A' and ch <= 'Z'):
    print("Given chr{} is an alphabet".format(ch))
elif (ch >= 'a' and ch <= 'z'):
    print("Given chr{} is an alphabet".format(ch))
elif (ch >= '1' and ch <= '9'):
    print("Given chr{} is an digit".format(ch))
else:
    print("Given chr{} is neither alphabet nnor an digit".format(ch))


# to check no. is leap year

year = int(input("year:"))
if year % 4 == 0 and year % 100 != 0:
    print("it is leap year")
elif year % 400 == 0:
    print("is leap year")
else:
    print("It is not leap year.")


# To calculate electricity bill

unit = float(input("enter unit:"))
if unit <= 100 and unit >= 0:
    bill = unit * 1.5
elif unit > 100 and unit <= 200:
    bill = (100 * 1.5) + (unit - 100) * 2.5
elif unit <= 300:
    bill = (100 * 1.5) + (100 * 2.5) + (unit - 200) * 4
elif unit <= 350:
    bill = (100 * 1.5) + (100 * 2.5) + (100 * 4) + (unit - 300) * 5
elif unit > 350:
    bill = (100 * 1.5) + (100 * 2.5) + (100 * 4) + (50 * 5) + (unit - 350) * 15
print("bill is", bill)


# whether given triangle is isosceles,equilatral,scalene
side1 = int(input("side1"))
side2 = int(input("side2"))
side3 = int(input("side3"))
if side1 == side2 == side3:
    print("triangle is equilaeral")
elif side1 == side2 or side2 == side3 or side1 == side3:
    print("triangle is isosceles")
else:
    print("triangle is scalene")


# to chk id's of strs are equal or not
str1 = str(input("str1"))
str2 = str(input("str2"))
if str1 == str2:
    print("strs are equal")
elif str1 < str2:
    print("str2 is greater")
else:
    print("str1 is greater")


# line if else (to chk greater no.)

num1 = int(input("num1"))
num2 = int(input("nnum2"))
max = num1 if num1 > num2 else num2
# op1          # op2       # op3      # op means operant
print(max)


# inline if-else

num = int(input("num"))
print("number is even" if num % 2 == 0 else "number is odd")



# LOOPS--

# to print str 100  times
count = 0
while count < 100:
    print("Programming is fun")
    count = count + 1


# to print str n times
n = int(input("n: "))
i = 1
while i <= n:
    print("ABC")
    i = i + 1  # indentation


# display frst 100 natural numbers
i = 1
while i <= 100:
    print(i, end='  ')
    i = i + 1


# counting from 1 to n
n = int(input(""))
i = 1
while i <= n:
    print(i, end='  ')
    i = i + 1


# calculate squares of even numbers
i = 1
while i <= n:
    if i % 2 == 0:
        print(i * i, end='  ')
    i = i + 1


# count odd numbers from 1 to n
i = 1
count = 0
while i <= n:
    if i % 2 != 0:
        count = count + 1
    i = i + 1  # accumulation operation
print("count of odd numbers", count)


# add odd numbers,accumulation operaton
i = 1
sum = 0  # use product=1 for products
while i <= n:
    if i % 2 != 0:
        sum = sum + i
    i = i + 1  # accumulation operation
print("sum of odd numbers", sum)


# product of odd no. from 1 to n
n = int(input(""))
n = int(input(""))
i = 1
prod = 1
while i <= n:
    if i % 2 != 0:
        prod = prod * i
    i = i + 1  # accumulation operation
print("product of odd numbers", prod)


# numberrs from 1 to n
n = int(input("n:"))
i = n
while i <= n:
    print(i, end='  ')
    i = i + 1


# print squares  of even numbers from 1 to n
n = int(input("n"))
i = 1
while i <= n:
    if i % 2 == 0:
        print(i * i, end='  ')
    i = i + 1


# count odd numbers from 1 to n
n = int(input("n"))
i = 1
count = 0
while i <= n:
    if i % 2 != 0:
        count = count + 1
    i = i + 1  # accumulation operation
print("count of odd numbers", count)


# #add odd numbers,accumulation operaton
n = int(input("n"))
i = 1
sum = 0  # use product=1 for products
while i <= n:
    if i % 2 != 0:
        sum = sum + i
    i = i + 1  # accumulation operation
print("sum of odd numbers", sum)


# to calculate product of odd numbrs from 1 to n
n = int(input(""))
i = 1
prod = 1
while i <= n:
    if i % 2 != 0:
        prod = prod * i
    i = i + 1  # accumulation operation
print("product of odd numbers", prod)


# to chk roots are imaginary or real
a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))
D = (b ** 2) - (4 * a * c)
if D > 0:
    print("Roots are real and unequal.")
elif D < 0:
    print("roots are unreal and imaginary.")
else:
    print("Roots are real and equal")

# good logics are always made in subconcious mind


# make table
n = int(input("enter number whose table is to be printed:"))
m = int(input("enter no. of multiples"))
i = 1
while i <= m:  # m iterations
    print("{}X{}={}".format(n, i, n * i))
    i = i + 1


# calculating factorial
n = int(input("enter no. whose factorial to be printed:"))
fact = 1
i = 1
if n < 0:
    print("Factorial cannot be computed")
elif n == 0:
    print("Factorial:1")
else:
    while i <= n:
        fact = fact * i
        i = i + 1
        print("factorial is :", fact)


# reverse loop
n = int(input("enter no. whose factorial to be printed:"))
fact = 1
i = n
if n < 0:
    print("Factorial cannot be computed")
elif n == 0:
    print("Factorial:1")
else:
    while i >= 1:
        fact = fact * i
        i = i - 1
        print("factorial is :", fact)


# count digits of no.
n = int(input("enter no. to count digits"))
count = 0
while n != 0:
    count = count + 1
    n = n // 10
print("number of digits in the number:", count)


# sum of digits of  number
n = int(input("sum of number to be printed:"))
sum = 0
rem = 0
while n != 0:
    rem = n % 10
    sum = sum + rem
    n = n // 10
    print("sum of digits", sum)


# print reverse of a number
n = int(input("enter number to finid reverse"))
sum = 0
rev = 0
while n != 0:
    rem = n % 10
    rev = rev * 10 + rem
    n = n // 10
print("reverse of number is", rev)


# palindrome numbers=number==its reverse like 121,111etc
n = int(input("enter no."))
sum = 0
rev = 0
orignal = n
while n != 0:
    rem = n % 10
    rev = rev * 10 + rem
    n = n // 10
if orignal == rev:
    print("no. is palindrom")
else:
    print("no. is not palindrome")



"""find if no. is armstrong no. = narchiastic or not like if 1634,153==1^3+5^3+3^3 satisfy,no. is armstrong  3 is no. of digits of no.
count digits to decide power
convert no. to str and use len()
math.pow()--import math
whetehr number given is perfect or not
multiple of 6=2,3,1 also,2+3+1=6
6 i not divisible by any number more than its half(3)"""


# else with while--only in python
i = 100
while i > 100:
    print("printing msg on true condition")
else:
    print("printing msg in false condition")



i = 1
while i <= 10:
    if i == 2:
        break
    print(i)
    i = i + 1
else:
    print("false")



# sum of digits from 1 to n
num = int(input("num:"))
i = 0
sum = 0
while i <= num:
    sum = sum + i
    i = i + 1
else:
    while num <= 0:
        sum = sum + num
        num = num + 1
print("sum:", sum)


# hdf/gcd calulator
x = int(input(""))
y = int(input(""))
if x == 0 or y == 0:
    print("non zero value")
else:
    if x < y:
        result = x
    else:
        result = y
        while result:
            if x % result == 0 and y % result == 0:
                break
        result = result - 1
print("gcd:", result)


# fibonacci series --term=sum of prev two terms==0 1 1 2 3  5 8 13
num1, num2 = 0, 1
n = int(input("enter no. till which fibonacci is to be printed:"))
i = 1
print("Fibonacci sequence:")
while i <= n:
    print(num1, end='  ')
    res = num1 + num2
    num1 = num2
    num2 = res
    i = i + 1


# for-loop
# for val in sequence: val is looping variable
# body of loop -print statement

str = "Hello"
for i in str:
    print(i)
# initially i pick h and print h,then e,l,l,o


# take a numeric list and transverse its data
l1 = [1, 2, 3, 4]
for i in l1:  # to use dict in for loop, use --for i in dict.items():
    print(i)


# print l2 is sequence
l2 = ["orange", "blue", "red", "green"]
for i in l2:
    print(i)

# take input color from user and match with list ,if not present than add into list
color = str(input("color:"))
l1 = ['red', 'blue', 'orange', 'green']
for i in l1:
    if i == color:
        print("color found")
        break
    else:
        print("color not found,updating")
        l1.append(color)
print("updated list is", l1)


# from list, display colors starting with y
l1 = ['yellow', 'red', 'orange']
print("color names starting with y:")
for i in l1:
    if i[0] == 'y':  # filteration
        print(i)


# 0 to 5
for i in range(6):
    print(i)


# 1 to 5
for i in range(1, 6):
    print(i)


# 1 3 5 7 9
for i in range(1, 10, 2):
    print(i)


# 10 9 8 7 6 5 4 3 2 1
for i in range(10, 0, -1):
    print(i)


# multiplication table with for loop
n = int(input("whose table u need:"))
m = int(input("table till:"))
for i in range(1, m + 1):
    print('{}X{}={}'.format(n, i, n * i))


# chk given no. is prime/composite
num = int(input("enter no"))
if num > 1:
    for i in range(2, (num // 2) + 1):
        if num % i == 0:
            print(num, "is not prime number")
            break
        else:
            print(num, "is prime no.")
else:
    print("no. is not prime no.")


# print pi upto 1 to n decimal places
import math
pi = math.pi
n = int(input("n:"))
for i in range(1, n + 1):  # nested placeholders
    print('{:.{}f}'.format(pi, i))

"""outer place holder value of pi
    inner placeholder no of digits after dot
    counting paerenthesis --correct in same order andpattern--treated as strings--((()))--means 3 depth"""


# check depth of string ((( and )))
str1 = input("str:")
x = 0  # starting braces
y = 0  # ending braces
length = len(str1)
for i in range(0, length):
    if str1[i] == '(':
        x = x + 1
    elif str1[i] == ')':
        y = y + 1
        if x == y:
            print("valid and depth", i)
        elif y > x:
            print("not valid and errors", y - x)
        else:
            print("not valid and errors", x - y)



# multiplication table 1 to 10
print("Multiplication Table")
print("|", end=' ')
for j in range(1, 11):
    print(" ", j, end=' ')
print()
print("-----------------------------------------")
for i in range(1, 11):
    print(i, '|', end='  ')  # statement of outer loop
    for j in range(1, 11):
        print(format(i * j, "4d"), end=' ')
print()  # jump to new line


# *****
# *****
# *****
# *****
# *****
for i in range(1, 6):
    for j in range(1, 6):
        print("*", end="  ")
    print()


# *
# * *
# * * *
# * * * *
n = int(input("n:"))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print("*", end='')
    print()



# * * * *
# * * *
# * *
# *
n = int(input("n: "))
for i in range(n, 0, -1):
    for j in range(1, i + 1):# (i, n)
        print("*", end='')
    print()



# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1
n = int(input("n: "))
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(j, end='')
    print()

# A
# A B
# A B C
# A B C D
# A B C D E
val = 65
n = int(input("n: "))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(chr(val), end='')
        val = val + 1
    val = 65
    print()


# abcd
# abc
# ab
# a
val = 97
n = int(input("n: "))
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(chr(val), end='')
        val = val + 1
    val = 97
    print()


# list of prime numbers between n and m
flag = 0
n = int(input("n: "))
m = int(input("m: "))
print("list of primes:")
for i in range(n, m + 1):
    for j in range(2, (i // 2) + 1):
        if i % j == 0:
            flag = 1
    if flag == 0:
        print(i, end=' ')
    flag = 0


# transposing a matrix
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
matrix1 = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
print("matrix:", matrix)
for i in range(3):
    for j in range(4):
        matrix1[j][i] = matrix[i][j]
print("transposed: ", matrix1)


# 1 2 3 4
num = 10
i = 1
while i <= num:
    if i % 5 == 0:
        break
    print(i)
    i = i + 1


# wap to chk no. is divisible by 5 or not
for num in range(1, 10):
    if num % 5 == 0:
        break
    else:
        print(num)


# print odd numbers from 1 to 10
for num in range(1, 10):
    if num % 2 == 0:
        continue
    print(num)  # will only print odd no. from 1 to ten

# 1 2    4 5 6 7 8 9
i = 0
while i < 9:
    i += 1
    if i == 3:
        continue
    print(i)  # print 1 to 9 except 3


# 11 to 19
for num in range(1, 20):
    if num <= 10:
        continue
    print(num)  # 11 to 19


# pass statement
a = 10
b = 20
if a < b:
    pass
else:
    print("a>b")


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # sequence loop
for num in numbers:
    if num % 2 != 0:
        pass
    else:
        print(num)


vowels = "aeiouAEIOU"
while True:
    char1 = input("vowel,or 9 to quit")
    if char1.isalpha() or char1 == "9":
        if char1 == "9":
            break
        if char1 in vowels:
            print("vowel")
        else:
            print("not vowel")  # terminate if given 9
    else:
        print("Wrong input")


# random module

import random

# randomly give any letter
seq = 'abcdefghijk'
print(random.choice(seq))

# randomly give any digit
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(random.choice(l1))

import random


l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
random.shuffle(l1)
print(l1)

import random

# give any int in this range
output = random.randint(1, 100)
print(output)

for i in range(10):
    random.seed(10)



print(random.randint(1, 100))

print(random.random())

print(random.randrange(2, 10))

print(random.randrange(2, 10, 4))

import math

print(math.floor(2.9))

print(math.ceil(2.1))

print(math.fmod(43.50, 4.5))

print(math.fabs(-12.9))  # same for -12 too--12.0

print(math.factorial(50))  # dont use negative number ,,C++ cant do,its compiler fail here

print(math.gcd(12, 16, 32))  # cant give 0

print(math.trunc(45.678))

# Lecture 24.
import math

print(math.exp(2))
print(math.log(5))
print(math.log10(5))
print(math.pow(2, 3))
print(math.sqrt(16))
print(math.sin(math.radians(30)))
print(math.cos(math.radians(0)))
print(math.tan(math.radians(45)))
print(math.hypot(3, 4))
print(math.radians(1))  # degree to radian
print(math.degrees(1))  # radian to degree

print(math.pi)
print(math.e)
print(math.tau)
print(math.inf)

x = -12
print(abs(x))
x = 12.50
y = 12.51
z = 12.49
p, q, r = 12.345, 34.897, 33.8376
print(round(x), round(y), round(z))
print(round(p), round(q), round(r))

x = 7
y = 3.45
z = 7.8j
p = "abcd"
print(isinstance(x, int))  # boolean
print(isinstance(y, int))
print(isinstance(z, complex))
print(isinstance(p, str))

'''
Unit-2 completed.
'''

'''
    unit 3
               '''


def display():
    print("hello everyone ")
    print("we are learning functions")


display()
display()
display()
 
for i in range(5):
    display()

i = 0
while i < 5:
    print("hello everyone we are learning functions")
    i = i + 1

import math


def add(a, b):
    print(a + b)


def prod(a, b):
    print(a * b)


def sub(a, b):
    print(a - b)


def mod(a, b):
    print(a % b)


x = int(input("first value:"))
y = int(input("second value:"))
add(x, y)
sub(x, y)
prod(x, y)
mod(x, y)


def add(a, b):
    return a + b


def prod(a, b):
    return a * b


def sub(a, b):
    return a - b


def mod(a, b):
    return a % b


x = int(input("first value:"))
y = int(input("second value:"))
print(add(x, y))
print(sub(x, y))
print(prod(x, y))
r1 = mod(x, y)
print(r1)


def factorial(n):
    fact = 1
    if n < 0:
        print("negative no.")
        exit()
    elif n == 0:
        print("factorial is", 1)
        exit()
    else:
        for i in range(1, n + 1):
            fact = fact * i
        return fact


x = int(input("enter no."))
r1 = factorial(x)
if r1 % 3 == 0:
    print("it is multiple of 3 and result is", r1)


def countingdigits(n):
    count = 0
    while n != 0:
        count = count + 1
        n = n // 10
    return count  # n and count are local variables , only loop knows about it


x = int(input("enter no."))  # x is global variable recognized by everyone
r1 = countingdigits(x)
print("count of digits is ", r1)
print("count of digit is", countingdigits(x))


def example(a, b, c):
    return a + 1, b + 1, c + 1


r1, r2, r3 = example(1, 2, 3)
print(r1, r2, r3)
print(example(1, 2, 3))  # Returns tuple.


def countingvowelsspaces(str1):
    vcount = 0
    scount = 0
    for i in str1:
        if i in "aeiouAEIOU":
            vcount += 1
        elif i == " ":
            scount += 1
    return vcount, scount


r1, r2 = countingvowelsspaces("hello everyone")
print(r1, r2)


# #positional arguements

def studentinfo(name, rollno, fees):
    print("name:", name, "rollno", rollno, "fees", fees)
    print("fees", fees)
    print("rollno", rollno)


studentinfo("abc", 321, 32.43)
studentinfo(32, "suresh", 32.23)
studentinfo(rollno=13, name="anuj", fees=45000)  # keyword arguement


# positional arguements

def studentinfo(*, name, rollno, fees):
    print("name:", name, "rollno", rollno, "fees", fees)
    print("fees", fees)
    print("rollno", rollno)


# studentinfo("abc",321,32.43)# wont work for *,--positional arguement
# studentinfo(32,"suresh",32.23)# wont work for *,--positional arguement
studentinfo(rollno=13, name="anuj", fees=45000)  # keyword arguement

# FOR ARBITRARY ARGUEMENTS
def example(*args):
    for i in args:
        print(i, " ", end="  ")
    print()


example(1, 2)
example(10, 12, 13)  # *arg would work in positional argument
example(108, 109, 200, 300, 400)


def example(*args):
    sum = 0
    for i in args:
        sum = sum + i
    print("sum is", sum)
    print()


example(1, 2)
example(10, 12, 13)
example(108, 109, 200, 300, 400)


# positional arbitrary arguement
def example(*args):
    sum = 0.0
    for i in args:
        sum = sum + i
    print("average is ", sum / len(args))


s11, s12, s13 = eval(input("enter marks of first section"))
s21, s22, s23, s24, s25 = eval(input("enter marks of second section"))
s31, s32, s33, s34, s35, s36, s37 = eval(input("enter marks of third section"))

example(s11, s12, s13)
example(s21, s22, s23, s24, s25)
example(s31, s32, s33, s34, s35, s36, s37)


# keyword arguements

def example(**kwargs):
    for i, j in kwargs.items():  # i will take key, j will take value
        print(i, ":", j, end=" ")
    print()


example(a="pqr", b="stu")  # can give a , b and c only one time
example(a="aaa", b="bbb", c="ccc", d="ddd")
example(a="abc", b="def", c="ghi")


# display only those pairs in which value starts with p

def example(**kwargs):
    for i, j in kwargs.items():
        if j[0] == "p":
            print(i, ":", j, end=" ")
    print()


example(a="pqr", b="stu")  # can give a , b and c only one time
example(a="aaa", b="bbb", c="ccc", d="ddd")
example(a="abc", b="def", c="ghi")


# easier way

def example(**kwargs):
    print(kwargs)  # cant access particular value


example(a="pqr", b="stu")  # gives dictionary
example(a="aaa", b="bbb", c="ccc", d="ddd")
example(a="abc", b="def", c="ghi")


def example(**kwargs):
    for i in kwargs:
        print(i, ":", kwargs[i], end=" ")
    print()


example(a="pqr", b="stu")  # can give a , b and c only one time
example(a="aaa", b="bbb", c="ccc", d="ddd")
example(a="abc", b="def", c="ghi")


'''
    unit 3
               '''

def display():
    print("hello everyone ")
    print("we are learning functions")

display()
display()
display()

for i in range (5):
    display()
i=0
while i<5:
    print("hello everyone we are learning functions")
    i=i+1

import math

def add(a,b):
    print(a+b)


def prod(a,b):
    print(a*b)

def sub(a,b):
    print(a-b)

def mod(a,b):
    print(a%b)



x=int(input("first value:"))
y=int(input("second value:"))
add(x,y)
sub(x,y)
prod(x,y)
mod(x,y)


def add(a,b):
    return a+b


def prod(a,b):
    return a*b

def sub(a,b):
    return a-b

def mod(a,b):
    return a%b



x=int(input("first value:"))
y=int(input("second value:"))
print(add(x,y))
print(sub(x,y))
print(prod(x,y))
r1=mod(x,y)
print(r1)


def factorial(n):
    fact=1
    if n<0:
        print("negative no.")
        exit()
    elif n==0:
        print("factorial is",1)
        exit()
    else:
        for i in range(1,n+1):
            fact=fact*i
        return fact

x = int(input("enter no."))
r1=factorial(x)
if r1%3==0:
    print("it is multiple of 3 and result is",r1)


def countingdigits(n):
    count=0
    while n!=0:
        count=count+1
        n=n//10
    return count# n and count are local variables , only loop knows about it

x=int(input("enter no."))# x is global variable recognized by everyone
r1=countingdigits(x)
print("count of digits is ",r1)
print("count of digit is",countingdigits(x))

def example(a,b,c):
    return a+1,b+1,c+1

r1, r2, r3 = example(1, 2, 3)
print(r1,r2,r3)
print(example(1, 2, 3)) # Returns tuple.



def countingvowelsspaces(str1):
    vcount=0
    scount=0
    for i in str1:
        if i in "aeiouAEIOU":
            vcount+=1
        elif i==" ":
            scount+=1
    return vcount,scount

r1,r2=countingvowelsspaces("hello everyone")
print(r1,r2)


# #positional arguements

def studentinfo(name,rollno,fees):
    print("name:",name,"rollno",rollno,"fees",fees)
    print("fees",fees)
    print("rollno",rollno)

studentinfo("abc",321,32.43)
studentinfo(32,"suresh",32.23)
studentinfo(rollno=13,name="anuj",fees=45000)#keyword arguement


#positional arguements

def studentinfo(*,name,rollno,fees):
    print("name:",name,"rollno",rollno,"fees",fees)
    print("fees",fees)
    print("rollno",rollno)

# studentinfo("abc",321,32.43)# wont work for *,--positional arguement
# studentinfo(32,"suresh",32.23)# wont work for *,--positional arguement
studentinfo(rollno=13,name="anuj",fees=45000)#keyword arguement


def example(*args):
    for i in args:
        print(i , " ", end="  ")
    print()

example(1,2)
example(10,12,13)# *arg would work in positional argument
example(108,109,200,300,400)



def example(*args):
    sum=0
    for i in args:
        sum=sum+i
    print("sum is",sum)
    print()

example(1,2)
example(10,12,13)
example(108,109,200,300,400)

#positional arbitrary arguement
def example(*args):
    sum=0.0
    for i in args:
        sum=sum+i
    print("average is ",sum/len(args))


s11,s12,s13=eval(input("enter marks of first section"))
s21,s22,s23,s24,s25=eval(input("enter marks of second section"))
s31,s32,s33,s34,s35,s36,s37=eval(input("enter marks of third section"))

example(s11,s12,s13)
example(s21,s22,s23,s24,s25)
example(s31,s32,s33,s34,s35,s36,s37)

# keyword arguements

def example(**kwargs):
    for i,j in kwargs.items():# i will take key, j will take value
        print(i,":",j,end=" ")
    print()
example(a="pqr",b="stu")# can give a , b and c only one time
example(a="aaa",b="bbb",c="ccc",d="ddd")
example(a="abc",b="def",c="ghi")

#display only those pairs in which value starts with p

def example(**kwargs):
    for i,j in kwargs.items():
        if j[0]=="p":
            print(i,":",j,end=" ")
    print()
example(a="pqr",b="stu")# can give a , b and c only one time
example(a="aaa",b="bbb",c="ccc",d="ddd")
example(a="abc",b="def",c="ghi")

#easier way

def example(**kwargs):
    print(kwargs)# cant access particular value

example(a="pqr",b="stu")# gives dictionary
example(a="aaa",b="bbb",c="ccc",d="ddd")
example(a="abc",b="def",c="ghi")


def example(**kwargs):
    for i in kwargs:
        print(i,":",kwargs[i],end=" ")
    print()
example(a="pqr",b="stu")# can give a , b and c only one time
example(a="aaa",b="bbb",c="ccc",d="ddd")
example(a="abc",b="def",c="ghi")

""" unit 3 lecture - 3,4"""

x=lambda a:a+10
print(x(5)) # give 15

x=lambda a,b:a*b
print(x(5,6))
# area of circle
area=lambda r: 3.14*r*r
print(area(2.3))

x= lambda a,b,c:a+b+c
print(x(5,6,2))

def myfunc(n):
    return lambda a: a*n

m1=int(input("enter no.: "))
m2=int(input("enter no.: "))#mydoubler takes value of lambda
mydoubler=myfunc(m1)# a=a*m1
print(mydoubler(m2))# m1=m1*m2

tax= lambda salary:salary*20/100
salary=int(input("salary: "))
print("tax to be paid: ",tax(salary))

doublenum= lambda x:x*2
a=int(input("a: "))
print(doublenum(a))

def addition(n):
    return n+n
numbers=(1,2,3,4)
result=(map(addition,numbers))#iterable
print(list(result))# returns [2(1+1),4(2+2),6(3+3),8(4+4)]

# can also use for i in result:
   # print(i)

def area(n):
    return 3.14*n*n
radius=(2,4,6,8)
result=(map(area,radius))
print(list(result))

# create map of factorial and reverse of number
# generate multiplication table
# suum of diff naturla numbers limits
#
# doubling number using other method

numbers=(1,2,3,4)
result=map(lambda x: x+x ,numbers)
print(list(result))

radius=(3,4,5,6)
result=map(lambda x: 3.14*x*x,radius)
print(list(result))

numbers1=[1,2,3]
numbers2=[4,5,6]
result=map(lambda x,y:x+y,numbers1,numbers2)
print(list(result))

p=(3000,4000,5000,6000)
r=(4,5,6)
t=(2,3,4)
result=map(lambda x,y,z:(x*y*z)/100,p,r,t)# p,r and t are iterables
print(list(result))

for i in result:
    print(i)

def fun(variable):
    letters=['a','e','i','o','u']
    if variable in letters :
        return True
    else:
        return False

seq=['g','e','e','j','k','i','s','p','r']
filtered=filter(fun,seq)
print(list(filtered))

def fun(dig):
    if dig%2==0:
        return True
    else:
        return False

seq=[2,3,4,5,6,7,8,9,0]
filtered=filter(fun,seq)
print(list(filtered))


seq=(2,3,4,5,6,7,8,9)

result=filter(lambda x: x%2!=0,seq)
print(list(result))

seq=(2,3,4,5,6,7,8,9)

result=filter(lambda x: x%2==0,seq)
print(list(result))

#list comprehension

l1=[1,2,3,4]
l2=[x*x for x in l1]
print(l2)# work like map function

fruits=['apple','banana','pineapple','kiwi','mango','orange']
newlist=[x for x in fruits if 'a' in x]
print(newlist)

l1=[1,2,3,4]
l2=[x*x for x in l1 if x%2==0]
print(l2)#gives 4 and 16
seq=(2,3,4,5,6,7,8,9)

result=filter(lambda x: x%2==0,seq)
print(list(result))


# find common elements
a=[1,2,3,5,7,9]
b=[2,3,6,7,9,8]
result=filter(lambda x: x in a,b)
print(list((result)))
print(list(x for x in a if x in b))

# variable defined under function is local variable.
# only statement inside func can access local variable.
# local variables automatically destroy after execution.
# created in stack frame,,destroyed after execution.
# stack frame--LIFO last in first out.
# stack is like library stack.
# size of stack is limited and size of heap is huge.



'''  unit-3 --- next lecture '''

globvar="hello"
def test1():
    global globvar
    globvar="good morning"


def test2():
    globvar = "good evening"


print(globvar)
test1()
print(globvar)
test2()
print(globvar)#no effect



x=10
def example1():
    x=20

def example2():
    global x
    x=x+1

def example3():
    global x
    x=x+2

example1()
example2()
example3()
print(x)# gives 13 bcoz x=20 is not considred


a=int(input())
def changeglobal():
    global a
    a=200
def changelocal():
    a=500
    print("local value",a)

print(a)
changeglobal()
changelocal()
print(a)


# define two func seprately and use one func as arguement to other func

a=15
def square(a):
    a=a*a
    return a
def double(a):
    a=a*2
    return a

def divby5(a):
    b=(a%5==0) # can also use if and else here
    return b
num=int(input("n: "))
print(square(double(a)))
print(divby5(square(double(num))))

 #  function composition
 # positional arguement
# returning func from func
#
def compose(*functions):
    def inner(arg):
        for f in reversed(functions):
            arg=f(arg)
        return arg
    return inner
def square(x):
    return x**2
def increment(x):
    return x+1
def half(x):
    return x/2

composed=compose(square, increment, half)
print(composed(5)) #square(increment(half(5)))
composed=compose(square,increment)
print(composed(5))

#factorial using recurssion

def recurfact(n):
    if n==0 or n==1:# base caase
        return 1 #single value--looking to wrap up recursion
    else:
        return n*recurfact(n-1)# recursive case
"""  5*recurfact(4)[24]
----4*recurfact(3)[6]
---3*recurfact(2)[2]
--2*recurfact(1)
----2*1
---n=1
,returning 1 --base case achieved,
recursion stops......"""
num=int(input(""))
if num<0:
    print("fact doesnot exist")
else:
    print(recurfact(num))

# display sum of n natural no.(repeated sum)((recursion))

def recursum(n):
    if n==1 or n==0:
        return n
    else:
        return n + recursum(n-1)

n=int(input("enter num:"))
if n<0:
    print("enter positive num")
else:
    print(recursum(n))

# reverse using recurssion

def recurrev(n,x):
    if n == 0 :
        return x
    else:
        x = (x*10) + (n%10)
        return recurrev((n//10),x)

num=int(input("x: "))
print(recurrev(num,0))

# fibonacci

def fibb(n):
    if n<=1:
        return n
    else:
        return (fibb(n-1) +fibb(n-2))

for i in range(0,10):
    print(fibb(i), end=" ")

# sum of digits of number using recursion
# count digits of number using recursion
# prime or composite chk using recursion
# armstrong no. check using recursion

"""  unit 3 is overr-- only till lesson-7 ,, 9 to 13 not in syllabus"""


























"""   Unit -- 4.   """

a="Hello"
c="Python"
print(a[0])# H
print(a[-1])# o
print(a[0:4])#
print(a[0:3])#
print(a[0:])#
print(a[::1])#
print(a[::-1])#
print(c[-1::-3])#Gives nt
print(c[4:1:-1])
print(c[4:1:1])# not logical, incorrect way of giving step
print(c[2:5:-1])# not logical





b="This is my first string"

print(b)
print(b[11])# positive indexing
print(b[-6])# negative indexing

lang="Python"
print(lang[0:])# gives python
print(lang[:6])# gives python



str="How are you?"



print("string is",str)

print(str[4:7])# are
print(str[2:5])# w a
print(str[-4:-1])# you
print(str[-2:-5:-1])# uoy
print(str[-4:])# you?


str=input("str: ")

if len(str)<3:
    print("output:",str)
else:
    print("output:",str[:2]+str[-2:])

str1=input("str:")

print(str1[1:-1])# gives ytho of python

a=input("str: ")

if len(a)==1:
    print(a)

elif len(a)==0:
    print("None")
else:
    print(a[-1]+a[1:-1]+a[0])



a=input("")
b=input("")

print(a+b+b[::-1]+a[::-1])# HELLOWORLD=HELLOWORLDDLROWOLLEH


str=input("str:")
num=int(input("num:"))

if num>=len(str) or num<0:
    print("num should be positive , less than length of str")
elif num<len(str):
    print(str[:num]+str[num+1:])# remove numberth character from string


str1=input("str1: ")
str2=input("str2: ")

print(" "+str1[1:]+str2[1:] + " ")

if len(str1[1:] + str2[1:])==0:
    print("null")





"""  Unit-4 ----- lecture 2,3. """
#
# Membership operator
# work as per UNICODES
a="Good morning"

print( "n" in a)
print("Good" in a)
print("morning" in a)
print("z" in a)


# repetition of strings

a="Mouse"

print(3*a)

b=3

print(((b-2)*2)*a)

# Question--

a=str(input("str: "))

print(4*a)

print(3*a[::-1])

a=str(input("str: "))

if len(a)>=3:
    print(3*a[:3])
else:
    print(a)


a=str(input("str: "))
b=int(input("times: "))

print(a*b)



# print str till nth index n times

a=str(input("str:"))
b=int(input("num:"))

if b<=len((a)):
    print(b*a[:b])

elif b<0 or b>len(str):
    print("num should be  +ve")

# # # strings-immutable,cant update--slice+concate

str="python"
str[0]="j" # not possible
del str[0] # not possible



# prints error-- a is not defined
a="hello"
del a  # deletes entire string
print(a)




# # In string python  to replace p with j remove p first and than add j externally..



# # in build string methods class name + dot operator

str="helLo welcOme tO Python"

print(str.capitalize())# only for first letter

print(str.upper())# capitalize every word

print(str.lower())

print(str.title())# capitalize frst letter of every word

print(str.swapcase())# upper to lower and lower to upper

print(str.split())# break string and make list of words

print(str.split("m"))# break string into 2 (left side of m and right side of m) and make list

# center(width,"fillchar")
# hello=====10-len of hello(5)=5


a="10,20,30,40"

print(a.split(","))


a="Hello"
b="Python"
print(a.center(10,"&"))
print(b.center(8,"@"))

a="heppy married life birthday birthday baby."

print(a.count("birthday"))#print 2

print(a.count("a"))

# # make definitions of functions dong in class
#

a="java is simple"
print(a.replace("java","python"))
print(a.replace("are","you"))
c="@"
print(c.join(a))

b="."
l1=["www","codetantra","com"]
print(b.join(l1))# convert list to string


#slide 47--homework
a="Python is great"
print(a.isupper())# boolean
print(a.islower())# boolean
print(a.isalpha())# false because of space and alpha=alphabets

c="hello programmer"

print(c.isalpha())
b="hello123"
print(b.isalpha())

a="245nfdgf"

print(a.isalnum())


a="245n fdgf"

print(a.isalnum())


a="245nfdgf@"

print(a.isalnum())

a="123"
print(a.isdigit())

a="233245tgf"
print(a.isdigit())

a="536"
print(a.isdigit())

a="         "

print(a.isspace())

a="  54  "

print(a.isspace())

a="Hello World"
print(a.istitle())

a="Hello python"
print(a.istitle())

# # escape characters=never printed=/n--new line and /t--tab space

a="hello\npython"
print(a)
print("hello\tpython")

print('It\'s very powerful')

print("It's very powerful")

print("hello \" everyone")# if u want to print " between string

print("hello\\how are you")

print("")
# # repr==representation func==to print \n as it is

str=("hello\tpython\npython is very intresting")
print(str)

print(repr(str))# print str as it is


print(r"hello\tpython\npython")#formating flags--nullify impact of backslash
print(R"hello\tpython\npython")

# # can also use \n\t together

a=str(input("str1:"))
b=str(input("str2:"))
if len(a)>len(b):
    print(b+a+b)
elif len(b)>len(a):
    print(a+b+a)
else:
    print("strings are of same length")

a="hello world"
print(a.startswith("h"))#boolean
print(a.startswith("he"))
print(a.startswith("hello"))
print(a.startswith("hey"))
print(a.endswith("d"))
print(a.endswith("ld"))
print(a.endswith("n"))
print(a.find("ld"))# not boolean,integer
print(a.find("o"))
print(a.find("java"))# gives -1==element/substring not found

b="hello python hello"
print(a.find("he"))# 0
print(a.find("hi"))# -1

# # len(a) work in dict tuple or anything

a="hello world"
print(min(a))# space=32
print(max(a))# w

a=str(input(""))
print(a[-12:-1])
if a[0:6]=="python" and a[-11:-1]=="programming":
    print("valid")
if str.startswith("Python") and str.endswith("programming"):
    print("valid")

# # string MOdule-like math module

import string

print(string.punctuation)
print(string.digits)
print(string.printable)# escape sequences not visible
print(string.capwords('hello python'))# work like title function
print(string.hexdigits)
print(string.octdigits)

# # slide 70 dry running --do urself print result after removing all punctuations

a=str(input("str: "))
b=str(input("str: "))
print(a.count(b))

# # make def of it slide 72

str=str(input(""))
for i in str:
    print(i*2,end="")

str=str(input(''))
result=" "
for i in str:
    result=result+2*i
print(result)

str=str(input("str"))
a=len(str)
b=a//2
if a%2==0:
    print(str[:b])
else:
    print(str[(b)+1:])


#    home workkkk



def find_char(a,b):
    i=0
    count=0
    while i < len(a):
        if b==a[i]:
            count=count+1
        i=i+1
    return count

a=str(input("str1: "))
b=str(input("str2: "))
print(find_char(a,b))


"""  Unit -4, lecture--4,5... """


str1=str(input("str: "))
fstr=""
sstr=""

if len(str1)==1:
    print(str1)
elif len(str1)==0:
    print("null")

for i in range(0,len(str1)):
    if i%2==0:
        fstr=fstr+str[i]
    else:
        sstr=sstr+str[i]

print("first: ",fstr)
print("second: ",sstr)
print("orignal: ",str)

# incremental order a=key===,k=k,e=ke,,y=key

a=str(input("str: "))
result=""
for i in range (0,len(a)+1):# first picl 1 chr than 2 chr than 3 chr
    result=result+a[:i]
print(result)


# \n and \t are non printable

a="rehan434 "
print(a.isprintable())
b="cfjdjvnxcmvlkf\nlanguage"
print(b.isprintable())

print("rehanmittal".isalpha())

print("\n".isalpha())


# very important

import string
print("Character\tASCII Code")
for i in string.ascii_letters:
    print(i,"\t\t",ord(i))

#  frequency

str1=str(input("str: "))
str3=sorted(str1)
printed=[]
for i in str3:
    if i not in printed:
        print("'{0}'\t{1}".format(i,str3.count(i)))

        printed.append(i)

print(printed)

a=str(input("str: "))
printed=[]
for i in a:
    if i not in printed:
        print(i,a.count(i))
        printed.append(i)



""" lesson 1 and 2 are completed"""

"""  next chapter--list. """

# List= Mutable,updatable,removable,addable.
# ordered means indexed
# 1d list- 1 list ,,2d list--list inside list ,,, array==2d and 3d

l1=[]
print(type(l1))

l2=list((1,2,3,4,5))# tuple converted to list
print(l2)
print(type(l2))

# converting string to list

a=str (input(""))
print(type(a))
b=(a.split(" "))
print(b)
print(type(b))# list

a=str (input(""))
print(type(a))
b=(a.split(","))
print(b)
print(type(b))

# item assignment=assignment updation
# item indexed deletion can be done in list,not in string

l1=[1,2,3,4]
l2=[4,3,2,1]
print(l1==l2)# false

l1=[1,2,3]
l2=[1,2,3]
print(l1==l2)# True

a=[1,2,3]
print(a*-1)# empty list

a=[1,2,3,4]
print(a*3)
print(a*0)
print([]*3)
# there is nothing like null list

#Recurssion: base case not designed properly--stack overflow can happen








data=str(input("data: "))
list1=data.split(",")
print(list1)
index=int(input("index: "))
if index < len(list1) and index>=(-(len(list1))):
    print("index: ",list1[index])
else:
    print("invalid")














char=["a","b","c","d"]
char[3]="xyz"
char.append("rehan")
char.append([1,2,3,4])
char.append(["e","f"])
print(char)
print(char[5][2])

# to add more than 1 item


char=["a","b","c","d"]
list2=[1,2,3]
char.extend(list2)
print(char)

l1=["hi","hello","lists"]
print(l1[0])
print(l1[1])
print(l1[2])
l1[2]="Python"
print(l1)
l1.append("Code is life")
print(l1)
l1.extend([45,67,98])# can add only 1 parameter
print(l1)

data=input("data: ")
element=input("element: ")
l1=data.split(",")
print(element in l1)

data=input("")
list1=data.split(",")
for i in range(0,len(list1)):
    list1[i]=int(list1[i])
if list1[0]==3 or list1[-1]==3:
    print("true")
else:
    print("false")

a=[1,2,3,4,5,6]
a[0:3]=[100,10,1]# updating through slicing
print(a)
a[0:3]=[]# remove frst 3 elements
print(a)
a[0:0]=[1,2,34,56,7]# inserts new values at start
print(a)
a[1:1]=[123,456,7]# insert new values at second place
print(a)


data=input("data: ")
l1=data.split(",")
print("before updating:",l1)
index=int(input("ind:"))
element=input("element: ")
l1[index]=element
if index<len(l1) and index >= (-len(l1)):
    print("affter updation: ",l1)
else:
    print("invalid")



data=input("data: ")
l1=data.split(",")
print(l1)
first=l1[0]
last=l1[-1]
max1=max(first,last)
print("largest among first,last elements: ",max1)





#############################################""" Unit-4 lecture-6,7. """#######################################################3

# Aliasing,,, deep copy
a=[1,2,3,4,5,6]
b=a# can create total 3 names
c=b
d=c
print(d)
print(c)
print(a)
print(b)
print(b is a)
print(a is b)
a[0]=100
print(a)
print(b)


# # cloning ==diff memory addresa,,shallow copy
#
# empty slice cloning
a=[1,2,3,4,5]
b=a[:]
print(a is b)# false
print(a)
print(b)
a[0]=100
print(a)# value updated
print(b)# value dont updATE


a=[1,2,3,4,5,6]
b=list(a)
print(a)
print(b)
a[0]=100
print(a)
print(b)



a=[1,2,3,4,5,6]
b=a.copy()
print(a)
print(b)
a[0]=100
print(a)
print(b)


d1=input("data1: ")
d2=input("data2: ")
l1=d1.split(",")
l2=d2.split(",")
if l1[-1]==l2[-1] or l1[0]==l2[0]:
    print(True)
else:
    print(False)
# print(l1[0],l1[-1] == l2[0],l2[-1])


a=10
b=20
print((a,b)==(10,20))

d1=[1,2,3,4,5,6,78,9]
print(d1)
del d1[5]# 5th index wala
print(d1)
del d1[2:]
print(d1)
del d1# memory refrence is dlted
print(d1)# error

d1=[1,2,3,4,5,6,78,9]
print(d1)
del d1[5]
print(d1)
del d1[2:]
print(d1)
d1.clear()# memory refrence is not dlted
print(d1)# empty list,, no error

d1=[1,2,3,4,3,5]
print(d1)
# deletes frst occurence of element only
d1.remove(3)# 3 remove hua
print(d1)
d1.remove(1)
print(d1)

#there is diff bw null and 0 use loop+membership operator to remmove every "same" element

# pop pop pop pop
# not only dlt but also return element  it is dlting
# delete  last element by default

l1=["red","yellow","cyan"]
elem=l1.pop()
print(elem)
print(l1)
elem1=l1.pop(-1)
print(elem1)
print(l1)# pop is vry imp,,even asked in interviews,,pushing and poping (dlt topmost element in stack) elements in stack
#
# slide 56
#

""" Unit-4 lecture-8,9.. """
#

# removing duplicates in a list

d1=input("")
l1=d1.split(",")
l2=[]
for i in range(len(l1)):
    if l1[i] not in l2:
        l2.append(l1[i])

print(l1)
print("after removing duplicates:",l2)



print(all([" ",",","1","2"]))# true
print(all([]))# true
print(all([0,1,2]))# false
print(all([False,1,2]))

print(any([]))
print(any([0,0,0]))
print(any([1,0,False]))

print(list(enumerate(["a","b","c","d","e"]))) # function composition (enumerate inside list )
# enumerate by default gives (index,value) tuples


# function chaining
a=input().split()


print(list("abcdef"))# [a,b,c,d,e,f]
print(list((1,2,3,4,5,"a","d")))

print(max([1,2,3,4,5,6,7]))
print(min([1,2,3,4,5,6,7]))

# array is collection of elements of same type
# study about its algorithm---bubble sort (sinking sort)


# cant print sorted directly ,never make change in list

orignal=[1,2,3,4,54,3,2,1]
sorted=sorted(orignal)
print(sorted)
print(sorted[::-1])

print(sum([1,2,3,4,21,3,5,6,7,5,34,32,5435,2]))# wont work in hetrogeneous data

# split gives list of strings
# we want integer == use int function for i in range(size):     l1[i]=int(l1[i])


data=input("")
l1=data.split(",")
size=len(l1)
for i in range(size):
    l1[i]=int(l1[i])

print(max(l1))
print(min(l1))
print("diff:",(max(l1) - min(l1)))


# construct dict out of data1 and data2

data1=input("")
data2=input("")
l1=data1.split(",")
l2=data2.split(",")
str1="{"
if len(l1)==len(l2):
    for i in range (len (l1)):
        str1=str1+"'"+l1[i]+"'"+":"+l2[i] +"'"+","
    print(str1[0:len(str1)-1]+"}")
else:
    print("lists are different lengths")

# subtracting elements of l2 from l1

data1=input("")
data2=input("")
l1=data1.split(",")
l2=data2.split(",")
size1=len(l1)
size2=len(l2)


if len(l1)==len(l2):
    for i in range(size1):
        l1[i]=int(l1[i])
    for i in range(size2):
        l2[i]=int(l2[i])
    l3=[]
    for i in range(0,size1):
        l3.append(abs(l1[i]-l2[i]))
    print(l3)
else:
    print("Lists are of different lengths")


l1=[1,2,3,4,5,6]
l1.insert(3,"abd")
print(l1)
l1.insert(len(l1),"e")
print(l1)
l1.insert(1,"rehan")
print(l1)


# insertion never overwrite data, shift data if inserting in between
# last index =len(a)-1
# inserting at -1 inserts at last second index
# overwriting means replacing

a=["a","b","d","a","f","g","a"]
b=a.count("a")
print(b)

# sorted dont make changes in orignal list
# sort also arranges characters as per ascii


x=["1","A","a","b","B","c","C"]
x.sort()
print(x)
x.sort(key=None,reverse=True)# descending order,if reverse=FALSE, returns ascending order
print(x)# prints reverse of sort()
x.sort(key=None,reverse=False)
print(x)
# these func make permanent changes
# # descending order and reversing is diff thing

x=[2,35,2,46,5,7,8,6,4,6,7]
x.reverse()
print(x)


# remember parameter type and return type
# transversing with == operator

data1=input("data1: ")
l1=data1.split(",")
size1=len(l1)
for i in range(size1):
    l1[i]=int(l1[i])
    a= l1.count(i)
count=0
element=int(input("element:"))
for i in range(0,len(l1)):
    if l1[i]==element:
        count=count+1
print(element,"occurs",count,"times")

# study about binary search

# if element next to x is also x print true

data=input("data: ")
l1=data.split(",")
print("list:",l1)
size1=len(l1)
for i in range(size1):
    l1[i]=int(l1[i])
find=int(input("find: ") )
for i in range(0,len(l1)-1):
    if l1[i]==find:
        if l1[i+1]==find:
            result= "true"
            break
    else:
        result ="false"


print(result)
# seq of elements=i ,data=j
data=input("data: ")
seq=input("seq of elements: ")
l1=data.split(",")
l2=seq.split(",")
size1=len(l1)
size2=len(l2)
for i in range(0,len(l1)):
    l1[i]=int(l1[i])

for i in range(0,len(l2)):
    l2[i]=int(l2[i])
count=0
for i in range(len(l2)):
    for j in range(len(l1)):
        if l1[i]==l2[i]:
            count+=1
            break# inner loop stops
if count==len(l1):
    print("exist")
else:
    print("doesnt exist")



# slide 85



""" Unit - 4 lecture--10,11"""

# write letters AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz

capA=input("Enter A: ")
smalla=input("Enter a: ")
i=ord("A")# 65
j=ord("a")# 97
list1=[]
for k in range(26):# 0 to 25 (total digits=total alphabets=26)
    list1.append(chr(i))
    list1.append(chr(j))
    i+=1
    j+=1

print(list1)

# check if list is sorted or not

data=input("data: ")
l1=data.split(",")
for i in range(len(l1)):
    l1[i]=int(l1[i])
if l1==sorted(list(l1)):
    print(True)
else:
    print(False)


data=input("Please enter the sentence: ")
str2=data.lower()
str3=sorted(str2)
printed=[]
for char in str3:
    if char not in printed:
        if char.isalpha():
            print(char,"\t",str3.count(char))
            printed.append(char)


"""  bye bye list  """
"""  hello tuplee   """

# tuple ==cant change/modify data==cant add,dlt,update elements==immutalbe list

a=(1,2,3,6,45)
print(a)
print(type(a))  # tuple
b=list(a)
print(b) # list
print(type(b))
c=tuple(b)
print(c) # tuple
print(type(c))

# tuple are faster than list bcoz it is not allowed to change
# preffered over list to have data write protected
# operations==read(cant change data) and write(can change data)
# preffered for keys ,,keys of dict are like tuples and also we cant dlt key alone,key vallue pair dlts,value changes,key dont change
# we can have list as item in tuple and can update it

t1=(1,2,3,[4,5],6)
print(t1)
t1[3][0]=42
print(t1)

# t1[0]=100 ,, error--tuplee does not support item assignment

# pop name came from popcorn

tuple1=(1,2,3,"hello",4)
print(tuple1)
print(type(tuple1))
print(list(tuple1))
print(type(list(tuple1)))



mytuple=("I","love","Python")
print("Given tuple: ",mytuple)
list1=list(mytuple)
print("After converting to list: ",list1)
list1[1]="practice"
print("list after chnging element",list1)
print("converting tuple to list: ",tuple(list1))



# make program so that teacher can see grid item and when clicked shows thumbnail and when i see the thumbnail of namit it should open it.

t1=("a",)# tuple it is just string without comma
print(t1)
print(type(t1))# tuple
print(t1[0])
print(t1[0])

# can use concatenation and repetetion on tuple,,mutable in it

data=input("data: ")
l1=data.split(",")
t1=tuple(l1)
print("list: ",l1)
print("tuple: ",t1)
ind=int(input("index: "))
# positive/zero index and negative index verification
if ind>=(-len(l1)) and ind<len(l1):
    print("element: ",t1[ind])
else:
    print("Index out of range")



t1=("this",10.0,"is","float",3.6)
print(t1[0])
print(t1[1])
print(t1[-1])
print(t1[0:])# all
print(t1[0:-1])# all except last
print(t1[::-1])


# tuple assignment
l1=["python","is","fun"]
a,b,c=l1
print(a)
print(b)
print(c)

(a,b,c)=(1,2,3)
print(a)
print(b)
print(c)

# filter take def function or lambda function as frst parameter

# (1,2,3)>(1,0,3)#return true as 1>1 or 2>0 or 3>3 is true
# tuple(_dict) gives only keys of dict
# works like logical or operator



data=input("data: ")
l1=data.split(",")
value=int(input("value:"))
t1=tuple(l1)
print("tuple*value: ",t1*value)
data1=input("data2: ")
l2=data1.split(",")
t2=tuple(l2)
print("concatenated: ",t1+t2)


# quick revision sheets unit 1,2,3,4 --Homework 3pages per chptr and make repository of all the chptrs done in class


#daniel lang ,,reema thareja ,, ppts

#~ tilde symbol --one"s comppliment


data=input("'data: ")
l1=data.split(",")
t1=tuple(l1)
print("tuple:",t1)
val=input("val:")
if val in t1:
    print("True")
else:
    print(False)

# we can dlt tuple but not its elements
# we can delete list element in tuple

tuple=(1,2,3,4,5,6,7,8,[4,5,6,7,4,6])
del tuple[8][3]
print(tuple)
del tuple
print(tuple)



data=input("data: ")
l1=data.split(",")
t1=tuple(l1)
index=int(input("index: "))
if index<len(l1) and index>=-len(l1):
    value=int(input("value:"))
    l1[1]=value
    print(tuple(l1))
else:
    print("Enter valid index")



data=input("data: ")
l1=data.split(",")
t1=tuple(l1)
index=int(input("index: "))
l2=[]
if index<len(l1) and index>=-len(l1):
    value=int(input("value:"))
    l2=list(t1)
    l2[index]=value
    t2=tuple(l2)
    print(t2)
else:
    print("Enter valid index")






# bharat reddy precisure oriented programming using c


""" unit 4 lec 12,13 ,,tuple lec-2"""

# remove indexth element
data=input("data: ")
l1=data.split(",")
t1=tuple(l1)
print("tuple: ",tuple(l1))
ind=int(input("index: "))

if ind!=-1:# will get extra output in case if run it directly (t1[:-1]+t1[-1+1:]) try dry running for ind=0

    if ind>=-len(t1) and ind<len(t1):
        print(t1[:ind] + t1[ind + 1:])
    else:
        print("enter valid index")
else:
    print("after removing:",t1[:ind])


# to chk if two tuples arre equal ==no. of elements.,seq of element,elements itself


#  to dlt an element A from tuple
data=input("data: ")
l1=data.split(",")
element=(input("element:"))

t1=tuple(l1)# save orignal copy of tuple to display in output
print("before deletion: ",t1)

if element in l1:
    l1.remove(element)
    t2=tuple(l1)
    print("after deletion: ",t2)
else:
    print("enter existing element")


# chk it once
data=(input('data: '))
l1=data.split(",")
t1=tuple(l1)
si=int(input(""))
ei=int(input(""))
if (si<len(l1) and ei<len(l1)) and (ei>=len(l1) and si>=len(l1)):
    print(t1[si:ei])
else:
    print("invalid index")

print(all((" ",",","1","2")))# any in tuple

print(all([]))# true

print(any([]))# false

print(all(()))# true

print(any(()))# false


x=(1,2,3,4,5,6)
print(tuple(enumerate(x))) # tuple

# question mark have some ascii code
# null string have 0 (false) ascii code

print(any(('','','',''))) # false bcoz

print(ord("0")) # 48

print(tuple("abcedf"))

# count how many times element is occuring
data=input("")
l1=data.split(",")
t1=tuple(l1)
print("tuple: ",t1)
element=input("element: ")
if element in t1:
    counter=t1.count(element)
    print(counter)
else:
    print("enter valid element")



# index element==take input of element and returns its index for frst time
# to know index of a element in tuple

data=input("data: ")
l1=data.split(",")
t1=tuple(l1)
print(t1)
element=(input("element: "))
if element in t1:
    index=t1.index(element)
    print(index)
else:
    print("enter existing element")












""" Unit-4 lec-14,15 After tuples, dictionary lec-1. """

# dict--unordered(codetantra) collection of (key:value) pairs--latest version of python--ordered before python 3.7--unordered
# key is immutable and value is mutable
# key must be unique,never duplicate,example registration num,,2 values can have same key
# dict is mutable ,can add and update key value pair,,cant chng key ,,we can dlt key value pair together,,cant dlt only key or only value
# syntax==key:value,,,bracket==curly
# key==immutable and unique--str,num and tuple
# list cant be key bcoz list is mutable,value can be list
# we only go for tuple in which list is not present
#

# always pass list of tuple as paramter to form dict==key,value

d={"jan":3,"feb":2,"may":4}
print(d)
print(type(d))

d1=dict([("one",1),("two",2),("three",3)])
print(d1)

print(d1['one'])
print(d1.get("one"))
# enumerate help to create dict and generate tuples


d1={"nepal":"kathmandu","india":"newdelhi",}
print(d1["nepal"])
print(d1.get("india"))
print(d1.get("srilanka"))# more handy  gives None

# print(d1["srilanka"])# gives key error

d1={2:100,1:100}
print(d1[2])
print(d1[1])


d1={"nepal":"kathmandu","india":"newdelhi",}
print(d1.get("australia","not available"))


# to print dict one by one


dict1={"name":"jay","number":"514","age":12}

# i take values of key
for i in dict1:
    print(i,dict1[i])

for i,j in dict1.items():
    print(i,j)

print(dict1.keys())# return keys in form of list
print(dict1.values())


# updating dict=====doubt





dict1={"name":"jay","number":"514","age":12}
print(dict1)
dict1["jay"]="rehan"
print(dict1)


# conversion is tough--need to use zip method

keys=input("data1: ")
values=input("data2: ")
l1=keys.split(",")
l2=values.split(",")
mydict=dict(zip(l1,l2))# zip creates pairs of tuples,if use zip directly,get memory address
print(mydict)
print(sorted(mydict.items()))# items method list of pair of tuples and sorted method sort dict as per key
print(list(zip(l1,l2)))
print(set(zip(l1,l2)))
print(tuple(zip(l1,l2)))
print(dict(zip(l1,l2)))

r=zip(l1,l2)
print(r)# gives memory address


# cant concatenatee two dicts


d1={1:2,3:4}
d2={6:7,8:9}
d1.update(d2)
print(d1)# method to concatenate dict




keys=input("data1: ")
values=input("data2: ")
l1=keys.split(",")
l2=values.split(",")
d1={}
if len(l1)!=len(l2):
    print("length should be equal")
else:
    for i in range(len(l1)):
        d1[l1[i]]=l2[i]
    print(sorted(d1.items()))# returns[(key,value),(key,value)]


data1=input("data1: ")
data2=input("data2: ")
l1=data1.split(",")
l2=data2.split(",")
mydict=dict(zip(l1,l2))
key=input("key: ")
if key in mydict:
    print("value:",mydict[key])
else:
    print("value:",mydict.get(key,"None"))

# # membership chk
data1=input("data1: ")
data2=input("data2: ")
l1=data1.split(",")
l2=data2.split(",")
mydict=dict(zip(l1,l2))
key=input("key: ")
if key in mydict:# checks only keys
    print(True)
else:
    print(False)

# always use sorted with dict1.items()
data1=input("data1: ")
data2=input("data2: ")
l1=data1.split(",")
l2=data2.split(",")
mydict=dict(zip(l1,l2))

for key, value in sorted(mydict.items()):
    print(value,key)


data1=input("data1: ")
data2=input("data2: ")
l1=data1.split(",")
l2=data2.split(",")
mydict=dict(zip(l1,l2))
for key,value in sorted(mydict.items()):
    print(value,"->",key)


# pop in dict take 1 argument(key) and that particular entry will be dlted.
# pop.item dlt last key value,dlt randomly any key value pair prior to python3.7

fruits={1:"apple",2:"orange",3:"mango",4:"grapes"}
print(fruits)
print(type(fruits))
print(fruits.pop(4))
print(fruits)
print(fruits.popitem())
print(fruits)
del fruits[2]
print(fruits)
fruits.clear()
print(fruits)

# del fruits
# print(fruits)==gives name error
# popitem work same as pop of list

#
data1=input("data1: ")
data2=input("data2: ")
l1=data1.split(",")
l2=data2.split(",")
mydict=dict(zip(l1,l2))
key=input("key: ")
if key in mydict:
    print("value:",mydict.pop(key))
    srtd=sorted(mydict.items())
    print((srtd))
else:
    print("key does not exist")


data1=input("data1: ")
data2=input("data2: ")
l1=data1.split(",")
l2=data2.split(",")
mydict=dict(zip(l1,l2))
# sort apply on list
l1=[]
for key in mydict:
    l1.append(mydict[key])
l1.sort()
print("min:",l1[-1])
print("min:",l1[0])


data1=input("data1: ")
data2=input("data2: ")
l1=data1.split(",")
l2=data2.split(",")
mydict=dict(zip(l1,l2))
key=input("keY: ")
if key in mydict:
    value=input("value: ")
    mydict[key]=value
    print("soted dict:",sorted(mydict.items()))
else:
    print("Key does not exist")

# # slide 42



""" Unit-4 lec-16,17 dictionary lec-2. """


# all() return true if all keys are true,,True in empty dict too,, empty list gives true


dict1={}
print(all(dict1)) # true
print(any(dict1)) # false
print(all({1:2,3:4,5:6,6:9})) # "" gives false,," " gives true empty or zero key gives false
print(any({"":2,2:5}))# true

# len counts key value pairs
# sorted returns only dict keys in sorted order,,dict.items() returns both
# sorted never make changes in data structure

# zip 2 times using(l1,l2) and(l2,l1)
data1=input("data1: ")
data2=input("data2: ")
l1=data1.split(",")
l2=data2.split(",")
mydict=dict(zip(l1,l2))
d3={}
# inserting new key value pair in dict
for key in mydict:
    d3[mydict[key]]=key
print("before exchange:",sorted(mydict.items()))
print("after exchange:",sorted(d3.items()))



troupe={("cleese","john"):[1,2,3],
        ("chapman","graham"):[4,5,6],
        ("idle","eric"):[7,8,9],
        ("jones","terry"):[10,11,12],
        ("gilliam","terry"):[13,14,15,16,17,18],
        ("palin","michael"):[19,20]}# ascending order of second name

for first,second in sorted(troupe):
    print(second,first,troupe[first,second])

# add keys of common value


data1=input("data1: ")
data2=input("data2: ")
l1=data1.split(",")
l2=data2.split(",")
for i in range (len(l1)):
    l1[i]=int(l1[i])
for i in range (len(l2)):
    l2[i]=int(l2[i])

data3 = input("data3: ")
data4 = input("data4: ")
l3= data3.split(",")
l4= data4.split(",")
for i in range (len(l3)):
    l3[i]=int(l3[i])
for i in range (len(l4)):
    l4[i]=int(l4[i])

dict3={}
dict2=dict(zip(l3,l4))
for key in list(dict1.keys())+list(dict2.keys()):
    dict3[key]=dict1.get(key,0)+dict2.get(key,0)
print(sorted(dict3.items()))



# element is key and its freq is its value
# count se bhi kar sakte hain

seq=input("seq: ")
l1=seq.split(",")
for i in range(len(l1)):
    l1[i]=int(l1[i])
t=tuple(l1) # not mandatory
d1={}

for i in t:
    if i not in d1:
        d1[i]=1# makes i:1
    else:
        d1[i]+=1

print("sorted dict: ",sorted(d1.items()))


# chk existence of key
l1=input("data1: ").split(",")
l2=input("data2: ").split(",")
l3=input("data3: ").split(",")
l4=input("data4: ").split(",")
d1=dict(zip(l1,l2))
d2=dict(zip(l3,l4))

key=input("")
if key in d1.keys() and key in d2.keys():
    print("present in both")
elif key in d1.keys():
    print("present in frst")
elif key in d2.keys():
    print("present in second")
else:
    print("key not present")

#
l1=input("data: ").split(",")
l2=input("data2: ").split(",")
d1=dict(zip(l1,l2))
d2=dict(zip(l2,l1))
for key,value in sorted(d1.items()):
    print(key,value)

# object oriented programming unit-5 ,,unit6--file handling,exception handling

for key,value in sorted(d2.items()):
    print(key,value)

# clear(_)--to verify len()=0
# aliasing-deep copy,,cloning--shallow copy
# copy()

d1={"mango":1,"apple":2,"banana":3,"grapes":4}
d1.setdefault("apple",10)# get method and updating, will not change value of 10,,returns 2
print(d1)
d1.setdefault("pappaya",5)# add pappaya:5 to dict
print(d1)
d3 = {1:"a",3:"b",5:"c"}
d5 = {1:"d",6:"e",8:"f"}
print(d3.update(d5))# concatenates and updates value of existing keys
d1.clear()
print(len(d1))

# make definitions of all the functions of dict
seq=("one","two","three")
dict=dict.fromkeys(seq,10)# creates dict with all having values 10
print(str(dict))


# # we need to convert zip to data structure
l1=[10,20,30]
print(tuple(zip(l1)))
# zip always return iterator
t1=(1,)
print(set(zip(t1)))

# atleast 2 parameters are required for zip function

""" Unt--4 , lAsT chapter,,Sparse matrix """

# list comprehensions- introduced in python2.0
# map() and filter() and reduce()
# syntax==[expression for an item in iterate if condition]
# [x for x in item if x in a]

l1=[]
for i in range(1,11):
    l1.append(i)
print(l1)

print([i for i in range(1,11)])# 1 to 10 ki list
print([i**2 for i in range(1,10)])# 1 to 9 ke square ki list
print([i**2 for i in range(1,10) if i%2==0])# 1 to  ke square ki list agar number even hai

# else nhi lga skte list comprehension me


n=10
print(["even" if (n%2==0) else "odd"]) # even

n=11
print(["even" if (n%2==0) else "odd"]) # even # try without sq brackts

str1=str(input(""))
print([x for x in str1])# list of words of string
print([x*2 for x in str1])


# document is class and getelementbyid is a class
# diff between alert and prompt bus,its bydefault-string,
# z index-konsi chiz upr ani chaie,,photo or anything






""" list comprehensions and Sparse Matrix lecture -2 """

# total marks--920 in codetantra, marks start to count from day 27
# nested list comprehension

x=[a*b for a in [1,2,3] for b in [10,20,30]]
print(x)
# map take every element . filter take slected elements
# taking duplicate element . can do nested if also,,they are nested list comprehension

x=[a for a in [10,8,5,4] for b in [4,7,5,10] if a==b]# works as filter--10,5,4,,try a!=b
print(x)

# nested if --frst chk if i%2==0 than chk i%3==0

x=[x for x in range (50) if x%2==0 if x%3==0]
print(x)

# Matrix in Python is Nested list.

matrix=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
transposed=[]
# nested while--
i=0
while i<len(matrix[0]):# len of 1,2,3,4==4,, i=0,1,2,3
    j=0
    lx=[]# temporary matrix ,,keeps initializing row by row
    while j<len(matrix):# no. of sublists==3
        lx.append(matrix[j][i])# indexes switched [0][0]=1,,[1][0]=5,,[2][0]=9
        j+=1# [0][1]=2  [1][1]=6   [2][1]=10
    transposed.append(lx)
    i+=1
print(transposed)

# nested for
# for row in matrix:,,row=[1,2,3,4],,row[0]=1, # frst appends 1, than 5, than 9

matrix=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
transposed=[]

for i in range(len(matrix[0])):
    transposed_row=[]
    for row in matrix:
        transposed_row.append(row[0])
    transposed.append(transposed_row)
print(transposed)


# Single list comprehension

matrix=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
transposed=[]

for i in range(len(matrix[0])):
    transposed.append([row[i] for row in matrix])# picks 1,5,9
print(transposed)# temporary list not required bcoz it itself gives list
#
matrix=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]# double list comprehension,,is not loop inside loop
transposed=[[row[i] for row in matrix]for i in range (len(matrix[0]))]
print(transposed)

# multiplication of matrix need 3 loops,,very very difficult in list comprehension
# matrix multiplication using nested for ,, addition, subtraction, division, and modulus
# sum of diagonal elements [row and column number are same]


l1=input("data: ").split()
x=[int(x) for x in l1]
print(x)

x=[int(x) for x in input("data: ").split()]
print(x)


# study sparse matrix,,do dry running




"""
        list comprehensions and Sparse Matrix lecture -3
                                                              """

# dictionery comprehensions

# # introduced in python 3 ,, we are using python 3
# # {key:value for key,value in iterable}
# # iterable--seq/any data structure

l1=[10,20,30,40]

x={ key : value for key,value in enumerate(l1) }
# expression/entry==key:value
print(x)# gives 0:10 ,1:20, 2:30, 3:40

# set comprehension is not there in syllabus


d2={i:i**2 for i in range(1,11)}
print(d2)# 1:1, 2:4, 3:9, 4:16
#
d1={k:"python" for k in "codetantra"}# dont take 1 key more than once ,,t comes only one time
print(d1)# comes in order,,,wrong in code tantra

d2={ i.lower():i for i in "PYTHON" }
print(d2)# p:P,y:Y..............

d1={x:chr(x) for x in range(65,91) }
d2={x:y for y,x in d1.items() }
print(sorted(d1.items()))
print(sorted(d2.items()))


# 50% submission, 51 to 100%,Total marks=920,Percentage will be decided out of 40
# 3 days left, 30x3=90 marks are deducted



# sparse matrix--- no need to waste time and space on 0 elements,,
# sparse matrix contains 3 lists/rows
# [[Row numbers for all non zero elements],[column numbers for all non zero elements],[list of all non zero elements]]
# 3 at (0,3),,4 at (0,5) ,, 7 at /(1,4) , 2 at (3,2) ,, 6 at (3,3)..........
# 0 0 3 4
# 0 0 5 0
# 0 0 0 0
# 0 2 6 0
#
# 2 0 0
# 0 1 0--ans would be [0,1][1,1][2,1]

# sparse matrix cbt 2 me nhi ayega




# Sparse Matrix Representation using lists

def sparseMatrix(sparseMatrix, m, n):
    # initialize size as
    size = 0
    for i in range(m):
        for j in range(n):
            if (sparseMatrix[i][j] != 0):
                size += 1

# number of columns in compressMatrix(size) should
# be equal to number of non-zero elements in sparseMatrix
    rows, cols = (3, size)
    compressMatrix = [[0 for i in range(cols)] for j in range(rows)]

    k = 0
    for i in range(m):
        for j in range(n):
            if (sparseMatrix[i][j] != 0):
                compressMatrix[0][k] = i
                compressMatrix[1][k] = j
                compressMatrix[2][k] = sparseMatrix[i][j]
                k += 1

print("Sparse representation:")
for i in compressMatrix:
    print(i)

m = int(input("Enter row size: "))
n = int(input("Enter col size: "))
print("Enter elements:")
mat = [[int(input()) for x in range (n)] for y in range(m)]
print("Sparse matrix is:")
for i in range(m):
    for j in range(n):
        print(mat[i][j],end = " ")
    print()
sparseMatrix(mat, m, n)


# chapter 5
# class and objects
#

# c languages with classes became c++,it is number 1 in term of competitive coding,very fast and efficient
# python is best for machine learning
# java is product of oracle now,,
# java is completely object oriented, cant write program without class,,main class and entry class
# python--fuunctional and seasonal,, object oriented
# <class "int">
# bache be like:-
# robut gophore ,,c++ ki official book
# bala goswami
# apne notes
# python came in 1992(official version)
# Guido van Rossum
# Bhailog language
# python--very userfriendly language
# behind the door will be exposed soon,,
# &a--ampercent a
# #


""" classes and objects lecture 2 """


class Car:
	__engineno = "EK1"
	__modelno = "VX6"
	def setcarinfo(self, engineno, modelno):
		self.__engineno = engineno
		self.__modelno = modelno
	def getcarinfo(self):
		print(self.__engineno, self.__modelno, self.color, self.year)
hondacity = Car()
engnumber = input("engine number: ")
hondacity.setcarinfo(engnumber, "SX6")
hondacity.color = "Blue"
hondacity.year = "2018"
hondacity.getcarinfo()
# # print(hondacity.__modelno)



# # class represent encapulation, abstraction (projector/lamp is working or not is area of concern,
# # no concern about how projector is working )and data hiding (hiding background detail and showing essential details) comes under encapulation
# # we know math modules, classes are also available,,we try to save things at background in object orieted programming
# # keep class def in seprate file and use it is abstraction
# # class is known as abstract data type but not in python
# # data hiding--by default, members of class are public,accessible inside as well as outside class,, use __ to make private (attribute)member,accessible only in class
# #
#
# # class is a keyword,name-ur choice,(rules of identifier)
# # name should start with capital letter, naming convention but not mandatory
# # define attributes of class, outside-- only in python,, all other language cant have empty class
# # <object_name=constructor(),,constructor is special method that have same name as that of class,,if dont define
# # internal constructor will be called automatically,,constructor initialise member of class
# # Assignment statements are requierd to initialize attribute of class
# # object is created using constructor
# # object is instance of class
# # object help to call behaviour
# # __init__==name of constructor in python,, when create object --only write constructor()
# # constructor is called when object is created,,constructor name=name of class
# # student type variable
# # class name acting as user defined datatype
# # x=9 inbuilt datatype,,userdefined datatype==student()
# # empployee type datatype()
# # objects are created but not linked to attribute or methods but can be created
class Student:# class=collection of attribute and methods
	pass
Stud_1 = Student()
Stud_2 = Student()
Stud_1.name = input('s1 name: ')# 3 instance attributes of class
Stud_1.age = int(input('s1 age: '))# can alsso make 5 attributes for 1st and 2 attributes for 2nd,, but dont do ,, what is point of making template than??
Stud_1.graduate = input('s1 degree: ')# 2 objects--student_1 and 2
Stud_2.name = input('s2 name: ')# <objectname>.(dot attribute)<attribute>
Stud_2.age = int(input('s2 age: '))
Stud_2.graduate = input('s2 degree: ')
print("Stud_1.name:", Stud_1.name)
print("Stud_1.age:", Stud_1.age)
print("Stud_1.graduate:", Stud_1.graduate)
print("Stud_2.name:", Stud_2.name)
print("Stud_2.age:", Stud_2.age)
print("Stud_2.graduate:", Stud_2.graduate)


# # defining own constructor,inside constructor-defining attributes,, also using class attribute
# # every method of class have frst parameter self--. self is parameter that have address of object , itself behavee as pbject ,refers to current object
# # class-student,,x is attribute(class attribute-have common value of all objects),
# # instance attributes--inside constructor def--created using def
# # name , age and email are local variables after self (name,age,email)
# # name age and email after .self are attributes
# # name that we will pass get passed to name attribute
# # self and dot work as inbuilt object -used to distinguish among attribute and local variables of class if they have same name
# # in constructor, always init is written
# # instance attributes--name age and email of self.name.........
# # memory--
#  stud_1  |   stud_2
# name     |    name
# age      |    age
# email    |   email,,     initialized via init
# # constructor initialize values and calls object automatically
# #
class Student:
	x=12
	def __init__(self, name, age, email):# taking 3 parameters,self automatically get passed
		self.name = name# self behave as student_1 and name age email are initialized for him
		self.age = age
		self.email = email

# program execution start here
Stud_1 = Student('SriRam', 25, 'ram@sch.com')
Stud_2 = Student('Lakshman', 28, 'laks@sch.com')
print('Stud_1 details =', Stud_1.name, Stud_1.age, Stud_1.email,Student.x)# x is class attribute,,accessible via class name and dot operator
print('Stud_2 details =', Stud_2.name, Stud_2.age, Stud_2.email,Student.x)# becoz they are common to all objects,,studnt.x gives 12 becoz x is given value 12
# #
# # this program doesnt enforce data hiding,prograns are accesed outside too

# # # how to access private --access them inside same class like def showdetails
class Student:
	__x=12# class attribute
	def __init__(self, name, age, email):# taking 3 parameters,self automatically get passed
		self.__name = name# self behave as student_1 and name age email are initialized for him
		self.__age = age# instance attribute
		self.__email = email
    def showdetails(self):
        print(self.__name,self.__age,self.__email, self.__x)
# program execution start here
Stud_1 = Student('SriRam', 25, 'ram@sch.com')
Stud_2 = Student('Lakshman', 28, 'laks@sch.com')
print('Stud_1 details =', Stud_1.name, Stud_1.age, Stud_1.email,Student.x)# x is class attribute,,accessible via class name and dot operator
print('Stud_2 details =', Stud_2.name, Stud_2.age, Stud_2.email,Student.x)
Stud_1.showdetails()
Stud_2.showdetails()
#
# # no constructor,have normal methods--for setting details and get regno.
# # def __init__(self):
#         self.att=NONE
# #         self.att2=None # default constructor
# # obj=car()# no need to pass self,, automatically accesses self
class Car:
	def setDetails(self, model, regno):# 2 parameters
		self.model = model# 2 instance attributes
		self.regno = regno# 3 methods and behaviours
	def getModel(self):
		return self.model
	def getRegno(self):
		return self.regno# can return also and print also
Hyundai = Car()# objects--hyundai and maruti
Maruti = Car()# internal/do nothing constructor working here,, we can overwrite it too
model1 = input('car1 model: ')
regno1 = input('car1 regno: ')
model2 = input('car2 model: ')
regno2 = input('car2 regno: ')
Hyundai.setDetails(model1, regno1)# extra step, bcoz constructor not used
Maruti.setDetails(model2, regno2)
print("Hyundai car details:", Hyundai.getModel(), Hyundai.getRegno())
print("Maruti car details:", Maruti.getModel(), Maruti.getRegno())
# # constructor--2 types---default and parameterized
# #

#
#
# from turtle import *
# color("red")
# begin_fill()
# pensize(10)
# left(50)
# forward(133)
# circle(50,200)
# right(140)
# circle(50,200)
# forward(133)
#
#
#
#
# class computer:
#     def __init__(self):
#         print("init")
#     def config(self):
#         print("1tb 256gb ryzen5")
#
#
# com1=computer()# init wala to object initialize hote hi ayga hi ayega!!!chahe call kr ya nhii
#
# omen=computer()
# computer.config(omen)
#
#
# omen.config()# config pass omen to self by default
# class computer:
#     def __init__(self,cpu,ram):
#         print("init")
#         print(cpu,ram)
#     def config(self):
#         print("1tb 256gb ryzen5")


# com1=computer("i5",17)# means com1,i5,17  # init wala to object initialize hote hi ayga hi ayega!!!chahe call kr ya nhii


# # len(l) is function whereas l1.append(1) is method










""" objects and classes lecture 3"""

# ex 4,2 and 3 are done
# ex 5 do urself

class Student:
	def __init__(self, name, age, email):
		self.name = name# instance attributes,local variables/parameters
		self.age = age# self is inbuilt place holder
		self.email = email#

name = input("s1 name: ")
age = int(input("s1 age: "))# init is only present in python,,init=initialization-

Stud_1 = Student(name, age, 'arya@gmail.com')# object creation,, calling of contructor,, without writing init here,,

# when we do student.getdetail(),, this extra step  is not needed in init

name = input("s2 name: ")
age = int(input("s2 age: "))# data hiding--  __ is used

Stud_2 = Student(name, age,'geetha@gmail.com')

print('Stud_1.name:', Stud_1.name)
print('Stud_2.name:', Stud_2.name)

class Student:

    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def studentDetails(self):
        print("name:", self.name, ", age:", self.age, ", email:", self.email)

name = input("name: ")
age = int(input("age: "))
email = input("email: ")
s1 = Student(name, age, email)
s1.studentDetails()# printing using method(function) rather than constructor


class Person:
    def setName(self, name):
        self.name = name
    def getName(self):
        return self.name
p1 = Person()
p2 = Person()
name1 = input('p1 name: ')
name2 = input('p2 name: ')
p1.setName(name1)
p2.setName(name2)
print("p1 name:", p1.getName())# create one instance attribute x and create method to return factorial or fibonacci series
print("p2 name:", p2.getName())# setter and getter # written inside print bcoz return is written in def


# very important
# polynorphism-appearance of one thing in multiple forms
# method overloading,,split(",")--overloading
# default parameters--value already assigned,, if pass value, get overwritten
class Greeting:

	def sayHello(self, name = None, wish = None):# only else will work without name and wish
		if name is not None and wish is not None:
			print ('Hello' + name + wish)# functionality 1
		elif name is not None and wish is None:
			print ('Hello' + name)# functionality 1
		else:
			print ('Hello')# functionality 1,, only 1 work at time
greet = Greeting()
# Call the method with zero, one and two parameters
greet.sayHello()#else
greet.sayHello('Ram')#elif
greet.sayHello('Ram,', 'Good Morning!!!')#if


# overload func area,area,triangle,and circle--3 parameters


# parameters are varied via default parameters and conditioons in overloading
#
#
# Inheritance
# acquring features of one class in other class--reuasability
# no need to write features from scratch again n again
# 1.(single/simple inheritance)-1 base clas and 1 derived class(super and sub in java),,
# 2.(multiple inheritance): more than 1 independent base classes --1 derived class
# project1+project 2 ki features in project 3
# 3.(heirarchial inheritance)-1 base class, multiple derived classes.
# 4.(multi level inheritance:)grandparent-parent-child
# 5.(hybrid inheritance):complex: combination of more than 1 type of inheritance
#
# in BMS , customer class  will be inherited in almost every class
# UML-unified modeling language--give class diagrams--read about it....
# (syntax):
#

class Car:
	def setenginemodel(self, engine):# method
		self.engine = engine
	def getenginemodel(self):# method
		print(self.engine)
class Honda(Car):
	def setcarmodel(self, model):
		self.model = model
	def getcarmodel(self):
		print(self.model)
# print(self.engine) is also possible
mycar = Honda() # always create object of derived class
mycar.setenginemodel('EK-1')# reusability
mycar.setcarmodel('V6')
print('Car Details:')
mycar.getenginemodel()# reusability
mycar.getcarmodel()


class Person:
    def setname(self, name):
        self.name = name
    def getname(self):
        print(self.name)

class Student(Person):
    def setage(self, age):
        self.age = age
    def getage(self):
        print(self.age)

name = input("Please enter a name: ")
age = int(input("Please enter age: "))
s1 = Student()
s1.setname(name)
s1.setage(age)
s1.getname()
s1.getage()


# inheritance always use "is-a" relationship,,[student is-a person]

# # Multiple inheritance
class Car:
    def setenginemodel(self, engine):
        self.engine = engine
    def getenginemodel(self):
        print(self.engine)
class Tyre:
    def settyrenumber(self, num):
        self.num = num
    def gettyrenumber(self):
        print(self.num)
class Honda(Car, Tyre):
    def setcarmodel(self, model):
        self.model = model
    def getcarmodel(self):
        print(self.model)
accord = Honda()
accord.setenginemodel('EK-1')
accord.setcarmodel('V6')
accord.settyrenumber(236)
print('Car Details: ')
accord.getenginemodel()
accord.getcarmodel()
accord.gettyrenumber()

# kal file handling hoga
# parso file handling khtam
# fir excepion handling or regular expression
class Car:
	def setenginemodel(self, engine):# method
		self.engine = engine
	def getenginemodel(self):# method
		print(self.engine)
class Tyre:
	def settyrenumber(self, num):# method
		self.num = num
	def gettyrenumber(self):# method
		print(self.num)
class Honda(Car, Tyre):# mutltiple inheritance#comma is operator used in it-- mutltiple inheritance
	def setcarmodel(self, model):
		self.model = model
	def getcarmodel(self):
		print(self.model)
accord = Honda()
accord.setenginemodel('EK-1')
accord.setcarmodel('V6')
accord.settyrenumber(236)
print('Car Details: ')
accord.getenginemodel()
accord.getcarmodel()
accord.gettyrenumber()


class Person:
	def setname(self, name):
		self.name = name
	def getname(self):
		print(self.name)
class Student(Person):
	def setage(self, age):
		self.age = age
	def getage(self):
		print(self.age)
class Address(Student):# multilevel inheritance,,most derived class
	def setaddress(self, address):
		self.address = address
	def getaddress(self):
		print(self.address)
s1 = Address()# object of most/newly derived class
s1.setname('SriRam')# s1 is object that can call any method/function
s1.setage('19')
s1.setaddress('Hyderabad')
s1.getname()
s1.getage()
s1.getaddress()



# Python program to demonstrate Hierarchical inheritance

# Base class
class Parent:
	def func1(self):
		print("This function is in parent class.")

# Derived class1
class Child1(Parent):# inherit integer to 2 diff classes, factorial in one, reverse in second
	def func2(self):
		print("This function is in child 1.")

# Derivied class2
class Child2(Parent):
	def func3(self):
		print("This function is in child 2.")


# Driver's code
object1 = Child1()
object2 = Child2()# number of objects = number of derived classes
object1.func1()
object1.func2()
object2.func1()
object2.func3()




class vehicle:
	'''General Vehicle class'''
	def __init__(self, name, price, regno):
		self.name = name
		self.price = price
		self.regno = regno
class car(vehicle):# heirarchial+multiple
	''' Class car inherits from Vehicle'''# derived class constructor take responsiblity of initializing member of base class constructor
	# hover pass value to car and car pass  it to base class constructor

	def __init__(self, name, price, regno, gear):
		self.name = name
		self.price = price
		self.regno = regno# sirf gear dalne ke liye baki 3 bhi dalne padege
		self.gear = gear
class boat(vehicle):
	''' Class boat inherits from vehicle'''
class hover(car, boat):
	'''Class hovercraft inherits from both car and boat'''
c1 = car('toyota', 1500000, 'car2121', 'auto')
b1 = boat('maruti', 1000000, 'boat0121')# pass only to vehicle, no relation with car
h1 = hover('toyota', 1500000, 'hover1212', 'manual')# car or boat dono k feature leti h# car  pe gya fir vehicle pe gya
print(type(c1).__name__, "\t", c1.name, "\t", c1.price, "\t", c1.regno, "\t", c1.gear)
print(type(b1).__name__, "\t", b1.name, "\t", b1.price, "\t", b1.regno, "\t")
print(type(h1).__name__, "\t", h1.name, "\t", h1.price, "\t", h1.regno, "\t", h1.gear)
print(c1.__doc__)








# # super is implicit inbuilt object object tht try to

class Person:
    # Constructor
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def display(self):
        print("Name is:",self.name," and Id is:",self.id)

class Emp(Person):
    def __init__(self, name, id,salary):
        super().__init__(name, id)# super act as object of base class
        self.salary=salary

    def output(self):
        print("Salary is:",self.salary)

Emp_details = Emp("Suresh", 101,23000)
Emp_details.display()
Emp_details.output()# constructor chaining

# # #
# # #
# # #
# # #
# # #
# Python program to demonstrate method overriding
# Defining parent class


class Parent:
    # Parent's show method
    def show(self):# method of same signature
        print("We are in base class")

# Defining child class
class Child(Parent):# why overriding ?? -  only definition is changed,method name is same
    # Child's show method
    def show(self):# hiding concept is overriding,, base class version never execute, only in case if object=parent()
        print("We are in derived class")

# Driver's code
obj1 = Parent()
obj2 = Child()# base class ka version hidden h, child wala hi chlega bs
obj1.show()
obj2.show()




# Python program to demonstrate method overriding
# Defining parent class


class Parent:
    # Parent's show method
    def show(self):# method of same signature
        print("We are in base class")

# Defining child class
class Child(Parent):# why overriding ?? -  only definition is changed,method name is same
    # Child's show method
    def show(self):# hiding concept is overriding,, base class version never execute, only in case if object=parent()
        print("We are in derived class")

# Driver's code
obj1 = Parent()
obj2 = Child()
obj1.show()
obj2.show()


#  # how to make private members

class Car:
    def setbrandname(self, brandname):
        self.brandname = brandname
    def getbrandname(self):
        print(self.brandname)
    def setmodel(self, model):
        self.model = model
    def getmodel(self):
        print(self.model)

class Accord(Car):
    def setbrandname(self, brandname):
        self.brandname = brandname
    def getbrandname(self):# overriden
        print(self.brandname)

obj = Accord()
brandname = input('brand: ')
modelname = input('model: ')
obj.setbrandname(brandname)
obj.setmodel(modelname)# accord(car) is working
obj.getbrandname()
obj.getmodel()



# Write Python code here
# # attribute outside of all blocks and methods - class attribute
# #
class sampleclass:
    count = 0  # class attribute
    def increase(self):
        sampleclass.count += 1# try self.count
        #self.count += 1

# Calling increase() on an object
s1 = sampleclass()
s1.increase()# count=1
print(s1.count)
# Calling increase on one more object
s2 = sampleclass()# count is same for both s1 and s2 # will target same prev value # count =
s2.increase()# count = 2
print(s2.count)# 2
print(sampleclass.count)# final val of count = 2



f=open("dmeofile.txt","w")# w mode-file dont exist than created
# if exist than existing data gets erased
f.write("Hello world")
f.close()# new file gets created(check ur left side in abc folder)


obj=open("dmeofile.txt","w")
obj.write("my first entry")
obj.close()

obj=open("dmeofile.txt","w")
str1=input("str: ")
obj.write(str1)
obj.close()
#
obj=open("dmeofile.txt","r")#
print(obj.read())
obj.close()# also prints it in console# write any content in there

obj=open("dmeofile.txt","a")# # addds new data in the end
str1=input("str: ")
obj.write(str1)
obj.close()
import random
outfile = open("Numbers.txt", "w")
for i in range(10):
	outfile.write(str(random.randint(0, 9)) + " ")# 0 and 9 also included, randrange-last value not considered
outfile.close()
infile = open("Numbers.txt", "r")
s=infile.read()
numbers=[eval(x) for x in s.split()]# see data and convert to relevant type
for number in numbers:
	print(number,end=' ')
infile.close()

import random
f=open("dmeofile.txt","w")
x=random.randint(1,10)
for i in range(1,11):
	f.write("{}x{}={}\n".format(x,i,x*i))

f.close()


import random
num=random.randint(1,9)
obj=open("multiplication.text","w")
for i in range(1,11):
    res=num*i
    val=

#
import random
num=random.randint(1,9)
obj=open("multiplication.txt","w")
for i in range(1,11):
    result=num*i
    value=str(num)+"X"+str(i)+"="+str(result)
    obj.write(value)
    obj.write("\n")
obj.close()
obj=open("multiplication.txt","r")
print(obj.read())




count=0
obj=open("source.txt","w")
str1=input("Enter file data...")
obj.write(str1)
obj.close()
obj=open("source.txt","r")
data=obj.read()
for char in data:
    if char=='a' or char=='e' or char=='i' or char=='o' or char=='u' or char=='A' or char=='E' or char=='I' or char=='O' or char=='U':
        count+=1
obj.close()
obj=open("Target.txt","w")
obj.write(str(count))



# # take string input, write data in file, open file, read data, count no. of vowels, write count in another file
#
# import random
# #
# f=open("dmeofile.txt","w")
# str1=str(input("str: "))
# f.write(str1)
# f.close()
# f1=open("dmeofile.txt","r")
#
# for i in range(len(str1)):
#     vcount=0
#     vowels="AEIOUaeiou"
#     if str1[i] in vowels:
#         vcount+=1
#     # f1.write(str(vcount))
#
# f.close()
# f2=open("dmeofile.txt","w")
# f2.write(str(vcount))
# f2.close()


""" file handling lec-2 """

# Program to show various ways to read and
# write data in a file.
file1 = open("myfile.txt","w")
L = ["This is Delhi \n","This is Paris \n","This is London \n"]

# \n is placed to indicate EOL (End of Line)
file1.write("Hello \n")
file1.writelines(L)# write multiple lines in file, 4 lines are written
file1.close() #to change file access modes

file1 = open("myfile.txt","r+")# r+ = read and write, have power of read mode only, if file dont exist,cant create it but w mode create it too

print("Output of Read function is ")
print(file1.read(5))# read only 5 characters from file,if we write 10,no. of chr printed are 8 bcoz (space+\n) takes 2 bytes
print()

# seek(n) takes the file handle to the nth byte from the beginning.
file1.seek(0)# used to reposition file cursor at any position in file, 0 means at begining
#
print( "Output of Readline function is ")
print(file1.readline())# read 1 line , if encounter \n, than ends there
print()

file1.seek(0)

# To show difference between read and readline
print("Output of Read(9) function is ")
print(file1.read(9))# ek line me nhi mila to dusri line me bhg gya chr read krne
print()

file1.seek(0)

print("Output of Readline(9) function is ")
print(file1.readline(9))# frst line me se 9 chr read honge

file1.seek(0)
# readlines function
print("Output of Readlines function is ")
print(file1.readlines())# read all lines of file but output is in list form
print()
file1.close()




fin = open('InputData3.txt', 'r')	    #Open the text Files for input and output
fout = open('NewK22PF.txt', 'w')
for line in fin:				        #for each line
    fout.write(line)				    #Write the line
fin.close()				                #Close the input file
fout.close()                			#Close the output file
fin = open('NewK22PF.txt' , 'r')
for line in fin:            			#for each line
    print(line,end='')      			#Print line
fin.close()                 			#Close the File


f1=open("dmeofile.txt","w")
f1.write("hello world\n")
f1.write("hello world\n")
f1.write("hello world\n")
f1.write("hello world\n")
f1.close()
f1=open("dmeofile.txt","r")
wordcount=charcount=linecount=0
for line in f1:
    linecount+=1# line=hello world, it dont count \n
    wordcount+=len(line.split())
    charcount+=len(line)
print("line:",linecount)
print("word:",wordcount)
print("char:",charcount)
f1.close()
# count number of lines, words and characters = ETP
#
#
#
# random access - very important
# very precious
obj=open("Demo.txt","w+")# write+read
obj.write("Hello World")#
obj.seek(3) #Move to 4th Byte hel>(l)<
print(obj.tell()) #Gives the byte number(in terms of index)
print(obj.read())# lo world
obj.seek(2,0)#Move 2 bytes further from beginning(0[First character at 0]+2=2)# # 0+2==(he>l<lo)
print(obj.read())# read(2) gives ll
obj.close()
obj=open("Demo.txt","rb")# read binary,
obj.seek(1)# 2 modes- text-for 1 (current)and 2(end) and binary
obj.seek(5,1)# move to e and that 5+1=6 -- till W #Move 5 bytes further from current position[1[Currently at 2nd byte]+5=6]
print(obj.read().decode("utf-8"))# positive offset, try removing decode(utf-8)
obj.seek(3)
obj.seek(-2,1)#Move 2 bytes back from current position # 3-2=1
print(obj.read().decode("utf-8"))
obj.seek(-3,2) #Move 3 bytes backward[Reference position is from end]# 2 is end, -3 take us to r and gives rld
print(obj.read().decode("utf-8"))

# Helloworld = 0 to 10

fr = open('TextData.txt','r') 			# Open the file for read
fw = open('NewFile.txt', 'w')   		# Open the file for write (new file)
fw.write(fr.read())				# Read the file and copy it to the new file
fr.close()					# Close the input file
fw.close()				# Close the new file
fr1 = open('NewFile.txt', 'r+')			# Open the new file as read / write
print(fr1.read(12))				# read and print the first 12 characters
print(fr1.tell())				# Print the read cursor position( position is 0 based)
print(fr1.write("this is the new text"))		# Write some text (length 20). This is always written at the end
print(fr1.seek(12))		# return where it is seeking		# Position the cursor at 12
print(fr1.read(1))				# Read and print the next character (at cursor position 12)
print(fr1.seek(15))				# Position the cursor at 15
print(fr1.read(10))				# Read and print 10 characters from this position
print(fr1.read())		# read() always reads the entire file irrespective of cursor position and changes the cursor position to the end
fr1.close()				# Close the file





# # 2 functions--dump and load
# # serialization-pickling dump() converting data to byte, deserialization - unpickling load() convert byte to data
# # open in binary convert to byte using dump, extract after loading(vice-versa process)-byte to data stream
import pickle

animalDict = { 'Cat': 2, 'Dog': 7, 'Lion': 4, 'Tiger': 9, 'Leopard': 11, 'Bear': 8, 'Elephant': 15 }
flowerDict={'Jasmine':101,'Lilly':102,'Rose':103}
outfile = open('animals','wb')# no extension required, opening binary file here,, animals.dat bhi likh skte h
pickle.dump(animalDict, outfile)# outfile==object related to animal
pickle.dump(flowerDict,outfile)#
outfile.close()
fst = open("animals", 'rb')				# Open the file as input binary
data = pickle.load(fst)			         # Read the first record
try:					# The Endof file is indicated as EOFError exception, we need to catch this exception
   while(True):# load will load only one record, loop help to load all the records
    print(data)# while true=infinite loop-never overs
    data = pickle.load(fst)# raise exception to stop loop, code that can generate exception is in try block
except:# this is only way to terminate loop
   print("Bye")# when loop reaches end of page, it says no more input output can be taken

import pickle  # imports the pickle library

Students = [['John', '501', 20, 92.5], ['Kohli', '502', 21, 95.5], ['Ganga', '503', 20, 90.5],
            ['Gayathri', '504', 20, 82.5], ['Krishna', '505', 20, 96.5]]
fst = open("students.dat", 'wb')  # Open the output file Notice the the b after w to indicate this is a binary file
for student in Students:  # one by one sub list stored in student
    pickle.dump(student, fst)  # Write each student
fst.close()  # Close the output file
fst = open("students.dat", 'rb')  # Open the file as input binary
data = pickle.load(fst)  # Read the first record
try:
    while True:
        print(data)  # The Endof file is indicated as EOFError exception, we need to catch this exceptio
    data = pickle.load(fst)
except:  # binary files - (extensionless) are faster but text files are readable
    print("Bye")  # write "" if u dont wish "bye" here

# create 2 classes and -- object-5 employees and 5 students and dump and load those objects, file in binary mode
# pickling concept and reference positions are taken from binary concept

import os.path
if os.path.isfile("myfile1.txt"):# checking existence of file
    print("myfile.txt exists")
else:
    print("myfile.txt does not exists")
# os.rename("myfile1.txt","newname1.txt")
# os.remove("newname1.txt")




import os.path
if os.path.isfile("myfile1.txt"):# checking existence of file
    print("myfile.txt exists")
else:
    print("myfile.txt does not exists")
# os.rename("myfile1.txt","newname1.txt")
# os.remove("newname1.txt")


obj=open("Hello.txt","x")# x mode - exclusive mode creates file # gives error if it already exist
# a+ -- append and read mode

# # pickling: marshelling and flattening
# # we cannot pickle -- lambda functions
# #
""" file handling is over """

""" exception handling """



""" Exception Handling"""

# try:
#     a=3
#     b=0
#     print(a/b)
# except ZeroDivisionError:
#     print("not divisible by zero")
#
#
#
#
# num1 = int(input("num1: "))
# num2 = int(input("num2: "))
# try:
#     # num1 = int(input("num1: "))
#     # num2 = int(input("num2: "))
#     num3 = num1 / num2
#     print(num3)
# except:# can handle all he possible errors
#     print("exception occurred")
#
# print("Program ended")
#
# # multiple except
#
# try:
#     a = int(input("a: "))
#     b = int(input("b: "))
#     c = a + b
#     d = a / b# name error dekhne k liye b ki jgha d likhdo
#     e = a * b
#     print("try successful")
# except ZeroDivisionError:
#     print("zero division error occurred")
# except NameError:
#     print("name error occurred")
# except Exception:# slide 10th
#     print("exception occurred")
#
# # multiple except
#
# try:
# 	a = int(input("a: "))
# 	b = int(input("b: "))
# 	c = a + b
# 	e = a / b
# 	print("try successful")
# except ArithmeticError:
# 	print("arithmetic error occurred ")
# except Exception:
# 	print("exception occurred")
# finally:# guaranteed to work whether there is error/exception or not,,obj.close() ya fir koi bhi msg user ko dena chaho toh
# 	print("executed in any condition")
#
# #
# try:
#     number1,number2=eval(input("Enter two numbers, separated by a comma: "))
#     result=number1/number2
#     print("Result is",result)
# except ZeroDivisionError:
#     print("Division by zero")
# except SyntaxError:
#     print("A comma may be missing in the input")
# except:
#     print("Something wrong in the input")
# else:
#     print("No exception")# work when there is no exception
# finally:
#     print("The finally clause is executed")# work everytime








