#!/usr/bin/env python
# coding: utf-8

# # Unit 02: First steps in Python I
# 
# <a rel="license" href="https://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons Licence" style="border-width:0" src="https://licensebuttons.net/l/by/4.0/88x31.png" title='This work is licensed under a Creative Commons Attribution 4.0 International License.' align="right"/></a>
# 
# Author: Dr Antonia Mey   
# Email: antonia.mey@ed.ac.uk
# 
# ### Learning objectives:
# * Interact with a Jupyter notebook
# * Declare variables
# * Print Variables
# * Getting help
# * Read data from a file
# 
# You will be using the following concepts:
# 
# - Variables
# - In-built functions such as `print()`
# 
# Some of the content is adapted from [Software carpentry lessons](http://swcarpentry.github.io/python-novice-gapminder/index.html).
# 
# ### Table of Contents
# 
# Notebook I (this notebook)   
# 1. [Variables and Assignments](#variables)    
# 2. [Data Types and Type Conversion](#datatypes)    
# 3. [Built in Functions and Getting Help](#debugging) 
# 
# Notebook II   
# 
# 4. [More Data Types: Booleans and Lists](Unit_02_variables_II.ipynb)
# 5. [More Data Types: Dictionaries and Tuples](Unit_02_variables_II.ipynb)  
# 6. [Reading Files](Unit_02_variables_II.ipynb)  
# 
# 
# ### Further reading for this topic
# 
# - [Software carpentry lessons](http://swcarpentry.github.io/python-novice-gapminder/index.html)
# 
# **<span style="color:black">Jupyter Cheat Sheet</span>**
# - To run the currently highlighted cell and move focus to the next cell, hold <kbd>&#x21E7; Shift</kbd> and press <kbd>&#x23ce; Enter</kbd>;
# - To run the currently highlighted cell and keep focus in the same cell, hold <kbd>&#x21E7; Ctrl</kbd> and press <kbd>&#x23ce; Enter</kbd>;
# - To get help for a specific function, place the cursor within the function's brackets, hold <kbd>&#x21E7; Shift</kbd>, and press <kbd>&#x21E5; Tab</kbd>;

# ### Warmup quiz

# An example of a typical mentimeter question to gauge the level of Python knowledge present in the class.
# <div>
# <img src="images/mentimeter_quiz.png" alt="drawing" width="400">
# </div>

# ## 1. Variables and Assignments
# <a id='variables'></a>
# ### Use variables to store values.
# 
# * Variables are names for values.
# * In Python the `=` symbol assigns the value on the right to the name on the left.
# * The variable is created when a value is assigned to it.
# * Here, Python assigns an `age` to a variable age and a name in quotes to a variable `first_name`.

# In[1]:


age = 42
first_name = 'Ahmed'


# * Variable names    
#    * can only contain letters, digits, and underscore _ (typically used to separate words in long variable names)
#    * cannot start with a digit
#    * are case sensitive (age, Age and AGE are three different variables)
# * Variable names that start with underscores like `__alistairs_real_age` have a special meaning so we won’t use these until we understand the convention.

# ### Use `print()` to display values

# * Python has a built-in function called `print()` that prints things as text.
# * Call the function (i.e., tell Python to run it) by using its name.
# * Provide values to the function (i.e., the things to print) in parentheses.
# * To add a string to the printout, wrap the string in single or double quotes.
# * The values passed to the function are called arguments.

# In[2]:


print(first_name, 'is', age, 'years old')


# * `print()` automatically puts a single space between items to separate them.
# * And wraps around to a new line at the end.

# <div class="alert alert-info"><b>Variables persist between cells</b>
#     
#     
# Be aware that <em>it is the order of execution of cells that is important</em> in a Jupyter notebook, not the <em>order</em> in which they appear. Python will remember <em>all</em> the code that was run previously, including any variables you have defined, irrespective of the order in the notebook. Therefore, if you define variables lower down the notebook and then (re)run cells further up, those defined further down will still be present. As an example, create two cells with the following content, in this order:
#     
# <code>print(atom)</code><br>
# <code>atom = Helium</code>
#     
# If you execute this in order, the first cell will give an error. However, if you run the first cell after the second cell it will print out 1. To prevent confusion, it can be helpful to use the <em>Kernel -> Restart & Run All</em> option which clears the interpreter and runs everything from a clean slate going top to bottom.</div>
#         

# ### Variables can be used in calculations
# ***
# We can use variables in calculations just as if they were values.    
# **Remember**, we assigned the value 42 to age a few lines ago.

# In[3]:


age = age + 3
print('Age in three years:', age)


# ### Python is case-sensitive
# 
# * Python thinks that upper- and lower-case letters are different, so `Name` and `name` are different variables.
# * There are conventions for using upper-case letters at the start of variable names so we will use lower-case letters for now.

# ### Use meaningful variable names
# 
# Python doesn't care what you call variables as long as they obey the rules (alphanumeric characters and the underscore).

# In[4]:


flabadab = 42
ewr_422_yY = 'Ahmed'
print(ewr_422_yY, 'is', flabadab, 'years old')


# ⚠️ **Use meaningful variable names** to help other people understand what the program does.
# The most important “other person” is your **future self**.

# ## Tasks:

# <div class="alert alert-success">
# <b>Task 1.1: Assign the following variables and print them:<br></b>
# 
# - Christina Miller to the variable name `Researcher_name`
# - Joseph Black to the variable name `Researcher_name_2`
# - 12 to the variable name `Carbon_mass`
# - Print all assigned variables
#     
# 
# </div>    

# In[5]:


# FIXME


# <details><summary {style='color:green;font-weight:bold'}> Click here to see the solution to Task 1.1</summary>
#     
# ```python
# 
# Researcher_name = "Christina Miller"
# Researcher_name_2 = "Joseph Black"
# Carbon_mass = 12
# print("Researcher one is:", Researcher_name)
# print("Researcher two is:", Researcher_name_2)
# print("The mass of carbon is:",Carbon_mass)
# 
# ```
# </details>

# <div class="alert alert-success">
# <b>Task 1.2: Arithmetic:<br></b>
#     
# In your head, or on paper, work out the following arithmetic as you would expect Python to do it using the rules of precedence.
#     
# 1. 20 + 7 * 9 - 4 = ?
# 2. 4 + 4 / 2 = ?
# 3. 2 * 5 ** 2 = ?
# 4. -9 / 3 ** 2 = ?
#     
# Check your answers using code cells.
#     
# Do you get the same answer if you assign variables to each value in the equation in 1?
# </b></div>

# In[6]:


# FIXME


# <details><summary {style='color:green;font-weight:bold'}> Click here to see the solution to Task 1.2</summary>
#     
# ```python
# 
# print(20 + 7 * 9 - 4)
# print(4 + 4 / 2)
# print(2 * 5 ** 2)
# print(-9 / 3 ** 2)
# 
# a = 20
# b = 7
# c = 9
# d = 4
# 
# print(a+b*c-d)
# 
# ```

# <div class="alert alert-success">
# <b>Task 1.3: Predicting Values:<br></b>
#     What is the final value of position in the program below? 
#     
# (Try to predict the value without running the program, then check your prediction, by using `print()` to query the value of position.)</div>

# In[7]:


initial = 'left'
position = initial
initial = 'right'


# In[8]:


# FIXME


# <details><summary {style='color:green;font-weight:bold'}> Click here to see the solution to Task 1.3</summary>
#     
# ```python
# print(position)
# ```
#     
# ##### Explanation
# The `initial` variable is assigned the value `'left'`. In the second line, the `position` variable also receives the string value `'left'`. In third line, the `initial` variable is given the value `'right'`, but the `position` variable retains its string value of `'left'`.
# </details>

# <div class="alert alert-success">
# <b>Task 1.3: Choosing a Name<br>
# Which is a better variable name, m, min, or minutes? Why?</b>
#     
# Hint: think about which code you would rather inherit from someone who is leaving the lab:
# 
# 1. `ts = m * 60 + s`
# 2. `tot_sec = min * 60 + sec`
# 3. `total_seconds = minutes * 60 + seconds`</div>

