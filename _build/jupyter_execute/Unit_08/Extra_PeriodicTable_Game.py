#!/usr/bin/env python
# coding: utf-8

# Making a periodic table quiz
# 
# 
# Original by [replit.com/@IsaacCHITTILAPP](https://replit.com/@IsaacCHITTILAPP)

# In[11]:


import numpy as np
import random
import mendeleev as mv
import pandas as pd


# In[3]:


cols = [ 'symbol', 'name', 'atomic_number']
ptable = mv.get_table('elements')[cols]


# In[4]:


ptable


# In[8]:


ptable.to_csv('ptable.csv',index=False)


# In[9]:


get_ipython().system("head 'ptable.csv'")


# In[12]:


pt = pd.read_csv('ptable.csv')


# In[13]:


pt


# In[5]:


qcount = int(input('How many questions do you want to brave this time?'))

score = 0
questions = 0


for i in range(0, qcount):
    
    randel = random.randint(0, 117)
    print('What is the name of an element ', ptable.iloc[randel]['symbol'])
    
    answer = input('')

    if answer.lower() == ptable.iloc[randel]['name'].lower():
        print('Correct!')
        score += 1
        questions += 1

    elif answer.lower() == 'quit':
        print('You got ' + str(score) + ' out of ' + str(questions))
        break

    else:
        print("Wrong, it's " + ptable.iloc[randel]['name'])
        questions += 1
        
print('You got %s out of %s questions!'%(score, questions))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


score = 0
questions = 0
startgame = input('Are you ready to start the Game? [Y/n]')

if startgame.lower()[0] == 'y':
    print('')
    print('Welcome to the periodic table quiz!')
    print('')
    print('Difficulty 1: Gives you an element symbol, and you must give the element name')
    print('')
    print('Difficulty 2: The same as difficulty 1 but it also asks you for the atomic number')
    print('')
    print('Difficulty 3: Gives you the atomic number and you have to give the element name and symbol')
    print('')
    print('All answers are not case sensitive, and simply type `quit` at any time to stop the game and get your score.')

    difficulty = input('Choose difficulty, 1, 2 or 3 : ')
    questioncount = int(input('How many questions?'))
    
    
    if difficulty == '1':
        for i in range(0, questioncount):
            randel = random.randint(0, 117)
            print(elements[randel][0])
            answer = input('')

            if answer.lower() == elements[randel][1]:
                print('Correct!')
                score += 1
                questions += 1

            elif answer.lower() == 'quit':
                print('You got ' + str(score) + ' out of ' +
                      str(questions))
                break

            else:
                print("Wrong, it's " + elements[randel][1])
                questions += 1
        print('You got ' + str(score) + ' out of ' + str(questions))

    elif difficulty == '2':
        for i in range(0, questioncount):
            randel = random.randint(0, 117)
            print(elements[randel][0])
            answer = input('')

            if answer.lower() == elements[randel][1]:
                print('Correct!')
                score += 1
                questions += 1
                answer = input('Atomic number:')

                if answer.lower() == elements[randel][2]:
                    print('Correct again!')
                    score += 1
                    questions += 1

                elif answer.lower() == 'quit':
                    print('You got ' + str(score) + ' out of ' +
                          str(questions))
                    break

                else:
                    print("Wrong, it's " + elements[randel][2])
                    questions += 1

            elif answer.lower() == 'quit':
                print('You got ' + str(score) + ' out of ' +
                      str(questions))
                break

            else:
                print("Wrong, it's " + elements[randel][1])
                questions += 1
        print('You got ' + str(score) + ' out of ' + str(questions))

    elif difficulty == '3':
        for i in range(0, questioncount):
            randel = random.randint(0, 117)
            print(elements[randel][2])
            answer = input('')

            if answer.lower() == elements[randel][1]:
                print('Correct!')
                score += 1
                questions += 1
                answer = input('Symbol:')

                if answer.lower() == elements[randel][0].lower:
                    print('Correct again!')
                    score += 1
                    questions += 1

                elif answer.lower() == 'quit':
                    print('You got ' + str(score) + ' out of ' +
                          str(questions))
                    break

                else:
                    print("Wrong, it's " + elements[randel][0])
                    questions += 1

            elif answer.lower() == 'quit':
                print('You got ' + str(score) + ' out of ' +
                      str(questions))
                break

            else:
                print("Wrong, it's " + elements[randel][1])
                questions += 1
        print('You got ' + str(score) + ' out of ' + str(questions))

else:
    print('Ok, quitting!')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


score = 0
questions = 0
startgame = input('Do you want to play(P) or use the periodic table(T)?')

if startgame.lower()[0] == 'p':
    knows_to_play = input('Do you know how to play?')
    if knows_to_play.lower()[0] == 'n':
        print('Welcome to the periodic table quiz!')
        print('')
        print('How to play:')
        print(
            'Difficulty 1: Gives you an element symbol, and you must give the element name'
        )
        print('')
        print(
            'Difficulty 2: The same as difficulty 1 but it also asks you for the atomic number'
        )
        print('')
        print(
            'Difficulty 3: Gives you the atomic number and you have to give the element name and symbol'
        )
        print('')
        print(
            'Modes: Endless mode will give you a never-ending quiz, set question count will let you choose how many questions you have.'
        )
        print('')
        print(
            'All answers are not case sensitive, and simply type quit at any time to stop the game and get your score.'
        )

    difficulty = input('Choose difficulty, 1, 2 or 3 ')
    mode = input('Choose mode, endless (E), or set question count, (S)')

    if mode.lower() == 'e':

        if difficulty == '1':
            while True:
                randel = random.randint(0, 117)
                print(elements[randel][0])
                answer = input('')

                if answer.lower() == elements[randel][1]:
                    print('Correct!')
                    score += 1
                    questions += 1

                elif answer.lower() == 'quit':
                    print('You got ' + str(score) + ' out of ' +
                          str(questions))
                    break

                else:
                    print("Wrong, it's " + elements[randel][1])
                    questions += 1

        elif difficulty == '2':
            while True:
                randel = random.randint(0, 117)
                print(elements[randel][0])
                answer = input('')

                if answer.lower() == elements[randel][1]:
                    print('Correct!')
                    score += 1
                    questions += 1
                    answer = input('Atomic number:')

                    if answer.lower() == elements[randel][2]:
                        print('Correct again!')
                        score += 1
                        questions += 1

                    elif answer.lower() == 'quit':
                        print('You got ' + str(score) + ' out of ' +
                              str(questions))
                        break

                    else:
                        print("Wrong, it's " + elements[randel][2])
                        questions += 1

                elif answer.lower() == 'quit':
                    print('You got ' + str(score) + ' out of ' +
                          str(questions))
                    break

                else:
                    print("Wrong, it's " + elements[randel][1])
                    questions += 1

        elif difficulty == '3':
            while True:
                randel = random.randint(0, 117)
                print(elements[randel][2])
                answer = input('')

                if answer.lower() == elements[randel][1]:
                    print('Correct!')
                    score += 1
                    questions += 1
                    answer = input('Symbol:')

                    if answer.lower() == elements[randel][0].lower():
                        print('Correct again!')
                        score += 1
                        questions += 1

                    elif answer.lower() == 'quit':
                        print('You got ' + str(score) + ' out of ' +
                              str(questions))
                        break

                    else:
                        print("Wrong, it's " + elements[randel][0])
                        questions += 1

                elif answer.lower() == 'quit':
                    print('You got ' + str(score) + ' out of ' +
                          str(questions))
                    break

                else:
                    print("Wrong, it's " + elements[randel][1])
                    questions += 1

    if mode.lower() == 's':
        questioncount = int(input('How many questions?'))
        if difficulty == '1':
            for i in range(0, questioncount):
                randel = random.randint(0, 117)
                print(elements[randel][0])
                answer = input('')

                if answer.lower() == elements[randel][1]:
                    print('Correct!')
                    score += 1
                    questions += 1

                elif answer.lower() == 'quit':
                    print('You got ' + str(score) + ' out of ' +
                          str(questions))
                    break

                else:
                    print("Wrong, it's " + elements[randel][1])
                    questions += 1
            print('You got ' + str(score) + ' out of ' + str(questions))

        elif difficulty == '2':
            for i in range(0, questioncount):
                randel = random.randint(0, 117)
                print(elements[randel][0])
                answer = input('')

                if answer.lower() == elements[randel][1]:
                    print('Correct!')
                    score += 1
                    questions += 1
                    answer = input('Atomic number:')

                    if answer.lower() == elements[randel][2]:
                        print('Correct again!')
                        score += 1
                        questions += 1

                    elif answer.lower() == 'quit':
                        print('You got ' + str(score) + ' out of ' +
                              str(questions))
                        break

                    else:
                        print("Wrong, it's " + elements[randel][2])
                        questions += 1

                elif answer.lower() == 'quit':
                    print('You got ' + str(score) + ' out of ' +
                          str(questions))
                    break

                else:
                    print("Wrong, it's " + elements[randel][1])
                    questions += 1
            print('You got ' + str(score) + ' out of ' + str(questions))

        elif difficulty == '3':
            for i in range(0, questioncount):
                randel = random.randint(0, 117)
                print(elements[randel][2])
                answer = input('')

                if answer.lower() == elements[randel][1]:
                    print('Correct!')
                    score += 1
                    questions += 1
                    answer = input('Symbol:')

                    if answer.lower() == elements[randel][0].lower:
                        print('Correct again!')
                        score += 1
                        questions += 1

                    elif answer.lower() == 'quit':
                        print('You got ' + str(score) + ' out of ' +
                              str(questions))
                        break

                    else:
                        print("Wrong, it's " + elements[randel][0])
                        questions += 1

                elif answer.lower() == 'quit':
                    print('You got ' + str(score) + ' out of ' +
                          str(questions))
                    break

                else:
                    print("Wrong, it's " + elements[randel][1])
                    questions += 1
            print('You got ' + str(score) + ' out of ' + str(questions))

elif startgame.lower() == 't':
    while True:
        searchfor = input(
            'Input any element information:Symbol, name or atomic number     ')

        print()
        for e in elements:
            for info in e:
                if info.lower()[:len(searchfor)] == searchfor.lower():
                    print(e[0], e[1], e[2])
                    break
        print()

        for e in elements:
            for info in e:
                if info.lower().find(searchfor.lower()) != -1:
                    print(e[0] + ' ' + e[1] + ' ' + e[2])
                    break
        print()
else:
    print('Ok, quitting!')


# In[ ]:





# In[ ]:




