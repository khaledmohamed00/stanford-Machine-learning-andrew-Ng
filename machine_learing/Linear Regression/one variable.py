import matplotlib as plt
import  numpy as np
import random as rad
from pylab import *
import pandas as pd

'''
trainingSet=[[2,5],[3,6],[1,5],[7,8],[4,3],[5,7],[5,9],[2,4],[2,3],[6,1],[4,0],[7,6],
             [0,3],[7,3],[5,8],[3,1],[7,9],[8,6],[4,2],[6,8],[5,5],[3,3],[1,1],[4,4],
             [2,2],[6,6],[7,7],[8,8],[5,8],[9,9],[9,6],[6,4],[4,0],[0,1],[1,3],[7,8],
             [3,6],[3,6],[3,6],[3,6],[3,6],[3,6],[3,6],[3,6],[3,6],[3,6],[3,6],[3,6]]
'''


trainingSet=pd.read_csv('data_1d.csv',header=None).as_matrix()#read training set from csv file
#mat=np.array(trainingSet)
#m=len(trainingSet)                                    #number of Training sets
m=len(trainingSet)
theta0=rad.randrange(0,9)                             #h=theta0+theta1*x
theta1=rad.randrange(0,9)
firstTheta0Iteration=0
firstTheta1Iteration=0
sum0=0                                                #sum at j0
sum1=0                                                #sum at j1
error0=9999
error1=9999
Jlist=[]
IterationList=[]
numberOfIterations=0
learning_factor=0.0003
def Linear_Regression_Gradient_descent():
    global numberOfIterations ,error0,error1,m,theta0,theta1,firstTheta0Iteration,firstTheta1Iteration
    while  abs(error0) >0.0001 and abs(error1) >0.0001:
            numberOfIterations+=1
            sum0=0
            sum1=0
            j=0
            for i in range(0, m):
                sum0 = sum0 + (theta0 + theta1 * trainingSet[i][0] - trainingSet[i][1])
                sum1 = sum1 + ((theta0 + theta1 * trainingSet[i][0] - trainingSet[i][1]) * trainingSet[i][0])
                j = j + (theta0 + theta1 * trainingSet[i][0] - trainingSet[i][1])**2

            print("Before: ",theta0,theta1)
            Jlist.append(j)
            temp0=theta0
            temp1=theta1
            theta0 = theta0 - (learning_factor / m) * sum0
            theta1 = theta1 - (learning_factor / m) * sum1
            if numberOfIterations==1:
                firstTheta0Iteration=theta0
                firstTheta1Iteration = theta1
            error0=theta0-temp0
            error1=theta1-temp1
            print("After: ",theta0,theta1)

    for i in range(0,numberOfIterations):                   #Filling the list with number of iteration
              IterationList.append(i)
def plot():
    plt.scatter(IterationList,Jlist)
    plt.xlabel("Iteration")
    plt.ylabel("J")
    fig1=plt.figure()

    x=np.linspace(0,100,1000)
    y=theta0+theta1*x
    y2=firstTheta0Iteration+firstTheta1Iteration*x
    plt.scatter(trainingSet[:,0],trainingSet[:,1])
    plt.ylabel("y")
    plt.xlabel("x")
    plt.plot(x,y)
    plt.plot(x,y2)
    plt.show()

Linear_Regression_Gradient_descent()
plot()