#!/usr/bin/env python
# coding: utf-8

# # Unit 09: Applications II  Protein SAXS and simulation data

# <a rel="license" href="https://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons Licence" style="border-width:0" src="https://licensebuttons.net/l/by/4.0/88x31.png" title='This work is licensed under a Creative Commons Attribution 4.0 International License.' align="right"/></a>
# 
# Authors: 
# - Dr Antonia Mey
# - Jasmin Güven   
# Email: antonia.mey@ed.ac.uk
# 
# Thanks to: Dr Rafal Szabla
# 
# ### Learning objectives
# By the end of this unit, you should be able to
# * Read and manipulate'real' data files and troubleshoot them.
# * Understand hidden characters in files.
# * Estimate error bars and plot them from absorbance data.
# * Analyse UV-Vis data using Beer-Lambert's law.
# * Load protein trajectory data from a simulation.
# * Compute running averages over trajectories (dataseries).

# ### Table of Contents
# 
# ### Application 2: Protein crystallography and simulations
# 1. [Working with protein crystals and molecular simulations](#1-working-with-protein-crystals-and-molecular-simulations)   
#     1.1 [PDB files](#11-pdb-files)     
#     1.2 [Measuring properties from crystal structures](#12-measuring-properties-from-crystal-structures)     
#     1.3 [What are molecular dynamics simulation?](#13-what-are-molecular-dynamics-simulations)    
# 2. [Excursion into thermodynamics or how to check the equilibration of a simulation](#2-excursion-into-thermodynamics-or-how-to-check-the-equilibration-of-a-simulation)    
#      2.1 [Tasks 4](#tasks-4)   
# 3. [Assessing the stability of a protein in a simulation](#3-assessing-the-stability-of-a-protein-in-a-simulation)    
#      3.1 [Tasks 5](#tasks-5)    

# **<span style="color:black">Jupyter Cheat Sheet</span>**
# - To run the currently highlighted cell and move focus to the next cell, hold <kbd>&#x21E7; Shift</kbd> and press <kbd>&#x23ce; Enter</kbd>;
# - To run the currently highlighted cell and keep focus in the same cell, hold <kbd>&#x21E7; Ctrl</kbd> and press <kbd>&#x23ce; Enter</kbd>;
# - To get help for a specific function, place the cursor within the function's brackets, hold <kbd>&#x21E7; Shift</kbd>, and press <kbd>&#x21E5; Tab</kbd>;

# # Import libraries

# In[1]:


import glob
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# # 1. Working with protein crystals and molecular simulations
# <a id="1-working-with-protein-crystals-and-molecular-simulations"></a>
# 
# Proteins are polymers that are made up of 20 different amino acids. It is possible to crystalise proteins and then use X-rays to probe their structure. 
# 
# All structural data of proteins are collected in the [protein data bank](https://www.rcsb.org) (PDB). With over 180000 protein structures available. 3D structure data is invaluable for applications in many different areas of chemistry, as proteins underpin most vital functions in living organisms as natural catalysts. 
# 
# ## 1.1 PDB files <a id="11-pdb-files"></a>
# 
# To store information about proteins a fileformat called pdb was invented. It stores the names of the atoms in the protein, as well as the 3D coordinates that were determined from the crystal structure. Don't worry you will not need to interact much with these files. In Jupyter we can visualise protein structures from pdb files in different ways. In the following we will use `py3Dmol`.
# 
# Run the code cell below to see the first 20 lines of a pdb file:

# In[ ]:


get_ipython().system('head -n 20 data/Section4/1aki.pdb')


# As part of her final year project Rachel has been looking at the **hen egg white lysozyme** protein. She has been investigating the structure of it and has also run simulations to look at its stability over time. But she needs some help with analysing the simulations and understanding the data. 
# 
# Let's start by visualising the protein in the notebook:

# In[ ]:


# Install py3Dmol
get_ipython().system('pip install py3Dmol')


# In[ ]:


import py3Dmol
# This line will grab the pdb file from the data bank
view = py3Dmol.view(query="pdb:1aki") 
view.setStyle({"cartoon":{"color":"spectrum"}})
view.show()


# ## 1.2 Measuring properties from crystal structures <a id="12-measuring-properties-from-crystal-structures"></a>
# 
# It is possible to measure different properties from the X-ray structure data, such as `bond lengths`, `angles`, etc. You will try some of this as part of the assessment.

