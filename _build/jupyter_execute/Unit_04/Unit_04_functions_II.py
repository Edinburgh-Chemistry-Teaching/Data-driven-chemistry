#!/usr/bin/env python
# coding: utf-8

# # Unit 04: Functions II
# 
# <a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons Licence" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" title="This work is licensed under a Creative Commons Attribution 4.0 International License." align="right"/></a>
# 
# Authors: 
# - Dr Claire Hobday and 
# - Dr Antonia Mey   
# Email: claire.hobday@ed.ac.uk
# 
# ### Learning objectives:
# 
# This session is split into two notebooks both discuss how to use and write your own functions.
# 
# - ***Functions I*** (Previous notebook)
#     - understand inbuilt functions 
#     - understand the format of a function
#     - input into functions
#     - using loops and conditionals in functions
#     - calling a function
# 
# - ***Functions II*** (This notebook)
#     - getting information out of a function
#     - how to write reusable code
#     - write functions to interrogate data
# 
# ### Table of Contents
# - [Previous notebook: Functions II](Unit_04_functions_I.ipynb)
# - [4. Returning values from a function](#returns)   
# - [5. Functions calling functions](#function)   
# 
# ### Links to documentation
# - [numpy](https://numpy.org/doc/stable/)
# - [matplotlib](https://matplotlib.org/stable/index.html)
# 
# **<span style="color:black">Jupyter Cheat Sheet</span>**
# - To run the currently highlighted cell and move focus to the next cell, hold <kbd>&#x21E7; Shift</kbd> and press <kbd>&#x23ce; Enter</kbd>;
# - To run the currently highlighted cell and keep focus in the same cell, hold <kbd>&#x21E7; Ctrl</kbd> and press <kbd>&#x23ce; Enter</kbd>;
# - To get help for a specific function, place the cursor within the function's brackets, hold <kbd>&#x21E7; Shift</kbd>, and press <kbd>&#x21E5; Tab</kbd>;

# ## 4. Returning values from a function
# <a id="returns"></a>
# 

# In all the examples previously, we have been using the `print()` to output our information from the function. Programmers rarely use functions to print to the screen as the `print()` function already does that for us. Normally functions are used to do something to the argument that is passed to it then return the result of that something.
# 
# Consider the `len()` function:
# ```python
# seq_len = len("ACGTGGGTA")
# ```
# In this code we pass a DNA sequence as a string to `len()` which  **returns** its length which we can assign to a variable, in this case called `seq_len`. 
# 
# This is a more versatile use of functions than just printing because we can now use the value of `seq_len` for many other purposes.
# 
# In the code below is a function called `square_it()` that takes a number, squares it and **returns** the square. 
# 
# <div class="alert alert-info">
# <b>Run it to see what happens.</b>
# </div>

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# In[2]:


def square_it(x):
    """Return the square of the number x"""

    square = x ** 2
    return square


# Call "square_it()" with the argument 9.
# Assign the returned value (which is 81) to the variable "y".
y = square_it(9.)
print(y)


# The function `square_it()` takes a number and stores it in the parameter `x`. `x` is squared (remember `**` is the power operator, i.e., `x` to the power 2 is x squared.). The square of `x` is assigned to the variable `square`. Finally, the function returns the value in `square` back to the main program where it is assigned to the variable `y`, and the printed.
# 

# In this next example, we input 3 variables, `deltaG`, `R` and `T` and return one value `K`, the equilibrium constant.
# These are related through the equation:
# 
# \begin{equation}
# K = \exp (\frac{-\Delta G}{RT}) 
# \end{equation}

# In[3]:


#we use numpy as np and use np.exp 
#This gives us access to the exponential function within numpy.
def equilibrium_constant(deltaG, R, T):
    K = np.exp(-deltaG / (R * T))
    return K

deltaG = -20.5 #kJ/mol
R = 8.314 #J/Kmol
R = 8.314 * 0.001 #kJ/Kmol
T = 300 #K

K = equilibrium_constant(deltaG, R, T)
print("The equilibrium constant is {:.3f}".format(K))


# ## Functions can return more than one value

