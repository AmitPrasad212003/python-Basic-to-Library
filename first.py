# print("Hello  of my world")
# print("hello me")
#
# print("""hello
# my
# world""")
# print("hello rint Hello world this is \nmy first python program \n hope you all like it....")
#
#
# # single line comments
# """ multiple line comments in python """
#
# # variables
#
# a = "hello my self"
# print(a)
#
# # User input
# name = input("Enter your name here ")
# print(name)
#

# age = int(input("Enter tour age here : "))
# print(age)
#
# length = float(input("Enter the length of the rectangle : "))
# print(length)

# exp1 = eval(input("enter any equation here : "))
# print(exp1)


# type casting

# to know the   datatype of variable
# name = "Amit "
# num1 = 356
#
# print(type(name))
# print(type(num1))

# implicit type conversion

# a= 123
# b = 1.23
#
# print(type(a))
# print(type(b))
#
# c = a+b
# print(c)
# print(type(c))

# explicit type conversion

# a= "123"
# b = 1.23
#
# print(type(a))
# print(type(b))
# # a = int(a)
# a = float(a)
#
# print("After conversion : ",type(a))
# c = a+b
# print(c)
# print(type(c))

# write a program to display a person`s name, age and adress in three different lines

# Name = "Amit"
# age = 21
# address = "654 lake street"
#
# print("Name : ",Name)
# print("Age : ",age)
# print("Address : ",address)

# Write a Program to swap Variable
# x =12
# y=13
# print("x : ",x)
# print("y : ",y)
# # method 1
#
# # temp = x
# # x=y
# # y=temp
#
# # method 2
# # left, right = right,left
# x,y=y,x
#
# print("x : ",x)
# print("y : ",y)

# Write a program to convert a float into integer
# x=12.4
# print(type(x))
# x=int(x)
# print(type(x))
# print(x)

# write  a program to take from a student for ID-card and then print it different lines.

# name = input("Enter the name of the student :")
# grade = input("Enter the grade of the Student : ")
# age = int(input("Enter the Age of the Student : "))
# email = input("Enter the E-mail ID  of the Student : ")
# Ph_no = input("Enter the Phone number of the student : ")
#
# print("student Identity card ")
# print("Name : ",name)
# print("Grade : ",grade)
# print("Age : ",age)
# print("E-mail ID : ",email)
# print("Phone Number : ",Ph_no)

# write a program to take an user input as integer then convert it to float
# x = int(input("Enter a nUmber hare : "))
# print(x)
# print(type(x))
# x = float(x)
# print(type(x))

# Operators
# Arithmetic  operator
# modulus %
# print(8%3)
# # floor divison
# print(8//3)
# print(8/3)
#
# print(3>2)
# logic operator
# print(3>4 or 3<4)
# print(3>4 and 3<4)
# print(not(3>4 or 3<4))
#  identity operator
# a = 123
# b = "123"
#
# print(a is b)
# print(a is not b)
# to find binary number of any number
# print(bin(10))
# a= 10
# b= 8
# print(a&b)
# a= 10
# b= 8
# print(a|b)
# a= 10
# b= 8
# print(a^b)
# zero fill left shift  bitwise operator
# print(10>>2)
# # zero fill right shift  bitwise operator
# print(10<<2)
# print(10<<1)

# membership operator
# a= "hello"
#
# print("e"in a)
# print("p"in a)
# print("p" not in a)
## conditonal statements
# marks =97
# if marks >= 90:
#     print("You will gat a mobile phone")
#
# print("Thank you ")

# marks = 87
# if marks>= 90 :
#     print("you will get a phone ")
# else:
#     print("no phone for 1 week ")
#
# print("Thank you ")
# marks =  87
# if marks >= 90:
#     print("You can go to a trip ")
# elif marks>=80 and marks <90:
#     print("you will get a new phone")
# elif marks >=70 and marks <80:
#     print("you will get a new book ")
# else:
#     print("you will not get your phone back ")

# marks = 97
# if marks >= 80:
#     print("you will get new phone ")
#     if marks >=95:
#         print("you can go to a trip ")
#
# else:
#     print("no phone for a month")

# marks = 97
#
# if marks >= 90: print("you will get a new phone ")

# marks =98
# print("you will go to a trip ") if marks >= 90 else print("no Phone for a month")

# write a program to check if a number is positive

# num = int (input("Enter a number "))
# if num > 0:
#     print("Number is positive .")
# elif num==0:
#     print("NUmber is zero ")
# else:
#     print("Number is Negative. ")

# write a program to check wether a number is odd or even

# num = int(input("Enter the number : "))
# if(num%2==0):
#     print(num,"is Even. ")
# else:
#     print(num,"is odd.")

# write a program to calculate area

# print("*** Area Calculator ***")
# print("""Press 1 to get the area of square
# Press 2 to get the area of rectangle
# Press 3 to get the area of circle
# Press 4 to get the area of triangle
#   """)
# choice = int(input("Enter a number Between 1-4 : "))
#
# if choice ==1:
#     side =float(input("Enter the length of one side : "))
#     Area = side*2
#     print("The Area of Square is : ",Area)
#
# elif choice ==2:
#     length = float (input("enter the length of the rectangle : "))
#     width = float (input("enter the width of the rectangle : "))
#     Area = length*width
#     print("The Area of rectangle is : ", Area)

# elif choice==3:
#     radius = float(input("Enter the radius of the circle : "))
#     Area = ((22/7)*(radius**2))
#     print("The area of circle is : ",Area)
# elif choice==4:
#     base = float(input("Enter the base of the trinagle :  ") )
#     height = float(input("Enter the height of the trinagle :  ") )
#     Area = 0.5 *height*base
#     print("The Area of Trianhle : ",Area)
# else:
#     print("***  Invalid Input ***")

# write a program check whether the passed letter is a vowel or not

# letter = input("Enter a letter here : ")
# if (letter in "aeiou")or(letter in "AEIOU"): #ya ye
# # if letter in "AEIOUaeiou":
#     print(letter," is a vowel")
# else:
#     print(letter,"it is a consonant")

# write a program to check if a number is a sigle digit number,
# 2-digit number and so on.., up to 5 digits

# num = int (input("Enter the number up to 5 digits : "))
# if num >=0 and num<=9:
#     print(num," is a single digits number ")
#
# elif num >=10 and num<=99:
#     print(num," is a double digits number ")
# elif num >=100 and num<=999:
#     print(num," is a triple digits number ")
# elif num >=1000 and num<=9999:
#     print(num," is a four digits number ")
# elif num >=10000 and num<=99999:
#     print(num," is a five digits number ")
# else:
#     print("Invalid Number or more than 5 digits")

# for i in range (1,11):
#     print(i,"My home.")
# for i in range (5,11,2):
#     print(i,"My home.")
# n = int(input("Enter the number : " ))
# print("Table of ",n," : ")
# for i in range (1,11):
#     print(n," * ",i," = ",n*i)
# n = 0;
# while n<=10:
#     print(n)
#     n+=2
#
# n = int(input("Enter the number : " ))
# i = 1
# print("Table of ",n," : ")
# while i<=10:
#     print(n, " * ", i, " = ", n * i)
#     i += 1
# while True:
#     print("hello world ")


# while True:
#     num1 = int (input("Enter a Number here : "))
#     num2 = int (input("Enter another Number here : "))
#     print(num1+num2)
#
#     repeat = input("Do you want to stop the Program : ")
#     if repeat == "yes":
#         break
# Nested looop

# for i in range (1,4):
#     for j in range (1,11):
#         print(j,end =" ")
#     print()

# for i in range (1,6):
#     for j in range (1,i+1):
#         print(j, end = " ")
#     print()

# for i in range(1,11):
#     if i == 3:
#         print("Add This song to the Favs..")
#     else:
#         print(i)

# common multiple
# for i in range (1,101):
#     if i % 8==0 and i%12 == 0:
#         print(i)

# n=1
#
# while n <=10 :
#     if n ==3 :
#         print ("Add this to favs.. ***")
#     else:
#         print(n)
#     n += 1

# for i in range(1,11):
#     if i==5:
#         continue
#     else:
#         print(i)
# for i in range(1,11):
#     if i==7:
#         break
#     else:
#         print(i)

# write a program to find a sum of all the even number up to 50

# sum = 0
# for i in range (1,51):
#     if i%2==0:
#         sum = sum + i
#
# print("Sum of even number is : ",sum)

# write a program to write first 20 number and their square number

# for i in range (1,21):
#     print(i,i**2)

# write a program to find sum of first 10 odd numbers using while loop

# sum =0
# n=0
# while n<= 20:
#     if n%2 != 0:
#         sum += n
#     n+=1
# print("The sum of first 10 odd number : ",sum)

# write a program to check if a number is divisible by 8 and 12, up to 100 number

# for i in range (1,101):
#     if i%8 ==0 and i%12==0 :
#         print(i)

# write a program to creata a billing system at supermarket.

# while True:
#     name = input("Enter customer's name : ")
#     total =0
#
#     while True :
#         print("** Enter the Amount and quantity **")
#         amount = float(input("Enter amount : "))
#         quantity = float(input("Enter quantity : "))
#
#         total += amount * quantity
#         repeat = input("Do you want to add more items ? ( Yes/ NO ) : ")
#         if repeat == "no" or repeat == "No":
#             break
#     print("="*40)
#     print("Name : ", name)
#     print("Amount to be Paid : ",total)
#     print("="*40)
#     print("***** Happy Shopping *****")
#     repeat1 = input("Do you want to add more items ? ( Yes/ NO ) : ")
#     if repeat1 == "no" or repeat1 == "No":
#         break

# a= "***** Why fit in, when you are bron to stand Out  *****"
# # write a program to find lenght of the following string.
# b = (len(a))
# print("Lenght of string A is : ",b)

# write a program to check how many times alphabet o is occuring.
# print("The number of times o is occuring is : ",a.count("o"))


# write a program to convert the whole string into lower and upper cases.

# x= a.lower()
# print(x)
# y= a.upper()
# print(y)

# write a program to convert the following string into a title .
# title means capatalised the first lettter of words in scentence
# z = a.title()
# print(z)

# write a program to find the index number of " fit in ".

# print(a.find("fit in"))

# *************************** pattern **********************************
#1
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# for i in range(1,6):
#     for j in range(1,6):
#         print(j,end = " ")
#     print()
#2
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end = " ")
#     print()
#3
# *
# * *
# * * *
# * * * *
# * * * * *
# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*",end = " ")
#     print()
#4
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(i,end = " ")
#     print()
#5
# 1 1 1 1 1
# 2 2 2 2
# 3 3 3
# 4 4
# 5

# for i in range(1,6):
#     for j in range(6,i,-1):
#         print(i,end = " ")
#     print()
#6
# * * * * *
# * * * *
# * * *
# * *
# *
# for i in range(1,6):
#     for j in range(6,i,-1):
#         print("*",end = " ")
#     print()
#7
#         *
#       * *
#     * * *
#   * * * *
# * * * * *
# for i in range(1,6):
#     for j in range(5,i,-1):
#         print(" ",end = " ")
#     for k in range(i):
#         print("*",end = " ")
#     print()
#8
# 1
# 2 1
# 3 2 1
# 4 3 2 1
# 5 4 3 2 1
# for i in range(1,6):
#     for j in range(i,0,-1):
#         print(j,end = " ")
#     print()

#9
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

# for i in range(1,6):
#     for j in range (1,i+1):
#         print("*",end = " ")
#     print()
# for i in range(5,0,-1):
#     for k in range (0,i-1):
#         print("*",end = " ")
#     print()

#10
# 1 2 3 4 5 6 7 8 9 10
# 2 4 6 8 10 12 14 16 18 20
# 3 6 9 12 15 18 21 24 27 30
# 4 8 12 16 20 24 28 32 36 40
# 5 10 15 20 25 30 35 40 45 50
# 6 12 18 24 30 36 42 48 54 60
# 7 14 21 28 35 42 49 56 63 70
# 8 16 24 32 40 48 56 64 72 80
# 9 18 27 36 45 54 63 72 81 90
# 10 20 30 40 50 60 70 80 90 100
# for i in range(1,11):
#     for j in range(1,11):
#         print(i*j,end = " ")
#     print()
# #11
# 1
# 2 4
# 3 6 9
# 4 8 12 16
# 5 10 15 20 25
# 6 12 18 24 30 36
# 7 14 21 28 35 42 49
# 8 16 24 32 40 48 56 64
# 9 18 27 36 45 54 63 72 81
# 10 20 30 40 50 60 70 80 90 100

#
# for i in range(1,11):
#     for j in range(1,i+1):
#         print(i*j,end = " ")
#     print()
#

  # Srting
# a ="Hello world"
# # print(type(a))
# # print(a)
# print(len(a))
# print(a.count("o"))
# print(a.upper())
# print(a.lower())
# print(a.index("o"))
# print(a.capitalize())
# print(a.find("l"))
#
# name = "john","RAhul"
# a = "My name is {} "
# print(a.format(name))

# name = "John"
# print(name.center(10," * "))
#

# # a = "Harry PotTTer and the goblet of fire"
# # print(a)
# #
# # # To find the length of the string
# # print(len(a))
# #
# # # to find the number of times a character is occuring
# # print(a.count("o"))
# # print(a.count("H"))
# #
# # # to convert each letter into upper case
# # print(a.upper())
# # to convert each letter into lower case
# print(a.lower())
# # to find the index of the string
# print(a.index("o"))
# print(a.index("o",15,35))
#
# # to convert the first letter to capital
# print(a.capitalize())
#
# # to convert a string into lower case
# print(a.casefold())
#
# # #

# # To write variable inside a string
#
# name = "John"
# age = 24
# b = "My name is {} and my age is {} "
# print(b.format(name,age))
#
# # it fill the given character and centralized a string
#
# print(name.center(20,"*"))

# a = "hello"
# b= "Hello123"
# c= "123456"
# d="HELLO"
# e=" "
# f = "Hello 123@"
# g="1.234"

#isalnum - Return true if all character in the string are alphanumeric
# print(a,a.isalnum())
# print(b,b.isalnum())
# print(c,c.isalnum())
# print(d,d.isalnum())
# print(f,f.isalnum())
# print(e,e.isalnum())
# print(g,g.isalnum())

#isalpha :- returns true if all character in the string are in the alphabet

# print(a,a.isalpha())
# print(b,b.isalpha())
# print(c,c.isalpha())
# print(d,d.isalpha())
# print(f,f.isalpha())
# print(e,e.isalpha())
# print(g,g.isalpha())

#isdecimal :- Returns true if all characters in the string are decimals

# print(a,a.isdecimal())
# print(b,b.isdecimal())
# print(c,c.isdecimal())
# print(d,d.isdecimal())
# print(f,f.isdecimal())
# print(e,e.isdecimal())
# print(g,g.isdecimal())

#isdigit :- Returns true if all characters in the string are digits