# ## 1.3 What are molecular dynamics simulations? <a id="13-what-are-molecular-dynamics-simulations"></a>
# Molecular dynamics (MD) simulations are a way to understand how proteins behave inside cells, by using a computer to model this behaviour. Cells are crowded environments full of proteins and water. 
# 
# Take a look at this movie of a simulation of a bacterial cell. 

# <img src='data/Section4/crowded_cell.mp4'></img>

# In a molecular dynamics (MD) simulation we model atoms and bonds like balls and springs and generate so called trajectories over time using Newton's Laws of motion. 
# 
# Newton's second law is given by:
# 
# $$\mathbf{F} = \frac{d^2\mathbf{r}_i}{dt^2}$$
# 
# where $\mathbf{F}$ is the force on each atom $i$ and $\mathbf{r}_i$ is the position of atom $i$. The above equation is solved at every time step over a number of time steps, to calculate the position and velocity of each atom. 
# 
# To get started with an MD simulation you need some initial coordinates for a protein. These are often taken from the protein data bank. 
# 
# Here you see an example of a short trajectory of a single protein: lysozyme.
# 

# <img src='data/Section4/lys.gif' width='400'></img>

# # 2. Excursion into thermodynamics or how to check the equilibration of a simulation
# <a id="2-excursion-into-thermodynamics-or-how-to-check-the-equilibration-of-a-simulation"></a>
# 
# Molecular simulations are often run in similar conditions that mimic a lab environment, namely at **constant temperature**, **constant pressure**, and **constant number of particles** (NPT). To achieve this, the simulation needs to get a chance to equilibrate and some clever algorithmic tricks need to be done to achieve $N$ i.e. number of particles, $T$ temperature, and $p$ pressure to be constant. 
# 
# This can be done with pressure and temperature equilibrations. If you want to know more about the algorithms used in these equilibrations, see https://ftp.gromacs.org/pub/manual/manual-5.0.4.pdf.
# 
# The temperature equilibration step is called NVT, because the number of atoms $N$, volume $V$ and temperature $T$ are kept constant. Similarly, the pressure equilibration step is called NPT.
# 
# We will also plot the **running average** to see the equilibration better. The running average, denoted SMA for Simple Moving Average, is defined as 
# 
# $$ \mathrm{SMA} = \frac{1}{k} \sum_{i = n-k+1}^{n} p_i$$
# 
# where $p$ is a data point, $k$ is the window and $n$ is the total number of data points. 

# # Tasks 4 <a id="tasks-4"></a>

# <div class="alert alert-success">
#     <b>Task 4.1 </b>: Plotting temperature over time from the MD simulation.
# </div>
# 
# The time is in picoseconds (ps) and the data is collected for 100 ps. The temperature is in Kelvin. 
# 
# * Load in a file called `temperature.txt` from the folder `data/Section5`. You can take a look at the file in the folder to see what character is used as the separator. 
# * Plot the temperature against time. 
# * Add axis correct axis labels.

# In[ ]:


# FIXME


# <details>
# <summary {style="color:green; font-weight:bold"}> Click here to see the solution to Task 4.1</summary>
#     
# ```python
# 
# # Load data in
# NVT = pd.read_csv("data/Section5/temperature.txt", sep = "\t")
# 
# # Get time and temperature in lists
# time = NVT["t"].tolist()
# temperature = NVT["T"].tolist()
# 
# 
# # Plot
# fig, ax = plt.subplots()
# ax.plot(time,temperature, color = "black")
# ax.set_xlabel("Time (ps)")
# ax.set_ylabel("Temperature (K)")
# plt.show()
# ```
# 
# </details>

# <div class="alert alert-success">
#     <b>Task 4.2</b>: Write a function that will compute the running average of an observable, e.g. temperature. 
# </div>
# 
# Define a function `SMA()` that takes in a list of data, total number of data points and the size of the window. Calculate the cumulative sum and from this calculate the running average, and return it.
# 
# Take a look at the draft Rachel has made, can you fix the function so that it will work? It is easiest to debug problems with the function if you try and plot the output with the data you are trying to compute the running average for.
# 
# You could also check visually if this is similar to the running average function you can find in `pandas`.
# 

# In[ ]:


# FIXME
def SMA(data, n, window):
    '''
    Function to calculate the simple moving average. 
    
    Parameters
    ----------
    data: list
        list of data 
    n: int
        total number of data points
    
    window: int
        size of the running average window
    '''

    S_i = 0
    cumulative_sum = []
    for i in range(n):
        cumulative_sum.append(S_i)
        S_i = S_i + data[i]
    cumulative_sum = np.array(cumulative_sum)    
    running_avg = cumulative_sum / float(window)
    return running_avge


# <details>
# <summary {style="color:green; font-weight:bold"}> Click here to see the solution to Task 4.2 </summary>
#     
# ```python
# # Example solution
# 
# def SMA(data, n, window):
#     """
#     Function to calculate the simple moving average. 
#     
#     Parameters
#     ----------
#     data: list
#         list of data 
#     n: int
#         total number of data points
#     
#     window: int
#         size of the running average window
#     """
# 
#     S_i = 0
#     cumulative_sum = []
#     for i in range(n):
#         S_i = S_i + data[i]
#         cumulative_sum.append(S_i)
#     cumulative_sum = np.array(cumulative_sum)    
#     running_avg = (cumulative_sum[window:] - cumulative_sum[:-window]) / float(window)
#     return running_avg
# 
# ```
# 
# </details>

# <div class="alert alert-success"><b>Task 4.3</b> Use the above function and plot the running average together with the original data.  </div> 
# 
# **10-ps average for NVT**
# 
# 1. Plot the temperature data in black, with label `"Data"`
# 2. Plot the 10-ps running average for temperature in red, with label `"10-ps average"`
# 3. Define axis labels and add a legend.
# 
# Do you think the simulation has equilibrated?

# In[ ]:


# FIXME

ax.plot(time,temperature, color = "black")


# <details>
# <summary {style="color:green; font-weight:bold"}> Click here to see the solution to Task 4.3</summary>
#     
# ```python
# fig, ax = plt.subplots()
# ax.plot(time, temperature, color = "black")
# ax.set_xlabel("Time (ps)")
# ax.set_ylabel("Temperature (K)")
# n_T = len(temperature)
# T_SMA = SMA(temperature, n_T, 10)
# ax.plot(time[10:],T_SMA, color = "red", label = "10-ps running avg.")
# ax.plot(time,temperature, color = "black", label = "Data")
# 
# ax.legend(loc="upper right")
# plt.show()
# ```
# 
# </details>

# <div class="alert alert-warning">
#     <b>Advanced Task 4.4</b>: NPT equilibration with density 
# </div>
# 
# The time is in picoseconds (ps) and the data is collected for 100 ps. The density is in kg m$^{-3}$. 
# 
# 1. Load in a file called `density.txt` from the folder `data`. You can take a look at the file in the folder to see what character is used as the separator. 
# 2. Plot the density against time. 
# 3. Plot the SMA of density in red.
# 4. Add correct axis labels and a legend.
# 

# In[ ]:


# FIXME


# <details>
# <summary> Click here to see the solution to Task 4.4 (advanced) </summary>
#     
# ```python
# # Load data in
# density_data = pd.read_csv("data/Section5/density.txt", sep = "\t")
# 
# time = density_data["t"].tolist()
# density = density_data["rho"].tolist()
# 
# n_rho = len(density)
# 
# 
# fig = plt.figure()
# ax = fig.add_subplot()
# ax.plot(time,density, color = "black")
# ax.set_xlabel("Time (ps)")
# ax.set_ylabel("Density (kg m$^{-3}$)")
# rho_SMA = SMA(density,n_rho,10)
# ax.plot(time[10:],rho_SMA, color = "red", label = "10 ps running avg.")
# ax.plot(time,density, color = "black", label = "Data")
# ax.legend(loc = "lower right")
# plt.show()
# ```
# 
# </details>

# # 3. Assessing the stability of a protein in a simulation <a id="3-assessing-the-stability-of-a-protein-in-a-simulation"></a>
# 
# In this part we will consider the root-mean-square deviation (RMSD) and the radius of gyration of the protein during the simulation. These two quantities are useful to judge if the protein maintains it shape, i.e. if the simulation is stable or the protein breaks apart. 
# 
# The root-mean square deviation is given by
# 
# $$\mathrm{RMSD} = \sqrt{\frac{1}{N} \sum_{i=0}^{N} (v_i - w_i )^2}$$
# 
# where $v_i$ is the position of a reference structure and $w_i$ is the structure we're interested in.
# 
# The radius of gyration is a *measure of the compactness* of a protein, and is given by
# 
# $$R_\mathrm{g}(x) = \sqrt{\frac{\sum_i m_i r_i(y)^2 + m_ir_i(z)^2}{\sum_i m_i}}$$
# 
# 
# 

# # Tasks 5 <a id="tasks-5"></a>

# <div class="alert alert-success">
#     <b>Task 5.1 </b>: Radius of gyration plot
# </div>
# 
# The radius of gyration data is given in the file `data/Section6/gyrate.txt`. The time is in picoseconds (ps) and the radius of gyration values are given in nanometers (nm). 
# 
# 1. Load the file gyrate.txt in.
# 2. Plot the radius of gyration. 
# 3. Add axis labels.
# 

# In[ ]:


# FIXME



# <details>
# <summary {style="color:green; font-weight:bold"}> Click here to see the solution to Task 5.1 </summary>
#     
# ```python
# 
# Rg_data = pd.read_csv("data/Section6/gyrate.txt", sep = "\t")
# 
# time = Rg_data["t"].tolist()
# Rg = Rg_data["Rg"].tolist()
# 
# fig = plt.figure()
# ax = fig.add_subplot()
# ax.plot(time, Rg, color = "k")
# ax.set_xlabel("Time (ps)")
# ax.set_ylabel("R$_\mathrm{g}$ (nm)")
# 
# ```
# 
# </details>

# <div class="alert alert-success">
#     <b>Task 5.2 </b>: Average radius of gyration
# </div>
# 
# We can calculate the average from the $R_\mathrm{g}$ data and use the standard deviation as an estimate of the error on the mean value. 
# 
# Code this in the cell below and output the values nicely.
# 

# In[ ]:


# FIXME


# <details>
# <summary {style="color:green; font-weight:bold"}> Click here to see the solution to Task 5.2</summary>
#     
# ```python
# 
# mean_Rg = np.mean(Rg)
# std_Rg = np.std(Rg)
# 
# print(f"Radius of gyration: ({mean_Rg:.2f} +/- {std_Rg:.2f}) nm")
# 
# ```
# 
# </details>

# <div class="alert alert-warning">
#     <b>Advanced Task 5.3 </b>: RMSD plots
# </div>
# 
# As with the above equilibration plots, we want to see if the RMSD plot levels off. 
# 
# To plot the RMSD plots, we have to load in two files: RMSD.txt and RMSD-xtal.txt (both are found in `data/Section6`), where the former is the simulated structure and the latter is the crystal structure. 
# 
# The RMSD is measured in nanometers (nm) and time is now in nanoseconds (ns).
# 
# 1. Load the files in.
# 2. Plot both RMSD and RMSD_xtal in the same plot. 
# 3. Add axis labels and a legend.
# 

# In[ ]:


# FIXME


# <details>
# <summary {style="color:green; font-weight:bold"}> Click here to see the solution to Task 5.3 </summary>
#     
# ```python
# 
# RMSD_data = pd.read_csv('data/Section6/rmsd.txt', sep = '\t')
# RMSD_xtal_data = pd.read_csv('data/Section6/rmsd-xtal.txt', sep = '\t')
# 
# RMSD_t = RMSD_data['t'].tolist()
# RMSD = RMSD_data['RMSD'].tolist()
# RMSD_xtal_t = RMSD_xtal_data['t'].tolist()
# RMSD_xtal = RMSD_xtal_data['RMSD'].tolist()
# 
# fig = plt.figure()
# ax = fig.add_subplot()
# ax.plot(RMSD_t, RMSD, color = 'black', label = 'MD structure')
# ax.plot(RMSD_xtal_t, RMSD_xtal, color = 'red', label = 'Crystal structure')
# ax.set_xlabel('Time / ns')
# ax.set_ylabel('RMSD / nm')
# ax.legend()
# 
# ```
# 
# </details>

# <div class="alert alert-warning"><b> Questions for discussion</b> </div>
# 
# 1. Has the protein stabilised in the MD simulation?
# 2. Why aren't the MD structure and the crystal structure always perfectly overlapping?

# <details><summary {style="color:green; font-weight:bold"}> Click here to see the answers</summary>
# 
# 1. Yes, you can see it levels off to roughly 0.1 nm.
# 2. This is because the MD structure has been energy-minimised and because the position restraints are not 100% accurate. 

# ## END UNIT 9
# ---
