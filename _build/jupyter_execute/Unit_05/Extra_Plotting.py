#!/usr/bin/env python
# coding: utf-8

# # Plotting 
# 
# <a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons Licence" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" title='This work is licensed under a Creative Commons Attribution 4.0 International License.' align="right"/></a>
# 
# 
# ### Extra material for Unit 05
# <br>
# 
# Authors: 
# - Dr Valentina Erastova
# - Hannah Pollak
# 
# Email: <valentina.erastova@ed.ac.uk>

# ## Matplotlib CheatSheet   <a id="cheatsheet"></a>
# There are some helpful [cheatsheets](https://matplotlib.org/cheatsheets/)
# 
# You may find the bellow useful:
# 
# ![Matplotlib Beginner cheat sheet](https://matplotlib.org/cheatsheets/handout-beginner.png)
# ![Matplotlib Intermid cheat sheet](https://matplotlib.org/cheatsheets/handout-intermediate.png)
# ![Matplotlib tips and tricks](https://matplotlib.org/cheatsheets/handout-tips.png)

# <a class="anchor" id="Practice1"></a>
# <div class="alert alert-info">
#     <b>PRACTICE - Plotting</b>  
#     <p>- generate a 1D array, $x$, between -10 and 10, in a step of 1 </p>
#     <p>- create an array $z$ of the same length as $x$ </p>
#     <p>- create subplots: </p>
#      <p>  <img src="FIGS/figsubplots.png" width="500"></p>
#              <p>  <img src="FIGS/figsubplots1.png" width="500"></p>
#     <b> NOTE - these produce equivalent plots:  </b> 
# <p>
#     
# ```python
# plt.figure()
# plt.subplot(1, 2, 1) 
# plt.subplot(1, 2, 2) 
# ```  
#     
# ```python
# fig,(ax1,ax2)=plt.subplots(1, 2) 
# ax1.plot(x, y1)
# ax2.plot(x, y2)
# ```  
#     
# ```python
# fig,ax=plt.subplots(1, 2) 
# ax[0].plot(x, y1)
# ax[1].plot(x, y2)
# ```  
# </p>   
#     <p>- plot $x^2$ and $\frac{1}{4}x^3$  using non-default line types and colours, label the plot</p>
#     <p>- on a subplot to the left plot $5x-exp(\frac{1}{z})$ add points over the last line, label everything</p>   
#     <p> - save figure <code> plt.savefig('name.extension') </code></p>
#     
# </div>

# In[1]:


# your solution 






# <details>
# <summary> <mark> EXAMPLE SOLUTION:</mark> </summary>
#     
# ```python
# 
# 
# import numpy as np
# import matplotlib.pyplot as plt
# 
# #generate array x
# x = np.linspace(-10, 10, 21) 
# 
# #generate array z of equivalent shape 
# z = np.linspace(-11, 28, x.shape[0])
# 
# #some math
# y1 = x**2
# y2 = 1/4*x**3
# y3 = 5*x-np.exp(1/z)
# 
# #plot these 
# 
# # create a figure - I prefer this way
# plt.figure()
# 
# #NOTE - you can also use:
# #fig,(ax1,ax2)=plt.subplots(1, 2) 
# #ax1.plot(x, y1)
# #ax2.plot(x, y2)
# 
# 
# plt.subplot(1, 2, 1) #1 plot per line, 2 per column, plot 1            
# plt.plot(x, y1, '.--', color='k', label='$x^2$')
# plt.plot(x, y2, 'x:', color='coral', label=r'$\frac{1}{4}x^3$') #note use or 'r' before the LaTex string
# plt.title('functions of $x$')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.legend(loc="upper left")
# 
# 
# plt.subplot(1, 2, 2) #1 plot per line, 2 per column, plot 2
# #set one label to use a few times
# l=r'$5x-exp(\frac{1}{z})$'
# plt.plot(x, y3, '-', color='teal')
# plt.plot(x, y3, marker='o', alpha=0.2, markersize=10, label=l)
# plt.title(l)
# plt.xlabel('x')
# plt.ylabel('y')
# plt.legend(loc="upper left")
# 
# #adjust the spacing between subplots, so they do not overlap
# #matplotlib.pyplot.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=None)
# plt.subplots_adjust(wspace=0.5)
# 
# #save image as .png (or .eps or .pdf or many other)
# plt.savefig("myfigure.png")
# 
# plt.show()
# ```
#     
# </details>
# 
# 
