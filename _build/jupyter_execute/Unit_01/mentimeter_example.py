#!/usr/bin/env python
# coding: utf-8

# # Mentimeter Example
# 
# This is an example notebook of how to embed Mentimeters in a markdown cell.

# In[ ]:


import sys
import os.path
sys.path.append(os.path.abspath('../'))
from helper_functions.mentimeter import Mentimeter


# In[ ]:


vote = Mentimeter(vote = 'mentimeter address here')
vote.show()

