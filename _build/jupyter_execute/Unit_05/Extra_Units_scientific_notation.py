#!/usr/bin/env python
# coding: utf-8

# # Working with Scientific Numbers and Quantities <a class="anchor" id="scinumb"></a>
# 
# ### Extra material for Unit 05
# 
# Authors:
# - Dr Valentina Erastova
# 
# Email: <valentina.erastova@ed.ac.uk> 

# Let's think about what numbers we _**plug into the command lines**_. The most expensive example of using wrong units is:
# 
# <img src="images/OrbiterCrash.png" width="600">
# 
# read full article [here](https://www.washingtonpost.com/wp-srv/national/longterm/space/stories/orbiter100199.htm )

# <div class="alert alert-warning">
# 
# **Example:** Distance (shortest route) between Edinburgh and London is  610 km. If you travel by train at an average speed 60 mph, how long will your travel be?
#     
# </div> 

# Recall:
# \begin{equation}
# \mathrm{time} = \frac{\mathrm{distance}}{\mathrm{speed}}
# \end{equation}
# 
# Correct the following:

# In[1]:


distance = 610
speed = 60

time = distance/speed

# FIXME
# convert km to miles
# 1 mile = 1.609 km 

factor = 1.609 #km/mile
distance_miles = distance/factor  
time = distance_miles/speed

print (f'Time of travel will be {time}')


# Corrected? Run the cell below to check if you got it right!

# In[2]:


if time > 8:
    print ("\n_______\n You are still missing something in the equation - think about units!") 


# <details>
#     <summary> <mark> SOLUTION:</mark> </summary>   
#    
# ```python
# distance = 610 #kilometers
# speed = 60 #miles per hour
# 
# #convert km to miles
# # 1 mile = 1.609 km  
# 
# factor = 1.609 #km/mile
#     
# distance_miles = distance/factor  
# 
# time = distance_miles/speed
# 
# print ('Time of travel will be', time, 'hours')
# ```
#  
# </details>

# ## 2.1 Units <a id="units"></a>

# Let's write the equation including units:
# 
# \begin{equation}
# t \text{[h]} = \frac{d \text{[km]}}{s \text{[m } \text{h}^{-1}\text{]}}
# \end{equation}
# 
# In the textbook/report/plot: 
# 
# &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   **physical quantity** is *italics*, e.g. \$m\$ is mass and m is metre   
# &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  **units** are straight with spaces betwen units, e.g. [ ms<sup>-1</sup>] is not same as [ m s<sup>-1</sup>]
# 
# in the notebook, use `#` to note your units and prevent a disaster! 

# The [Pint](https://pint.readthedocs.io/en/stable/index.html) package is a great tool to keep track of the units. 
# It does not come as a default on our Jupyter Notebook, and so we have to install it.

# In[3]:


get_ipython().system('pip install pint')


# Here we will only show an example, please follow the tutorial and manual of the Pint package if you decide to use it! 

# In[4]:


from pint import UnitRegistry

ureg = UnitRegistry()

#from before we know
distance = 610  #kilometers
speed = 60  #mph

#assign distance and speed their units
distance = distance * ureg.kilometer
print(f'Distance of our travel is {distance}')

#or ask for base, i.e. SI units
distance_SI = distance.to_base_units()
print(f'SI distance is {distance_SI}')


# In exactly same way we can assign speed its units, and check what is speed a measure of.
# We can then convert it to the unit we would like.

# In[5]:


#define speed
speed = speed * ureg.mile_per_hour  # mile/hour
print(f'Our average speed is {speed}')
print(f'Speed is a measure of {speed.dimensionality}')

#convert speed
speed_kmh = speed.to(ureg.kilometer_per_hour)
print(f'The speed of {speed} is equal to {speed_kmh}')


# Try to change convert distance and speed to other units.

# In[6]:


# FIXME


# <details>
#     <summary> Click here to see additional operations you can carry out using Pint!</summary>   
# 
# Convert distance to meters:<br>
# ```python
# #we can convert the distance to  meters
# distance_m = distance.to(ureg.meter)
# print('Distance should be in meters like this', distance_m)
#     
# ```
# 
# SI units: 
# ```python
# #or ask for base, i.e. SI units
# distance_SI = distance.to_base_units()
# print('SI distance is', distance_SI)
#     
# ```
# 
# Miles:
#     
# ```python
# #we can convert the distance to other common units, such as miles
# distance_nonSI = distance.to(ureg.miles)
# print('Distance in other units...', distance_nonSI)   
#     
# ```
# 
# Make the distance human-readable:    
# ```python
# #human readable
# distance_human = distance.to_compact()
# print('Most of humans would use this measure of distance', distance_human)
# ```
#  
# What if we try to assign a distance to be miles per hour? 
#     
# ```python
# distance_notOK = distance.to(ureg.mile_per_hour)
# ```
#     
# Can you convert speed into unusual units, such as decameter per fortnight?<br>
# We should be able to, as these are a measure of [length] per [time]
#     
# ```python    
# #define speed
# speed = speed * ureg.mile_per_hour  # mile/hour
# print('Speed is a measure of', speed.dimensionality)
# 
# #we can also decide to use a more unusual unit
# speed_odd = speed.to( ureg.decameter / ureg.fortnight)  
# #yep, fortnight is a registered unit of time in Pint package
# print('This is an unusual measure of speed', speed_odd)
# ```
# </details>

# Now that we know how to convert measurement units, let's go back to our original problem and calculate the travel time correctly. Does it match? what you did earlier? 

# In[7]:


ti = distance/speed_kmh

print(f'Our value of time is a measure of {ti.dimensionality}')

ti_h = ti.to(ureg.hour)
print (f'Our travel time is {ti_h}')

ti_day = ti.to(ureg.day)
print (f'or {ti_day.to_reduced_units()}')


# ### 2.1.1 Base vs Derived Units <a id="base_units"></a>

# Here we have shown the unit convertions working with **Base units**:
# 
# |  Base quantity    ||  SI base unit    || 
# |:-:|:-:|:-:|:-:|
# | length  |  \$l,\$ \$ x,\$ \$ r\$ |  meter |  m |   
# | mass  | \$m\$  | kilogram  |  kg |   
# |  time, duration | \$t\$  |  second |  s |   
# |  electric current | \$I,\$ \$  i\$  |  ampere |  A |   
# |  thermodynamic temperature | \$T\$  |  kelvin |  K |   
# | amount of substance  | \$n\$ |  mole |  mol |   
# |  luminous intensity | \$I_v\$  | candela	|cd |  

# There are also **Derived units**, for example:
# 
# - 1 N is the force required to accelerate a 1 kg mass by 1 m s<sup>-2</sup>   
# N = kg m s<sup>-2</sup>   
#         
# - 1 J is the energy expended in moving a distance of 1 m against a force of 1 N   
# J = N m = kg m<sup>2</sup> s<sup>-2</sup>   
#         
# - 1 J is the energy required to move a charge of 1 C through a potential difference of 1 V   
# J = C V   
# - and so on...    
# 
# _**When evaluating equations always multiply the units as well as the numbers and check that they work out correctly!**_
# 
# **Dimentions of the units** - either side of an equality MUST be the same! 
# 
# &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    \$c\$ = 2.998 x 10<sup>8</sup> m s<sup>-1</sup>   
# &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  or  
# &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    \$c\$ / m s<sup>-1</sup>  =  2.998 x 10<sup>8</sup>   

# <img src="images/mrIncreadible_meter.jpg" width="500">

# ### 2.1.2 Scientific Notation <a id="sci_notation"></a>

# Very large/small numbers can be written using scientific notation. For example, *C-O* single bond is 1.165 Å, we know that $1 \text{Å}=10^{−10}$ m, so we can write it as $1.165 \times 10^{-10}$ m, which is Python can also be written as `1.165e-10`.

# <div class="alert alert-info">
# <b>Working example:</b> What is the pressure of 1.00 mol of an ideal gas in a 1.00 m<sup>3</sup> vessel at 298 K?      
# </div>

# Recall:
# \begin{equation}
# pV = nRT
# \end{equation}
# 
# Rearrange:
# \begin{equation}
# p = \frac{nRT}{V}
# \end{equation}
# 
# Check units: 
# \begin{equation}
# p = \frac{ \text{mol} \text{ J K}^{-1} \text{mol}^{-1} \text{ K}} {\text{m}^{3}} = \frac{\text{J}} {\text{m}^{3}} = \frac{\text{N m}} {\text{m}^{3}} = \frac{\text{N}} {\text{m}^{2}} = \text{N m}^{-2}
# \end{equation}
# 
# 

# In[8]:


#declare known values
n = 1.00 # mol
R = 8.315 # J K-1 mol-1
T = 298 # K
V = 1.00 # m3

#calculate p
p = (n*R*T)/V  # N m-2

print(f'The pressure is {p} N m-2')


# Run the cell below to find out if you calculate it correctly.

# In[9]:


if p != 2477.87:
    print("\n_______\n You should be getting 2477.87 N m-2")
else:
    print("Well done!")


# ### 2.1.3 Significant figures

# Does the pressure reported above feature a correct number of significant figures? Unlikely!
# 
# You should always report the same number of significant figures as the _poorest_ dataset. To do this, use `round (number, x)` , where `x` is number of digits = 0 by defaut. `x > 0` for right side of the `321.123`, and `x < 0` for the left.

# Let's try to round the pressure to correct the significant figures.

# In[10]:


#What is x = ?

x = -1  # x = 1, or x = 2, or x = 3, or x = -1, or x = -2, ...
p_rnd = round(p, x)

print(f'The pressure is {p_rnd} N m-2') 


# Run the cell below to see whether you did it right!

# In[11]:


if p_rnd != 2480.0:
    print("\n_______\n Not there yet... should be 2480 N m-2")
else:
    print("Well done!")


# You can type sub and super scripts as follows:

# In[12]:


SUB = str.maketrans("0123456789-+", "₀₁₂₃₄₅₆₇₈₉₋₊")
SUP = str.maketrans("0123456789-+", "⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁺")

#Example
acid = 'H2SO4'.translate(SUB)
print('Sulfuric acid is {acid}')

units = 'km h-1'.translate(SUP)
print(f'Speed units are {units}')


# <div class="alert alert-info">
# Combine the <code>round(p, x)</code> with appropriate string formatting in an excercise below to get the following output: <code>Pressure is = 2480 N m⁻²</code>
# </div>

# In[13]:


# declare known values
n = 1.00 # mol
R = 8.315 # J K-1 mol-1
T = 298 # K
V = 1.00 # m3

# calculate p
p = (n*R*T)/V  # N m-2

# round the pressure
p_rnd = round(p, -1)

# units prettify
units="N m-2".translate(SUP)

# print 
print (f'Pressure is = {p_rnd:.0f} {units}') 


# <details>
#     <summary> <mark> SOLUTION:</mark> </summary>   
# 
# ```python
#     
# #declare known values
# n = 1.00 # mol
# R = 8.315 # J K-1 mol-1
# T = 298 # K
# V = 1.00 # m3
# 
# #calculate p
# p = (n*R*T)/V  # N m-2
# 
# 
# #round the pressure
# p_rnd = round(p, -1)
# 
# #units pretify
# units="N m-2".translate(SUP)
# 
# # print
# print ('Pressure is = %.0f %s' %(p_rnd, units))
# ```
# </details>

# ### 2.1.5 Scientific Constants <a id="sci_const"></a>

# Instead of looking up the gas constant on Wikipedia (or where did you look it up?) and then copy-pasting or typing it in, we can profit from the [scientific constants](https://docs.scipy.org/doc/scipy/reference/constants.html) `scipy.constants`, giving us a much more accurate value according to [CODATA Recommended Values of the Fundamental Physical Constants 2018](https://physics.nist.gov/cuu/Constants/) 
# 
# ```python
# from scipy.constants import R
# ```
# or more generally 
# ```python
# from scipy import constants 
# ```
# 
# Remembering all the full names and symbols can be tricky, so use the `constants.find('gas')` to help you here!

# In[14]:


from scipy import constants 

# list of physical_constant keys containing a string 'gas'
constants.find('gas')


# We now know that our constant is called 'molar gas constant' so we can import its value, and also check units and precision.

# In[ ]:


R_value=constants.value('molar gas constant')
R_units=constants.unit('molar gas constant')
R_prec=constants.precision('molar gas constant')

print(f'R = {R_value} {R_units} and has the following precision {R_prec}')


# The `precision of 0.0` means that the **value of molar gas constant is exact**, indeed during the 2019 redefinition of SI base units both Avogadro number and Boltzmann constant have been defined with exact numerical values, making gas constant, R, also exact.

# <div class="alert alert-success">
#     <b>Task:</b> <br>
# Update your code to benefit from the <code>scipy.constants</code> package. How much difference does it make?
# </div>

# <details>
#     <summary>  <mark> SOLUTION:</mark> </summary>   
# 
# ```python        
# from scipy import constants 
# 
# # get R
# R_value = constants.value('molar gas constant')
# 
# #declare known values
# n = 1.00 # mol
# R = 8.315 # J K-1 mol-1
# T = 298 # K
# V = 1.00 # m3
# 
# #calculate p using the manually written R
# p = (n*R*T)/V  # N m-2
# print (f'Pressure is = {p:.5f} N m-2')
# 
# #calculate p using R from the scipy.constants
# p_const=(n*R_value*T)/V
# print(f'Pressure using scipy.constants is = {p:.5f} N m-2')
# 
# #find the difference
# diff=p-p_const
# diff_pr= 2*diff*100/(p+p_const)
# print(f'The difference due to use of more precice constant is = {diff:.5f}, which makes it = {diff_pr:.3f} percent')
# 
# print ('Nevertheless, out other measurments have much greater margin of precision,
#        and so we must report the pressure as before...')
# 
# p_rnd = round(p_const, -1)
# units = "N m-2".translate(SUP)
# 
# print (f'Pressure is = {p_rnd:.0f} {units}')
# ```
# </details>

# See all the good practices on [Units](#units), [Scientific Notation](#sci_notation), [Constants](#sci_const) and [String formating](string_formatting) (seen in Part II of this Unit) applied in the short code below: 

# In[ ]:


from scipy import constants 

# get R
R_value = constants.value('molar gas constant')

#declare known values
n = 1.00 # mol
T = 298 # K
V = 1.00 # m3
    
p_rnd = round(p_const, -1)
units="N m-2".translate(SUP)

print (f'Pressure is = {p_rnd:.0f} {units}')


# ---
