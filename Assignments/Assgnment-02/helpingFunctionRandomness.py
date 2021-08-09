#!/usr/bin/env python
# coding: utf-8

# In[15]:


import numpy as np
def Create_Papulation_Randomly(gens):
    ## take initial gens and create more random papulation
    
    NumberOFIndex = np.random.randint(0,len(gens))
    
    for i in range(0,NumberOFIndex):
        RandomIndex = np.random.randint(0,NumberOFIndex)
        gens[RandomIndex]=1
    return gens


## fiteness function count the number of 1's in the list
def Calcualte_fitness(chromosome):
    
    NumOfOne = 0
    for Num in range(0,len(chromosome)):
        if chromosome[Num]==1:
            NumOfOne+=1
    fitness=NumOfOne
    return fitness
    