# print(a,a.isdigit())
# print(b,b.isdigit())
# print(c,c.isdigit())
# print(d,d.isdigit())
# print(f,f.isdigit())
# print(e,e.isdigit())
# print(g,g.isdigit())

# isnumeric :- Returns True if all character in the string are numeric

# print(a,a.isnumeric())
# print(b,b.isnumeric())
# print(c,c.isnumeric())
# print(d,d.isnumeric())
# print(f,f.isnumeric())
# print(e,e.isnumeric())
# print(g,g.isnumeric())

# islower :- Check if the string is lower case or not
#
# print(a,a.islower())
# print(b,b.islower())
# print(c,c.islower())
# print(d,d.islower())
# print(f,f.islower())
# print(e,e.islower())
# print(g,g.islower())

#isupper :- Return true if all character in the string are upper case
#
# print(a,a.isupper())
# print(b,b.isupper())
# print(c,c.isupper())
# print(d,d.isupper())
# print(f,f.isupper())
# print(e,e.isupper())
# print(g,g.isupper())

# isspace :- Returns True if all characters in the string are whitespace


# print(a,a.isspace())
# print(b,b.isspace())
# print(c,c.isspace())
# print(d,d.isspace())
# print(f,f.isspace())
# print(e,e.isspace())
# print(g,g.isspace())

# istitle :- Return true if the string follows the rules of title
#
# print(a,a.istitle())
# print(b,b.istitle())
# print(c,c.istitle())
# print(d,d.istitle())
# print(f,f.istitle())
# print(e,e.istitle())
# print(g,g.istitle())

# endwith() :- Returns true if the string ends with the specified value

# a = "Harry Potter"
# print(a,a.endswith("r"))
# print(a,a.endswith("p"))
# print(a,a.endswith("t",6,9))

# stratwith() :- Returns true if the string starts with the specified value

# a= "Harry potter"
# print(a.startswith("H"))
# print(a.startswith("p"))
# print(a.startswith("p",6,9))

# swapcase() :- swaps cases, lower case becomes upper case and vice versa

# a="Harry potter"
# print(a.swapcase())

# strip() :- Returns a trimmed version of the string

# a ="   Harry Potter    "
# b ="  ***** Harry Potter   ...... "
# print(a)
# print(a.strip())
# print(a.strip())
# print(b.strip(".,*, "))
# print(b.strip("*, "))

# split() :- splits the string at the specified separator, and returns a list

# a = "#OOFD#BRB#OMW#TB"
# b= "HEllo. my name is john. i am 21 year old."
# print(a.split())
# print(a.split("#"))
# print(b.split("."))

# ljust() :- Returns a left justified version of the string
# a = "Harry potter "
# x = a.ljust(20)
# print(x,"is my favotrite movie")
# x = a.ljust(20,"*")
# print(x,"is my favotrite movie")

# rjust() :- returns a right justified version of the string

# a = "harry potter"
# x = a.rjust(20)
# print(x,"is my favotrite movie")
# x = a.rjust(20,"*")
# print(x,"is my favotrite movie")

# replace() :- Return a string where a specified value is replaced with a specified value

# a = "My name  is john"
# b = "my name is john . john like to play football."
# print(a)
# print(a.replace("john", "lisa"))
# print(b.replace("john","Amit"))

# rindex() :- Searches the string for a specified value and returns
# the last position of where it was found.

# a = "Harry potter and the Prisoner of Azkaban "
# print(a.rindex("Prisoner"))
# print(a.rindex("Harry"))
# print(a.rindex("a",6,20))

# rfind () :- Search the string for a specified value and returns the last position of where it was found

# a = "Harry potter and the Goblet of fire"
# print(a.rfind("potter"))
# print(a.rfind("Harry"))
# b = " bibidy bobidy boo"
# print(b.rfind(" "))
# print(b.rfind("dy"))
# print(b.rfind("i"))
# print(b.rfind("dy",6,12))
# print(b.rfind("dy",6,14))

# # String slicing
# a= "Harry potter and the goblet of fire"
# b="0123456789"
# print(a)
# print(a[0:5])
# print(a[6:12])
# print(a[:5])
# print(a[-4:])
# print(b)
# print(b[::2])
# print(b[:7:])
# print(b[:7:2])
# print(b[::-1])
# print(b[6::-1])

# Fibonacci series

# a = 0
# b = 1
#
# n = int(input("Enter a Number here : "))
# if n==1:
#     print(1)
# else:
#     print(a, end = " ")
#     print(b, end = " ")
#     for i in range(2,n):
#         c = a+b
#         a = b
#         b = c
#         print(c,end = " ")
#
# # prime or not
# num = int(input("Enter a number here : "))
#
# if num <= 1:
#     print("it is not a prime number.")
# else:
#     for i in range(2,num):
#         if num%i == 0:
#             print(num,"number is not a prime number. ")
#             break
#     else:
#      print(num,"is a prime number.")
#
# print(25//2)
# print(25/2)

# check the number is palindrome or not

