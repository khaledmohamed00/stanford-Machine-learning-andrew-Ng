import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from scipy.io import loadmat


data=loadmat('data/ex7data1.mat')
X=data['X']

#print data



def PCA(X):
    X=np.array(X)
    X=(X-X.mean())/X.std()

    cov=(X.T.dot(X))/X.shape[0]
    #print X.shape(0)
    #print cov.shape
    #print cov
    #print sigma.shape
    #print X.T*X.T.shape
    U,S,V=np.linalg.svd(cov)

    return U,S,V


def projection(X,U,K):
    U_red=U[:,0:K]

    Z=U_red.T.dot(X.T)
    return Z,U_red*-1




def recover(Z,U_red):
    print Z.shape
    print U_red.shape
    X=Z.T.dot(U_red.T)
    print X.shape
    return X

'''
U,S,V=PCA(X)
print U,'\n'
K=1
Z,U_red=projection(X,U,K)
X_approx=recover(Z,U_red)
print X_approx
fig, ax = plt.subplots(figsize=(12,8))
X=(X-X.mean())/X.std()
X_approx=(X_approx-X_approx.mean())/X_approx.std()
#X_approx=X_approx/4
ax.scatter(X[:,0],X[:,1],marker='x',c='r')
ax.scatter(X_approx[:,0],X_approx[:,1],marker='o',c='b')
plt.show()
'''
data=loadmat('data/ex7faces.mat')
#print faces['X'].shape
faces=data['X']
face1=faces[1,:]
#print face.shape
#fig=plt.figure()
#ax1 = fig.add_subplot(32,32)
#ax1.imshow(...)
#ax2 = fig.add_subplot(2,2,2)
#face1=np.reshape(face1,(32,32))
#print face/255
#plt.imshow(face1,cmap='gray')
#plt.show()

U,S,V=PCA(faces)
K=100
Z,U_red=projection(faces,U,K)
faces_approx=recover(Z,U_red)
#print faces_approx.shape

face_approx=np.reshape(faces_approx[0,:],(32,32))
#print face/255
#ax2 = fig.add_subplot(32,32)

plt.imshow(face_approx,cmap='gray')
plt.show()
