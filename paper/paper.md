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
Data-Driven Chemistry is a course aimed at undergraduate students in Chemistry with no prior knowledge in programming and programatic data analysis. It is designed as an 10 week long course, typically spanning a whole semester, to give an introduction to Python programming used for data analysis typically found in a Chemistry degree. The course consists of 10 Jupyter notebooks which get worked through in a blended learning environment of live coding and explanations, followed by a set of in-course tasks to be solved individually or in a pair programming scenario. Typically demonstrators will be available to help with the content. The content of the notebook covers an introduction to Python, plotting with Python and statistical analysis, and data fitting all with a focus on chemistry related tasks and datasets. Some of these tasks where aligned with the labs carried out in the same semester. While not following fully following Software carpentry templates and guidelines, the introduction to Python covered in Notebook 2-4 is adapted from the core lesson on [Plotting and Programming in Python](http://swcarpentry.github.io/python-novice-gapminder/). Generally, we generally followed carpentry design ideas as best as possible for the lesson design. In the original course the material was hosted online using the Notable service provided by the University of Edinburgh, here we have migrated to content for convenience to Google Colab. While in principle this course is designed to be taught in a blended learning environment as a whole, each notebook will cover a set of self-contained topics. This modular design allows for aspects of the course to be reused and mix-and-matched with other courses. The online hosting with worked examples also allows this course to be used for self-guided learning and thus learning is not limited to a university classroom setting. 

# Statement of Need
The modern world is a digital world allowing for upscaling and automation of chemical processes through robots[@] but also fast production of large scale datasets [@]. Analysis with GUI interfaces or spreadsheet based tools may not be easily allow for a robust, fast, and reproducible analysis of these large scale data. Programming based solutions fare much better at these kind of tasks, but programming is not typically taught as a skill across Chemistry degrees, unlike in Physics, Maths, or even Biology[@white2022data]. To make sure Chemistry graduates, competing with other STEM graduates, do not lack computational skills both the Royal Society of Chemistry [@employability] and the American Chemical Society [@neiles2020professional] have identified good computational skills as a key for employability [@hill2019undergraduate]. This course was designed to address this gap in the chemistry curriculum at the University of Edinburgh and making the material available open source hopefully encourages their use in many other educational settings. Introducing aspects of programming broadly into a chemistry degree, have been explored in very recent years, through for example incorporating programming aspect into a course on mathematics for chemists [@hutchison2021integrating]. While this give a good foundation of programming, students often wonder why they have to learn dry aspects of programming without direct application to their degree choice. There are excellent resources for self study through books [@tanemura2022python], or more general material to study Python programming [@carpentries,@others]. However, little material exists for a general introduction to programming and data analysis geared towards complete novices, without a specific focus, on for example, physical chemistry [@baptista2021using], analytical chemistry [@menke2020series], or machine learning for chemistry [@lafuente2021gentle]. The course presented here, bridges this gab in teaching the basics of Python programming, and how these concepts can be applied to data in physics, inorganic, analytical, and even organic chemistry.   

# Course Development Background
In 2019, motivated, as outlined by the statement of need, a compulsory undergraduate course for teaching data analysis in Python with a subject focus on Chemistry was approved in the School of Chemistry at the University of Edinburgh. With the start of the pandemic, the development of the course was accelerated and ran in a shorter version (six, 3-hour workshops instead of ten 3-hour workshops) in the autumn of 2020 as a replacement for in-person physical chemistry labs. Since then, the full 10 times 3-hour workshop course was run in the academic year of 2021/22 fully online, and 2022/23 in-person. The material presented here is the fine tuned material of three years of development and tested for suitability to be delivered online or in-person. 


# Learning Outcomes, Content, and Structure
- Learning outcomes paste from course overview?
-  Our strategy was to incorporate as many other aspects of the chemistry curriculum into the teaching of Python. This allows some reminder and repetition of chemistry concepts students will have learned in the first and second semester of their Undergraduate degree, but also motivates given the domain specific twist.
- For structure cite this: [@muller2022pcp]



# Conclusion

I'll be a conclusion

# Author's Contribution
James Cumby (JC), Valentina Erastova (VE), Claire Hobday (CH), and Antonia Mey (ASJSM) are teaching this course at the University of Edinburgh since 2021/22 and contributed roughly equally to the material creation and teaching. See below for more details. Rafal Szabla (RS) taught one unit and created content for it in 2020/21, when the course was run as a Physical chemisstry lab replacement in a shortened form. 
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
