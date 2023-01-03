#!/usr/bin/env python
# coding: utf-8

# # Unit 10 - Analysing NMR Data from Start to Finish <a class='tocSkip'>
# $$\require{mhchem}$$
#     
# <a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons Licence" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" title='This work is licensed under a Creative Commons Attribution 4.0 International License.' align="right"/></a>
# 
# Author: Dr James Cumby   
# Email: james.cumby@ed.ac.uk

# ## Overview
# In this Unit, we will focus on handling real experimental results using Python, from the initial stage of importing data right through to fitting models and plotting the results.
# While you could achieve this manually using Origin or Excel, hopefully you'll see that writing code makes the analysis easier, particularly when you have lots of data!
# <div class="alert alert-info">
# <b>
# Note:</b> this session does not intend to teach new concepts, but may inadvertently introduce different ways of achieving the same results. Please ask me/a demonstrator if you unsure.
# </div>

# ### Learning Objectives
# 
# This unit covers the learning outcomes of the entire course:
#  - Perform numerical operations such as vector algebra and calculate simple statistics on data sets.
#  - Write readable, well-documented and modular code.
#  - Break a problem into logical steps, and use loops and decision operations to solve tasks.
#  - Import and clean experimental data, and choose the appropriate variable types to hold information.
#  - Fit models to numerical data, and plot the results in a number of different formats.
# 
# 
# ### Table of Contents
# 1. [The Problem](#problem)     
# 2. [Reading Data](#read)
# 3. [NMR data exploration](#explore)
# 4. [Peak hunting](#peak)
# 5. [Analysing Results](#analysis)
# 
# 
# ### Link to documentation:
# 
# You may wish to include links to package documentation here, if you wish to refer to them later.
# 

# In[1]:


# Add any packages you need to import here


# ## 1. The Problem
# <a id='problem'></a>
# > Do you get more peaks in the <sup>1</sup>H NMR spectrum if you have an odd number of heteroatoms compared with an even number?
# 
# The information available is a CSV file containing the number of heteroatoms and an identifier for the molecules, and a folder of NMR data with the matching identifiers. You do not know the chemical formulae.

# ### Surveying the class
# <img src="images/mentimeter_1.png" alt="isolated" width="400"/>

# # Tasks
# 
# You will work in pairs or small groups to try and answer this question, with help and guidance from academic demonstrators. Don't worry if you can't immediately solve the problem - try out a few ideas, and ask for help when you're ready!
# 
# If you get stuck don't panic - you will be given hints throughout the workshop, and a model answer will be made available after the session.

# <div class="alert alert-success">
# <b>Task 1.1 Thinking about the problem</b>
# 
# In small groups, discuss the following:
# - the chemistry behind the problem;
# - what steps are required to solve the problem.
# 
# As you discuss your ideas, add steps to the mentimeter:
# </div>

# <img src="images/mentimeter_2.png" alt="isolated" width="400"/>
## Gather some ideas:


# <details><summary {style='color:green;font-weight:bold'}> Click here to see solution to Task. </summary>
#     
# Some ideas:
# - Collect NMR data
# - Collect information on hetero atoms
# - most abundant isotopes of heteroatoms
# </details>

# <!-- begin silent_answer -->
# ## 2. Reading Data
# <a id='read'></a>
# 
# <div class="alert alert-info">
# <b>Data:    
# </b>
# You will find all the data you need to answer the question in the directory <code>data</code>. The summary file tells you about the hetero atom counts, the weights file about the molecular weights. In <code>data/NMR_data</code> you find many files with different spectra. 
# </div>
# 
# ### Task 2
# 
# <div class="alert alert-success">
# <b>Getting started with the data</b>
#     
# 1. Import the <code>NMR_summary.csv</code> file   
# 2. Work out how to read a single NMR spectrum from a file    
# 3. Write a function <code>read_NMR_data</code>that can read in all NMR files    
# </div>
# <!-- end silent_answer -->

# <!-- begin silent_answer -->
# ### 2.1 - Import summary file
# First, we need to import the summary data file; here we'll use Pandas.
# <!-- end silent_answer -->

# In[2]:


# FIXME



# <!-- begin silent_answer -->
# ### 2.2 - Read in NMR data file
# First, we need to work out how to read one file
# <!-- end silent_answer -->

# In[3]:


# FIXME


# <!-- begin silent_answer -->
# ### 2.3 - Read in all NMR files
# Now we can read one file, we should write a function that can read them all.
# <!-- end silent_answer -->

# In[4]:


# FIXME


# <!-- begin silent_answer -->
# ## 3. NMR data exploration
# <a id='explore'></a>
# To answer the problem
# > Do you get more peaks in the <sup>1</sup>H NMR spectrum if you have an odd number of heteroatoms compared with an even number?
# 
# we will need to determine the number of peaks in a spectrum. 
# 
# <div class="alert alert-info">
# <b>Questions to ask of the data</b>
#     
# To peak search automatically, we need the NMR data to have similar numerical values. Things to check are: 
# 
# - What range of chemical shift do they cover?
# - What is the maximum intensity?
# - How noisy is the baseline?
# </div>
# <!-- end silent_answer -->

# <!-- begin silent_answer -->
# ## Task 3
# 
# <div class="alert alert-success">
# <b>Exploring the data:</b>
#     
# 1. Write a function that can quantify the following information:   
#     - Range of chemical shifts   
#     - Maximum intensity   
#     - Level of noise in the spectrum background   
# 2. Extract and store these values for all NMR data    
# 3. Plot histograms of each of each parameter, and decide whether any corrections to the data are required   
# 4. Make any corrections required   
# </div>
# <!-- end silent_answer -->

# <!-- begin silent_answer -->
# ### 3.1/3.2 - Extract key features from each spectrum
# <!-- end silent_answer -->

# In[5]:


#FIXME


# <!-- begin silent_answer -->
# ### 3.3 - Plot histograms across all NMR data
# <!-- end silent_answer -->

# In[6]:


# FIXME


# <!-- begin silent_answer -->
# ### 3.4 - Apply corrections to standardise the data
# 
# For peak searching to work effectively, we need to standardise our data. The simplest change would be to normalise the intensity values so that, e.g. the maximum is 100.
# <!-- end silent_answer -->

# In[7]:


# FIXME


# <!-- begin silent_answer -->
# ## NMR peak hunting
# <a id='peak'></a>
# A number of different peak finding algorithms exist, but here we will focus on `scipy.signal.find_peaks` that you saw in unit 7. Use this to determine the number of peaks in each NMR spectrum, and store these values for plotting. We can optimise the peak finding using the `prominence` parameter (in this case; other problems might need different parameters).
# <!-- end silent_answer -->

# <!-- begin silent_answer -->
# ## Task 4
# 
# <div class="alert alert-success">
# <b> Finding Peaks:</b>
#     
# 1. Write a function capable of extracting peaks from any of the NMR spectra
# 2. Test how the peak-fitting parameters affect the number of peaks determined
#     > Hint: "prominence" is particularly useful for these peak shapes
# 3. Optimise these parameter(s) to determine the number of peaks in each spectrum
# </b>
# <!-- end silent_answer -->

# <!-- begin silent_answer -->
# ### 4.1 - Function to extract peaks
# <!-- end silent_answer -->

# In[8]:


# FIXME


# <!-- begin silent_answer -->
# ### 4.2 - Optimising the prominence parameter
# 
# To find peaks automatically we need to choose a prominence value. Let's systematically test a few different ones and see what the effect is on number of peaks. There are many ways to tackle this, but here we'll use the power of pandas to plot multiple curves quickly (and neatly)!
# <!-- end silent_answer -->

# In[9]:


# FIXME


# <details><summary {style='color:green;font-weight:bold'}> Click here to see some discussion on the prominence parameter. </summary>
#     
# A prominence above ~1 seems to give a fairly constant number of peaks, but anything below this gives a number of peaks strongly dependent on this parameter.
# 
# We will choose prominence = 1 to avoid biasing the number of peaks in one spectrum over another. It is possible that we are missing some "real" peaks, but we are unlikely to do better in one spectrum than another.
#     
# </details>

# <!-- begin silent_answer -->
# ### 4.3 - Optimise the parameters and extract peak count
# 
# <!-- end silent_answer -->

# In[10]:


# FIXME


# <!-- begin silent_answer -->
# ## 5. Analysing the results
# <a id='analysis'></a>
# Now we have computed the number of peaks, we can this for each spectrum in order to answer the original question.
# <!-- end silent_answer -->

# <!-- begin silent_answer -->
# ### Task 5
# <div class="alert alert-success">
# <b> Plotting:</b>
#     
# Plot graphs to determine whether the number of heteroatoms influences the number of NMR peaks.
# </div>
# <!-- end silent_answer -->

# In[11]:


# FIXME


# <!-- begin silent_answer -->
# # Conclusions
# <div class="alert alert-info">
# <b>
# Key points:</b>
#     
# - Starting from a hypothesis and some available data, you have been able to work through the problem logically to reach a conclusion.
# - It is important to inspect and "clean" your data before automating your analysis, as some assumptions may be incorrect.
# - There is more than one way to perform these sorts of analysis, but it is important to be aware of the benefits/limitations of different approaches.
# 
# <!-- end silent_answer -->

# # Tasks to complete after this session
# 
# - Read through the notebook with solutions, and check that you have understood the steps
# - Find and read the documentation for any Python commands you are less familiar with
# - Think about other ways to solve the problem, and try to implement/compare them
# - Extend your analysis to explore other peak searching approaches (or parameters)
# - Use statistical methods you have learned to quantify any correlations we have observed

# 
