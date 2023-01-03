#!/usr/bin/env python
# coding: utf-8

# # Unit 01: Problem Solving I
# 
# <a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons Licence" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" title='This work is licensed under a Creative Commons Attribution 4.0 International License.' align="right"/></a>
# 
# Authors: 
# - Dr James Cumby 
# - Dr Antonia Mey
# 
# Emails: james.cumby@ed.ac.uk 

# ## Overview
# 
# Programming is almost entirely about **problem solving**, *i.e.* how do you take a complex problem and break it down in to manageable steps that a computer can perform. Whilst this is a useful skill for programming and data analysis, it is much more generally applicable, both within your degree and beyond. Importantly, problem solving is a skill that has to be learned, and this unit (and this course in general) will try to develop this skill.

# ### Learning objectives:
# 
# By the end of this unit, you should be able to:
# - Interact with a Jupyter notebook
# - Break a complex problem into smaller steps;
# - Consider how those steps might be implemented as code (developed more later in the course);
# - Use pseudocode to develop simple algorithms
# 
# <!-- begin no_present -->
# Some of the content is adapted from [Software carpentry lessons](http://swcarpentry.github.io/python-novice-gapminder/index.html).
# <!-- end no_present -->

# ### Table of Contents
# 
# 1. [Getting Started with Jupyter Notebooks](#1-getting-started-with-jupyter-notebooks)    
#     1.1 [Following the "Lecture"](#11-following-the-lecture)    
#     1.2 [Tasks how to](#tasks_how_to)    
# 2. [Notebook Layout](#12-notebook-layout)
# 3. [The Jupyter Kernel](#12-the-jupyter-kernel) 
# * [Tasks](#tasks)
# * [Next notebook: Problem solving II](Unit_02_problem_solving_II.ipynb)

# ### Link to Jupyter documentation:
# 
# You can find useful information about using Jupyter at [docs.jupyter.org](https://docs.jupyter.org/en/latest/).
# 
# ### Further reading: 
# - Kenneth Reitz and Tanya Schlusser, The Hitchhiker's Guide to Python, 2nd Ed., Sep 2016, ISBN: 978-1491933176 
# - Christian Hill, Learning Scientific Programming with Python, 2nd Ed, Dec 2020, ISBN: 978-1108745918
# - Al Sweigart, Automate The Boring Stuff With Python, 2nd Ed., Oct 2019, ISBN: 978-1593279929 
# - Eric Matthes, Python Crash Course, 2nd Ed., May 2019, ISBN: 978-1593279288
# - Alex Martelli, Anna Ravenscroft, Steve Holden, Python in a Nutshell, 3rd Ed., 2017, ISBN: 978-1449392925

# **Useful Jupyter Commands:**
# **<span style="color:black">Jupyter Cheat Sheet</span>**
# - To run the currently highlighted cell and move focus to the next cell, hold <kbd>&#x21E7; Shift</kbd> and press <kbd>&#x23ce; Enter</kbd>;
# - To run the currently highlighted cell and keep focus in the same cell, hold <kbd>&#x21E7; Ctrl</kbd> and press <kbd>&#x23ce; Enter</kbd>;
# - To get help for a specific function, place the cursor within the function's brackets, hold <kbd>&#x21E7; Shift</kbd>, and press <kbd>&#x21E5; Tab</kbd>;

# ## 1 Getting Started with Jupyter Notebooks<a id="1-getting-started-with-jupyter-notebooks"></a>

# <!-- begin tutor -->
# ### 1.1 Following the "lecture" <a id="following-the-lecture"></a>
# - Slides cover the main points in the session
# - Notebooks serve as complete 'handouts'
# - **Don't** try to read the notebook as we go!
# - My suggestion is:
#     - Use <kbd>&#x21E7; Shift</kbd> and <kbd>&#x23ce; Enter</kbd> to keep your notebook in the same place as the talk
#     - If you want to make extra notes, edit existing cells (and save a copy of the notebook after!) 
# 
# <!-- end tutor -->

# Over the next ten units you will learn how to use computer programming to help with chemistry. We will focus on Python: an easy-to-learn, but very powerful, programming language. As well as powering many of the apps on your phone, Python is widely used in many different disciplines. 
# 
# Python code can be run in many ways, but we will use Jupyter Notebooks like the one you're reading currently. Jupyter Notebooks allow you to combine live code and explanatory text in the same document, and can work like a digital lab book for computer code. 

# ### 1.2 Tasks and Solutions
# <a id='tasks_how_to'></a>
# There are **Tasks** in each unit for you to try by yourself. These are shown in green, like this:

# <div class="alert alert-success"><b>Task xx: This is a task.</b>
# 
# This is a description of the task. **Try to do the task yourself first!**
# </div>
# 

# If you get stuck, the solutions are provided in a drow-down window below the task description:

# <details><summary {style="color:green;font-weight:bold"}> Click here to see the solution to Task xx. </summary>
# 
# ```python
# # Solution code
# # Try the task yourself first
# # You can ask demonstrators for help
# ```
# 

# Try to avoid copy-pasting solutions.

# There are also some **Advanced tasks** which you should only attempt if you have time. Similarly, there are also extra exercises shown in yellow:

# <div class="alert alert-warning"><b> Advanced Task XX: More information on Task</b>
# 
# This is a description of an extra exercise that you can try out if you have time.
# </div>

# **Example tasks** are in the similar format to the above, but are worked through in a live session.

# ## 2. Notebook Layout
# <a id="#12-notebook-layout"></a>

# <!-- begin no_present -->
# A Jupyter notebook consists of a series of **cells** which can contain either formatted text (a **Markdown cell**) or executable code (a **code cell**). The type of a cell can be changed using the toolbar at the top of the page.
# For example, if you click on this cell it will be highlighted by a box, and the toolbar will display 'Markdown':
# ![Image showing 'Markdown' in drop-down box](images/markdown_dropdown.png)
# 
# The cell below is a **code** cell. In addition to showing **Code** in the drop-down box (try clicking on it!), code cells also display the text `In []:` to the left-hand side. If the code cell has been executed, a number will appear between the square brackets.
# 
# <!-- end no_present -->

# <!-- begin tutor -->
# Jupyter Notebooks contain **cells**:
# <!-- end tutor -->

# In[ ]:


# this is a code cell


# <!-- begin tutor -->
# Cells contain either code or formatted text (**Markdown**) and can be switched from the toolbar:
# ![Image showing 'Markdown' in drop-down box](images/markdown_dropdown.png)
# <!-- end tutor -->

# ### Command mode and edit mode <a id="command-mode-and-edit-mode"></a>

# In Jupyter, each cell can be switched between two modes:
# 
# <br>
# <dl>
#     <dt>Edit Mode</dt>
#     <dd>Allows you to modify the text or code</dd>
#     <dt>Command mode</dt>
#     <dd>Allows you to execute the code in a cell</dd>
# </dl>

# <!-- begin tutor -->
# - Press <kbd>&#x23ce; Enter</kbd> to switch to edit mode
# - <kbd>Esc</kbd> will switch back to command mode
# <!-- end tutor -->

# By default the notebook begins in command mode.
# <div class="alert alert-info">
# <b>When you are in command mode</b>, you can press <kbd>&#x23ce; Enter</kbd>to switch to edit mode. The left border of the cell you currently have selected will turn green, and a cursor will appear.
# </div>
# 
# <div class="alert alert-info">
# <b>When you are in edit mode</b>, you can press <kbd>Esc</kbd> to switch to command mode. The left border of the cell you currently have selected will turn blue, and the cursor will disappear.
# </div>
# 

# ### Markdown cells <a id="markdown-cells"></a>
# 
# Markdown cells can display formatted text and pictures, and are an excellent way to describe what your code does and discuss the results (imagine a lab report with interactive calculations). I strongly encourage you to use Markdown cells in your work!

# In **command mode** a markdown cell might look like this:
# 
# ![Markdown cell in command mode](images/command-mode-markdown-rendered.png)
# 
# Then, when you press <kbd>&#x23ce; Enter</kbd>, it will change to **edit mode**:
# 
# ![Markdown cell in edit mode](images/edit-mode-markdown.png)
# 
# Now, when we press <kbd>Esc</kbd>, it will change back to **command mode**:
# 
# ![Markdown cell in command mode after editing](images/command-mode-markdown-unrendered.png)
# 
# Notice that the markdown cell no longer looks like it did originally; we need to **run** the cell in order to display the formatted markdown. Do this by pressing <kbd>Ctrl</kbd> and <kbd>&#x23ce; Enter</kbd>, and then it will go back to looking like it did originally:
# 
# ![Markdown cell after running the cell](images/command-mode-markdown-rendered.png)

# ### Your turn!
# Test out this cell, switching between **command mode**, **edit mode** and **running** the cell.

# ### Code cells <a id="code-cells"></a>
# 
# Code cells contain code that should run, and possibly produce an output (such as graphs, tables, numbers, etc).

# Similar to Markdown cells, code cells have both **command** mode:
# 
# ![Code cell in command mode](images/command-mode-outline.png)
# 
# and **edit** mode (switch to **edit** mode using <kbd>&#x23ce; Enter</kbd>):
# 
# ![Code cell in edit mode](images/edit-mode-outline.png)
# 
# Pressing escape will go back to **command mode** again:
# 
# ![Code cell in command mode again](images/command-mode-outline.png)
# 
# The main difference between markdown and code cells is that if we press <kbd>Ctrl</kbd> and <kbd>&#x23ce; Enter</kbd>, this will **run** the code in the code cell:
# 
# ![Running code cell](images/code-cell-run.png)

# ### Running code cells <a id="116-running-code-cells"></a>

# Code cells can contain any valid Python code in them. When you run the cell, the code is executed and any output is displayed.
# 
# <div class="alert alert-info">
#     You can execute cells with <kbd>Ctrl</kbd> and <kbd>&#x23ce; Enter</kbd> which will keep the current cell selected, or <kbd>&#x21E7; Shift</kbd> and <kbd>&#x23ce; Enter</kbd> which will move to the next cell.
# </div>

# ### Your turn:
# 
# Try running the following cell and see what it prints out (don't worry about understanding the code for now):

# In[ ]:


print("Printing cumulative sum from 1-10:")

total = 0

for i in range(1, 11):
    total += i
    print( f'Sum of 1 to {i} is {total}')

print( 'Done printing numbers.' )


# You'll notice that the output beneath the cell corresponds to the `print` statements in the code. Here is another example which only prints out the final total.

# In[ ]:


total = 0

for i in range(1, 11):
    total += i

print(total)


# ## 3 The Jupyter Kernel <a id="12-the-jupyter-kernel"></a>

# <!-- begin tutor -->
# The **kernel** is in charge of executing Python code.
# <!-- end tutor -->

# When you first start a notebook, you are also starting what is called a **kernel**. This is a special program that runs in the background and executes Python code. Whenever you run a code cell, you are telling the kernel to execute the code that is in the cell, and to print the output (if any).

# ### Restarting the kernel

# If you are sure your code is correct but it keeps giving you errors then restarting the kernel often helps.
# 
# The restart kernel button is the circular arrow in the toolbar (pointed to by the red arrow in this image).
# 
# ![](images/restart-kernel-button.png)
# 

# ### Help with Jupyer Notebooks <a id="118-help-with-jupyer-notebooks"></a>

# <div class="alert alert-info">
# There are many keyboard shortcuts for the notebook. To see a full list of these, go to <b>Help $\rightarrow$ Keyboard Shortcuts</b>.
# </div>
# 
# <div class="alert alert-info">To learn a little more about what things are what in the Jupyter Notebook, check out the user interface tour, which you can access by going to <b>Help$\rightarrow$User Interface Tour</b>.</div>

# ## Tasks <a id="task"></a>
# Please work through these tasks in groups of two or three. Don't worry if you don't finish the in the alloted time!

# <div class="alert alert-success"> 
# <b> Task 1.1: Controlling Cells </b>
# 
# In the Jupyter notebook page are you currently in Command or Edit mode?
# Switch between the modes. 
# - Use the shortcuts to generate a new cell. 
# - Use the shortcuts to delete a cell. 
# - Use the shortcuts to undo the last cell operation you performed.
# 
# </div>

# 
# <details><summary {style='color:green;font-weight:bold'}> Click here to see solution to Task 1.1 </summary>
#     
# - switch between command and edit modes using <kbd>&#x23ce; Enter</kbd> and <kbd>Esc</kbd>
# - Add a cell in command mode either above (<kbd>A</kbd>) or below (<kbd>B</kbd>) the current one
# - Use <kbd>D</kbd>, <kbd>D</kbd> from command mode to delete a cell
# - <kbd>Z</kbd> will undo the deletion
#     
# </details>

# <div class="alert alert-success"> 
# <b> Task 1.2: Markdown lists </b>
# 
# Create a nested list in a Markdown cell in a notebook that looks similar to this (the bullet design will depend on your browser settings):
# 
# ![nest_list](images/nested_list.png)
# 
# </div>

# In[2]:


# FIXME


# <details><summary {style='color:green;font-weight:bold'}> Click here to see the solution to Task 1.2.</summary>
# 
# **Markdown Input:**
# ```
# 1. Get funding
# 2. Do work.
#     - Design Experiment
#     - Collect data
#     - Analyze
# 3. Write up.
# 4. Publish
# ```
# 
# **Rendered Output:**
# 1. Get funding
# 2. Do work.
#     - Design Experiment
#     - Collect data
#     - Analyze
# 3. Write up.
# 4. Publish
#     
# </details>

# <div class="alert alert-success"> 
# <b> Task 1.3: Maths in code cells </b>
# 
# What happens if you write some Maths in a code cell and execute it?
# 
# What happens if you then switch it to a Markdown cell? For example, put the following in a code cell:
# 
# ```Python
# 6*7+12
# ```
# </div>

# In[ ]:


# FIXME


# <details><summary {style='color:green;font-weight:bold'}> Click here to see the solution to Task 1.3</summary>
# 
# <br>
# <dl>
#     <dt> Code cell </dt>
#     <dd> Math operations are performed and the numerical answer returned </dd>
#     <dt> Markdown cell </dt>
#     <dd> Operations are simply rendered as text (see task 1.4 for rendering equations) </dd>
# 
# </details>

# <div class="alert alert-success"> 
# <b> Task 1.4: Equations </b>
# 
# Standard Markdown (such as we're using for these notes) won't render equations, but the Notebook will. 
# 
# Create a new Markdown cell and enter the following:
# `$$\sum_{i=1}^{N} 2^{-i} \approx 1$$`
# 
# (It's probably easier to copy and paste.) What does it display?
# 
#  What do you think the underscore (_), circumflex (^) and dollar signs ($) do?
#  </div>

# In[ ]:


# FIXME


# <details><summary {style='color:green;font-weight:bold'}> Click here to see the solution to Task 1.4.</summary>
# 
# $$\sum_{i=1}^{N} 2^{-i} \approx 1$$
# 
# - Dollar signs ($) surrounding text cause it to be rendered in 'math mode'
#     - Investigate the difference between single and double dollars
# - Underscore (_) causes the next character (or group surrounded by curly brackets, {..}) to be subscripted
# - Circumflex (^) works to superscript
# </details>

# <div class="alert alert-success"> 
# <b> Task 1.5: Closing and restarting </b>
# 
# - Close your Jupyter notebook and restart it. 
# - Restart the Kernel
# - Try opening a blank notebook
# 
# </div>

# <div class="alert alert-warning"> 
# <b> Extra Task 1.6: Extra Taks </b>
# 
# Try to create a table using a markdown cell, containing for instance the formula masses of the first 6 elements.
# </div>

# <details><summary {style='color:green;font-weight:bold'}> Click here to see the solution to Exercise 1.6</summary>
# 
# <br>
# 
# | Element name | Element mass (g mol<sup>-1</sup>) |
# |--------------|----------------------------------:|
# | H            |                             1.008 |
# | He           |                             4.003 |
# | Li           |                             6.941 |
# | Be           |                             9.012 |
# | B            |                            10.811 |
# | C            |                            12.011 |
# 
# </details>
# 

# ## Next Notebook
# 
# [Unit 01 Problem solving II](Unit_01_problem_solving_II.ipynb)
# 

# ---
