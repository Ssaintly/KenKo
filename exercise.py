import pandas as pd
import numpy as np
import random
from scipy.sparse import csr_matrix
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
import seaborn as sns


# Reading CSV files
inputURL = ".\csv\\"

Exr= pd.read_csv(inputURL + "exercise.csv" , encoding= 'unicode_escape')

def Exercise_recommendation(wt, ht, age, gender, Target):

    if(gender=="male"):
        calNeed= 5 + (99*wt) + (6.25*ht)-(4.92*age)+1500
    else :
        calNeed=  (9.99*wt) + (6.25*ht)-(4.92*age)-161+1000


    if(Target=="Weight Loss"):
        calNeed= (50/100)*calNeed
    elif(Target=="Healthy"):
        calNeed= (30/100)*calNeed
    else:
        calNeed=(20/100)*calNeed


    calNeed/=6

    neigh = KNeighborsClassifier(n_neighbors=15)

    length= len(Exr)



    i=0
    X=[]
    for i in range(0, length):
        j=list(Exr.iloc[i,[1]])
        X.insert(i,j)
        y=list(Exr.iloc[:,0])

    X=np.array(X)
    y=np.array(y)


    y = y[~np.isnan(X).reshape(-1)]
    X=X[~np.isnan(X)]
    X=X.reshape(-1,1)

    neigh.fit(X, y)


    
    #Preping the required calories to burnt
    j=np.array(calNeed)
    j=j.reshape(-1,1)

    #getting the indexes of k nearest neighbors for value j
    ans=neigh.kneighbors(j, return_distance=False)
    ans=ans[0]


    #giving Name of the Exercise recommended for user
    
    print("We recommend you to do 5-6 these  Exercises, 10 min each:")
    for i in range (0,len(ans)):
        c=ans[i]
        print(y[c])


Exercise_recommendation(62, 165, 20, "Female", "Weight Loss")