# The above function returned just a single value, but functions can return as many values as we like.
# 
# See the example below for finding the roots of a quadratic equation. 
# 
# $$ y = ax^2 + bx + c $$
# 
# where, $a = 1$, $b = 4$, and $c = 2$. 
# 
# And of course the postive and negative roots are:
# $$ x+ = \frac{-b + \sqrt{b^2 - 4ac}}{2a} $$
# 
# $$ x- = \frac{-b - \sqrt{b^2 - 4ac}}{2a} $$

# In[4]:


#Here we are using numpy's squareroot function np.sqrt
def get_roots(a, b, c):
    x_plus = (-b + np.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    x_minus = (-b - np.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    return x_plus, x_minus

x_plus, x_minus = get_roots(1, 4, 2)
print(f"The positive root is {x_plus}")
print(f"The negative root is {x_minus}")


# The function returns both values stored in the variables `x_plus` and `x_minus` simultaneously back to the main program.

# ## 5.  Functions can call functions
# <a id="function"></a>

# As we've seen a function can be called form inside another function. The code below shows an example we've already seen.

# In[5]:


def say_hello(name):
    """Print Hello name"""
    
    print(f"Hello {name}")
    
say_hello("Bob")


# In this example we call the function `say_hello()` which we have written. Our function calls the inbuilt function `print()`.
# 
# But our function can also call another function that **we** have written.
# 
# Remember the function which converts fahrenheit to celsius?
# ```python
# def fahr_to_celsius(temp):
#     return ((temp - 32) * (5 / 9))
# ```
# Let's write another one which will convert celsius to kelvin:
# 

# In[6]:


def fahr_to_celsius(temp):
    return ((temp - 32) * (5 / 9))
def celsius_to_kelvin(temp_c):
    return temp_c + 273.15


# Now, let's convert Farhenheit to Kelvin. 
# 
# We could write out the formula, but we don’t need to. Instead, we can compose the two functions we have already created:

# In[7]:


def fahr_to_kelvin(temp_f):
    temp_c = fahr_to_celsius(temp_f)
    temp_k = celsius_to_kelvin(temp_c)
    return temp_k


# In[8]:


print("boiling point of water in Kelvin:", fahr_to_kelvin(212.0))


# ## The scope of a variable is the part of a program that can ‘see’ that variable.
# 
# - There are only so many sensible names for variables.
# - People using functions shouldn’t have to worry about what variable names the author of the function used.
# - People writing functions shouldn’t have to worry about what variable names the function’s caller uses.
# - The part of a program in which a variable is visible is called its scope.

# In[9]:


pressure = 103.9

def adjust(t):
    temperature = t * 1.43 / pressure
    return temperature


# - `pressure` is a *global variable*.
#    - Defined outside any particular function.
#    - Visible everywhere.
# - `t` and `temperature` are local variables in adjust.
#    - Defined in the function.
#    - Not visible in the main program.
#    - Remember: a function parameter is a variable that is automatically assigned a value when the function is called.

# In[10]:


print("adjusted:", adjust(0.9))
print("temperature after call:", temperature)


# ## Tasks

# <div class="alert alert-success">
# <b>Task 5.1: Trace the values of all variables in this program as it is executed.
#  </b>
# (Use <code>—</code> as the value of variables before and after they exist.)

# In[ ]:


limit = 100

def clip(value):
    return min(max(0.0, value), limit)

value = -22.5
print(clip(value))


# <details><summary {style="color:green;font-weight:bold"}> Click here to see solution to Task 5.1. </summary>
#     
# ```python
# limit = 100
# # value = -
# 
# def clip(value):
#     return min(max(0.0, value), limit)
# 
# value = -22.5
# # value = -22.5
# print(clip(value))
# # value = -22.5
# ```

# <div class="alert alert-success">
# <b>Task 5.2: Modify your code from Task 2.2 so that the function <code>average()</code> returns the average of a list of numbers rather than printing it.</b>

# In[ ]:


def average(x):
    """Average of a list of numbers"""
    print(sum(x) / len(x))
    #FIXME


# In[ ]:


Titre_values = [22.2, 23.3, 22.3, 22.4, 22.4, 23.0, 22.0, 22.1, 21.9]


# In[ ]:


ave = average(Titre_values)
print(ave)


# <details><summary {style="color:green;font-weight:bold"}> Click here to see solution to Task 5.2 </summary>
#     
# ```python
# def average(x):
#     """Average of a list of numbers"""
#     return sum(x) / len(x)
# ```

# <div class="alert alert-success">
# <b>Task 5.3: Now write a program that will not only calculate the average, but also the standard deviation of these values and return both values. </b>
# </div>
# 
# Hint: Have a look at this [wikipedia article](https://en.wikipedia.org/wiki/Average) and remember to use the math module. 
# 
# You can also check your answer by running the following code:
# 
# ```python
# import numpy as np
# print(np.mean(Titre_values))
# print(np.std(Titre_values))
# ```

# In[ ]:


def ave_std_dev(x):
    #FIXME


# In[ ]:


ave, std_dev = ave_std_dev(Titre_values)
print(ave)
print(std_dev)


# ##### Solution
# <details><summary {style="color:green;font-weight:bold"}> Click here to see solution to Task 5.3 </summary>
#     
# ```python
# def ave_std_dev(x):
#     """Average of a list of numbers
#     Parametres
#     -----------
#     x : 1-D array of floats or ints
#         List of values to be averaged
#     Returns
#     -------
#     avg : float
#         averge of the list
#     std : float
#         standard deviation of list
#     """
#     
#     avg = (sum(x) / len(x))
#     x_minus_average_square = 0
#     for x_i in x:
#         x_minus_mean = x_i - avg
#         x_minus_average_square = x_minus_average_square + (x_minus_mean ** 2)
#     std_dev = math.sqrt(1 / (len(x)) * x_minus_average_square)
#     return avg, std_dev
# ```
# 

# <div class="alert alert-success">
# <b>Task 5.4: Write a function (<code>split_name</code>) that splits someone's full name into a forename and surname and returns both of these separately.</b> Test it out using the list <code>full_names</code>.
# 

# In[ ]:


def split_name():
    #FIXME


# In[ ]:


full_names = ["Harry Potter", "Hermione Granger", "Ronald Weasley"]


# In[ ]:


for name in full_names:
    forename, surname = split_name(name)
    print(f"{surname.upper()} {forename}")


# <details><summary {style="color:green;font-weight:bold"}> Click here to see solution to Task 5.4 </summary>
#     
# ```python
# def split_name(full_name):
#     """Split a full name into forename and surname"""
#     idx = full_name.find(" ")
#     forename = full_name[:idx]
#     surname = full_name[idx+1:]
#     return forename, surname
# ```    
# 
# 

# <div class="alert alert-success">
# <b>Task 5.5: Write a program that passes a peptide sequence to a function called <code>peptide_mass</code> and return its molecular mass.</b>

# In[ ]:


masses = {
    "A" : 71.03711,
    "C" : 103.00919,
    "D" : 115.02694,
    "E" : 129.04259,
    "F" : 147.06841,
    "G" :  57.02146,
    "H" : 137.05891,
    "I" : 113.08406,
    "K" : 128.09496,
    "L" : 113.08406,
    "M" : 131.04049,
    "N" : 114.04293,
    "P" :  97.05276,
    "Q" : 128.05858,
    "R" : 156.10111,
    "S" :  87.03203,
    "T" : 101.04768,
    "V" :  99.06841,
    "W" : 186.07931,
    "Y" : 163.06333}


# In[ ]:


def peptide_mass(peptide):
    #FIXME

for peptide in ["CPHRALIAIT", "NGQSVCGMSG", "WPFYWRICNH", "DLQVIDQMNW", "CEWIMYVTDE"]:
    print(f"Mass of {peptide} is {peptide_mass(peptide):.5f} Daltons")


# <details><summary {style="color:green;font-weight:bold"}> Click here to see solution to Task 5.5 </summary>
#     
# ```python
# def peptide_mass(peptide):
#     """calculate the molecular mass of peptide"""
#     mass = 0
# 
#     for aa in peptide:
#         mass += masses[aa]
#         
#     return mass
# ```
# 