# In[9]:


#FIXME


# <details><summary {style='color:green;font-weight:bold'}> Click here to see the solution to Task 1.3. </summary>
#     
# ```python
# 
# ```
# 
# `minutes` is better because `min` might mean something like “minimum” (and actually is an existing built-in function in Python that we will cover later).
#  </details>

# <div class="alert alert-success">
# <b>Task 1.4: Challenge:<br></b>
# If you assign <code>a = 123</code>, what happens if you try to get the second digit of a via <code>a[1]</code>? What happens if you use <code>str(a[1])</code></div>

# In[10]:


#FIXME


# <details><summary {style='color:green;font-weight:bold'}> Click here to see the solution to Task 1.4</summary>
#     
# ```python
# print(a[1])
# print(str(a[1]))
# ```
#     
# Numbers are not strings or sequences and Python will raise an error if you try to perform an index operation on a number. In the next part on types and type conversion we will learn more about types and how to convert between different types. If you want the Nth digit of a number you can convert it into a string using the `str` built-in function and then perform an index operation on that string.
# </details>

# <div class="alert alert-warning">
# <b>Advanced Task 1.5: Fill in the blanks to get a substring</b>
# </div>

# In[11]:


atom_name = 'carbon'
print('atom_name[1:3] is:', #FIXME)


# <details><summary {style='color:green;font-weight:bold'}> Click here to see the solution to Task 1.5.</summary>
#     
# ```python
# atom_name = 'carbon'
# print('atom_name[1:3] is:', atom_name[1:3])
# ```
# </details>

# <div class="alert alert-info"> <b>Key Points</b>
# 
# - Use variables to store values.   
# - Use `print()` to display values.   
# - Variables persist between cells.   
# - Variables must be created before they are used.  
# - Variables can be used in calculations.   
# - Use an index to get a single character from a string.
# - Use a slice to get a substring.
# - Python is case-sensitive.
# - Use meaningful variable names.
# </div>

# ## 2. Data Types and Type Conversion
# <a id='datatypes'></a>

# ### Every value has a type
# 
# * Every value in a program has a specific type.
# * Integer (`int`): represents positive or negative whole numbers like 3 or -512.
# * Floating point number (`float`): represents real numbers like 3.14159 or -2.5.
# * Character string (usually called “string”, `str`): text.
#   * Written in either single quotes or double quotes (as long as they match).
#   * The quote marks aren't printed when the string is displayed.

# ### Use the built-in function type to find the type of a value
# 
# * Use the built-in function `type()` to find out what type a value has.
# * Works on variables as well.
#   * But remember: ⚠️ the *value* has the type — the *variable* is just a label.

# In[ ]:


print(type(52))


# In[ ]:


fitness = 'average'
print(type(fitness))


# ### Types control what operations (or methods) can be performed on a given value
# 
# A value's type determines what the program can do to it.

# In[ ]:


print(5 - 3)


# In[ ]:


print('hello' - 'h')


# ### You can use the “+” and “*” operators on strings
# 
# “Adding” character strings concatenates them.

# In[ ]:


full_name = 'Ahmed' + ' ' + 'Walsh'
print(full_name)


# * Multiplying a character string by an integer N creates a new string that consists of that character string repeated N times.
#   * Since multiplication is repeated addition.

# In[ ]:


separator = '=' * 10
print(separator)


# ### Strings have a length (but numbers don't)
# 
# The built-in function `len()` counts the number of characters in a string.

# In[ ]:


print(len(full_name))


# In[ ]:


print(len(52))


# ### Use an index to get a single character from a string
# ***
# * The characters (individual letters, numbers, and so on) in a string are ordered. For example, the string 'AB' is not the same as 'BA'. Because of this ordering, we can treat the string as a list of characters.
# * Each position in the string (first, second, etc.) is given a number. This number is called an index or sometimes a subscript.
# * Indexes are numbered from 0.
# * Use the position's index in square brackets to get the character at that position.   
# <div>
# <img src="images/indexing.png" alt="drawing" width="300">
# </div>

# In[ ]:


atom_name = 'helium'
print(atom_name[0])


# ### Use a slice to get a substring
# 
# * A part of a string is called a **substring**. A substring can be as short as a single character.
# * An item in a list is called an **element**. Whenever we treat a string as if it were a list, the string's elements are its individual characters.
# * A **slice** is a part of a string (or, more generally, any list-like thing).
# * We take a slice by using `[start:stop]`, where `start` is replaced with the index of the first element we want and `stop` is replaced with the index of the element just after the last element we want.
# * Mathematically, you might say that a slice selects `[start:stop)`.
# * The difference between `stop` and `start` is the slice’s length.
# * Taking a slice does not change the contents of the original string. Instead, the slice is a copy of part of the original string.

# In[ ]:


atom_name = 'sodium'
print(atom_name[0:3])


# ### Must convert numbers to strings or vice versa when operating on them
# 
# Cannot add numbers and strings.

# In[ ]:


print(1 + '2')


# * Not allowed because it's ambiguous: should 1 + '2' be 3 or '12'?
# * Some types can be converted to other types by using the type name as a function.

# In[ ]:


print(1 + int('2'))
print(str(1) + '2')


# ### Can mix integers and floats freely in operations
# 
# * Integers and floating-point numbers can be mixed in arithmetic.
# * Python 3 automatically converts integers to floats as needed. 

# In[ ]:


print('half is', 1 / 2.0)
print('three squared is', 3.0 ** 2)


# ### Variables only change value when something is assigned to them
# 
# * If we make one cell in a spreadsheet depend on another, and update the latter, the former updates automatically.
# * This does **not** happen in programming languages.

# In[ ]:


first = 1
second = 5 * first
first = 2
print('first is', first, 'and second is', second)


# * The computer reads the value of `first` when doing the multiplication, creates a new value, and assigns it to `second`.
# * After that, `second` does not remember where it came from.

# ## Tasks

# <div class="alert alert-success">
# <b>Task 2.1: Rational numbers:</b>
#     
# What type of value is 3.4? How can you find out?</div>

# In[ ]:


#FIXME


# <details><summary {style='color:green;font-weight:bold'}> Click here to see the solution to Task 2.1</summary>
#     
# ```python
# print(type(3.4))
# ```
# It is a floating-point number (often abbreviated “float”).
# </details>

# <div class="alert alert-success">
# <b>Task 2.2: Automatic type conversion:</b>
#     
# What type of value is $3.25 + 4$? </div>

# In[ ]:


# FIXME


# <details><summary {style='color:green;font-weight:bold'}> Click here to see the solution to Task 2.2. </summary>
#     
# ```python
# result = 3.25 + 4
# print(result, 'is', type(result))
# ```
# It is a float: integers are automatically converted to floats as necessary.
# </details>

# <div class="alert alert-success"><b>Task 2.3: Choosing a type:</b>
#     
# What type of value (integer, floating point number, or character string) would you use to represent each of the following? 
#     
# Try to come up with more than one good answer for each problem.
# 
# 1. Number of days since the start of the year.
# 2. Time elapsed from the start of the year until now in days.
# 3. Serial number of a piece of lab equipment.
# 4. A lab specimen's age
# 5. Current population of a city.
# 6. Average population of a city over time.
#     
# (You should give a Markdown solution)</div>

# In[ ]:


# 1.
# FIXME


# In[ ]:


# 2.
# FIXME


# In[ ]:


# 3.
# FIXME


# In[ ]:


# 4.
# FIXME


# In[ ]:


# 5.
# FIXME


# In[ ]:


# 6.
# FIXME


# <details><summary {style='color:green;font-weight:bold'}> Click here to see the solution to Task 2.3. </summary>
# Explanation <br>    
#   
# 1. Integer, since the number of days would lie between 1 and 365. <br>
# 2. Floating point, since fractional days are required <br>
# 3. Character string if serial number contains letters and numbers, otherwise integer if the serial number consists only of numerals <br>
# 4. This will vary! How do you define a specimen's age? whole days since collection (integer)? date and time (string)? <br>
# 5. Choose floating point to represent population as large aggregates (eg millions), or integer to represent population in units of individuals. <br>
# 6. Floating point number, since an average is likely to have a fractional part.
# </details>
# 

# In[ ]:


#FIXME


# <div class="alert alert-success"><b>Task 2.4: Predicting types:</br></b>
#     
# What are the types of each of the following numbers?
# 
# - 6   
# - 10.3   
# - -99.0   
# - 1.0   
# </div>

# In[ ]:


# TRY ME


# <details><summary {style='color:green;font-weight:bold'}> Click here to see the solution to Task 2.4. </summary>
# 
#     6 -> integer
#     10.3 -> floating point
#     -99.0 -> floating point
#     1.0 -> floating point
#     
# If you are unsure use the <code>type</code> function.
# </details>
# 

# <div class="alert alert-success"><b>Task 2.4: Strings to numbers:</br></b>
#     
# You can convert a float to an integer in the following way: 
# <code>print(int(3.4))</code> 
#     
# What kind of output do you get for the following conversions? 
# 
# Why do some of them fail?
# 
# 1. <code>print("string to float:", float("3.4"))</code>
# 2. <code>print("float to int:", int(3.4))</code>
# 3. <code>print("string to float:", float("Hello world!"))</code>
# 4. <code>print("fractional string to int:", int("3.4"))</code>
# </div>

# In[ ]:


# 1.
# FIXME


# In[ ]:


# 2.
# FIXME


# In[ ]:


# 3.
# FIXME


# In[ ]:


# 4.
# FIXME


# <details><summary {style='color:green;font-weight:bold'}> Click here to see solution to Task 2.4 </summary>
#     
# 1. ```python
# print("string to float:", float("3.4"))
# ```
# 2. ```python
#  print("float to int:", int(3.4))
# ```
# 3. ```python
# print("string to float:", float("Hello world!"))
# ```
# 4. ```python
# print("fractional string to int:", int("3.4"))
# ```
# 
# What do you expect this program to do? It would not be so unreasonable to expect the Python 3 `int` command to convert the string “3.4” to 3.4 and an additional type conversion to 3. After all, Python 3 performs a lot of other magic - isn’t that part of its charm?
# However, Python 3 throws an error. Why? To be consistent, possibly. If you ask Python to perform two consecutive typecasts, you must convert it explicitly in code.
# </details>

# <div class="alert alert-success"><b>Task 2.5: Operations on numbers:</br></b>
# 
# - What type of number do you get if you do 4 / 2?
# - What type of number do you get if you do 4 // 2?
# 
# </div>

# <details><summary {style='color:green;font-weight:bold'}> Click here to see the solution to Task 2.5. </summary>
# 
# ```python
#     print(4/2, "is of type", type(4/2))
#     print(4//2, "is of type", type(4//2))
# ```
# </details>

# <div class="alert alert-info"> <b>Key Points<br></b>
# 
# - Every value has a `type()`.
# - Use the built-in function `type~ to find the type of a value.
# - Types control what operations can be done on values.
# - Strings can be added and multiplied.
# - Strings have a length (but numbers don't).
# - Must convert numbers to strings or vice versa when operating on them.
# - Can mix integers and floats freely in operations.
# - Variables only change value when something is assigned to them.</div>
# 
# 

# ## 3. Built-in Functions and Getting Help
# <a id='debugging'></a>

# ### Use comments to add documentation to programs
# 
# - You can use `#` to set a comment. Typically you would place a space after the `#` before writing the comment.
# - You can also use `"""` for longer comments that stretch across multiple lines.

# In[ ]:


# This sentence isn't executed by Python.
adjustment = 0.5   # Neither is this - anything after '#' is ignored.


# In[ ]:


"""This is also a way to comment, but if you just want to 
write comments over
multiple lines.
This way you don't have to use the # symbol at the start of each line
"""
weight = 0.5
print('The weight is:',weight)


# ### A function may take zero or more arguments
# 
# * We have seen some functions already — now let's take a closer look.
# * An **argument** is a value passed into a function.
# * `len()` takes exactly one.
# * `int`, `str`, and `float` create a new value from an existing one.
# * `print` takes zero or more.
# * `print` with no arguments prints a blank line.
#   * Must always use parentheses, even if they're empty, so that Python knows a function is being called.
# * `id()` returns a unique integer (identity) of a passed argument object.
# * You will learn how to write your own functions in Session 4.

# In[ ]:


print('before')
print()
print('after')


# ### Commonly-used built-in functions include max and min
# * Use `max()` to find the largest value of one or more values.
# * Use `min()` to find the smallest.
# * Both work on character strings as well as numbers.
#   * “Larger” and “smaller” use (0-9, A-Z, a-z) to compare letters.

# In[ ]:


print(max(1, 2, 3))
print(min('a', 'A', '0'))


# ### Functions may only work for certain (combinations of) arguments
# 
# * `max()` and `min()` must be given at least one argument.
#    * “Largest of the empty set” is a meaningless question.
# * And they must be given things that can meaningfully be compared.
# 

# In[ ]:


print(max(1, 'a'))


# ### Use the built-in function help to get help for a function
# * Every built-in function has online documentation.

# In[ ]:


help(min)


# ### Python reports a syntax error when it can't understand the source of a program
# * Won't even try to run the program if it can't be parsed.
# 

# In[ ]:


# Forgot to close the quote marks around the string.
name = 'Feng


# In[ ]:


# An extra '=' in the assignment.
age = = 52


# In[ ]:


print("hello world"


# ### The error message can help
# * The message indicates a problem on first line of the input (“line 1”).
# * In this case the “ipython-input” section of the file name tells us that we are working with input into IPython, the Python interpreter used by the Jupyter Notebook.
# * The `-xx-` part of the filename indicates that the error occurred in cell XX of our Notebook.
# * Next is the problematic line of code, indicating the problem with a `^` pointer.

# ## Python reports a runtime error when something goes wrong while a program is executing

# In[ ]:


age = 53
remaining = 100 - aege # mis-spelled 'age'


# * Fix syntax errors by reading the source and runtime errors by tracing execution.

# ### The Jupyter Notebook has two ways to get help
# 
# * Place the cursor anywhere in the function invocation (i.e., the function name or its parameters), hold down `shift`, and press `tab`.
# * Or type a function name with a question mark after it.

# In[ ]:


get_ipython().run_line_magic('pinfo', 'len')


# In[ ]:


len()


# ### The function `id()` can help you understand how a variable is assigned

# In[ ]:


print("id of 'Curie' =", id('Curie'))

name = 'Curie'

print("id of name =", id(name))

first_name = name

print("id of first_name =", id(first_name))

name_lower_case = 'curie'

print("id of name_lower_case =", id(name_lower_case))


# * The `id()` function returns a unique integer number for every unique value it is used with.
# 
# * In the above example, we have used the `id()` function with variables a, b and c and got their corresponding ids.
# 
# * The `id()` function returns the integer same integer for both a = 5 and 5, as well as b.

# ### Every function returns something
# 
# * Every function call produces some result.
# * If the function doesn't have a useful result to return, it usually returns the special value `None`.

# In[ ]:


result = print('example')
print('result of print is', result)


# <div class="alert alert-info"> <b>Key Points<br></b>
# 
# * Use comments to add documentation to programs.
# * A function may take zero or more arguments.
# * Commonly-used built-in functions include `max` and `min`.
# * Functions may only work for certain (combinations of) arguments.
# * Functions may have default values for some arguments.
# * Use the built-in function `help` to get help for a function.
# * The Jupyter Notebook has two ways to get help.
# * Every function returns something.
# * Python reports a syntax error when it can't understand the source of a program.
# * Python reports a runtime error when something goes wrong while a program is executing.
# * Fix syntax errors by reading the source code, and runtime errors by tracing the program's execution.</div>

# ![indexing](images/break.png)

# # Next notebook:
# 
# [Unit 02 variables II](Unit_02_variables_II.ipynb)
