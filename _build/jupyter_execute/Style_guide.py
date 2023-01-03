#!/usr/bin/env python
# coding: utf-8

# # Title of notebook

# <a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons Licence" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" title='This work is licensed under a Creative Commons Attribution 4.0 International License.' align="right"/></a>
# 
# Author: Dr James Cumby   
# Email: james.cumby@ed.ac.uk

# ## Overview
# 
# A brief introduction to the Unit
# 
# ### Learning Objectives
# 
# - List learning objectives
# 
# ### Table of Contents
# - [1 first item in toc](#link) 
#     - [1.1 first subitem in toc](#link3)
# - [2 second item in toc](#link2)
# 
# Use TOC if the notebook is long, doesn't have to be there if the notebook is short.
# 
# ### Further reading for this topic
# - give links here
# 
# ### Link to documentation:
# You can find the full documentation at [scipy.org](https://scipy.org).
# 
# **<span style="color:black">Jupyter Cheat Sheet</span>**
# - To run the currently highlighted cell and move focus to the next cell, hold <kbd>&#x21E7; Shift</kbd> and press <kbd>&#x23ce; Enter</kbd>;
# - To run the currently highlighted cell and keep focus in the same cell, hold <kbd>&#x21E7; Ctrl</kbd> and press <kbd>&#x23ce; Enter</kbd>;
# - To get help for a specific function, place the cursor within the function's brackets, hold <kbd>&#x21E7; Shift</kbd>, and press <kbd>&#x21E5; Tab</kbd>;

# In[2]:


# This would be where we should put global imports in the notebook
import matplotlib.pylab as plt


# ## 1 Use Level 2 heading for section headings
# ### 1.1 Use Level 3 heading for subsection headings

# ## Tasks:
# 
# Make sure tasks are numbered. 
# 
# Tasks are announced using an alert alert-success box in this way:
# <div class="alert alert-success">
# <b>Task 5.2: Write a function that computes bond lengths:</b>
#     
#  Task instructions 
# </div>
# and followed by an incomplete cell. All exercises should be numbered. 
# Missing parts are indicated by:
# 
# ```python
# #FIXME
# ```
# 
# Solutions to tasks are given in the cell below using the following details tag that can be used for expansion using the standardised text to do so:
# 
# <details><summary {style='color:green;font-weight:bold'}> Click here to see solution to Task. </summary>
#     
# ```python
# from math import sqrt
# ```
#     
#   

# <div class="alert alert-warning">
# <b>Advanced Task 5.3: Extra exercises are given in yellow </b>
#     
# and more instructions here
# </div>  

# ## Additional information noteworthy things
# 
# <div class="alert alert-info">
# <b>Anything noteworthy should be added to an info box. You can use the <code>I am code</code> tags to write code here</b>
# 
#  But it doesn't all have to be in bold
# </div>
# 
# To give extra attention use the exclamation mark warning sign: ⚠️ (Literally copy this icon and put it into the file)

# ## Questions for deliberation:

# <div class="alert alert-danger"><b>
# Question:</b> What is the difference between <code>tuple</code>, <code>array</code> and a <code>list</code>? 
# </div>
# 
# Questions should use the alert-danger class.

# ### Some formatting:
# 
# - All equations should be type set using LaTex, i.e. $\Delta \Delta G$ and not ΔΔG. 
# - Make sure you format equations according to ACS, or AMS guidelines, i.e. subscripts that are short for a word should not be in italics, e.g. Measured intensity should be $I_{\mathrm{m}}$. The same applies to quantities in equations, $\mathrm{time} = \ldots$
# - All packages should be highlighted in code, i.e. `scipy`. 
# - Common abbreviations could be highlighted either in the Readme or the first notebook. 
# - use `'` but `"` where necessary, i.e. a string with a string inside it. 

# ## Structure of directory for each Unit

# ### Images
# Any images that are displayed in the notebook should be in an `images` directory, arranged in this way: `Unit_xx/images/name_of_image.png`
# 
# ### Data
# Any data used in the notebook should be in a `data` directory, arranged in this way: `Unit_xx/data/name_of_data_file.txt`

# ### License
# 
# All data and images need to be licensed under CC-BY. Each notebook should have the CC-BY badge at the top as shown above. 

# ### Language
# 
# Use inclusive language:
# - not master or slave
# - not parent or child
# - avoid complicated language such as parsing a file without explaining it. 

# ## Python Style Guide
# 
# In general we should follow PEP8. But let's not break a leg over it: https://peps.python.org/pep-0008/ 

# ### Things we should definitely do:
# 1. Use fStrings: https://realpython.com/python-f-strings/ 
# 2. Place a space between a hashtag for a comment and code e.g.:
#     
#     ```Python
#     # This is a comment
#     a = 20
#     ```
# 3. Avoid overflowing line lengths.
# 4. Every function should be documented.
# 5. Use descriptive variable names e.g. (don't go and change everything, but some examples my be very bad):
#    
#    ```Python
#    # bad
#    x = np.array([3,4,5,6])
#    # good
#    pressures = np.array([3,4,5,6])
#    ```
# 6. Update all instances of random number generators to match this: https://numpy.org/neps/nep-0019-rng-policy.html

# In[ ]:




