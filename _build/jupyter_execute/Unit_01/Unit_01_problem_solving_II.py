#!/usr/bin/env python
# coding: utf-8

# $$\require{mhchem}$$
# # Unit 01: Problem Solving II
# 
# <a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons Licence" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" title='This work is licensed under a Creative Commons Attribution 4.0 International License.' align="right"/></a>
# 
# Author: Dr James Cumby   
# 
# Email: james.cumby@ed.ac.uk

# ### Learning objectives:
# 
# By the end of this unit, you should be able to:
# - interact with a Jupyter notebook
# - break a complex problem into smaller steps;
# - consider how those steps might be implemented as code (developed more later in the course);
# - use pseudocode to develop simple algorithms
# 
# <!-- begin no_present -->
# Some of the content is adapted from [Software carpentry lessons](http://swcarpentry.github.io/python-novice-gapminder/index.html).
# <!-- end no_present -->

# ### Table of Contents
# 1. [Problem solving and algorithms](#1-problem-solving-and-algorithms)    
#     1.1 [Understanding a problem and its solution](#11-understanding-the-problem-and-its-solution)     
# 2. [Step 1: Aim(s)](#2-step-1-aims)     
#      2.1 [Tasks 1](#tasks-1)    
# 3. [Step 2: Information](#3-step-2-information)     
# 4. [Step 3: Constructing an algorithm](#4-step-3-work-out-a-series-of-steps-to-get-from-start-to-finish)     
# 5. [Pseudocode](#5-pseudocode)    
# 6. [Choosing an algorithm](#127-choosing-an-algorithm)     
# 7. [Tasks 2](#tasks-2)    
# 8. [Recap](#recap)    
# 9. [Feedback](#feedback)    
# 

# **<span style="color:black">Jupyter Cheat Sheet</span>**
# - To run the currently highlighted cell and move focus to the next cell, hold <kbd>&#x21E7; Shift</kbd> and press <kbd>&#x23ce; Enter</kbd>;
# - To run the currently highlighted cell and keep focus in the same cell, hold <kbd>&#x21E7; Ctrl</kbd> and press <kbd>&#x23ce; Enter</kbd>;
# - To get help for a specific function, place the cursor within the function's brackets, hold <kbd>&#x21E7; Shift</kbd>, and press <kbd>&#x21E5; Tab</kbd>;

# ### Link to Jupyter documentation:
# 
# You can find useful information about using Jupyter at [docs.jupyter.org](https://docs.jupyter.org/en/latest/).

# ## 1. Problem solving and algorithms <a id="1-problem-solving-and-algorithms"></a> 
# There are a number of steps involved in solving a problem:
# 1. Understand what the problem is and what it is asking for
#     - Do you have enough information to solve it immediately?
# 2. Understand what the correct solution needs to be capable of (or equally not capable of)
# 3. Work out a series of steps to get from start to finish 
#     - 'Solve the problem'!
# 4. Check that the solution works as expected

# This unit will look at steps 1-3 and give you practice in breaking down complex problems.

# ### Import libraries <a id="import-libraries"></a>
# We need a few additional Python features ('Libraries', see [Unit 03](../Unit_03/Unit_03_loops.ipynb)) in this session - make sure to run the following cell!

# In[1]:


import sys
import os.path
sys.path.append(os.path.abspath('../'))
from helper_functions.mentimeter import Mentimeter
from helper_functions.formatting import format_pseudocode
from IPython.display import IFrame


# ## 1.1 Understanding the problem and its solution <a id="11-understanding-the-problem-and-its-solution"></a>

# Some problems have very clear goals, and once you have got used to them are relatively straighforward to solve, i.e.
# > Find the value of x for which
# >
# >$$x - y = 6$$
# > and
# >$$2x + y = 18.$$
# 
# Even if a large number of steps are involved, the process is well-defined.
# 

# In contrast, some questions are much less defined, and these are quite challenging to overcome. Sometimes this is due to an uncertain objective, while sometimes there is a shortage of information.
# 
# > How would you synthesise 2,3-Dimethyl-2-cyclopenten-1-one from readily-available starting materials?
# 
# > ![2,3-Dimethyl-2-cyclopenten-1-one structure](./images/dimethyl_2_cyclopenten_1_one.png)
# 
# (You'll see this in year 3)

# ## 2. Step 1: Aim(s)<a id="2-step-1-aims">

# The first step of any problem is understanding what you are required to do, and working out whether you have all of the information required to solve it. Consider the following question and then vote in the poll below.
# 
# > Cheese is acidic, due to the presence of lactic acid. When cheese melts it can separate into milk solids and fat; this can be avoided by keeping the pH of the cheese mixture around 5.2. How much citric acid and/or sodium citrate must be added to cheese to prevent it from separating during melting?

# ### Mentimeters
# 
# This is an example of the type of questions students get asked to answer via Mentimeter:
# 
# Please see [mentimeter_example.ipynb](mentimeter_example.ipynb) for an example on how to embed Mentimeters into markdown cells.
# <img src="images/mentimeter.png" alt="mentimeter" width="400"><img>

# ## 3. Step 2: Information <a id="3-step-2-informatioon"></a>

# Once you have determined the objective of a problem, you then need to work out if you have the information and knowledge required to solve it. For instance, the following question has a clear goal, but what additional information is required?
# 
# > If human hair is composed mainly of the protein α-keratin, estimate the rate of incorporation of amino acid units per follicle per second.

# ### Tasks 1<a id="tasks-1"></a>
# 
# In pairs or groups of three, discuss the objective for the following questions, and any information you may require.

# <div class="alert alert-success"> 
# <b> Task 1.1: If you could imagine an electron to have the same mass as the planet Mercury, which planet would have approximately the same mass as the proton?</b>
# </div>

# <!-- begin answer -->
# <details><summary {style='color:green;font-weight:bold'}> Click here to see the solution to Task 1.1</summary>
# 
# Need to know the electron : proton mass ratio, and also planet mass ratios <br>
# 
# Answer: Saturn (approximately)
# <!-- end answer -->

# <div class="alert alert-success"> 
# <b> Task 1.2: Based purely on standard electrode potentials, which simple binary reaction would give the largest overall potential difference vs the standard hydrogen electrode?</b>
# </div>

# <!-- begin answer -->
# <details><summary {style='color:green;font-weight:bold'}> Click here to see the solution to Task 1.2</summary>
# 
# We need a list of electrode potentials, and to combine the most positive and negative values involving one species (to have a binary reaction overall). Other sources exist, but from [wikipedia](https://en.wikipedia.org/wiki/Standard_electrode_potential_(data_page)) the most negative half reaction is
# 
#    $$
#    \ce{Sr^+ + e^- -> Sr(s)}\qquad E_{\mathrm{vs\ SHE}} = -4.101\ \mathrm{V}
#    $$
#    while the most positive (anionic) half reaction is
#    $$
#    \ce{F2(g) + 2e^- -> 2F^-}\qquad E_{\mathrm{vs\ SHE}} = +2.87\ \mathrm{V}
#    $$
#    Overall:
#    $$
#    \ce{Sr + F2 -> SrF2}\qquad E_{\mathrm{vs\ SHE}} = +6.971\ \mathrm{V}
#    $$
# 
# <!-- end answer -->

# <div class="alert alert-success"> 
# <b> Task 1.3: If you placed a crystal of Tourmaline on top of a crystal of Herapathite and looked through them, what might you observe?</b>
# </div>

# <!-- begin answer -->
# <details><summary {style='color:green;font-weight:bold'}> Click here to see the solution to Task 1.3</summary>
# 
# Tourmaline (a borosilicate mineral) and herapathite (iodoquinine sulfate) are both optically active; the latter is used in optical polarizers. Depending on the relative orientation of the crystals, the colour and/or transparency is likely to change.
# <!-- end answer -->

# ## 4. Step 3: Constructing an algorithm<a id="4-step-3-constructing-an-algorithm"></a>

# Once you have determined the problem and have all the information required, you then need to construct an algorithm (sequence of steps) to get to the answer. 

# ### Aside - program construction
# 
# In general, computer programs consist of very few essential 'building blocks' (you will learn about these throughout the course):
# 
# 
# Operations | Loops | Decisions
# ---------- | -------- | -----------
# These are things like adding/multiplying numbers, reading or writing files, displaying a graph, etc. | These allow you to repeat things more than once, for instance iterating over files | Decisions (of IF statements) divert the flow of a program by doing some sort of test
# ![Green rectangle representing an operation](./images/operation_schematic.png) | ![Schematic of a loop](./images/loop_schematic.png) | ![Schematic of a decision operation](./images/decision_schematic.png)

# These can be combined together to create quite complex algorithms:
# <img src="./images/complex_schematic.png" alt="Combination of loops, decisions and operations as a schematic" width="400"></img>
# 

# > Hint: If you find this sort of graphical programming helpful to understand algorithm logic, check out [Blockly](https://developers.google.com/blockly)!

# ## 5. Pseudocode <a id="5-pseudocode"></a>
# 

# Loops and decision statements are normally shown as indented:
# 
# ```
# for each item in a sequence:
#     do something
# ```
# 
# Indents can be nested:
# 
# ```
# if x is 5:
#     if y is 10:
#         do something
# ```
# 
# This indentation is essential in Python (see Unit 03)!

# The previous examples were a form of 'pseudocode'; a way of writing down an algorithm without worrying about the specific commands required to run correctly. Pseudocode is often more readable than 'real' computer code, and can in theory be translated into any programming language.

# <!-- begin tutor -->
# Pseudocode summarises the steps of an algorithm without using a specific syntax.
# <!-- end tutor -->

# For instance, the following 'pseudocode' describes an algorithm to print any files containing the text 'Benzene'
# 
# ```
# for each file in a list of files:
#     open file and read contents
#     if 'Benzene' is in file contents:
#         print file name
#     close file    
# ```

# The same algorithm written for Python might look like:
# 
# ``` python
# for file in list_of_file_names:
#     file_handle = open(file, 'r')
#     contents = f.readlines()
#     if 'Benzene' in contents:
#         print(file)
#     file_handle.close()
# ```

# ## 6. Choosing an algorithm <a id="6-choosing-an-algorithm"></a>
# Often, there are multiple valid solutions to a problem. You should try to appreciate other approaches, but find one that you understand.
# 
# As a simple example, in your head work out the answer to
# 
# $$
# 54 + 17
# $$

# How did you do it?
# - $50 + 10 = 60$, then $60 + 4 + 7 = 71$
# - $54 + 10 = 64$, then $64 + 7 = 71$
# - $50 + 17 = 67$, then $67 + 4 = 71$
# - Something else...?

# <div class="alert alert-success">
# <b> Worked example: Finding alcohols</b>
# 
#  If you were given 1000 random Infrared spectra from small molecules, how could you determine which ones were alcohols?
# </div>

# <details><summary {style='color:green;font-weight:bold'}> Click here to see solution to the Worked example. </summary>
# 
# <!-- begin livecode -->
# ```
# FOR each spectrum:
#     Find absorption for $2600 < \nu < 3500$
#     fit background
#     IF absorption - background > threshold:
#         assign as alcohol
# ```
# <!-- end livecode -->
# </details>

# ### Some potential problems to consider when developing an algorithm

# **The OH-stretching region near 3000 cm<sup>-1</sup> is not unique**
# 
# ![Benzene vs benzoic acid IR](./images/benzene_benzoic_acid_IR.png)
# 
# *Data obtained from Coblentz Society, Inc., "Evaluated Infrared Reference Spectra" in **NIST Chemistry WebBook, NIST Standard Reference Database Number 69**, Eds. P.J. Linstrom and W.G. Mallard, National Institute of Standards and Technology, Gaithersburg MD, 20899, https://doi.org/10.18434/T4D303, (retrieved December 14, 2022).*
# 
# - One solution could be to examine the peak width - alcohol OH peaks are typically broad

# **The background signal is not guaranteed to be ~100% T**
# 
# ![Comparison of IR background absorption](./images/IR_background_comparison.png)
# 

# ### Tasks 2 <a id="tasks-2"></a>
# 
# In your groups, discuss and solve the following problems. Try to use a "Pair Programming" approach.

# <div class="alert alert-success"> 
# <b> Task 1.4: NMR spectroscopy </b>
# 
# Some reactions can be monitored in-situ by NMR spectroscopy, by following the growth of a new NMR peak with time. For such a reaction, what order would you need to perform the following steps in order to plot a concentration vs time profile?
# 
# 
# > Drag the boxes into the correct order, remembering to indent things that should be performed inside the loop
# 
# </div>

# In[2]:


IFrame(' https://parsons.herokuapp.com/puzzle/17312c8d7d1d44348ed1bff8886c54da', 950, 600)


# <!-- begin answer -->
# 
# <details><summary {style='color:green;font-weight:bold'}> Click here to see solution to Task 1.4 </summary>
# 
# ```
# FOR each NMR spectrum:
#     read in NMR data file(s)
#     extract time from NMR file
#     fit NMR peak of interest
#     extract peak area
#     convert area to concentration
# plot concentration vs time
# ```
# <!-- end answer -->

# <div class="alert alert-success">
# <b>Task 1.5: Write a function that computes bond lengths:</b>
# 
# If you were given a sequence of atomic coordinates during a reaction that were for some reason in the wrong order, how might you try to put them back in the correct sequence? For example, consider the sequence of five steps from an S<sub>N</sub>2 reaction shown below (imagining you had the atomic coordinates):
# 
# ![SN2 Reaction steps](./images/SN2_reaction_steps.png)
# 
# > Hint: If you know how far each atom must move to get to a different step, the next step along the S<sub>N</sub>2 reaction will be the one with the smallest (total) distance
# 
# </div>
# 

# In[3]:


IFrame(' https://parsons.herokuapp.com/puzzle/7b69c59b740c4d8e82dcbd2875dd5ffe', 950,500)


# <!-- begin answer -->
# 
# <details><summary {style='color:green;font-weight:bold'}> Click here to see solution to Task 1.5 </summary>
# 
# ```
# FOR each pair of structures:
#     Determine (summed) distance between equivalent pairs of atoms (e.g. O-O, Br-Br etc).
# Assign largest distance as that between start/end points
# Use starting point as `current` step
# LOOP continuously:
#     Find minimum distance from current step
#     IF not already part of sequence:
#         Assign to sequence.
#     IF next in sequence is the end point:
#         STOP - problem complete.
#     Change `current` step to next in sequence
# ```
# 
# <!-- end answer -->

# <div class="alert alert-warning">
# <b>Advanced task: Pseudocode</b>
#  Write a pseudocode algorithm to determine the molecular weight from an arbitrary chemical formula, e.g. (CH3)3CBr or CH3C(O)CN.
# </div>  
# 

# ## Recap <a id="recap"></a>
# This session has covered:
# - How to break down a problem
#     - Know *what* you are trying to answer
#     - Determine if you have all the information you need before starting
# - Constructing an algorithm
#     - Multiple ways of solving the problem
#         - as long as it works, *how* isn't important
#     - Try to think of pitfalls of your solution
#         - One solution may often be faster, more robust, easier to read, etc...

# ### Feedback <a id="14-feedback"></a>
# 
# Please say what you did and didn't like about this session!
# 
# Students are asked to give feedback at the end of each session. Separate Mentimeter quizzes ask for positive and negative feedback in order help improve the course unit.
# <img src="./images/feedback_1.png" alt="feedback_1" width="400"></img>

# ## END UNIT 1

# ---
