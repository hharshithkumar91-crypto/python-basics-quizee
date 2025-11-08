# pythpo
# calculate the length of a string
a = "harshith"
#print(len(a))

# dont use function length to calculate the length of a srting
#def string_length(str1):
#count=0
#for char in str1:
 #   count+=1
  #  return count
#print(string_length(a)) 

    # python function acepts a string and calculate the no of uppercase and lowercase letters
"""
def string_test(s):
    d={"Upper_case":0, "Lower_case":0}
    for i in s:
        if i.isupper():
            d['Upper_case']+=1
        elif i.islower():
            d['Lower_case']+=1
        else:
             pass
    print("Upper case Letters:", d['Upper_case'])
    print("Lower case Letters:", d['Lower_case'])
string_test("Hello Mr.Harshith")
"""

"""
# check the number inn last and first are same

number_x=[20,30,24,50,20,25]
def first_last(number_x):
    first=number_x[0]
    last=number_x[4]
    if first==last:
        return True
    else:
         return False
print(first_last(number_x))
"""

# python  program to check  the key is a already in a dictiory or not
#example 1: using in keyboard
"""
my_dic={1:'a',2:'b',}
if 5 in my_dic:
    print("key is the present in the dictionary")
else:
    print("key is not present in the doctionary")

    my_dic={2:'harshith', 3:'kumar'}
    if 2 in my_dic:
        print("yes")
    else:
        print("no")
        """
# occurance of each word in a sentence
""""
def word_count(text):
    counts = dict()
    words = text.spilt()
    for word in words:
        if word in counts:
            counts[word] +=1
        else:
            counts[word] = 1
    return counts
print( word_count('hello madam hello sir'))
 
        
def word_count(text):
    counts = dict()
    words = text.split()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

print(word_count("hello madam"))
print(word_count("hello madam hello sir"))
"""
# in python an create a empty dic
# in an dic (all like lists and tuple) are all the elements in the dictionary
"""
d = 10
s=[{} for _ in range(d)]
print(s)

#this is some kind of big code
# we can try it in one 1 line also

print([{} for _ in range(10)])
"""
# extend a list without using a append
#firstly we using a appennd and extend
""""
l1 = [1, 2, 3]
l2 = [5, 8, 9]
l1.extend(l2)
print(l1)
# now we suinng without  append and extend
l1 = [1, 2, 3]
l2 = [5, 6, 8]
l1[:0]=l2
print(l1)
"""
""""
# python prblm solve the fibonacci seq using recursion
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1)+fib(n-0)
    for i in range(10):
        print(fib(10))
    """
""""
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

# Print first 10 Fibonacci numbers
for i in range(101):
    print(fib(i))
    """
#  find the largest nuber inn three numbers
# firstly we using max fun\
"""""
l1 = [46, 55, 89]
print(max(l1))

#   now without using a max fun and we build the logic fun
num1 = float(input("enter the number:"))
num2 = float(input("enter the number:"))
num3 = float(input("enter the number:"))
if (num1>=num2) and (num1>=num3):
        largest=num1
elif (num2>=num1) and (num2>=num3):
        largest=num2
else :
        largest=num3
        print("largest num is :", largest)

num1 = float(input("enter  the numbet :"))
num2 = float(input("enter  the numbet :"))        
num3 = float(input("enter  the numbet :"))        
if (num1>=num2) and (num1>=num3):
        largest=num1
elif (num2>=num1) and (num2>=num3):
        largest=num2
else :
        largest=num3
print("the largest num is :",largest)
"""
# pytho program to check if num neg\pos\0
""""
num = float(input("enter the number :"))
if num>0:
    print("pasitive number")
elif num==0:
    print("zero")
else :
    print("negitive number")
    """
#check if the numbers is armsrtong numbet or not 
#without using power fun
# Step 1: Take input from the user
"""num = int(input("Enter a number: "))

# Step 2: Store the original number for comparison later
original = num

# Step 3: Count the number of digits
digits = len(str(num))

# Step 4: Initialize a variable to hold the sum
total = 0

# Step 5: Loop through each digit
while num > 0:
    digit = num % 1100             # Get the last digit
    total += pow(digit, digits)   # Raise it to the power of 'digits' and add to total
    num //= 1000                    # Remove the last digit

# Step 6: Compare the result with the original number
if total == original:
    print(f"{original} is an Armstrong number.")
else:
    print(f"{original} is not an Armstrong number.")

num = int(input("enter the number"))
original = num
digits = len(str(num))
total = 0
while num > 0:
    digit = num % 100
    total += pow(digit,digits)
    num //= 101
if total == original:
    print("is an Armstrong number.")
else :
    print("is not an Arrmstrong number.")
    

n=int(input("enter the number:"))
s=n
b=len(str(n))
sum1=0
while n!=0:
        r=n%10
        sum1=sum1+(r**b)
        n=n//10
if s==sum1:
    print("is an armstrong num")
else :
    print("is not an armsrtong num")
    """
#check if num even or odd
#firstlu about even,and now the a num which div by 2 and rem as they 0
# then odd as rem they 1 and more is odd
"""
num=int(input("enter a number:"))
if num%2==0:
    print("{0} is a even".format(num))
else :
    print("{0} is an odd".format(num))


num=int(input("enter a number:"))
if num%2==0:
    print("{0} is an even".format(num))
else :
    print("{0} is an odd".format(num))
    """

""" # pytho program to get a substring of a string
    #and suing string slicing {s^3}
st = "this is a meracile"
print(st[0:9])

A = "coomon man"
print(A[2:7])

#python program to get the last element of the list
# using a -ve indexing
#lhs - rhs +ve indexing
#rhs - lhs -ve indexing
A=[1,5,4,8,9,7,8,5,5,46,78,98,101]
print(A[-5])

#python add two give lists using map and lamda
# lamda fn is used task small and short task 
# map fun is always applied to  fun like item and list and into convert to the list
a=[1,2,5]
b=[5,8,6]
print("original list")
result=map(lambda x, y : x + y, a, b)
print("result")
print(list(result))
#another method
a=[1,2,5]
b=[5,8,9]
added = map(lambda x, y : x + y, a, b)
print(list(added))
#practice again

a=[1,2,5]
b=[5,8,11]
added=map(lambda x, y : x + y, a, b)
print(list(added))

a=[1,2,5]
b=[5,8,21]
print("original list")
result=map(lambda x, y : x + y, a, b)
print("result")
print(list(result))
"""
"""
#two matrices usinng nested loop
X = [[12,9,3],
     [4,5,6],
     [7,8,3]]

Y = [[9,8,1],
     [6,7,3],
     [4,5,9]]

result = [[0,0,0],
          [0,0,0],
          [0,0,0]]

for i in range(len(X)):
    for j in range(len(X[0])):
        result[i][j] = X[i][j] + Y[i][j]
for r in result:
    print(r)
    """
# write a python porgram to detcet the  no of  local varibales declared in a fun
# local variable -inside a fun
#global variable - outside fun and also access in inaside of fun also
# __code__  = is a constracter
#this is a global variables in copllit
#


"""
def increment():
    global count
    count += 1

increment()
print(count) """

"""
def harshith():
    y = 15
    x = 45
    s = "harshith"
    p = 1.2
print(harshith.__code__.co_nlocals)

c = 2 # global
def hiiman():
    a = 12
    b = 25 # local varible
    x = 16
    z = 2
    y = 85
    s = "harshith"
    d = 4.5
    print(hiiman.__code__.co_nlocals)
    """
