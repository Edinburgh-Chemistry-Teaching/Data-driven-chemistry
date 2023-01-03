#!/usr/bin/env python
# coding: utf-8

# # Loading and Manipulating Structured Data
# 
# ### Extra material for Unit 05
# 
# Authors:
# - Dr Valentina Erastova
# - Hannah Pollak
# 
# Email: <valentina.erastova@ed.ac.uk> 

# ### When should I use `numPy` and when `Pandas` ?
# <a class="anchor" id="numpy_pandas"></a>
#     
# In Python, there are multiple ways to load and work with datafiles.
#     
# One possible option is to use [**`np.loadtxt`**](https://numpy.org/doc/stable/reference/generated/numpy.loadtxt.html) function to read textfile data into a numpy array. Following the link we can check how `loadtxt` expects a file to be formatted. The comment lines should starts  with `#` and the values within one row are expected to be separated by a "whitespace" (=one or multiple space or tab characters). For example a file like this:
#  
# ```
# # AUTHORS: Schmidt J, Institute of Plant Biochemistry, Halle, Germany
# # m/z int. rel.int.
#   27.000 64.627 5
#   30.000 121.469 11
#   32.000 45.386 3
#   41.000 16.304 0
#   42.000 3731.328 372
#   44.000 29.229 1
# ```
# will be read in correct. BUT, if the formatting of the file differs from the expected structure, i.e. if in the `filename.txt` values are separated by `,` instead of a whitespace, or if lines were commented with `;` instead of `#`, the file would only be read correctly if the delimeters and comments are stated: 
# 
# ```python
# np.loadtxt('filename.txt', delimiter=',', comments=';')
# ```
#     
# Another way is to store a textfile data in a **pandas DataFrame**. In this case, we have to use [`pandas.load_csv`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html). Following the link to their documentation we can see that the function expects the row values to be separated by `,` and by default it will not expect any commented lines. 
# 
# 
# ### Viewing the datafile in the Jupyter Notebook 
# <a class="anchor" id="head"></a>
# 
# Before loading the data into the notebook it is good to take a closer look at its structure. 
# 
# To do this we can use `head`. Since this command is not a python command we have to add a `!` before it. To only see first 24 lines, add `-24` before filename `filename.txt`.
# 
# ```python
# !head -24 filename.txt
# ```
# Another command you may come across is `cat` - use it in the similar way.
# 
# ```python
# !cat -24 filename.txt
# ```

# <a class="anchor" id="Practice2"></a>
# <div class="alert alert-info">
# <b>PRACTICE - Loading Data from a File </b>    
#     
# Let's try to load an example file ```array_test.txt``` with pandas and assign it into a dataframe. 
#     
# First, check how the file looks like with ```!head``` then load the file (do you need to import pandas?)
#     
# ```python
# filename = 'DATA/array_test.txt'
# example_df = pd.read_csv(filename)
# example_df.head(5)
# ```    
# </div>
#      

# In[1]:


#!head 'array_test.txt'
get_ipython().system("cat 'DATA/array_test.txt'")


# In[2]:


import numpy as np
import pandas as pd


# <div class="alert alert-info">
#     
# As we can see, ```read_csv``` was not able to correctly read the file. Therefore, we have to provide ```read_csv``` with the correct ```delimiter``` and ```comment``` information. If comments are only at the beginning of the file, alternatively, they could also be skipped with ```skiprows```. Compared to ```loadtxt```, ```read_csv``` is much more flexible when it comes to reading files which are formatted in a non-standard way. By default, ```read_csv``` uses the first row for column lables. If this is not desired you have to specify ```header=None```.
# 
# ```python
# example_df = pd.read_csv(filename, comment='#', delimiter='\s+', header=None)
# ```
#     
# </div>

# In[3]:


# change the way you read the header



# <div class="alert alert-info">
#     
# Compared to `loadtxt`, `read_csv` is much more flexible when it comes to reading files which are formatted in a non-standard way. Additionally, DataFrames give the possibility to assign column labels and an index which can make data accession more intuitive. This makes them especially useful for large datasets. If no information is given, the first row will be used as column names and the index will be just the row numbers.
# 
# Let's assign column names and an index:
# 
# ```python
# example_df.columns=['c0', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7']
# example_df.index=['a', 'b', 'c', 'd', 'e']
# ```
#     
# </div>

# In[4]:


# assign columns and index

filename = 'DATA/array_test.txt'
example_df = pd.read_csv(filename)
example_df.head(5)



# <div class="alert alert-info">
#     
# Can you read the other file ```array_test2.txt```in the same way as```array_test.txt```? Or do you need to provide the correct ```delimiter``` and ```comment``` information? What about the header?
#     
# Check the file and decide.
# 
# </div>

# In[5]:


# read in another file
example2_df.index=['a', 'b', 'c', 'd', 'e']
example2_df


# <details>
# <summary> <mark> EXAMPLE SOLUTION:</mark> </summary>
# 
# 
# Read in 'array_test.txt' file: 
# 
# ```python
# import pandas as pd
# 
# filename = 'DATA/array_test.txt'
# example_df = pd.read_csv(filename)
# example_df.head(5)
#     
# ```
# 
# Change the way you read the header:
#   
# ```python    
# example_df = pd.read_csv(filename, comment='#', delimiter='\s+', header=None)
# example_df
#     
# ```
#    
# Assign columns and index:
#     
# ```python
# example_df.columns=['c0', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7']
# example_df.index=['a', 'b', 'c', 'd', 'e']
# example_df
# 
#     
# ```
#     
# 
# Read in 'array_test2.txt' file: 
#     
# ```python
# filename2 = 'DATA/array_test2.txt'
# example2_df=pd.read_csv(filename2, comment=';',delimiter=',')
# example2_df
#     
# ```
# 
#     
# Note that this file has a header, so you do not need to assign the columns. It is still usefule to assign the index:
#     
# ```python
# example2_df.index=['a', 'b', 'c', 'd', 'e']
# example2_df
#     
# ```
# 
# </details>
# 

# ---
# 
# [back to top](#teabags)

# ### Accessing the Data in an Array  
# 
# In ```numpy```, different entries of an array can be accessed by specifying their row and column numbers. 
# 
# In ```pandas```, with `loc` and `iloc`, entries can be selected either by index and column label, or by the column and index numbers. 
# 
# **Remember:** When selecting data using row and column numbers, counting always starts from 0!
# 
# 
# 
# ### Numpy VS Pandas cheat sheet <a class="anchor" id="numpy_pandas_cheatsheet"></a>
# 
# 
# <img src="images/numpy_pandas_1.png" width="500">
#  
# <img src="images/numpy_pandas_2.png" width="500">

# 
# [back to top](#teabags)

# In[ ]:




