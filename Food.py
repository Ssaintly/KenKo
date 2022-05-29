import pandas as pd
import numpy as np
import random
from scipy.sparse import csr_matrix
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
import seaborn as sns
import app 


# Reading CSV files
inputURL = ".\csv\\"

bf= pd.read_csv(inputURL + "breakfast.csv" , encoding= 'unicode_escape')
lunch= pd.read_csv(inputURL + "lunch.csv" , encoding= 'unicode_escape')
dinner= pd.read_csv(inputURL + "dinner.csv" , encoding= 'unicode_escape')
drinks= pd.read_csv(inputURL + "beverages.csv" , encoding= 'unicode_escape')
extras= pd.read_csv(inputURL + "dessert_snack.csv" , encoding= 'unicode_escape')
nonVeg= pd.read_csv(inputURL + "NonVeg.csv" , encoding= 'unicode_escape')



#A Gentle Water reminder and drinks offering function(just an Extra Part)
def Hydrated(age, gender):
    if(age>=9 and age<=13):
        if(gender=="male"):
            H2O=2.5
        else:
            H2O=2.1
    
    elif(age>=14 and age<=18):
        if(gender=="male"):
            H2O=3.4
        else:
            H2O=2.4
    elif(age>=19 ):
        if(gender=="male"):
            H2O=3.7
        else:
            H2O=3.0

    Print("Hey! buddy try to drink more if you haven't met your daily requirement of water, which is ",H2O)



def Dk(dietType):
    if(dietType=="Weight Loss"):
        print("Sorry we recommend You to not drink for your current goal...")
    else:
        for i in range (0,len(drinks)):
            X=list(drinks.iloc[:,0])
        print("Yoo!! your lucky drink for today is ", X[random.randint(0,16)])


    




#main-function

def food_recommendation(wt, ht, age, gender, dietType, dietTime, Category ):
    n=14


    #getting the amount of calorie needed with RMR value
    if(gender=="male"):
        calNeed= 5 + (99*wt) + (6.25*ht)-(4.92*age)
    else :
        calNeed=  (9.99*wt) + (6.25*ht)-(4.92*age)-161

    
    

    #Checking the required Diet Calories
    if(dietType=="Weight Gain"):
        p=2
        if(gender=="male"):
            calNeed= calNeed + 1000
        else :
            calNeed= calNeed +750

    elif(dietType=="Weight Loss"):
        p=6
        
        if(gender=="male"):
            calNeed= calNeed-300
        else :
            calNeed= calNeed-500
    else:
        p=4

    # print(calNeed)

    calNeed= calNeed/3
    



    #checking the dietTime and Category of User
    if(dietTime=="breakfast"):
        calories=bf

    elif(dietTime=="Lunch"):
        calories=lunch
        if(Category=="NonVeg"):
            calories=nonVeg

    elif(dietTime=="Dinner"):
        calories=dinner
        if(Category=="NonVeg"):
            calories=nonVeg   


    calNeed= calNeed/p




    #giving required neighbors value
    neigh = KNeighborsClassifier(n_neighbors=14)

    lenCal=len(calories)
    




    #getting values for X and Y from dataset
    i=0
    X=[]    
    for i in range(0,lenCal):
        j=list(calories.iloc[i,[1]])
        X.insert(i,j)
        y=list(calories.iloc[:,0])

    
        


    X=np.array(X)
    y=np.array(y)

    #removing NaN 
    y = y[~np.isnan(X).reshape(-1)]
    X=X[~np.isnan(X)]
    X=X.reshape(-1,1)

    neigh.fit(X, y)




    #Preping the required calories
    j=np.array(calNeed)
    j=j.reshape(-1,1)

    #getting the indexes of k nearest neighbors for value j
    ans=neigh.kneighbors(j, return_distance=False)
    ans=ans[0]




    #giving Name of the dishes recommended for user
    for i in range (0,len(ans)):
        c=ans[i]
        print(y[c])


    if(dietType=="Weight Gain"or dietType=="Healthy"):
        for i in range (0,len(extras)):
            Xtr=list(extras.iloc[:,0])
        print("\n")
        print("Yo!! We also wanna give you reward cheat for your goal:")
        print("you can also have ", Xtr[random.randint(0,40)], "\nKudoos!!!!!!!!! ;) ")
        



#Calling Function
n_age = app.age
wt = app.weight
ht = app.height


food_recommendation(wt, ht, n_age,"male", "Weight Loss","Dinner","NonVeg")
