---
title: 'Course Materials for an Introduction to Data-Driven Chemistry'
tags:
  - chemistry
  - python
  - undergraduate
authors:
  - name: James Cumby
    orcid: 0000-0003-xxxx-xxxx
    affiliation: "1"
  - name: Matteo T. Degiacomi (?)
    orcid: 0000-0002-xxxx-xxxx
    affiliation: "3"
  - name: Valentina Erastova
    orcid: 0000-0002-6747-3297
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
  - name: Hannah Pollak
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
 - name: Durham
   index: 3 

date: 23 November 2022
bibliography: paper.bib
---

# Summary
Data-Driven Chemistry is a course aimed at undergraduate students in Chemistry with no prior knowledge of programming and programmatic data analysis. It is designed as a 10-week-long course, introducing Python programming and its usage in data analysis typically required for a Chemistry degree. The course consists of 10 Units, designed to be used in a blended learning environment of live coding and explanations, followed by a set of in-course tasks to be solved individually or through pair programming.
Generally, we aimed to follow Carpentry design ideas as closely as possible for each Unit. While, in principle, this course is designed to be taught as a whole, each Unit will cover a set of self-contained topics. The idea behind the modular design is to make the reuse and mix-and-matched with other courses as easy as possible.
The original material was hosted online using the Notable service provided by the University of Edinburgh, for the user convinience, here we have migrated the content to Google Colab. The online hosting on Colab will enable self-guided learning, as well as classroom-based learning, ensuring that the learning is not only limited to a university classroom setting.

# Statement of Need
The modern world is digital, allowing for upscaling and automation of chemical processes through robots [@], but also fast production of large-scale datasets [@]. Data analyses carried out with Graphical User Interfaces (GUI), or spreadsheet-based tools are often limited in robustness, speed, and reproducibility. Programmatic solutions fare much better in this context, but programming is not typically taught as a skill across Chemistry degrees, unlike in Physics, Mathematics, or even Biology [@white2022data]. Both the Royal Society of Chemistry [@employability] and the American Chemical Society [@neiles2020professional] have identified good computational skills as a key for graduate employability [@hill2019undergraduate]. Our course is designed to address this gap in the undegraduate Chemistry  curriculum at the University of Edinburgh, and thus, to ensure that Chemistry graduates remain competitive with other STEM graduates. The material is made available as open source, with the hope that it may be used in other educational settings.

In recent years, programming has been integrated into Chemistry degrees as a course on _Mathematics for Chemists_ [@hutchison2021integrating]. While this approach provides a good foundation of programming, students are often left with little applications or examples relevant to their specific degree. There are excellent resources for self-study through books [@tanemura2022python] as well as more general material for self-study of Python programming [@carpentries,@others]. Some material exists for a general introduction to programming and data analysis with a focus on, for instance, physical chemistry [@baptista2021using], analytical chemistry [@menke2020series], or machine learning for chemistry [@lafuente2021gentle]. However, little material is available for complete novices that combines teaching the basics of Python programming along with how it can be applied to data in physical, inorganic, analytical, and even organic chemistry. The presented course bridges this gap. 

# Overview, Content, and Structure
## Target Audience 
The course is aimed at early year undergraduate students in Chemistry, either first or second year, with little or no programming background in Python or other languages. The cohort size is typically around 100 students. During the first lecture, the 2022/23 cohort was asked the question: "Do you know how to code?". 
Overwhelmingly (62%), students replied with "I have no prior coding experience", while an additional 30% replied "I only have some basic Python or coding experience". Only one respondent answered that they were confident in the use of Python. 

At the end of the course students should be proficient in using Python to:
- Break a problem into logical steps, and use loops and decision operations to solve tasks;
- Perform numerical operations such as vector algebra and calculate simple statistics on data sets;
- Read and clean experimental data, visualise the data and draw appropriate conclusions from the data through simple statistical analysis;
- Fit models to numerical data, and present results in a clear and well documented manner;
- Write readable, well-documented short snippets of code for data analysis making use of functions, loops, and conditionals.

## Content
The course is structured similarly to [@muller2022pcp]. Data-Driven Chemistry module consists of 10 Units, each meant for a 3-hour workshop session, either in-person or online, and provides further tasks for completion at home. 
A summary of each unit can be found in the Table 1 below:

| Unit | Content Summary                 | Materials |
|------|---------------------------------|-----------|
| 1    | An Introduction to algorithmic thinking and using Jupyter              |[Link to Notebook](https://github.com/Edinburgh-Chemistry-Teaching/DDC/blob/main/Unit_01/Unit_01.ipynb)|
| 2    | Variables (`int`, `float`, `string`), Lists, Dictionaries and Tuples in Python|[Link to Notebook](https://github.com/Edinburgh-Chemistry-Teaching/DDC/blob/main/Unit_02/Unit_02.ipynb) |
| 3    | Loops and conditional                                                  |[Link to Notebook](https://github.com/Edinburgh-Chemistry-Teaching/DDC/blob/main/Unit_03/Unit_03.ipynb) |
| 4    | Functions, Pandas, and basic Input/Output                                        |[Link to Notebook](https://github.com/Edinburgh-Chemistry-Teaching/DDC/blob/main/Unit_04/Unit_04.ipynb) |
| 5    | An introduction to plotting, units and statistics                      |[Link to Notebook](https://github.com/Edinburgh-Chemistry-Teaching/DDC/blob/main/Unit_05/Unit_05.ipynb) |
| 6    | Comparisson of distributions, t-tests and molecular geometries             |[Link to Notebook](https://github.com/Edinburgh-Chemistry-Teaching/DDC/blob/main/Unit_06/Unit_06.ipynb) |
| 7    | Correlations in data and fitting data                                  |[Link to Notebook](https://github.com/Edinburgh-Chemistry-Teaching/DDC/blob/main/Unit_07/Unit_07.ipynb) |
| 8    | Applications I: Finding Peaks on MassSpec, Fitting Radioactive Decay and Writing a Chemistry Quiz                                                        |[Link to Notebook](https://github.com/Edinburgh-Chemistry-Teaching/DDC/blob/main/Unit_08/Unit_08.ipynb) |
| 9    | Applications II:   -- more specifics                                                         |[Link to Notebook](https://github.com/Edinburgh-Chemistry-Teaching/DDC/blob/main/Unit_09/Unit_09.ipynb) |
| 10   | Applications III:   -- more specifics                                                       |[Link to Notebook](https://github.com/Edinburgh-Chemistry-Teaching/DDC/blob/main/Unit_010/Unit_10.ipynb)|
*Table 1: Summary of course material*

The content is roughly grouped into three main parts. `Unit_01` to `Unit_04` introduce concepts around algorithmic thinking and Python syntax, including variables, loops, functions, libraries, documentation, how to get help, and how to read-in files. This was largely adapted from [Plotting and Programming in Python](http://swcarpentry.github.io/python-novice-gapminder/). `Unit_05` to `Unit_07` introduce concepts from SciPy [@virtanen2020scipy], NumPy [@harris2020array], Matplotlib [@hunter2007matplotlib] and Pandas [@team2022pandasdev] to carry out basic statistical analysis and plotting of chemistry-related data. Our strategy here was to incorporate as many other aspects of the chemistry curriculum while teaching Python. For example, students will have already seen a lot of mathematical concepts around fitting data and comparing distributions, but now are presented with a dataset relevant to their degree. The domain specific twist aims to boost motivation in students to engage with these mathematical concepts. Therefore, `Unit_08` to `Unit_10` covers specific application examples in chemistry from different areas of chemistry. Some of the applications directly tie into their lab experiments (e.g. UV-Vis spectroscopy and NMR data). During each 3-hour workshop with around 100 learners, we had 10 teaching assistants available for help and we offered, 1-hour long Q&A sessions every other week for additional help. 


# Assessment and feedback

The course was formally assessed at Edinburgh using NBGrader [@jupyter2019nbgrader], however we also made use of informal feedback within the sessions with built-in quizzes into the Notebooks using (Mentimeter)[https://www.mentimeter.com]. We polled students to test, understanding of material, critical thinking, background knowledge, and to gather feedback to improve the material further. This generally lead to good engagement from students. Figure 1 shows an example of a Mentimeter quiz.   
![image](figures/Mentimeter.png)
*Figure 1: Example of how a Mentimeter poll can be directly embedded into a Jupyter notebook.*


# Conclusion

We presented a modular course on Python for Chemistry students targeted at complete novices and hope it is of value to other teaching Python to Chemistry students. Running the material through Colab removes all installation requirement, making the course more easily accessible to novices; let them be students in guided university settings, or other chemistry enthusiasts. 

# Author's Contribution
Authors are listed in alphabetical order, specific contributions by each author are found in the following: James Cumby (JC), Valentina Erastova (VE), Claire Hobday (CH), and Antonia Mey (ASJSM) have been teaching this course at the University of Edinburgh since 2021/22 and contributed roughly equally to the material creation and teaching. See below for more details. Rafal Szabla (RS) taught one unit and created content for it in 2020/21, when the course was run as a Physical chemistry lab replacement in a shortened form. 
**JC:** Is the course organiser for the module taught at the University of Edinburgh and created the material for `Unit_01` and `Unit_09`, contributed to `Unit_05`, gave feedback on everyones material, and helped edit the manuscript.   
**VE:** Created material for `Unit_05` and `Unit_08`, contributed to `Unit_06`, and helped edit the manuscript.   
**JG:** Contributed material to `Unit_09`, and helped edit the manuscript.    
**CH:** Created material for `Unit_03` and `Unit_04`, and helped edit the manuscript.   
**ASJSM:** Created material for `Unit_02`, `Unit_06`, `Unit_07`, and `Unit_10`, provided feedback and small contributions to most other units, and wrote the manuscript.    
**HP:** Contributed material to `Unit_05`, Unit_08, and helped edit the manuscript.    
**RS:** Created the material for molecular geometries forming part of `Unit_06`, and gave feedback on the manuscript. 


# Acknowledgements 

We would like to acknowledge Matteo Degiacomi, Software Carpentries, and all the PhD student demonstrators who helped with teaching the material, giving feedback and creating some of the assignments. 

# References
