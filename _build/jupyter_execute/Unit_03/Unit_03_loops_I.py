#!/usr/bin/env python
# coding: utf-8

# # Unit 03: Loops, Pandas and Simple Plotting I
# 
# <a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons Licence" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" title='This work is licensed under a Creative Commons Attribution 4.0 International License.' align="right"/></a>
# 
# Author: Dr Claire Hobday   
# 
# Email: claire.hobday@ed.ac.uk
# 
# ## Learning objectives:
# 
# By the end of this unit, you should be able to
# - use in-built functionality in Python
# - import modules and libraries 
# - use the `math` module to do some simple scientific computing tasks
# - develop more `pandas` skills to deal with large volumes of data
# - use logical operations to filter data
# - understand and use the different types of loops to do repetitive tasks including:
#     - `for`
#     - `if`
#     - `else`/`elif`
#     - `while`
#     - `break`
# - combine these tools to analyse data in a large file containing information about the periodic table
# - use tools from Python to understand trends in the periodic table
# 
# Some of the material was adapted from [Python4Science](https://github.com/Degiacomi-Lab/python4science/blob/master/2_Python_numerical_data.ipynb), as well as [Software Carpentries](http://swcarpentry.github.io/python-novice-gapminder/index.html).

# ### Table of Contents
# 1. [Working with Libraries](#1-working-with-libraries)  
#    1.1 [Importing Libraries](#11-importing-libraries)     
#    1.2 [Tasks ](#tasks-1)   
# 2. [Working with the Pandas Library](#2-working-with-the-pandas-library)
# 3. [Loops](#3-loops)    
#    3.1 [For Loops](#31-for-loops)   
#    3.2 [Tasks](#tasks-321)    
#    3.3 [Conditional Loops](#32-conditional-loops)    
#    3.4 [Tasks](#tasks-3)
#    
# [Unit 03 Loops II](Unit_03_loops_II.ipynb)
# 
# 
# ### Links to documentation
# 
# You can find useful information about using `math` and `pandas` at
# - [math](https://docs.python.org/3/library/math.html)
# - [pandas](https://pandas.pydata.org/)
# - [anaconda](https://anaconda.org)
# - [PyPI](https://pypi.org)

# **<span style="color:black">Jupyter Cheat Sheet</span>**
# - To run the currently highlighted cell and move focus to the next cell, hold <kbd>&#x21E7; Shift</kbd> and press <kbd>&#x23ce; Enter</kbd>;
# - To run the currently highlighted cell and keep focus in the same cell, hold <kbd>&#x21E7; Ctrl</kbd> and press <kbd>&#x23ce; Enter</kbd>;
# - To get help for a specific function, place the cursor within the function's brackets, hold <kbd>&#x21E7; Shift</kbd>, and press <kbd>&#x21E5; Tab</kbd>;

# ## 1. Working with Libraries <a id='1-working-with-libraries'></a>

# ### 1.1 Importing Libraries <a id="11-importing-libraries"></a>

# ### Most of the power of a programming language is in its libraries.
# 
# - A library is a collection of files (called modules) that contains functions for use by other programs.
# - May also contain data values (e.g. numerical constants) and other things.
# A library’s contents are supposed to be related, but there’s no way to enforce that.
# - The Python standard library is an extensive suite of modules that comes with Python itself.
# - Many additional libraries are available from anaconda or PyPI (the Python Package Index, see above for links).

# ### A program must import a library module before using it.
# - Use `import` to load a library module into a program’s memory.
# - Then refer to things from the module as `module_name.thing_name`.
#   - Python uses `.` to mean “part of”.
# - We will be using a library called `pandas`

# ### Import specific items from a library module to shorten programs.
# - Use `from ... import ...` to load only specific items from a library module.
# - Then refer to them directly without library name as prefix.
# 
# Run the cell below to import all the required libraries for this unit:

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt

# Make the helper functions accessible
import sys
import os.path
sys.path.append(os.path.abspath('../'))
from helper_functions.mentimeter import Mentimeter


# ### Quick aside on printing variables
# 
# To print variables together with strings, we can use [f-strings](https://realpython.com/python-f-strings/).
# 
# The structure of f-strings is as follows: 
# ```python
# my_variable = 4
# print(f"some text before a variable: {my_variable}")
# ```
# This prints the following:
# ```python
# some text before a variable: 4
# ```

# Run the below cell to import $\cos$ and $\pi$ from the library `math`:

# In[ ]:


# We are importing the functions cos and the value pi from the library math
from math import cos, pi

print(f"cos(pi) is {cos(pi)}")


# ### Create an alias for a library module when importing it to shorten programs.
# 
# - Use `import ... as ...` to give a library a short alias while importing it.
# - Then refer to items in the library using that shortened name.

# In[ ]:


import math as m

print(f"cos(pi) is {m.cos(m.pi)}")


# ## Tasks 1<a id="tasks-1"></a> 

# <div class="alert alert-success">
# <b>Task 1.1: Jigsaw Puzzle (Parson’s Problem) Programming Example</b>
# 
# 
# Rearrange the following statements so that a random DNA base is printed and its index in the string. Remember that you've already imported math above! You can check it in an empty cell below to understand what it is doing. 
#     
# </div>

# In[ ]:


from IPython.display import IFrame
IFrame("https://parsons.herokuapp.com/puzzle/7cf55d16a0454de580f31418505f3b54", width=1000, height=400)


# In[ ]:


# Test out the code in this cell once you have the right order!


# <details><summary {style='color:green;font-weight:bold'}> Click here to see solution to Task 1.1 </summary>
#     
# ```python
# import math 
# import random
# bases = "ACTTGCTTGAC" 
# n_bases = len(bases)
# idx = random.randrange(n_bases)
# print(f"Random base {bases[idx]} base index {idx}.")
# 
# ```
#  </details>

# <div class="alert alert-success">
# <b>Task 1.2: Importing With Aliases</b>
# 
# 
# 
# 1. Fill in the blanks so that the program below prints `90.0`.
# 2. Rewrite the program so that it uses `import` without `as`.
# 3. Which form do you find easier to read?
#     
# </div>

# In[ ]:


# Question 1
import math as m
angle = # FIXME.degrees(# FIXME.pi / 2)
print(# FIXME)


# In[ ]:


# Question 2


# <details><summary {style='color:green;font-weight:bold'}> Click here to see solution to Task 1.2 </summary>
#     
# Filling in the right variables:  
#     
# ```python
# import math as m
# angle = m.degrees(m.pi / 2)
# print(angle)   
#     
# ```
# Re-writing the program without an import as:
#     
# ```python
# import math
# angle = math.degrees(math.pi / 2)
# print(angle)  
#     
# ```   
#     
# *Explanation*:
#   
# Since you just wrote the code and are familiar with it, you might actually find the first version easier to read. But when trying to read a huge piece of code written by someone else, or when getting back to your own huge piece of code after several months, non-abbreviated names are often easier, except where there are clear abbreviation conventions.
# 
#  </details>

# <div class="alert alert-success">
# <b>Task 1.3: Importing specific items</b>
# 
# 
# 
# 1. Import the exponential function from the math libary.
# 2. Use it to work out $e^{10}$.
# 3. Import a function from math which will allow you to raise a number to a power of your choice.
# 4. Raise $6^5$
#     
# </div>

# In[ ]:


# FIXME


# <details><summary {style='color:green;font-weight:bold'}> Click here to see solution to Task 1.3 </summary>
#     
# Filling in the right variables:  
#     
# ```python
# #1
# from math import exp 
# #2
# number= exp(10)
# print(number)
# #3
# from math import pow
# #4
# powered = pow(6,5)
# print(powered)   
# ```   
#     
# *Explanation*:
#   
# The first part should be relatively straightforward. For part 3, you may need to google the math library and read the documentation to find the function that you need to raise a number to the power of another number. 
# 
#  </details>

# <div class="alert alert-info"> <b>Key Points</b>
# 
# - Most of the power of a programming language is in its libraries.
# - A program must import a library module in order to use it.
# - Import specific items from a library to shorten programs.
# - Create an alias for a library when importing it to shorten programs.
#     
#  </div>

# # 2. Working with the Pandas Library <a id="2-working-with-the-pandas-library"></a>
# 
# In [Unit 02](../Unit_02/Unit_02_variables_II.ipynb), we looked at a couple of different ways of opening files, in this session we are going to exclusively use `Pandas`. 
# 
# Pandas is a library in Python that works much like Excel, but we have the added advantage of being able to manipulate the data in a programmatic way. 
# 
# 
# The community-agreed alias for `pandas` is `.pd`, so loading `pandas as pd` is assumed **standard practice** for all of the pandas documentation.

# In[ ]:


import pandas as pd


# ### Import the data

# Now, we need to import the data into what pandas calls a `DataFrame`, which takes the input data and formats it as a sort of "spreadsheet" with this form:
# 
# 
# 
# ![pandas-data-structure.svg](images/pandas-data-structure.svg)

# In[ ]:


# Use pandas to read the csv file:
data = pd.read_csv("files/ptable.csv") 
# View the imported dataframe, note how the index column "element" is in bold: 
data 


# Now that we've imported this data, we will learn some more fundamental python concepts in order to examine the data at the end of the session. 
# 
# <br>

# ### Accessing the dataframe <a id="accessing-the-dataframe"></a>
# 
# We are now going to try and view the dataframe in different ways </br>
# - `data.head()` shows us the first 5 lines of the dataframe.... Note how python counts from 0. </br>
# - `data.tail()` shows us the last 5 lines of the dataframe.</br>
# - `data.columns` lists us all the column headers which are properties associated with the elements.
# 
# Test them out below:

# In[ ]:


data.head()


# In[ ]:


data.tail()


# In[ ]:


data.columns


# We might also be interested in knowing what the datatypes are for the columns.

# In[ ]:


print(f"Period is data type {data['Period'].dtype}")


# It is also possible to change the datatype of a column in a dataframe using `.astype()` function.

# In[ ]:


data["Period"] = data["Period"].astype(float)


# In[ ]:


print(f"Period is data type {data['Period'].dtype}")


# <div class="alert alert-info">
# Once we learn a little more about how to play around with arrays, we will come back and analyse this data.
# </div>

# # 3. Loops
# 
# <a id='3-loops'></a>
# ![loop.png](images/loop.png)
# 
# 
# A loop is used for iterating over a set of statements.
# There are many different kinds of loops that can be useful in different situations. We are going to go through some of the most common types of loops. 

# ## 3.1 For loops
# <a id='31-for-loops'></a>
# This loop is used for iterating over some kind of a sequence. That can be a list, tuple, dictionary, string, etc.
# 
# Everything that is inside the for statement is going to be executed a number of times.
# ![loop2.png](images/loop2.png)
#     
#   
# 
# If we think about how we would define a `for` loop in python it would have the structure:
# ```Python
# for variable in iterable:
#     statement(s) 
# ```
# 
# where:
# * `variable` is a variable 
# * `iterable` is a collection of objects such as a list or tuple
# * `statement(s)` in the loop body (denoted by the **indent**) are executed once for each item in **iterable**.
# 
# The loop variable `variable` takes on the value of the next element in `iterable` each time through the loop, until we have iterated through all items in `iterable`.

# Let's take a look at some simple examples that show us how powerful `for` loops can be, and how they must be properly structured to be interpreted by Python. 

# ### Example 1
# 
# The first line of the `for` loop must end with a colon, and the body must be indented.
# 

# In[ ]:


for number in [2,3,5]:
    print(number)


# This `for` loop is equivalent to:

# In[ ]:


print(2)
print(3)
print(5)


# We can see that the `for` loop is a much more efficient way of doing this task, than having to type of `print(value)`. 

# In[ ]:


# FIXME
for number in [2,3,5]:
print(number)


# In[ ]:


# FIXME
for number in [2,3,5]
    print(number)


# ### Example 2

# Loop variables can be called anything. So please try to make them be as meaningful as possible

# In[ ]:


for kitten in [2, 3, 5]:
    print(kitten)


# In[ ]:


for numbers in [2,3,5]:
    print(numbers)


# ### Example 3

# The body of a loop can contain many statements.
# However, its best practise to keep a loop to no more than a few lines long.

# In[ ]:


primes = [2, 3, 5]
for p in primes:
    squared = p ** 2
    cubed = p ** 3
    print(p, squared, cubed)


# ### Example 4
# 

# Use `range` to iterate over a sequence of numbers.
# 
# The built-in function `range` produces a sequence of numbers.
# 
# Not a list: the numbers are produced on demand to make looping over large ranges more efficient. Its easier than typing `[2,3,5,7,9,11,13]` like we have done in above examples.
# 
# `range(N)` is the numbers `0..N-1`
# 
# Exactly the legal indices of a list or character string of length N
# 
# e.g. `range(5)` would be `0,1,2,3,4`

# In[1]:


print("a range is not a list: range(0, 3)")
for number in range(0, 3):
    print(number)


# ### Example 5 
# 

# The Accumulator pattern turns many values into one.
# 
# A common pattern in programs is to:
#  1. Initialize an accumulator variable to zero, the empty string, or the empty list.
#  2. Update the variable with values from a collection.

# In[ ]:


# Sum the first 10 integers.
total = 0
for number in range(10):
    total = total + (number + 1)
print(total)


# - Read `total = total + (number + 1)` as:
#  - Add 1 to the current value of the loop variable `number`.
#  - Add that to the current value of the accumulator variable `total`.
#  - Assign that to `total`, replacing the current value.
# - We have to add `number + 1` because `range` produces `0..9`, not `1..10`.

# ## Tasks 2 <a id="tasks-2"></a>

# <div class="alert alert-success">
# <b>Task 2.1: Practice Accumulating 1</b>
# 
# 
# Fill in the blanks 
#     
# </div>

# In[ ]:


# Total length of the strings in the list: ["red", "green", "blue"] => 12
total = 0
for word in ["red", "green", "blue"]:
    ____ = ____ + len(word) # FIXME
print(total)


# <details><summary {style='color:green;font-weight:bold'}> Click here to see solution to Task 2.1 </summary>
#     
# ```python
# total = 0
# for word in ["red", "green", "blue"]:
#     total = total + len(word)
# print(total)
# ```
# </details>  

# <div class="alert alert-success">
# <b>Task 2.2: Practice Accumulating 2</b>
# 
# Fill in the blanks 
#     
# </div>

# In[ ]:


# List of word lengths: ["red", "green", "blue"] => [3, 5, 4]
lengths = ____ # FIXME
for word in ["red", "green", "blue"]:
    lengths.____(____) # FIXME
print(lengths)


# <details><summary {style='color:green;font-weight:bold'}> Click here to see solution to Task 2.2</summary>
#     
# ```python
#  
# lengths = []
# for word in ["red", "green", "blue"]:
#     lengths.append(len(word))
# print(lengths)
# 
# ```
# 
# 
#  </details>

# <div class="alert alert-success">
# <b>Task 2.3: Practice Accumulating 3</b>
# 
# Fill in the blanks
# </div>

# In[ ]:


# Concatenate all words: ["red", "green", "blue"] => "redgreenblue"
words = ["red", "green", "blue"]
result = ____  # FIXME
for ____ in ____: # FIXME
    ____  # FIXME
print(result)


# <details><summary {style='color:green;font-weight:bold'}> Click here to see solution to Task 2.3 </summary>
#     
# ```python
# words = ["red", "green", "blue"]
# result = ""
# for word in words:
#     result = result + word
# print(result)
# 
# ```
# 
# 
#  </details>
# 

# <div class="alert alert-success">
# <b>Task 2.4: Create a whole loop</b>
# 
# 
# Start out with an empty string `acronym=""`.
# Generate a loop that uses the words 'red', 'green', 'blue' and the function `upper()` that by the end of the loop the acronym contains "RBG" when you type `print(acronym)`
#     
# </div>

# In[ ]:


# FIXME
acronym = ""


print(acronym)


# <details><summary {style='color:green;font-weight:bold'}> Click here to see solution to Task 2.4 </summary>
#     
# ```python
# acronym = ""
# for word in ["red", "green", "blue"]:
#     acronym = acronym + word[0].upper()
# print(acronym)
# 
# ```
# 
# 
#  </details>

# <div class="alert alert-success">
# <b>Task 2.5: Cumulative Sum</b>
# 
# 
# Reorder and properly indent the lines of code below so that they print a list with the cumulative sum of data. The result should be `[1, 3, 5, 10]`.
#     
# </div>

# In[ ]:


# FIXME
cumulative.append(sum)
for number in data:
cumulative = []
sum += number
sum = 0
print(cumulative)
data = [1,2,2,5]


# <details><summary {style='color:green;font-weight:bold'}> Click here to see solution to Task 2.5</summary>
#     
# ```python
# data = [1,2,2,5]
# cumulative = []
# sum = 0
# for number in data:
#     sum += number
#     cumulative.append(sum)
# print(cumulative)
# 
# ```
# 
# 
#  </details>

# <div class="alert alert-success">
# <b>Task 2.6: Identifying Variable Name Errors</b>
# 
# 
# 1. Read the code below and try to identify what the errors are without running it.
# 2. Run the code and read the error message. What type of `NameError` do you think this is? Is it a string with no quotes, a misspelled variable, or a variable that should have been defined but was not?
# 3. Fix the error.
# 4. Repeat steps 2 and 3, until you have fixed all the errors.
#     
# </div>

# In[ ]:


for number in range(10):
    # use a if the number is a multiple of 3, otherwise use b
    if (Number % 3) == 0:
        message = message + a
    else:
        message = message + "b"
print(message)


# <details><summary {style='color:green;font-weight:bold'}> Click here to see solution to Task 2.6 </summary>
#     
# ```python
# message = ""
# for number in range(10):
#     # use a if the number is a multiple of 3, otherwise use b
#     if (number % 3) == 0:
#         message = message + "a"
#     else:
#         message = message + "b"
# print(message)
# 
# ```
# ##### Explanation:
# The variable `message` needs to be initialized and Python variable names are case sensitive: `number` and `Number` refer to different variables.
# 
#  </details>
# 

# <div class="alert alert-info"> <b>Key Points:</b>
# 
# - A for loop executes commands once for each value in a collection.
# - A `for` loop is made up of a collection, a loop variable, and a body.
# - The first line of the `for` loop must end with a colon, and the body must be indented.
# - Indentation is always meaningful in Python.
# - Loop variables can be called anything (but it is strongly advised to have a meaningful name to the looping variable).
# - The body of a loop can contain many statements.
# - Use `range` to iterate over a sequence of numbers.
# - The Accumulator pattern turns many values into one.
#                                                    
# /div>

# ## 3.2 Conditional Loops <a id='32-conditional-loops'></a>

# Computer programming is often referred to as a "language" and often we use similar nomenclature to traditional languages. Here we will discover how **conditional** `loops` are interpretted by Python. Conditionals are used much like the tense in languages to speculate about what could happen with respect to an if clause. 
# 
# E.g. If it rains, take an umbrella. Or, if the pH is below 7, it's acidic. 
# 
# Notice how the first phrase controls the content of the second phrase.
# 
# E.g. If it's sunny, wear sunscreen. Or if the pH is above 7, it's basic. 
# 
# 
# We could take this analogy and allow more options,
# e.g.  if the pH is above 7, it's basic. Otherwise (or else) it's acidic. Notice how we can categories the information by these conditional statements. 
# 
# 
# We can use `if` statements to allow our computer programs to do different things for different data. 

# ### Use `if` statements to control whether or not a block of code is executed

# ### Example 6 - `if`

# Use an `if` statement to control whether or not a block of code is executed.
# - An `if` statement (more properly called a conditional statement) controls whether some block of code is executed or not.
# - Structure is similar to a `for` statement:
#     - First line opens with `if` and ends with a colon
#     - Body containing one or more statements is indented (usually by 4 spaces or a tab)

# In[ ]:


mass = 3.54
if mass > 3.0:
    print(f"{mass} is large")


# In[ ]:


mass = 2.07
if mass > 3.0:
    print(f"{mass} is large")


# Things that you should notice:
# - The importance of ending the first line of the `for` loop in a colon.
# - How the computer does not return anything in the second code block as it does not meet the `if` statement criteria. 

# ### Example 7 - `if`
# 

# Conditionals are often used inside loops.
# - Not much point using a conditional when we know the value (as above).
# - But useful when we have a collection to process.

# In[ ]:


masses = [3.54, 2.07, 9.22, 1.86, 1.71]
for mass in masses:
    if mass > 3.0:
        print(f"{mass} is large")


# ### Example 8 - `if` and `else`

# Use `else` to execute a block of code when an `if` condition is not true.
# - `else` can be used following an `if`.
# - Allows us to specify an alternative to execute when the `if` statement criterie is not met.

# In[ ]:


masses = [3.54, 2.07, 9.22, 1.86, 1.71]
for mass in masses:
    if mass > 3.0:
        print(f"{mass} is large")
    else:
        print(f"{mass} is small")


# ### Example 9 - `if` and `elif`

# Use `elif` to specify additional tests.
# - May want to provide several alternative choices, each with its own test.
# - Use `elif` (short for “else if”) and a condition to specify these.
# - Always associated with an `if`.
# - Must come before the `else` (which is the “catch all”).

# In[ ]:


masses = [3.54, 2.07, 9.22, 1.86, 1.71]
for mass in masses:
    if mass > 9.0:
        print(f"{mass} is HUGE")
    elif mass > 3.0:
        print(f"{mass} is large")
    else:
        print(f"{mass} is small")


# ### Example 10 - order of conditions

# Conditions are tested once, in order.
# - Python steps through the branches of the conditional in order, testing each in turn.
# - So ordering matters.

# In[ ]:


grade = 85
if grade >= 70:
    print("grade is C")
elif grade >= 80:
    print("grade is B")
elif grade >= 90:
    print("grade is A")


# We can see here that our condition is met in the first conditional `if` statement, so none of the `elif` statements are evaluated.

# ### Example 11 - using conditionals to evolve the values of variables
# 

# In the example below we use `if` and `else` within a `for` loop in order to change the value of `velocity`.
# 
# Notice:
# - the indent for the `for` loop and also for the `if` and `else` statements.
# - the use of the colon at the end of `for`, `if` and `else` statements.
# - The program must have a `print` statement outside the body of the loop to show the final value of velocity, since its value is updated by the last iteration of the loop.

# In[ ]:


velocity = 10.0
# Execute the loop 5 times
for i in range(5): 
    print(f"try {i}:{velocity}")
    if velocity > 20.0:
        print("moving too fast")
        velocity = velocity - 5.0
    else:
        print("moving too slow")
        velocity = velocity + 10.0
print(f"final velocity: {velocity}")


# # Tasks 3 <a id="tasks-3"></a>

# <div class="alert alert-success">
# <b>Task 3.1: Trimming values:</b>
# 
# 
# Fill in the blanks so that this program creates a new list containing zeroes where the original list’s values were negative and ones where the original list's values were positive.
# 
# </div>

# In[ ]:


original = [-1.5, 0.2, 0.4, 0.0, -1.3, 0.4]
result = ____ # FIXME
for value in original:
    if ____: # FIXME
        result.append(0)
    else:
        ____ # FIXME
print(result)


# Output should look like this:   
# ```[0, 1, 1, 1, 0, 1]```

# <details><summary {style='color:green;font-weight:bold'}> Click here to see solution to Task 3.1 </summary>
#     
# ```python
#     
# original = [-1.5, 0.2, 0.4, 0.0, -1.3, 0.4]
# result = []
# for value in original:
#     if value<0.0:
#         result.append(0)
#     else:
#         result.append(1)
# print(result)
# 
# ```
# 
# 
#  </details>

# <div class="alert alert-success">
# <b>Task 3.2: Initializing</b>
# 
# 
# Modify this program so that it finds the largest and smallest values in the list no matter what the range of values originally is.
# 
# What are the advantages and disadvantages of using this method to find the range of the data?
#     
# </div>

# In[ ]:


values = [...some test data...] # FIXME
smallest, largest = None, None
for v in values:
    if ____: # FIXME
        smallest, largest = v, v
    ____: # FIXME
        smallest = min(____, v) # FIXME
        largest = max(____, v) # FIXME
print(smallest, largest)


# <details><summary {style='color:green;font-weight:bold'}> Click here to see solution to Task 3.2 </summary>
#     
# ```python
# values = [-2,1,65,78,-54,-24,100]
# smallest, largest = None, None
# for v in values:
#     if smallest==None and largest==None:
#         smallest, largest = v, v
#     else:
#         smallest = min(smallest, v)
#         largest = max(largest, v)
# print(smallest, largest)
# 
# ```
# 
# 
#  </details>

# <div class="alert alert-info"> <b>Key Points:</b>
# 
# - Use `if` statements to control whether or not a block of code is executed.
# - Conditionals are often used inside loops.
# - Use `else` to execute a block of code when an `if` condition is *not* true.
# - Use `elif` to specify additional tests.
# - Conditions are tested once, in order.
# - Create a table showing variables' values to trace a program's execution.
# </div>

# # Next notebook
# 
# [Unit 03 Loops II](Unit_03_loops_II.ipynb)
