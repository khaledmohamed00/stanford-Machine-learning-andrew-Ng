import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from scipy.io import loadmat
import random
import cv2

def find_closest_centroids(X, centroids):

    k=centroids.shape[0]
    m=X.shape[0]
    c=np.zeros(m)

    closest_index=-1
    for i in range(m):
        closest_distance = 10000000
        for j in range(k):
            distance=np.sum((np.power((X[i,:]-centroids[j,:]),2)))
            if distance<closest_distance:
                closest_distance=distance
                closest_index=j
        c[i]=closest_index


    return c



def compute_centroids(X, c, k):
    m=X.shape[0]
    centroids=[]
    for j in range(k) :
       sum=np.array(np.zeros(X.shape[1]))
       count=0
       for i in range(m):
          if c[i]==j:
            sum=sum+X[i]
            count+=1
       centroids.append(sum/count)
    return np.array(centroids)



def run_k_means(X, centroids, max_iters):
    k=centroids.shape[0]
    for _ in range(max_iters):
        c=find_closest_centroids(X,centroids)
        centroids=compute_centroids(X,c,k)
    return c,centroids


def init_centroids(X, k):
    m,n=X.shape
    init=np.random.randint(0,m,k)
    centroids=[]
    for i in range(k):
        centroids.append(X[init[i],:])

    return np.array(centroids)



def plot_clusters(X,c):
    cluster1 = X[np.where(c == 0)[0],:]
    cluster2 = X[np.where(c == 1)[0],:]
    cluster3 = X[np.where(c == 2)[0],:]
    fig, ax = plt.subplots(figsize=(12,8))
    ax.scatter(cluster1[:,0], cluster1[:,1], s=30, color='r', label='Cluster 1')
    ax.scatter(cluster2[:,0], cluster2[:,1], s=30, color='g', label='Cluster 2')
    ax.scatter(cluster3[:,0], cluster3[:,1], s=30, color='b', label='Cluster 3')


    ax.legend()
    plt.show()





'''
data = loadmat('data/ex7data2.mat')
X=data['X']
X=np.array(X)
#centroids=np.array([[3, 3], [6, 2], [8, 5]])
centroids=init_centroids(X,3)
#c=find_closest_centroids(X,centroids)

#print compute_centroids(X,c,3)
#print c[0:3]
c,centroids=run_k_means(X,centroids,10)



plot_clusters(X, c)


    #print c[0:3],centroids

#print data['X']
'''
image_data = loadmat('data/bird_small.mat')
A = image_data['A']
A=np.array(A)
#print A[0][0]
# normalize value ranges
A = A / 255.
#print A[0][0]

#plt.imshow(A)
plt.show()
# reshape the array
'''
X = np.reshape(A, (A.shape[0] * A.shape[1], A.shape[2]))

# randomly initialize the centroids
initial_centroids = init_centroids(X, 16)

# run the algorithm
idx, centroids = run_k_means(X, initial_centroids, 10)

# get the closest centroids one last time
#idx = find_closest_centroids(X, centroids)

# map each pixel to the centroid value
X_recovered = centroids[idx.astype(int),:]

# reshape to the original dimensions
X_recovered = np.reshape(X_recovered, (A.shape[0], A.shape[1], A.shape[2]))
print X_recovered[0][0]
plt.imshow(X_recovered)

plt.show()

#cv2.imshow('imag',X_recovered)
#if cv2.waitKey(20000) & 0xFF == 27:

 #   cv2.destroyAllWindows()

#cv2.destroyAllWindows()

'''