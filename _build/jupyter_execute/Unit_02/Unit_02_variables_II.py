#!/usr/bin/env python
# coding: utf-8

# # Unit 02: First steps in Python II

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
# ### Table of Contents
# 
# Notebook I   
# 1. [Variables and Assignments](Unit_02_variables_I.ipynb)    
# 2. [Data Types and Type Conversion](Unit_02_variables_I.ipynb)    
# 3. [Built in Functions and Getting Help](Unit_02_variables_I.ipynb)
# 
# Notebook II (this notebook)
# 
# 4. [More Data Types: Booleans and Lists](#advanced_types_i)
# 5. [More Data Types: Dictionaries and Tuples](#advanced_types_ii)
# 6. [Reading Files](#reading)

# ## 4. More Data Types: Booleans and Lists
# <a id='advanced_types_i'></a>

# ### `Bool` is a binary type where a variable can either be `True` or `False`
# Note how the syntax highlighting tells you that `True` and `False` are key words, and how they are case dependent.

# In[ ]:


two_is_a_prime = True
pi_is_an_integer = False


# In[ ]:


print(type(two_is_a_prime))
print(type(pi_is_an_integer))


# ### A list stores many values in a single structure

# * Doing calculations with a hundred variables called `pressure_001`, `pressure_002`, etc., would be at least as slow as doing them by hand.
# * Use a list to store many values together.
#   * Contained within square brackets `[...]`.
#   * Values separated by commas `,`.
# * Use `len` to find out how many values are in a list.

# In[ ]:


pressures = [0.273, 0.275, 0.277, 0.275, 0.276]
print('pressures:', pressures)
print('length:', len(pressures))


# ### Use an item's index to fetch it from a list
# * Just like strings

# In[ ]:


print('zeroth item of pressures:', pressures[0])
print('fourth item of pressures:', pressures[4])


# ### Lists' values can be replaced by assigning new values to them
# * Use an index expression on the left of assignment to replace a value.

# In[ ]:


pressures[0] = 0.265
print('pressures is now:', pressures)


# ### Appending items to a list extends the list
# * Use `list_name.append()` to add items to the end of a list.

# In[ ]:


primes = [2, 3, 5]
print('primes is initially:', primes)
primes.append(7)
print('primes has become:', primes)


# * `append()` is a method of lists.
#   * Like a function, but tied to a particular object.
# * Use `object_name.method_name()` to call methods.
#   * Deliberately resembles the way we refer to things in a library.
# * We will meet other methods of lists as we go along.
#   * Use help(list) for a preview.
# * `extend()` is similar to `append()`, but it allows you to combine two lists. For example:

# In[ ]:


teen_primes = [11, 13, 17, 19]
middle_aged_primes = [37, 41, 43, 47]
print('primes is currently:', primes)
primes.extend(teen_primes)
print('primes has now become:', primes)
primes.append(middle_aged_primes)
print('primes has finally become:', primes)


# Note that while `extend()` maintains the “flat” structure of the list, appending a list to a list makes the result two-dimensional - the last element in `primes` is a list, not an integer.

# ### Use `del` to remove items from a list entirely
# * We use `del list_name[index]` to remove an element from a list (in the example, 9 is not a prime number) and thus shorten it.
# * `del` is not a function or a method, but a statement in the language.

# In[ ]:


primes = [2, 3, 5, 7, 9]
print('primes before removing last item:', primes)
del primes[4]
print('primes after removing last item:', primes)


# ### The empty list contains no values
# * Use `[]` on its own to represent a list that doesn't contain any values.
#   * “The zero of lists.”

# ### Lists may contain values of different types
# * A single list may contain numbers, strings, and anything else.

# In[ ]:


goals = [1, 'Create lists.', 2, 'Extract items from lists.', 3, 'Modify lists.']


# ### Character strings can be indexed in the same way as lists
# * Get single characters from a character string using indexes in square brackets.

# In[ ]:


element = 'carbon'
print('zeroth character:', element[0])
print('third character:', element[3])


# ### Character strings are immutable
# 
# * Cannot change the characters in a string after it has been created.
#   * Immutable: can't be changed after creation.
#   * In contrast, lists are mutable: they can be modified in place.
# * Python considers the string to be a single value with parts, not a collection of values.

# In[ ]:


element[0] = 'C'


# * Lists and character strings are both collections.

# ### Indexing beyond the end of the collection is an error
# * Python reports an `IndexError` if we attempt to access a value that doesn't exist.
#   * This is a kind of [runtime error](http://swcarpentry.github.io/python-novice-gapminder/04-built-in/#runtime-error).
#   * Cannot be detected as the code is parsed because the index might be calculated based on data.

# ### You can sort a list in place using list_variable_name.sort()

# In[ ]:


wavelengths_in_nm = [560, 780, 340, 570]
print(wavelengths_in_nm)
wavelengths_in_nm.sort()
print(wavelengths_in_nm)


# ## Tasks

# <div class="alert alert-success"><b>Task 4.1: Working with lists I</b>
#     
# Create the following lists:
# 
# - A list containing the first 5 prime numbers
# - A list containing elements 11-15
# - A list containing the formation enthalpy of H$_2$O, molar entropy of H$_2$O and the Gibbs free energy of H$_2$O. This list should have 6 elements, the values and strings indicating what value will follow next in the list. Use the data below for this:
#     
# 
# | $\Delta_\mathrm{f} H^{\circ}$ in kJ/mol | $S_\mathrm{m}^{\circ}$ in J/K mol | $c_\mathrm{p}$ in J/kg K |
# |-----------------------------------------|-----------------------------------|------------------------|
# | -285.83                                 | 69.95                             | 4189                   |
#     
# Carefully consider your variable name for each list. 
# </div>

# In[ ]:


# FIXME


# <details><summary {style='color:green;font-weight:bold'}> Click here to see the solution to Task 4.1 </summary>
#     
# ```python
# primes = [2, 3, 5, 7, 11]
# elements = ['Na', 'Mg', 'Al', 'Si', 'P']
# thermodynamic_data_h2o = ['enthalpy of formation',-285.83 ,'molar entropy',69.95 , 'specific heat', 4148]
# 
# ```
# </details>

# <div class="alert alert-success"><b>Task 4.2: Working with lists II<br></b>
#     
# Using the lists you have assigned above:
# 
# - print each list
# - print the length of each list
# - remove the first element of the elements list
# - reassign the value of specific heat $c_\mathrm{p}$ to 4184 as the above value is wrong.
# - reassign your primes list to be an empty list
# </div>

# In[ ]:


# FIXME


# <details><summary {style='color:green;font-weight:bold'}> Click here to see the solution to Task 4.2 </summary>
#     
# ```python
# # print each list
# print(primes)
# print(elements)
# print(thermodynamic_data_h2o)
# 
# # print length of each list
# print(len(primes))
# print(len(elements))
# print(len(thermodynamic_data_h2o))
# 
# # remove first element
# del elements [0]
# print(elements)
# # reassign specific heat value
# thermodynamic_data_h2o[-1] = 4184
# # make primes an empty list
# primes = []
# 
# ```
# </details>

# <div class="alert alert-success"><b>Task 4.3: Lists with booleans<br></b>
#     
# 
# Create and empty list and append 3 elements of type boolean to it. Make a random choice if the boolean is true or false.
#    
# </div>

# In[ ]:


# FIXME


# <details><summary {style='color:green;font-weight:bold'}> Click here to see the solution to Task 4.3 </summary>
#     
# ```python
# boolean_list = []
# boolean_list.append(True)
# boolean_list.append(False)
# boolean_list.append(True)
# print(boolean_list)
# 
# ```
# </details>

# <div class="alert alert-success"><b>Task 4.4: How large is the slice?<br></b>
# 
# If ‘low’ and ‘high’ are both non-negative integers, how long is resulting list ```values[low:high]``` ? 
#     
# Try a few examples.
# 
# Notice how lists can be sliced in the same way as strings!
# </div>

# In[ ]:


values = [2,5,7,2,4,7,9,0,33,1,245]


# In[ ]:


#FIXME


# <details><summary {style='color:green;font-weight:bold'}> Click here to see the solution to Task 4.4 </summary>
# # Examples  
#     
# ```python
# print(values[1:4])
# print(values[4:5])
# ```
#     
# The list `values[low:high]` has high - low elements. For example, `values[1:4]` has the 3 elements `values[1]`, `values[2]`, and `values[3]`. Note that the expression will only work if `high` is less than the total length of the list `values`.
# </details>

# <div class="alert alert-success"><b>Task 4.5: Fill in the blanks<br></b>
#     
# 
# Write a bit of code that the following is printed in the Jupyter cell you are running the bit of Python code 
#     
# `first time: [1, 3, 5]`    
# `second time: [3, 5]`
# </div>

# In[ ]:


# FIXME
values = []
# FIXME


# <details><summary {style='color:green;font-weight:bold'}> Click here to see the solution to Task 4.1 </summary>
#     
# ```python
# values = []
# values.append(1)
# values.append(3)
# values.append(5)
# print('first time:', values)
# values = values[1:]
# print('second time:', values)   
# 
# ```
# </details>
# 

# <div class="alert alert-warning"><b>Advanced Task 4.6: From Strings to Lists and Back<br></b>
# 
# Given the code below:
#     
# ```Python
# print('string to list:', list('tin'))    
# print('list to string:', ''.join(['g', 'o', 'l', 'd']))
# 
# ```
# 
# Answer the following questions:    
# 1. What does `list('some string')` do?
# 2. What does `'-'.join(['x','y','x'])` do?
# 
# </div>

# In[ ]:


print('string to list:', list('tin'))


# In[ ]:


print('list to string:', ''.join(['g', 'o', 'l', 'd']))


# In[ ]:


# 1. 
#FIXME


# In[ ]:


# 2.
#FIXME


# <details><summary {style='color:green;font-weight:bold'}> Click here to see the solution to Advanced Task 4.6 </summary>
#     
# 1. ```python
#     list('some string') 
# ```
# converts a string into a list containing all of its characters.
# 2. ```python
#     .join 
# ```
#     returns a string that is the concatenation of each string element in the list and adds the separator between each element in the list. <br>
#     This results in `x-y-z`. The separator between the elements is the string that provides this method.  
# 
# </details>
# 

# <div class="alert alert-warning"><b>Task 4.7: Working with the End<br></b>
# 
# 
# Execute the cell below, what does it print?
# 
# 1. How does Python interpret a negative index?
# 2. If a list or string has N elements, what is the most negative index that can safely be used with it, and what location does that index represent?
# 3. If `values` is a list, what does `del values[-1]` do?
# 4. How can you display all elements but the last one without changing `values`? (Hint: you will need to combine slicing and negative indexing.)
# 
# <code>element = 'helium'
# print(element[-1])</code>
# </div>

# In[ ]:


# 1.
#FIXME


# In[ ]:


# 2.
#FIXME


# In[ ]:


# 3.
#FIXME


# In[ ]:


# 4.
#FIXME


# <details><summary {style='color:green;font-weight:bold'}> Click here to see solution to Task 4.7 </summary>
#     
# ```python
# ```
# The program prints `m`. 
#     <br>
# 1. Python interprets a negative index as starting from the end (as opposed to starting from the beginning). The last element is `-1`. <br>
# 2. The last index that can safely be used with a list of N elements is element -N, which represents the first element. <br>
# 3. `del values[-1]` removes the last element from the list. <br>
# 4. `values[:-1]` 
#     
# 
# 
# </details>

# <div class="alert alert-warning"><b>Task 4.8: Sort and Sorted:<br></b>
# 
# What does program A print and what does program B print? In simple terms, explain the difference between <code>sorted(letters)</code> and <code>letters.sort()</code>.
# </div>

# In[ ]:


# Program A
letters = list('gold')
result = sorted(letters)
print('letters is', letters, 'and result is', result)


# In[ ]:


# Program B
letters = list('gold')
result = letters.sort()
print('letters is', letters, 'and result is', result)


# <details><summary {style='color:green;font-weight:bold'}> Click here to see solution to Task 4.8 </summary>
#     
# 
# 
# Program A prints
# 
# ```Python
# letters is ['g', 'o', 'l', 'd'] and result is ['d', 'g', 'l', 'o']
# 
# ```
# 
# Program B print
# 
# ```Python
# letters is ['d', 'g', 'l', 'o'] and result is None
# ```
# 
# `sorted(letters)` returns a sorted copy of the list `letters` (the original list `letters` remains unchanged), while `letters.sort()` sorts the list `letters` in-place and does not return anything.
#     
# </details>

# <div class="alert alert-warning"><b>Advanced Task 4.9: Copying or not:<br></b>
# 
# What do these two programs print? 
#     
# In simple terms, explain the difference between `new = old` and `new = old[:]`.
#     
# (You should give a Markdown answer)
# </div>

# In[ ]:


# Program A
old = list('gold')
new = old      # simple assignment
new[0] = 'D'
print('new is', new, 'and old is', old)


# In[ ]:


# Program B
old = list('gold')
new = old[:]   # assigning a slice
new[0] = 'D'
print('new is', new, 'and old is', old)


# In[ ]:


# FIXME


# <details><summary {style='color:green;font-weight:bold'}> Click here to see solution to Task 4.8 </summary>
#     
# 
# Program A prints
# 
# ```Python
# new is ['D', 'o', 'l', 'd'] and old is ['D', 'o', 'l', 'd']
# ```
# 
# Program B prints
# 
# ```Python
# new is ['D', 'o', 'l', 'd'] and old is ['g', 'o', 'l', 'd']
# ```
# 
# 
# `new = old` makes `new` a reference to the list `old`; `new` and `old` point towards the same object.
# `new = old[:]` however, creates a new list object `new` containing all elements from the list `old`; `new` and `old` are different objects.
#     
# </details>

# <div class="alert alert-info"> <b>Key Points<br></b>
# 
# * A list stores many values in a single structure.
# * Use an item’s index to fetch it from a list.
# * Lists’ values can be replaced by assigning to them.
# * Appending items to a list lengthens it.
# * Use `del` to remove items from a list entirely.
# * The empty list contains no values.
# * Lists may contain values of different types.
# * Character strings can be indexed like lists.
# * Character strings are immutable.
# * Indexing beyond the end of the collection is an error.</div>

# ## 5. More Datatypes: Dictionaries and Tuples
# <a id='advanced_types_ii'></a>

# ### Dictionaries are an unordered collection of key and value pairs.
# **Keys are:**
# * Immutable: You cannot change them after assignment
# * Unique: You can only have the same key once in a dictionary
# * not stored in any particular order
# 
# **Values:**
# * Do not have restrictions
# * Do not have to be immutable or unique
# 
# You create a dictionary by putting `key:value` pairs in `{}`
# 
# ![dictionaries](images/dictionaries.png)

# In[ ]:


birthdays = {'Newton' : 1642, 'Darwin' : 1809}


# ### Retrieve a dictionary value by putting a key in `[]`.
# * This is just like indexing strings and lists

# In[ ]:


print(birthdays['Newton'])


# ### Just like using a phonebook or dictionary add values by assigning to it.

# In[ ]:


birthdays['Turing'] = 1612 


# ### Overwrite a value by assigning it as well.
# Oh no we made a mistake Allan Turing's birthyear is actually 1912.

# In[ ]:


birthdays['Turing'] = 1912


# ### A key must be in a dictionary before use

# In[ ]:


birthdays['Nightingale']


# ### You can test if a key is present using `in`

# In[ ]:


print("Nightingale" in birthdays)
print("Darwin" in birthdays)


# ### Values can be of any type, also list

# In[ ]:


periodic_table = {'group_one' : ['H', 'Li', 'Na', 'K', 'Rb', 'Cs', 'Fr'], 'group_eight':['He', 'Ne', 'Ar', 'Kr', 'Xe', 'Rn']}


# In[ ]:


print(periodic_table['group_one'])


# ## Tasks

# <div class="alert alert-success"><b>Task 5.1: Convert list to dictionary:<br></b>
#     
# Given the following two lists, rewrite them as a dictionary:   
#     
# <code>keys['Curie', 'Noether', 'Sommerville']
# values['French', 'German', 'British']</code>
# </div>

# In[ ]:


scientists = {#FIXME}


# <details><summary {style='color:green;font-weight:bold'}> Click here to see solution to Task 5.1 (remember to test out this answer above!)</summary>
#     
# ```python
# scientists = {'Curie':'French','Noether':'German', 'Sommerville':'British'}
#     
# print(scientists)
# print(type(scientists)) 
# ```
# </details>

# <div class="alert alert-success"><b>Task 5.2: Check if a key is in a dictionary<br></b>
# 
# Assign the variable <code>key_exists</code> and print it to check if the following keys exist in the dictionary below:
# 
# ```python
# periodic_table = {
#     'group_one' : ['H', 'Li', 'Na', 'K', 'Rb', 'Cs', 'Fr'],
#     'group_two':[], 
#     'group_three':[], 
#     'group_eight':['He', 'Ne', 'Ar', 'Kr', 'Xe', 'Rn']
#     }
# ```
# 
# 1. `group_one`
# 2. `halogens`
# 3. `metals`
# </div>

# In[ ]:


periodic_table = {
    'group_one' : ['H', 'Li', 'Na', 'K', 'Rb', 'Cs', 'Fr'],
    'group_two':[],
    'group_three':[],
    'group_eight':['He', 'Ne', 'Ar', 'Kr', 'Xe', 'Rn']
    }
key_exists = #FIXME
print(key_exists)


# <details><summary {style='color:green;font-weight:bold'}> Click here to see solution to Task 5.2.1 </summary>
#  
# key: `group_one`    
# ```python
# periodic_table = {
#     'group_one' : ['H', 'Li', 'Na', 'K', 'Rb', 'Cs', 'Fr'], 
#     'group_two':[], 
#     'group_three':[], 
#     'group_eight':['He', 'Ne', 'Ar', 'Kr', 'Xe', 'Rn']
#     }
# key_exists = 'group_one' in periodic_table
# print(key_exists)
# ```
# prints `True`
# </details>
# 

# In[ ]:


periodic_table = {
    'group_one' : ['H', 'Li', 'Na', 'K', 'Rb', 'Cs', 'Fr'],
    'group_two':[],
    'group_three':[],
    'group_eight':['He', 'Ne', 'Ar', 'Kr', 'Xe', 'Rn']
    }
key_exists = #FIXME
print(key_exists)


# <details><summary {style='color:green;font-weight:bold'}> Click here to see solution to Task 5.2.2 </summary>
#     
# key: `halogens` 
#     
# ```python
# periodic_table = {
#     'group_one' : ['H', 'Li', 'Na', 'K', 'Rb', 'Cs', 'Fr'], 
#     'group_two':[], 
#     'group_three':[], 
#     'group_eight':['He', 'Ne', 'Ar', 'Kr', 'Xe', 'Rn']
#     }
# key_exists = 'halogens' in periodic_table
# print(key_exists)
# ```
# prints `False`
# </details>

# <details><summary {style='color:green;font-weight:bold'}> Click here to see solution to Task 5.2.3 </summary>
# 
# key: `metals`
# 
# ```python
# periodic_table = {
#     'group_one' : ['H', 'Li', 'Na', 'K', 'Rb', 'Cs', 'Fr'], 
#     'group_two':[], 
#     'group_three':[], 
#     'group_eight':['He', 'Ne', 'Ar', 'Kr', 'Xe', 'Rn']
#     }
# key_exists = 'metals' in periodic_table
# print(key_exists)
# ```
# prints `False`
# </details>

# ### A tuple is an immutable heterogenous sequence.
# * This is essentially a list that cannot be changed after creation.
# * You can create a tuple using `()` instead of `[]`.

# In[ ]:


elements = ('H', 'He', 'Li', 'Br', 'B', 'C')


# ### Tuples are still indexed with square brackets `[]` and can be sliced:

# In[ ]:


print(elements[0])
print(elements[-1])
print(elements[1:4])


# ### You can query the length of a tuple.

# In[ ]:


len(elements)


# ### But because they are immutable you cannot reassign or append elements to the tuple

# In[ ]:


elements.append('N')


# In[ ]:


elements[0] = 'Hydrogen'


# <div class="alert alert-info"> <b>Key Points</b>
# 
# * A dictionary is an unordered collection of key and value pairs.
# * Keys must be unique and are immutable.
# * Values can be of any type and are mutable and don't have to be unique.
# * `{}` are used to create an empty dictionary.
# * You can add to a dictionary by giving it a new key, value pair.
# * You can query if a key exists using `in`.
# * Tuples are lists that cannot be changed after their creation (immutable).
# * `()` are used for creating a tuple.
# * To access elements of a tuple you still use `[]`.
# </div>

# ## 6. Reading Files
# <a id='reading'></a>

# ### There are many different ways to read files in Python.
# 
# * One way is to use the built-in function `open()`
# * The output of open returns a `file object`
# * When reading files it just dumps the content of the file into a string
# * Sometimes reading a file can also be called **parsing** a file, particularly if the content of the file has a complicated structure. 

# In[ ]:


reader = open('primes.txt', 'r') # create a file object
data = reader.read() ## read content of file into data
reader.close() ## close the reader
print(data)


# * The second argument for `open` `'r'` indicates that you are reading a file. You can also use `'a'` for appending to a file or `'w'` for just writing to a file. 

# ### Using the `open` function means alot of post formatting strings needs to be done on the file content

# In[ ]:


print(type(data))


# * You can use the attribute split on a string and it will split instances of a string according to the argument given.

# In[ ]:


data_split = data.split(',') # this uses the delimiter , to split the data


# In[ ]:


print (data_split)


# * All files have so called **hidden characters** you wouldn't see if you opened them in word. 
# * One such hidden character is the `\n` this is an end of line character used for machines to know to move to the next line.
# * You can get a *tab* using the tab character given by `\t`

# In[ ]:


data = data.strip('\n') # \n is a new line character that is hidden, strip removes it


# In[ ]:


data_split = data.split(',')


# In[ ]:


print(data_split)


# ### There are tools available that are better at reading file content that will come already pre-formatted

# In[ ]:


import numpy as np ## you'll learn about imports next week
primes = np.loadtxt('primes.txt', delimiter=',')


# In[ ]:


print(primes)


# ## Tasks

# <div class="alert alert-success"><b>Task 6.1: Hidden characters and string formatting:<br></b>
# 
# Let's have a look at different behaviours of strings.
# 1. Use the print function for the following string: `"The element carbon has mass 12.\nThe element oxygen has mass 16.\n"`
# 2. What happens if you replace the `\n` character with `\t`?
# 3. What happens if you use `sentence.split(' ')` on the string?
# 4. What about if you use `sentence.split('t')` on the string?
# </div>

# In[ ]:


sentence = "The element carbon has mass 12.\nThe element oxygen has mass 16.\n"
# FIXME


# <details><summary {style='color:green;font-weight:bold'}> Click here to see solution to Task 6.1 </summary>
#     
# ```python
# # 1. 
# print(sentence)
# 
# # 2.
# new_sentence = "The element carbon has mass 12.\tThe element oxygen has mass 16.\t"
# print(new_sentence)
# 
# # 3.
# split_space = sentence.split(' ')
# print(split_space)
# 
# # 4.    
# split_t = sentence.split('t')
# print(split_t)
# 
# ```
#     
# When using `sentence.split(' ')`. The spaces are removed and each word is put into a list. Each element of the list is a string consisting of a word. There is some mess around the new line characters though. 
#     
# When using `sentence.split('t')`. The all `t`s are removed and each part is split into a list. Notice, how the splitting is case sensitive!
# </details>

# <div class="alert alert-success"><b>Task 6.2: Writing a file:<br></b>
# 
# Take a look at the `open(filename, 'r')` functionality. 
#     
# In a similar way you can write a file using `open(filename,'w')`. 
# 
# Define a string and write it to file. 
# </div>

# In[ ]:


my_string = '#FIXME'
writer = #FIXME
writer.write(my_string)
writer.close()


# <details><summary {style='color:green;font-weight:bold'}> Click here to see solution to Task 6.2 </summary>
#     
# ```python
# my_string = 'I am a fun string to be written to file'
# writer = open('test.dat', 'w' )
# writer.write(my_string)
# writer.close()
# 
# ```
# </details>

# ## END UNIT 2

# ---
