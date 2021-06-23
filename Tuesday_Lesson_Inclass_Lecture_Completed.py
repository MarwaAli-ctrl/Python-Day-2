#!/usr/bin/env python
# coding: utf-8

# # Functions, Scoping, Data Collections 1 & List Comprehensions

# ## Tasks Today:
# 
# <i>Monday Additions (or, and ... if statements)</i>
# 
# 1) String Manipulation <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) strip() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) title() <br>
# 2) Working With Lists <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) min() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) max() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; c) sum() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; d) sort() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; e) Copying a List <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; f) 'in' keyword <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; g) 'not in' keyword <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; i) Checking an Empty List <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; j) Removing Instances with a Loop <br>
# 3) List Comprehensions <br>
# 4) Tuples <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) sorted() <br>
# 5) Functions <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) User-Defined vs. Built-In Functions <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) Accepting Parameters <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; c) Default Parameters <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; d) Making an Argument Optional <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; e) Keyword Arguments <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; f) Returning Values <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; g) *args <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; h) Docstring <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; i) Using a User Function in a Loop <br>
# 6) Scope

# ### String Manipulation

# ##### .lstrip()

# In[3]:


# string.lstrip()

mystring = '   asd#10 238al KBAWEJHKndas    oej    '

# I forgot, strings are immutable. We can't directly change them
lstripstr = mystring.lstrip()

lstripstr


# ##### .rstrip()

# In[4]:


# string.rstrip()
rstripstr = mystring.rstrip()

rstripstr


# ##### .strip()

# In[5]:


# string.strip()

stripstr = mystring.strip()
stripstr


# ##### .title()

# In[15]:


# string.title()

sentence = 'benedict cumberbatch can be called many names and people still know who you are talking about.'
# Makes The First Letter Of Every Word Capitalized 
titles = sentence.title()
# MAKES EVERYTHING CAPS
uppers = sentence.upper()
# makes everything lowercase
lowers = sentence.lower()

name = 'bUrTON GUSTer'
name = name.title()
name


# ### String Exercise <br>
# <p>Strip all white space and capitalize every name in the list given</p>

# In[26]:


names = ['    coNNor', 'max', ' EVan ', 'JORDAN']
# HINT: You will need to use a for loop for iteration
# hint 2.0: you need to change the values in that list
            # use an index loop for this
for i in range(len(names)):
    print(i, names[i])
    names[i] = names[i].title().strip()
    print(i, names[i])

print(names)


# ### Working With Lists

# ##### min()

# In[41]:


# min(list)
nums = [123, 342.10, 1, 23, 4589071, 3, 17.47]


# whats happening in the background of the built-in min function
def min(list_of_numbers):
    ans = list_of_numbers[0]
    for n in list_of_numbers:
        if n < ans:
            ans = n
    return ans

min(nums)


# ##### max()

# In[42]:


# max(list)

max(nums)


# ##### sum()

# In[43]:


# sum(list)
# requires numerical data types

sum(nums)


# ##### sorted()

# In[59]:


# sorted(list)
# out of place algorithm
# does not modify original, makes copy
# returns the new list

nums = [123, 342.10, 1, 23, 4589071, 3, 17.47]
nums_sorted = sorted(nums, reverse=True)
nums_sorted


# ##### .sort() <br>
# <p>Difference between sort and sorted, is that sorted doesn't change original list it returns a copy, while .sort changes the original list</p>

# In[57]:


# list.sort()
# in-place algorithm
# modifies original

nums.sort()
nums

animals = ['27 foxes', '@dolphin', '  sea cucumber', '1monkey', 'albatross', 'Albatross']
nothin = animals.sort()
print(animals)
print(nothin)
# use sorted when you don't want to alter original list, use .sort() when you want to alter original list


# In[79]:


# when you set a variable equal to a function call
# var = max([12, 3, 4])
# whats actually happening is that when that line of code runs
# the variable is set equal to the return value of the function
# not the function call itself

# why i could only do this with a list
# because I always forget strings are immutable. you cant change strings
mylist = ['foxes']