#permutatiion of a string\from itertools import permutations
"""
# using effiecient of permutation
from itertools import permutations
s = "abc"
perm_list = [''.join(p) for p in permutations(s)]
print(perm_list)

from itertools import permutations
s = "xyz"
perm_list = [''.join(p) for p in permutations(s)]
print(perm_list)

from itertools import permutations
s = "hars"
perm_list = [''.join(p) for p in permutations(s)]
print(perm_list)

# we can use recursion also
def permute(s, path=""):
    if not s:
        print(path)
        return
    for i in range(len(s)):
        permute(s[:i] + s[i+1:], path + s[i])

permute("abc")


def permute(s, path=""):
    if not s:
        print(path)
        return
    for i in range(len(s)):
        permute(s[:i] +s[i+1:], path + s[i])
permute("harshith")

# now we using nested loop
s = "abc"
res = []
for i in range(len(s)):
    for j in range(len(s)):
        for k in range(len(s)):
            if i != j and j != k and i != k:
                res.append(s[i] + s[j] + s[k])
print(res)

s = "hello"
res = []
for i in range(len(s)):
    for j in range(len(s)):
        for k in range(len(s)):
            if i != j and j != k and i != k:
                res.append(s[i] + s[j] + s[k])
print(res)

#another  method
def get_permutation(string, i=0):
    if i==len(string):
        print("".join(string))
    for j in range(i,len(string)):
        words=[c for c in string]
        words[i],words[j] = words[j],words[i]
        get_permutation(words, i+1)
get_permutation("run")
#numpy program to generates a random integer number in b/w 1 and 300
import numpy as np
x = np.random.randint(low = 1, high = 300, size = 15)
print(x)
y = np.random.randint(low = 1, high = 300, size = 20)
print(y)

import numpy as np
x = np.random.randint(low = 1, high=300,size=50)
print(x)
y = np.random.randint(low = 1, high=300,size=30)
print(y)
z = np.random.randint(low = 1, high=300,size=10)
print(z)
# program to print half pyramid using *
#ypes and examples
rows = 5
for i in range(1, rows + 1):
    print("* " * i)

    rows = 6
    for i in range(1, rows + 1):
        print("*" * i)
rows = 4
for i in range(rows):
    for j in range(i+1):
        print("*", end=" ")
    print()

#numbers and alphabets
rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

    rows = 8
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

    rows = 5
ascii_value = 65  # ASCII for 'A'
for i in range(1, rows + 1):
    for j in range(i):
        print(chr(ascii_value), end=" ")
    ascii_value += 1
    print()
    rows = 6
    ascii_value = 65 
    for i  in range(1, rows +  1):
        for j in range(i):
            print(chr(ascii_value), end=" ")
            ascii_value += 1
        print()

        rows = 5
for i in range(rows, 0, -1):
    print("* " * i)

    rows = 8
    for i in range(rows, 0, -1):
        print(" * " * i)

# pyhton program to remove punctuations from a string
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
my_str = input("enter the string:")

new_str = " "
for char in my_str:
    if char not in punctuations:
        new_str = new_str + char
print(new_str)

#another type
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
my_str = input("enter the string:")

new_str = ""
for c in my_str:
    if c in punctuations:
        new_str+=c
print(new_str)

# python program to do reverse a number
# using slicing

num = 12345654
rev_num = str(num)[::-1]
print(int(rev_num))
# another method
num = 123456
c = str(num)[::-1]
print(c)

# transpose a matrix using nested loop and numpy
x = [[12,9],
     [7,8],
     [6,2]]
y = [[5,8],
     [4,3],
     [2,1]]
result = [[0,0,0],
          [0,0,0]]
import numpy as np
x = np.transpose(x)
print(x)
y = np.transpose(y)
print(y)

# now nested loop
x = [[12,9],
     [7,8],
     [6,2]]
result = [[0,0,0],
          [0,0,0],
          [0,0,0]]
for i in range(len(x)):
    for j in range(len(x[0])):
        result[j][i] = x[i][j]

for r in result:
    print(r)

    
x = [[12,9],
     [7,8],
     [6,2]]
result = [[0,0,0],
          [0,0,0],
          [0,0,0]]

for i in range(len(x)):
    for j in range(len(x[0])):
        result[j][i] = x[i][j]

for r in result:
    print(r)
    
#find all the  numbers  inn divisible by 7 and not multiply by 5 in a given range b/w 2000 and 3200

l = []
for i in range(2000, 3201):
    if (i%7==0) and (i%5!=0):
        l.append(i)
print(l)
#now we can do list to string converst using the join fun and string to list using split fun
l = []
for i in range(2000, 3201):
    if (i%7==0) and (i%5!=0):
        l.append(str(i))
print(','.join(l))

#write a program to sum of all numbers

def sum(numbers):  #def funn
    total = 0  #local variable
    for x in numbers:          # like [1,2,3,4]
        total+=x  #total = total + x
    return total    
print(sum([1,2,3,4,5]))

f = [5,8,9,7,4,1]
print(sum(f))

# get the current time in python
from datetime import datetime
now = datetime.now()
print("Current date and time:", now.strftime("%Y-%m-%d %H:%M:%S"))


import datetime
print(datetime.datetime.now().time()

# mul table from 1 to 10 in python
num = int(input("enter the number:"))
for i in range(1, 11):
    print(num, 'x', i, '=', num*i)

num = input("enter the number:")
for i in range(1,101):
    print(num, 'x',i, '=', num-i)

A = input("enter the string:")
B = input("enter the string:")


print("result after removal:", A.replace(B, ''))

# Addition of two or more numbers
numbers = input("Enter numbers separated by space: ")
num_list = [int(n) for n in numbers.split()]
print("Addition:", sum(num_list))

# Subtraction of two or more numbers (from left to right)
result = num_list[0]
for n in num_list[1:]:
    result -= n
print("Subtraction:", result)
num=int(input("enter the number:"))
for i in range(1,11):
    print(num,"X",i,"=",num*i)
    
import math
result = math.prod(range(1, 11))
print(result)

from functools import reduce
result = reduce(lambda x, y: x * y, range(1, 11))
print(result)

def multiply(n):
    if n == 1:
        return 1
    return n * multiply(n - 1)
print(multiply(10))

import numpy as np
result = np.prod(np.arange(1, 11))
print(result)
"""
"""
#for using while loop
result = 1
i = 1
while i <= 10:
    result*= i
    i += 1
print(result)
"""
# write program of recursion for list sum