# num = int(input("Enter a number here : "))
# temp = num
# rev = 0
# while num > 0:
#     dig = num%10
#     rev = rev*10 + dig
#     num = num//10
#
# if rev == temp:
#     print(temp," is a palindrome.")
# else:
#     print(temp," is not palindrome")


# # write a program to calculate area
# while True:
#     print("*** Area Calculator ***")
#     print("""Press 1 to get the area of square
#     Press 2 to get the area of rectangle
#     Press 3 to get the area of circle
#     Press 4 to get the area of triangle
#       """)
#     choice = int(input("Enter a number Between 1-4 : "))
#
#     if choice ==1:
#         while True:
#             side =float(input("Enter the length of one side : "))
#             Area = side*2
#             print("The Area of Square is : ",Area)
#             repeat = input("Do you want to calculate again (yes/no)")
#             if repeat == "no" or repeat == "No":
#                 break
#
#     elif choice ==2:
#         while True:
#             length = float (input("enter the length of the rectangle : "))
#             width = float (input("enter the width of the rectangle : "))
#             Area = length*width
#             print("The Area of rectangle is : ", Area)
#             repeat = input("Do you want to calculate again (yes/no)")
#             if repeat == "no" or repeat == "No":
#                 break
#
#     elif choice==3:
#         while True:
#             radius = float(input("Enter the radius of the circle : "))
#             Area = ((22/7)*(radius**2))
#             print("The area of circle is : ",Area)
#             repeat = input("Do you want to calculate again (yes/no)")
#             if repeat == "no" or repeat == "No":
#                 break
#     elif choice==4:
#         while True:
#             base = float(input("Enter the base of the trinagle :  ") )
#             height = float(input("Enter the height of the trinagle :  ") )
#             Area = 0.5 *height*base
#             print("The Area of Trianhle : ",Area)
#             repeat = input("Do you want to calculate again (yes/no)")
#             if repeat == "no" or repeat == "No":
#                 break
#     else:
#         print("***  Invalid Input ***")
#
#     repeat1= input("Do you want to calculate again (yes/no)")
#     if repeat1 == "no" or repeat1 == "No":
#         break

# write a program to separate the following string into coma(,) separated values.

# A = "OOTD.YOLO.ASAP.BRB.GTG.OTW"
# b= A.split(".")
# print(b)
# write a program to sort string alphabetically in python

# a= input("Enter anything here : ")
# b = sorted(a)
# print(b)

# write  a program to remove a given character from a sting.
#

# a = "Hello"
# b=a.replace("e","")
# print(b)

# write a program to remove dot(.) from the following string.

# z = "F.R.I.E.N.D.S."
# b = z.replace(".","")
# print(b)

# write a Program to check the number of occurrence of a substring in a sting.

# a = "She Sells seashells on the sea shore "
# b = a.count("sea")
# print("The number times substring sea is occuring is ",b)

# Take an input from a user as a string then , reverse it.

# a = input("Enter anything here : ")
# print(a[::-1])

# Write a program to check if a string is contains only digits.

# a = input("enter anything here : ")
# b= a.isdigit()
#
# if b==True:
#     print(a,"Is contain only digits")
# else:
#     print(a,"Is does not contains only digits")

# write a program to check if a string is palindrome.
# a = input("enter anything here : ")
# rev = a[::-1]
#
# if a==rev:
#     print(a,"Is a palindrome number.")
# else:
#     print(a,"is not a palindrome number.")

# write a program to find number of vowel in a string.
# a = input("enter anything here : ")
# vowels = 0
# for i in a :
#     if i =="a" or i=="A" or i =="e" or i=="E" or i =="i" or i=="I" or i =="o" or i=="O" or i =="u" or i=="U" :
#         vowels += 1
#
# print("The number of vowels in the following are : ",vowels)

# write a program to check if every word in a string begins with a capital letter.

# a = input("Enter anything here : ")
# print(a.istitle())



# ========== Lists ========
#
# fruits = ["apple", "Mango", "Banana",12 ,12.12]
# print(fruits)
# print(type(fruits))

# slicing lists

# a= ["Ironman", "Thor","Captain America", "Hulk"]
# print(a[1])
# print(a[-1])
# print(a[1:3])
# print(a[:2])
# print(a[:3])
# print(a[1:])
# print(a[::2])
# print(a[-3:-1])
# print(a[::-1])
# print(a[-1:-4:-1])

# list iteration

# iteration using for loop
# a= ["Ironman", "Thor","Captain America", "Hulk"]
# for i in a:
#     print(i)

# Iteration using for loop with range and length function

# a= ["Ironman", "Thor","Captain America", "Hulk"]
# for i in range(len(a)):
#     print(a[i])

# iteration using while loop
# a= ["Ironman", "Thor","Captain America", "Hulk"]
# i=0
# while i <(len(a)):
#     print(a[i])
#     i+=1

# iteration using  short- hand for loop

# a= ["Ironman", "Thor","Captain America", "Hulk"]
# [print(i) for i in a ]

# list function
# a= ["Ironman", "Thor","Captain America", "Hulk","Hulk"]
# print(a)
#to find the length of a list

# print(len(a))
#
# # to count an occurence of a particular element
# print(a.count("Hulk"))
# print(a.count("Thor"))
# print(a.count(""))
#
# # to add to the list
# a.append("Spiderman")
# print(a)
#
# # to add to a specific location
#
# a.insert(1,"vision")
# print(a)
#
# # to remove from a list
#
# a.remove("Hulk")
# # a.remove("Spiderman")
# print(a)
#
# # to remove from a certain location
#
# print(a.pop(1))
# print(a)

# a= ["Ironman", "Thor","Captain America", "Hulk","Hulk"]
# to create a copy of a list

# # b= a
# # print(b)
# # print(a)
# b= []
# print(b)
# b = a.copy()
# print(b)
#
# # to acces an element
#
# print(a.index("Ironman"))
#
# # to entend an element / add two list
#
# c=["vision","spiderman"]
# a.extend(c)
# print(a)
# to reverse the list
# a= ["Ironman", "Thor","Captain America", "Hulk","Hulk"]
# a.reverse()
# print(a)

# to sort the list

# a.sort()
# print(a)
# d=[1,7,4,9,2]
# # d.sort()
# # print(d)
# # #
# # # to clear all the data from the list
# #
# a.clear()
# d.clear()
# print(a)
# print(d
# )
# list comprehension
#
# l1 = [30,40,34,42,45]
# # l4 =l1
# # print(l4)
# l2 = []
# for i in l1 :
#     if i>40:
#         l2.append(i)
#
# print(l1,"\n",l2)
#
# l3 = [i for i in l1]
# print(l3)
# l3 = [i for i in l1 if i >40]
# print(l3)

# A = ["Ross","Rachel","Monica","Joe"]
#
# # write a program to swap first and fort element
# A[0],A[3] = A[3],A[0]
# print(A)
#
# # write a program to add a new value at second position.
#
# A.insert(1,"Phoebe")
# print(A)
#
# # write a program to delete a value from 3rd position.
# A.pop(2)
# print(A)

# B = [13,7,12,10]
# write a program to multiply all the number in the list.
# mul = 1
# for i in (B):
#     mul *= i
# print(mul)

# write a program to get the largest number from the list .
# # Arrange the list in ascending order
# B.sort()
# print(B)
# print("The largest value in the given list is : ",B[-1])
# print("The smallest value in the given list is : ",B[0])


# ============ TUPLES =============
# a= "apple", "mango","banana",1232,"NOkia"
# print(type(a))
# print(a)
# # single tuple fromat
# b= ("Ironman",)
# print(type(b))

# silicing of tuples
# print(a[1:3])
# print(a[:3])
# print(a[2:])
# print(a[::2])
# print(a[1::2])
# print(a[::-1])
# print(a[2::-1])
# iteration of tulples
# with for loop

# for i in a:
#     print(i)

# along with range and lenght in for loop

# for i in range(len(a)):
#     print(a[i])

# along with while loop:

# i=0
# while i<len(a):
#     print(a[i])
#     i+=1

# # # conversion of Tuples and tuples functions
# a= "apple", "mango","banana",1232,"NOkia"
# print("Before conversion : ",type(a))
#
# a=list(a)
# print("after conversion : ",type(a))
#
# a.append("vivio")
# print(a)
# a= tuple(a)
# print(type(a))
# print(a)
#
# print(a.count("vivio"))
# print ("The index off nokia is :",a.index("NOkia"))


# Introduction to Dictionary

# Employee_Data = {"name":"John","age": 24, "gender":"male"}
# print(Employee_Data)
# print(Employee_Data["age"])
#
# # Iteration in Dictionary
# # printing all the key names one by one
# for x in Employee_Data:
#     print(x)
#
# # printing all the value names one by one
#
# for x in Employee_Data:
#     print(Employee_Data[x])
#
# # using value function
# for x in Employee_Data.values():
#     print(x)
#
# # using item function for both key and value
#
# for x,y in Employee_Data.items():
#     print(x,"-",y)


# Dictionary function

# Student = {"name":"John","age": 24, "gender":"male"}

# #get : give the value of key
# x= Student.get("name")
# print(x)
# x= Student.get("")
# print(x)
#
# #item
# a= Student.items()
# print(a)
#
# #key : gives the key of dictionary
#
# b= Student.keys()
# print(b)
#
# # values: gives the values of dictionary
# c = Student.values()
# print(c)
#
# # copy
# d = Student.copy()
# print(d)
#
# e = Student
# print(e)

# Student = {"name":"John","age": 24, "gender":"male"}
# #setdefault
# # x = Student.setdefault("age")
# # print(x)
# #update
# # Student.update({"age":45})
# # print(Student)
# #pop
# # Student.pop("age")
# # print(Student)
# # Student.pop("gender")
# # print(Student)
# #popitem : it is used to pop from last location
# p=Student.popitem()
# print(Student)
# print(p)
# #clear : to delete all item of dictionary
#
# c = Student.clear()
# print(c)
# print(Student)

# Nested Dictionary