def example(something):
    # IGNORE WHATS HAPPENING ON LINE 14 OTHER THAN THAT IT IS MODIFYING THE ORIGINAL LIST
    # THIS IS NOT COPYING A LIST LIKE BELOW - THIS IS SOMETHING DIFFERENT THAT YOU DO NOT NEED TO KNOW FOR NOW
    something[:] = something + ['birds', 'ducks']
    return None

print(example(mylist))

print(mylist)


# ##### Copying a List

# In[82]:


# [:] copies a list, doesn't alter original
# this is a form of List Slicing
names = ['Burton Guster', 'Bruton Gaster', 'Lavender Gooms', 'Doctor McTock', 'Methuselah Honeysuckle']
print(names)
othernames = names[:]
print(othernames)

# can also copy a list using .copy()
othernamestwo = names.copy()
print(othernamestwo)


# In[ ]:


# example why you might copy
# I want to know which of my names start with B
# I don't want to delete my other names - I care about knowing all of my names for future use
# So, I would make a copy of my list and modify that
# This would maintain whats called 'Data Integrity'
    # in other words, we don't lose any data when working with our data


# ##### 'in' keyword

# In[83]:


# in and not in are used for membership tests
# they are conditional operators
# see day 1 conditionals for more detail

names = ['Burton Guster', 'Bruton Gaster', 'Lavender Gooms', 'Doctor McTock', 'Methuselah Honeysuckle']

if 'Bruton Gaster' in names:
    print('Thats not my name.')


# ##### 'not in' keyword

# In[84]:


if 'Gus TT Showbiz' not in names:
    print('Thats not my name.')


# ##### Checking an Empty List

# In[96]:


# if l_1: or if l_1 == []:

l_1 = []
print(type(l_1), len(l_1))

# evaluates to True if l_1 is empty
if l_1 == []:
    print('yea its empty')

# evaluates to False if l_1 is empty
if l_1:
    print('wont print')

# evaluates to True if l_1 is empty
if not l_1:
    print('empty #2')

x = None
if not x:
    print('var is none means not var evals to True')


# ##### Removing Instances with a Loop

# In[100]:


# while, remove
animals = ['bird', 'bird', 'government drone', 'bird', 'cat', 'dog', 'squirrel']

# can use the list.remove() method to remove one instance of a value
animals.remove('bird')
print(animals)

# to remove all instances, use a while loop with .remove() and our in keyword
while 'bird' in animals:
    animals.remove('bird')
print(animals)


# ### List Exercise <br>
# <p>Remove all duplicates<br><b>Extra: Create a program that will remove any duplicates from a given list</b></p>
#  Do this for homework in addition to the two exercises at the bottom

# In[ ]:


names = ['connor', 'connor', 'bob', 'connor', 'evan', 'max', 'evan', 2, 2, 2, 3, 3, 4, 'bob', 'kevin']
# Hint 1: You will need an append
# Hint 2: Using an empty list will make life easier



# ### List Comprehensions <br>
# <p>Creating a quickly generated list to work with<br>*result*  = [*transform*    *iteration*         *filter*     ]</p>

# ##### In a list comprehension we have a few pieces:
# 1. The first is the counter/ variable - IN this the variable is x
# 2. then we have a transform for the variable
# 3. The finale part of a list comp is called the condition
# 
# ```python
#     [transform, variable, condition]
# ```

# In[106]:


# number comprehension

# With a regular for loop
cubes = []
for number in range(1,11):
    cubes.append(number**3)
print(cubes)

# IN a list comprehension we have a few pieces:
# The first is the counter/ variable - IN this the variable is x
# Then we have a transform for the variable 
# The finale part of a list comp is called the condition
#[variable, transform, condition]

cubes2 = [x**3 for x in range(1,11)]
print(cubes2)


# In[107]:


cubesnotdiv3 = [x for x in cubes2 if x%3 != 0]
print(cubesnotdiv3)


# In[111]:


# nesting list comprehension is a thing you can do
# kind of like nesting for loops
nestedexp = [[x**y for y in range(2,5)] for x in range(1,11)]
print(nestedexp)

# same thing with nested for loops
nestedexploop = []
for x in range(1,11):
    exps = []
    for y in range(2,5):
        exps.append(x**y)
    nestedexploop.append(exps)
print(nestedexploop)


# There are a few benefits to using List comprehensions. The most obvious would be that we now have shorter code to work with instead of using 3+ lines of code in the for loop variant.
# 
# Another is an added benefit to memory usage. Since the list's memory is allocated first before adding elements to it, we don't have to resize the list once we add elements to it.
# 
# Lastly, list comprehensions are considered the "pythonic" way to write code by the PEP8 standards (Python Style Guide)

# In[116]:


# square number comprehension
squares = [x**2 for x in range(1,20)]
print(squares)


# In[118]:


# string comprehension
yells = ['a'*x+'h' for x in range(1,20)]
print(yells)

animals = ['bird', 'bird', 'government drone', 'bird', 'cat', 'dog', 'squirrel']
animals = [x+'!' for x in animals]
print(animals)


# ### Tuples <br>
# <p><b>Defined as an immutable list</b></p><br>Seperated by commas using parenthesis

# In[122]:


# syntax clue for a tuple is () without a word right before
# var = (something, something) <-- tuple
# var = something(something, something) <-- function call

mytuple = ('you', 'cant', 'change', 'me')

animals = ['bird', 'bird', 'government drone', 'bird', 'cat', 'dog', 'squirrel']
animaltuple = tuple(animals)

# just like a list, tuples are iterable, indexed, ordered
# but they are IMMUTABLE -> cant be changed after creation

#access a value just like a list
print(animaltuple[2])

#loop
for animal in animaltuple:
    print(animal)

# cannot modify
# ERROR on line below
# animaltuple[2] = 'nope'


# ##### sorted()

# In[125]:


anituple = ('bird', 'government drone', 'bird', 'cat', 'dog','bird',  'squirrel')
sortedanimals = sorted(anituple)
print(sortedanimals)
# can call sorted on a tuple bc it makes a copy as a list and sorts that list
# if you want a tuple again, just convert the resulting list
sortedanimals = tuple(sortedanimals)
print(sortedanimals)


# ##### Adding values to a Tuple

# In[129]:


anituple = ('bird', 'government drone', 'bird', 'cat', 'dog','bird',  'squirrel')
# cannot directly add a value to a tuple
# but we can convert to a list, modify, then convert back
print(anituple)
anituple = list(anituple)
print(anituple)
anituple.append('fox')
print(anituple)
anituple = tuple(anituple)
print(anituple)


# ### More on type conversion
# <p>Knowing common type conversions can allow you to modify data in ways that wouldn't normally work</p>
# <p>Important type conversion below: string to list of words, string to list of chars, list to string </p>

# In[142]:


# 1. string to list of individual characters
mystring = 'fennec fox'
listchars = list(mystring)
print(listchars)

# 2. string to list of words
# string.split(optional_delimiter) defaults to whitespace
listwords = mystring.split() # most common usage
esplit = mystring.split('e')
nnsplit = mystring.split('nn')
print(listwords)
print(esplit)
print(nnsplit)

# 3. converting a list to a string
# .join method
# separator.join(list)
# join on a single space
wordsjoin = ' '.join(listwords)
print(wordsjoin)
# join on nothing (empty string)
lettersjoin = ''.join(listwords)
print(lettersjoin)
# join on whatever you want
weirdjoin = '@'.join(listwords)
print(weirdjoin)


# ## Functions

# ##### User-Defined vs. Built-In Functions

# In[152]:


# we've been using function this whole time even if you haven't realized it
# max(), min(), range(), len(), list(), int(), any_word(), something.otherthing(thing) <-- all function calls
# they're all running a process/algorithm that has been defined and named
# those are mostly examples of built-in function
# all we have to do with a built-in is the FUNCTION CALL
# we don't need to worry about defining a built-in -> its definition is built-in to python

# calling a built-in # THIS IS A FUNCTION CALL
print('Look at this print function being called on this string.')

# a user-defined function on the other hand
# before we can use it/call it/run it
# we have to actually define what it does, what its called, and how to use it
# its a more involved process than using a built-in
# but it gives us lots of freedom in how we design our processes/algorithms for use in function

# the blueprint for defining a function is as follows:
# def function_name(parameters):
    # do stuff
    # return something

