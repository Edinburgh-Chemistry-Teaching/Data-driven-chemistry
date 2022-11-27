---
title: 'Course Materials for An Introduction to Data-Driven Chemistry'
tags:
  - chemistry
  - python
authors:
  - name: James Cumby
    orcid: 0000-0003-xxxx-xxxx
    affiliation: "1"
  - name: Valentina Erastova
    orcid: 0000-0002-xxxx-xxxx
    affiliation: "1"
  - name: Jasmin Güven
    orcid: 0000-0002-xxxx-xxxx
    affiliation: "1"
  - name: Claire Hobday
    orcid: 0000-0002-xxxx-xxxx
    affiliation: "1"
  - name: Antonia S. J. S. Mey
    orcid: 0000-0001-5911-0472
    affiliation: "1"
  - name: Hannah Pollack
    orcid: 0000-0002-xxxx-xxxx
    affiliation: "1"
  - name: Rafal Szabla
    orcid: 0000-0002-xxxx-xxxx
    affiliation: "2"
affiliations:
 - name: EaStCHEM School of Chemistry, University of Edinburgh, Edinburgh, United Kingdom 
   index: 1
 - name: Warclaw
   index: 2

date: 23 November 2022
bibliography: paper.bib
---

# Summary
Data-Driven Chemistry is a course aimed at undergraduate students in Chemistry with no prior knowledge in programming and programatic data analysis. It is designed as an 10 week long course, typically spanning a whole semester, to give an introduction to Python programming used for data analysis typically found in a Chemistry degree. The course consists of 10 Jupyter notebooks which get worked through in a blended learning environment of live coding and explanations, followed by a set of in-course tasks to be solved individually or in a pair programming scenario. Typically demonstrators will be available to help with the content. The content of the notebook covers an introduction to Python, plotting with Python and statistical analysis, and data fitting all with a focus on chemistry related tasks and datasets. Some of these tasks where aligned with the labs carried out in the same semester. While not following fully following Software carpentry templates and guidelines, the introduction to Python covered in Notebook 2-4 is adapted from the core lesson on [Plotting and Programming in Python](http://swcarpentry.github.io/python-novice-gapminder/). Generally, we followed carpentry design ideas as best as possible when designing the different units. In the original course the material was hosted online using the Notable service provided by the University of Edinburgh, here we have migrated to content for convenience to Google Colab. While in principle this course is designed to be taught in a blended learning environment as a whole, each notebook will cover a set of self-contained topics. This modular design allows for aspects of the course to be reused and mix-and-matched with other courses. The online hosting with worked examples also allows this course to be used for self-guided learning and thus learning is not limited to a university classroom setting. 

# Statement of Need
The modern world is a digital world allowing for upscaling and automation of chemical processes through robots[@] but also fast production of large scale datasets [@]. Analysis with GUI interfaces or spreadsheet based tools may not be easily allow for a robust, fast, and reproducible analysis of these large scale data. Programming based solutions fare much better at these kind of tasks, but programming is not typically taught as a skill across Chemistry degrees, unlike in Physics, Maths, or even Biology[@white2022data]. To make sure Chemistry graduates, competing with other STEM graduates, do not lack computational skills both the Royal Society of Chemistry [@employability] and the American Chemical Society [@neiles2020professional] have identified good computational skills as a key for employability [@hill2019undergraduate]. This course was designed to address this gap in the chemistry curriculum at the University of Edinburgh and making the material available open source hopefully encourages their use in many other educational settings. Introducing aspects of programming broadly into a chemistry degree, have been explored in very recent years, through for example incorporating programming aspect into a course on mathematics for chemists [@hutchison2021integrating]. While this give a good foundation of programming, students often wonder why they have to learn dry aspects of programming without direct application to their degree choice. There are excellent resources for self study through books [@tanemura2022python], or more general material to study Python programming [@carpentries,@others]. However, little material exists for a general introduction to programming and data analysis geared towards complete novices, without a specific focus, on for example, physical chemistry [@baptista2021using], analytical chemistry [@menke2020series], or machine learning for chemistry [@lafuente2021gentle]. The course presented here, bridges this gab in teaching the basics of Python programming, and how these concepts can be applied to data in physics, inorganic, analytical, and even organic chemistry.   

# Course Development Background
In 2019, motivated, as outlined by the statement of need, a compulsory undergraduate course for teaching data analysis in Python with a subject focus on Chemistry was approved in the School of Chemistry at the University of Edinburgh. With the start of the pandemic, the development of the course was accelerated and ran in a shorter version (six, 3-hour workshops instead of ten 3-hour workshops) in the autumn of 2020 as a replacement for in-person physical chemistry labs. Since then, the full 10 times 3-hour workshop course was run in the academic year of 2021/22 fully online, and 2022/23 in-person. The material presented here is the fine tuned material of three years of development and tested for suitability to be delivered online or in-person. 


# Overview, Content, and Structure
## Target Audience 
The course is aimed at early year undergraduate students in Chemistry, either first or second year, with little or no programming background in Python or other languages. The cohort of 2022/23 responded to the question: "Do you know how to code?" overwhelmingly with "I have no prior coding experience"  (62%) and a good 30% with only some basic Python or coding experience. Only one respondent answered that they were confident in the use of Python. The goal of the course is to equip students with the knowledge to use Python in data-analysis typically encountered in Chemistry. At the end of the course students should be proficient in using Python to:

- Break a problem into logical steps, and use loops and decision operations to solve tasks.
- Perform numerical operations such as vector algebra and calculate simple statistics on data sets.
- Read and clean experimental data, visualise the data and draw appropriate conclusions from the data through simple statistical analysis
- Fit models to numerical data, and present results in a clear and well documented manner.   
- Write readable, well-documented short snippets of code for data analysis making use of functions, loops, and conditionals. 


## Structure and Assessment
The way in which the course is structured is similar to [@muller2022pcp]. The first four units give an introduction to algorithmic thinking and Python syntax and were partially adapted from [Plotting and Programming in Python](http://swcarpentry.github.io/python-novice-gapminder/). Very little focus on domain specific chemistry content is provided in this session to avoid too much mental load in terms of new concepts. `Unit_05` to `Unit_07` cover essentials in statistics students will have encountered in their mathematics course. This includes topics around probability distributions, comparing datasets, statistical testing (t-tests) and plotting. the last three Units are the core units around applications to domain specific concepts in chemistry making use of the learned tools. The course had one 3-hour workshop per week with the material covered, using a blended learning environment with live coding and time for problem solving either alone or in a pair-programming setting. For around 100 students 10 PhD student demonstrators were available for help with immediate questions, as well as the instructor themselves. Most 3-hour sessions were roughly split into 1 hour of teaching and 2 hours of answering questions, typically with no more than 20 minutes teaching blocks at a time. After the first three sessions students had additional formative assessment in Edinburgh's online learning environment with automated feedback (Not included in this material here). In addition we offered 1-hour Q&A sessions every other week for students to get help with questions around the material. We used three summative assessment notebooks through NBgrader [@jupyter2019nbgrader] released after week one, four, and seven, worth 50% of the course and a mini-project released in week 8 with two weeks completion. None of the assessment material is included here. 

## Content
Data-Driven Chemistry consists of 10 Units, each meant for a 3-hour workshop session, either in-person or online. A summary of each unit can be found in the table below:

| Unit | Content Summary                 | Materials |
|------|---------------------------------|-----------|
| 1    | An Introduction to algorithmic thinking and using Jupyter              |[Link to Notebook] (https://github.com/Edinburgh-Chemistry-Teaching/DDC/blob/main/Unit_01/Unit_01.ipynb)|
| 2    | Variables (int, float, string), Lists, Dictionaries and Tuples in Python|[Link to Notebook] (https://github.com/Edinburgh-Chemistry-Teaching/DDC/blob/main/Unit_02/Unit_02.ipynb) |
| 3    | Loops and conditional                                                  |[Link to Notebook] (https://github.com/Edinburgh-Chemistry-Teaching/DDC/blob/main/Unit_03/Unit_03.ipynb) |
| 4    | Functions, Pandas, and basic IO                                        |[Link to Notebook] (https://github.com/Edinburgh-Chemistry-Teaching/DDC/blob/main/Unit_04/Unit_04.ipynb) |
| 5    | An introduction to plotting, units and statistics                      |[Link to Notebook] (https://github.com/Edinburgh-Chemistry-Teaching/DDC/blob/main/Unit_05/Unit_05.ipynb) |
| 6    | comparing distributions, t-tests, and molecular geometries             |[Link to Notebook] (https://github.com/Edinburgh-Chemistry-Teaching/DDC/blob/main/Unit_06/Unit_06.ipynb) |
| 7    | Correlations in data and fitting data                                  |[Link to Notebook] (https://github.com/Edinburgh-Chemistry-Teaching/DDC/blob/main/Unit_07/Unit_07.ipynb) |
| 8    | Applications I  -- more specifics                                                        |[Link to Notebook] (https://github.com/Edinburgh-Chemistry-Teaching/DDC/blob/main/Unit_08/Unit_08.ipynb) |
| 9    | Applications II   -- more specifics                                                         |[Link to Notebook] (https://github.com/Edinburgh-Chemistry-Teaching/DDC/blob/main/Unit_09/Unit_09.ipynb) |
| 10   | Applications III   -- more specifics                                                       |[Link to Notebook] (https://github.com/Edinburgh-Chemistry-Teaching/DDC/blob/main/Unit_010/Unit_10.ipynb)]

The content is roughly grouped into 3 main parts. `Unit_01` to `Unit_04`, introduce concepts around algorithmic thinking, Python syntax including, variables, loops, functions, libraries, documentation, how to get help, and how to read in files. `Unit_05` to `Unit_07` then introduces concepts from `scipy` [@],  `numpy` [@], matplotlib [@], and pandas [@] to do basic statistical analysis and plotting of Chemistry related examples. Our strategy here was to incorporate as many other aspects of the chemistry curriculum into the teaching of Python. So for example students will have seen a lot of mathematical concepts around fitting data and comparing distributions which now has direct application. Reminding students of mathematical concepts they learned in their first year allows repetition and applications to problems in chemistry. The domain specific twist aims to boost motivation in students to engage with these mathematical concepts. `Unit_08` to `Unit_10` covers specific application examples in chemistry from different areas of chemistry [...expand here on what we actually cover. ] Some of the applications directly tie into their lab experiments. 


# In workshop Self-assessment and feedback

-  Mentimeter for in-course assessment. 

# Conclusion

After three years, the material is still in development and will be adjusted based on student's feedback. However, we hope that the material in its current state will be useful to others and its modular aspect means even parts of the material can be adapted and reused for teaching settings aimed at Chemistry students. Removing the barrier for installation through running Colab means it is accessible for novices both in a guided university setting and any chemistry enthusiast. 

# Author's Contribution
Authors are listed in alphabetical order, specific contributions by each author are found in the following: James Cumby (JC), Valentina Erastova (VE), Claire Hobday (CH), and Antonia Mey (ASJSM) have been teaching this course at the University of Edinburgh since 2021/22 and contributed roughly equally to the material creation and teaching. See below for more details. Rafal Szabla (RS) taught one unit and created content for it in 2020/21, when the course was run as a Physical chemistry lab replacement in a shortened form during the pandemic. 
**JC:** Is the course organiser for the module taught at the University of Edinburgh and created the material for `Unit_01` and `Unit_09`, contributed to `Unit_05`, gave feedback on everyones material, and helped edit the manuscript.   
**VE:** Created material for `Unit_05` and `Unit_08`, contributed to `Unit_06`, and helped edit the manuscript.   
**JG:** Contributed to material for `Unit_10`, and helped edit the manuscript.    
**CH:** Created material for `Unit_03` and `Unit_04`, and helped edit the manuscript.   
**ASJSM:** Created material for `Unit_02`, `Unit_06`, `Unit_07`, and `Unit_10`, provided feedback and small contributions to most other units, and wrote the manuscript.    
**HP:** Contributed to material for `Unit_05`, and helped edit the manuscript. 
**RS:** Created the material for molecular geometries forming part of `Unit_06`, and gave feedback on the manuscript. 


# Acknowledgements 

We would like to acknowledge Matteo Degiacomi, Software Carpentries, and all the PhD student demonstrators who helped with teaching the material, giving feedback and creating some of the assignments. 

# References