# Employees = {1:{"Name": "John","Age":23,"Gender":"Male"},
#              2:{"Name": "lisa","Age":21,"Gender":"female"},
#              3:{"Name": "peter","Age":53,"Gender":"Male"}}
# print(Employees)
# print(Employees[1])
# print(Employees[1]["Gender"])
# print(Employees[2]["Age"])

# Write a python program to sort a dictonary by value.

# a= {"a":12,"b":23,"c":4,"e":2,"d":3,"f":34}
# a = sorted(a.values())
# print(a)

# write a python script to print a dictionary where
# the key are number between 1 and 15 and the values are square of keys.

# a ={}
# for i in range(1,16):
#     a[i] = i**2
#
# print(a)

# write a program to multiply all the items in a dictionary.
# a= {"a":12,"b":23,"c":4,"e":2,"d":3,"f":34}
#
# print(a["c"])
# product = 1
# for i in a :
#     product *= a[i]
#
# print(product)
#
# # write a python program to sort a dictionary by key .
# a= {"a":12,"b":23,"c":4,"e":2,"d":3,"f":34}
#
# a = sorted(a.keys())
# print(a)




# 1. Convert the following dictionary into JSON format

import json
# Student_data = {"name":"David","age":13,"marks":87}
# print(type(Student_data))
# data = json.dumps(Student_data)
# print(data)
# print(type(data))

# Access the value of age from the given JSON data.
# Student_data =""" {"name":"David","age":13,"marks":87}"""
#
# data = json.loads(Student_data)
# print(data["age"])

# Pretty print following JSON data.
# Student_data = {"name":"David","age":13,"marks":87}
# data = json.dumps(Student_data,indent=4,separators=(",","="))
# print(data)

# Access the nested key "marks" from the following nested data

# Student_data = """{"Student":{
#         "grade":"David",
#         "marks":{
#         "math":87,}
#         }}"""
# data = json.loads(Student_data)
# print(data["student"]["grade"]["name"]["marks"])
# worng code

# Access the nested key "marks" from the following nested data
#
# Student_data = """{"student":
#                      {"grade":
#                         {"name":"David","marks":87}
#                     }
#                 }"""
#
# data = json.load(Student_data)
# print(data["student"]["grade"]["marks"])

# ================= Set ================= #

# a = {"Ironman", "Hulk", "Captain America"}
# print(a)
# print(type(a))
#
# iteration of set (only one method is there)
# for x in a:
#     print(x)

#  ==== Set functions ====  #
# add
# a.add("spiderman")
# print(a)

# # pop : randomly pop any element of the set
#
# x = a.pop()
# print(a)
# print(x)

# remove : remove particular element in the set

# a.remove("Hulk")
# print(a)

#dicard : similar like remove
# a.discard("Hulk")
# print(a)

# copy
# b = a.copy()
# print(b)

# a = {"Ironman", "Hulk","Thor", "Captain America"}
# b = {"Superman", "Batman","Wonder-woman"}
# c = {"Hulk","Thor"}
# #isdisjoint
# print(a.isdisjoint(b))
# print(a.isdisjoint(c))
# #issubset
# print(a.issubset(c))
# print(c.issubset(a))
# print(b.issubset(a))
# #issupperset
# print(a.issuperset(b))
# print(a.issuperset(c))
# #update
# a.update(c)
# print(a)
# a.update(b)
# print(a)
#
# # clear
# a.clear()
# print(a)

# a = {"Ironman", "Hulk","Thor", "Captain America"}
# b = {"Superman", "Batman","Wonder-woman"}
# c = {"Hulk","Thor","Spiderman"}

# #union
# print(a.union(b))
# print(a.union(c))
# # Difference (subtract the common item in set)give new set
# print(a.difference(c))
# # Difference update change in same set
# a.difference_update(c)
# print(a)
# intersection: give new set (common element of the set)
# x = a.intersection(c)
# print(x)
# x = a.intersection(b)
# print(x)
# # intersection Update in these changes in same set
# a.intersection_update(c)
# print(a)
# a.intersection_update(b)
# print(a)
#
# # symmetric difference : ignore common value in the union of set and give new set.
# x = a.symmetric_difference(c)
# print(x)
# x = a.symmetric_difference(b)
# print(x)
# # Symmetric Diiference updates : it is similar like symmetric differnce but the changes in same set
# a.symmetric_difference_update(c)
# print(a)
# a.symmetric_difference_update(b)
# print(a)

# write a program to find max and min in a set.
# a = {12,56,34,8,54,90,1,57}
# minimum = min(a)
# maximum = max(a)
#
# print("The minimum value in the given set is :  ",minimum)
# print("The maximum value in the given set is :  ",maximum)

#write a program to find common elements in three lists using sets.

# a = [1,2,5,6,8]
# b = [4,5,6,7]
# c = [1,9,6,2,5]
# print("The common elements in the given three list are : ",set(a)&set(b)&set(c))

# write a program  to find difference between two sets.
# a = {1,2,5,6,8}
# b = {1,9,6,2,5}
#
# print(a.difference(b))
# print(b.difference(a))

# write a python program to remove an item from a set if it is present in the set.
# a = {1,2,5,6,8}
# # a.discard(8)
# # print(a)
# a.discard(12)
# print(a)

# write a program to check if a set is a subset of another set.

# a = {1,2,3,45,6}
# b = {2,3,1}
#
# print(b.issubset(a))
# print(a.issubset(b))



# ====== Function ===== #
# Example
# def hello():
#     print("HELLO WORLD")
#
# hello()

# def add():
#     x = 56
#     y = 23
#     print(x+y)
#
# add()

# parameters and arguments
# def add(x,y): #parameters
#     print(x+y)
#
# add(2,3)  # Arguments
# add(45,565)

# funtion of calculate rectangle area

# def rect(length,width):
#     print("The area of the rectangle is : ", length*width)
#
# rect(12,3)

# def hello(*name):
#     print("Hllo, my name is ",name[0,1,2]) # for axis use  the  index value(0,1,2)
#
# hello("john", "lisa","peter")  # Arbitary Arguments

# return statements
# def hello():
#     return ("Hello world")
#
# print(hello())
#
# def add(a,b):
#     return ("The addition of two number is : ", a+b)
#
# print(add(34,54))

# ====== Recursion ===== #

# def hello():
#         print("Hello")
#         # return hello()
#
# print(hello())

# factorial of n number

# def fact(n):
#     if n==1:
#         return 1
#     else:
#         return (n*fact(n-1))
#
# print(fact(5))
# print(fact(4))

# a = lambda b:b*5
# print(a(5))

# x = lambda a,b,c:(a+b)*c
# print(x(3,6,8))


# local variables

# x = 24
# print("First variable x : ",x)
# def hello():
#     x = 25
#     return x
# print(hello())
#
# print(x)

# global variable

# x = 24
# print("First variable x : ",x)
# def hello():
#     global x
#     x = 25
#     return x
# print(hello())
#
# print(x)

# Write a function maximum of three number in python.

# def max_num(x,y,z):
#     if x>y and x>z:
#         print(x,"is the greatest number.")
#     elif(y>x and y>z):
#         print(y,"is the greatest number.")
#     else:
#         print(z,"is the greatest number.")
#
# max_num(45,56,23)

# Write a pyton function to create and print a list where the value are the square of number between 1 and 30.

# def create_list():
#     l = []
#     for i in range(1,31):
#         l.append(i**2)
#
#     return l
#
# print(create_list())

# write a python function that takes a number as a parameter and check if the number is prime or not.

# def check_prime(num):
#     if num == 1 :
#         print(num,"It is not a prime number.")
#     if num == 2 :
#         print(num,"It is a prime number.")
#
#     for i in range(2,num):
#         if num % i == 0:
#             print("It is not a prime number.")
#             break
#     else:
#         print("It is a Prime number")
#
# check_prime(13)

# write a python function to sum all the number in a list.
# def add(numbers):
#     total = 0
#     for i in numbers :
#         total = total+i
#     return(total)
#
# print("The sum of all the item in the list is : ",add([12,34,45,56,45,43]))

# solution 2: using Recursion.

# def add(number):
#     if len(number) == 1:
#         return (number[0])
#     else:
#         return ((number[0])+add(number[1:]))
#
# print("The sum of all the item in the list is : ",add([12,34,45,56,45,43]))

# write a python program to solve the Fibonacci Sequence
#using recursion.

# def fibonacci(num):
#     if num == 1:
#         return 0
#     elif num == 2:
#         return 1
#     else:
#         return (fibonacci(num-1)+fibonacci(num-2))
#
# print(fibonacci(10))

# Modules
# import datetime
# x = datetime.datetime.now()
# print(x)

# y = datetime.datetime(2003,3,21)
# print("DAy name : ",y.strftime("%A"))
# print("day short name : ",y.strftime("%a"))
# print("Months name : ",y.strftime("%B"))
# print("Months number : ",y.strftime("%m"))
# print("Year : ",y.strftime("%Y"))
# print("Last two digits of year : ",y.strftime("%y"))
# print("AM/PM : ",y.strftime("%p"))
# print("Minutes : ",y.strftime("%M"))
# print("seconds : ",y.strftime("%S"))
# print("microseconds : ",y.strftime("%f"))

# import random
#
# x = random.randint(1,6)
# print(x)

# l = ["Heads","Tails"]
# x = random.choice(l)
# print(x)

# import math
# x = max(34,23,45,32)
# print("The maximum value is : ",x)
# x = min(34,23,45,32)
# print("The minimum value is : ",x)
#
# a = pow(2,5)
# print(a)
#
# b = math.sqrt(345)
# print(b)
#
# c = abs(-12.32) # absolute gives +ve value of any number.
# print(c)
# # ceil gives greatest nearest value of integer.
# k = math.ceil(23.4)
# print(k)
# # floor gives lowest nearest value of integer.
# m = math.floor(23.4)
# print(m)

# creation modules

# import demo
# a = demo.add(3,45)
# print(a)

# import demo as d
# a = d.add(34,45)
# print(a)
# b = d.employee["Name"]
# print(b)