# def keyword is our syntax clue that a function is being defined
def hello(a_name):
    greeting = f'Hello, {a_name}!'
    return greeting
# function definition is above^ but doesn't actually DO anything yet

#if we want our function to actually DO stuff, we need to CALL it
# function_name(values for parameters)
print(hello('Marwa'))
print(hello('Aaron'))
print(hello('Todd'))


# ##### Accepting Parameters

# In[155]:


# like we saw in the above example, a functions parameters are inputs that can be passed to the function
# in the function definition, we need to provide placeholder variables for whatever might be passed as a parameter
# these placeholders also determine how many things can be passed as input to our function
def paint_animal(animal, color):
    return f'You painted the {animal} {color}. Why?'

fox = 'Fennec Fox'
bird = 'Golden Eagle'
unkillablebear = 'Tardigrade'

color_a = 'chartreuse'
color_b = 'purple'
color_c = 'indigo'

# follow the position specified in our function definition (line 4) when passing in values to our function call (line 16)
print(paint_animal(unkillablebear, color_c))
print(paint_animal(fox, color_a))
print(paint_animal(fox, color_c))
print(paint_animal('Bear', 'magenta'))


# In[ ]:


# Lets say your working on a whiteboard or a codewars question
# And they give you the following info
# Example:
# count_animals(sentence) -> 3

# that is telling you that your function should accept one string as a parameter
# and return one integer as output
# so you could immediately know to set up your function like this:
def count_animals(a_string_sentence):
    integer_count = 0
    # then figure out how to count the animals in the string
    return integer_count

# other example
# Input: 'Fennec Fox', 'chartreuse'
# Output: 'The Fennec Fox drank some Chartreuse.'
def cocktails(a_person_or_animal, a_drink)
    sentence = ''
    # then figure out how to build the sentence
    return sentence


# ##### Default Parameters

# In[161]:


# you've seen with some built-ins there are parameters that have a default behavior,
    # and you can specify some other behavior
# examples being range(10) vs. range(1, 10, 2) # start and step of range are default 0 and 1
    # or print('hey') vs. print('hey', end='!') # end of print is default '\n'
    # or sorted(list, reverse=True) # reverse of sorted is default False

# you can do defaults with your own functions
# lets make the animal default to a fox for our paint function
# we provide the default value in the parenthesis of the definition when we give the parameter a name
def paint_default_animal(color, animal='fox'):
    return f'You painted the {animal} {color}. Why?'

# default arguments must follow non-default arguments so we flipped order of color and animal

# call the function! don't need an animal name! can provide one if we want!
print(paint_default_animal('fire truck red'))
print(paint_default_animal('blue', animal='shark')) # using keyword argument for animal
print(paint_default_animal('blue', 'shark')) # using positional argument for shark


# ##### Making an Argument Optional

# In[167]:


# same idea as a default argument
# you just have it default to something specific to nullify its effect
def addition(x, y, z=0):
    return x + y + z
print(addition(2, 3))

def greeting(first, middle='', last='Smith'):
    return f'Hello {first} {middle} {last}'
print(greeting('John'))


# ##### Keyword Arguments

# In[168]:


# last_name='Max', first_name='Smith' in the function call
print(paint_default_animal(animal='Fennec Fox', color='fire truck red'))
# see above


# # Creating a start, stop, step function

# In[174]:


def myrange(stop, start=0, step=1):
    nums = []
    while start < stop:
        nums.append(start)
        start += step
    return nums

print(myrange(12))
print(myrange(start=27, stop=99, step=17))


# ##### Returning Values

# In[177]:


# how the return keyword works
# the return keyword is a keyword, not a function
# you dont need parenthesis in your return line
# if you have parenthesis in your return line -> like return(thing) or return ('hello')
# you may inadvertently return a tuple

# you can only return one piece or collection of data
# like one list, one tuple, one string
# you cannot return seven integers independently

# as soon as a function reaches its return statement, the function stops
# similar to a break statement in a loop
def leap_year(year):
    if year%4 == 0:
        if year%100 == 0:
            if year%400 == 0:
                return True
            return False
        return True
    return False
leap_year(2000)

# you can have a function with no return statement -> that function will return None

# if you want to save the returned value from a function
# set a variable equal to the function call
leapyear2020is = leap_year(2000)
leapyear2020is


# ##### Docstring

# In[181]:


# the docstring is documentation attached to a function to help developers!
# good code has docstrings
# i always forget to write my docstrings
# docstrings are pulled up with help() or ?

def paint_animal(color, animal='fox'):
    """
        Function requires a color to be passed as a parameter.
        Optionally, an animal name can be passed.
        If no animal name is passed, defaults to 'fox'.
        Will ask you why you painted the animal that color.
    """
    return f'You painted the {animal} {color}. Why?'

get_ipython().run_line_magic('pinfo', 'paint_animal')
help(paint_animal)


# ##### Using a User Function in a Loop

# In[185]:


def paint_animal(animal, color='black'):
    return f'You painted the {animal} {color}. Why?'

fox = 'Fennec Fox'
bird = 'Golden Eagle'
unkillablebear = 'Tardigrade'

color_a = 'chartreuse'
color_b = 'purple'
color_c = 'indigo'

animals = [fox, bird, unkillablebear]
colors = [color_a, color_b, color_c]

#for x in animals:
    #print(paint_animal(x))
    
# orrrrrr
paintings = []
for animal in animals:
    for color in colors:
        paintings.append(paint_animal(animal, color))
print(paintings)


# ## Function Exercise <br>
# <p>Write a function that loops through a list of first_names and a list of last_names, combines the two and return a list of full_names</p>

# In[ ]:


first_name = ['John', 'Evan', 'Jordan', 'Max']
last_name = ['Smith', 'Smith', 'Williams', 'Bell']

# Output: ['John Smith', 'Evan Smith', 'Jordan Williams', 'Max Bell']


# ## Scope <br>
# <p>Scope refers to the ability to access variables, different types of scope include:<br>a) Global<br>b) Function (local)<br>c) Class (local)</p>

# In[191]:


# global variables are defined outside of functions and/or classes
# global variables can be used everywhere
# global scope
animal = 'global fox'
print(animal)

# function definition
# variables defined inside a function have local scope
# they can only be accessed and used inside of that function
def afunc():
    local_variable = 'local bear'
    print(local_variable)
    print(animal)
    # if we want to use it outside of the function, we have to return it
    return local_variable

#function call
afunc()

# saving the function call so that the return value is a globally scoped variable
global_bear = afunc()
print('now global ' + global_bear)

# trying to print a locally scoped variable globally will produce a 'not defined' error
# run this for a fun error: print(local_variable)


# # Exercises

# ## Exercise 1 <br>
# <p>Given a list as a parameter,write a function that returns a list of numbers that are less than ten</b></i></p><br>
# <p> For example: Say your input parameter to the function is [1,11,14,5,8,9]...Your output should [1,5,8,9]</p>

# In[9]:





# ## Exercise 2
# 
# <br>
# <p>Write a function that takes in two lists and returns the two lists merged together and sorted<br>
# <b><i>Hint: You can use the .sort() method</i></b></p>

# In[3]:


l_1 = [1,2,3,4,5,6]
l_2 = [3,4,5,6,7,8,10]

#lets put them togtherrr

print ("The original list 1 is : " + str(l_1))
print ("The original list 2 is : " + str(l_2))
  
barbz = sorted(l_1 + l_2)
  
print ("The combined sorted list is : " + str(barbz))


# # Exercise 3
# ### List Exercise <br>
# <p>Remove all duplicates<br><b>Extra: Create a program that will remove any duplicates from a given list</b></p>
#  Do this for homework in addition to the two exercises at the bottom
# 

# In[4]:


names = ['connor', 'connor', 'bob', 'connor', 'evan', 'max', 'evan', 2, 2, 2, 3, 3, 4, 'bob', 'kevin']
# Hint 1: You will need an append
# Hint 2: Using an empty list will make life easier

names = ['connor', 'connor', 'bob', 'connor', 'evan', 'max', 'evan', 2, 2, 2, 3, 3, 4, 'bob', 'kevin']
print ("The original list is : " +  str(names))

res = []
[res.append(x) for x in names if x not in res]
  
# printing list after removal 
print ("The list after removing duplicates : " + str(res))


# In[ ]:




