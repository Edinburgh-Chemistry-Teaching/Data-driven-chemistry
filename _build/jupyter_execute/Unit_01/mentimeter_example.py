#!/usr/bin/env python
# coding: utf-8

# # Mentimeter Example
# 
# This is an example notebook of how to embed Mentimeters in a markdown cell.

# In[1]:


import sys
import os.path
sys.path.append(os.path.abspath('../'))
from helper_functions.mentimeter import Mentimeter


# In[2]:


vote = Mentimeter(vote = 'mentimeter address here')
vote.show()

