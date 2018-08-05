import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import fmin_cg
from scipy.io import loadmat
from sklearn.preprocessing import normalize
import sklearn
data = loadmat('data/ex5data1.mat')
X=data['X']
y=data['y']
Xval=data['Xval']
yval=data['yval']
lamda=0
theta = np.asarray([1,1])

#print data['X'].shape, data['y'].shape


def sigmoid(z):
    return 1 / (1 + np.exp(-z))



def plot_linear_reg(X,Y,theta_trained):

    plt.scatter(X, Y)
    plt.xlabel("change in water level X")
    plt.ylabel("water flowing out of a dam Y")
    u=np.array(X)
    v = 1.0*theta_trained[0] + 1.0*theta_trained[1] * u
    #v=X.dot(theta_trained)
    #print v.shape
    plt.plot(u, v,label='linear Regression line')
    plt.show()


def cost(theta,X,y,lamd):
   theta=np.array(theta)
   X=np.array(X)
   X=np.insert(X,0,np.ones(X.shape[0]),axis=1)
   y=np.array(y)
   theta = np.reshape(theta,(theta.size, 1))

   first=X.dot(theta)-y
   
   f=np.power(first,2)
   j=np.sum(f)+lamd*np.sum(np.power(theta[1:].T,2))

   return j/(2*len(X))

'''
def linearRegCost(X,y,theta,lamb):
    J = np.sum(np.power(X*theta-y,2)) + lamb*(theta[1:].T*theta[1:])
    #return J/2/y.shape[0]

    return J/2*y.shape[0]
'''

def gradient(theta,X,y,lamda):
    theta = np.array(theta)
    theta=np.reshape(theta,(theta.size,1))
    y=np.array(y)
    X = np.array(X)
    X = np.insert(X, 0, np.ones(X.shape[0]), axis=1)
    print X.shape
    print y.shape
    print y
    grad=X.T.dot((X.dot(theta)-y))+lamda*theta
    grad=grad/(len(X))

    #print grad.shape

    return grad.ravel()









'''
lamda=0
y=np.array(y)
X = np.array(X)
theta = np.asarray([1,1])

print cost(theta,X,y,lamda)
print gradient(theta,X,y,lamda)
plot_graph(X,y,theta_trained)
'''
def train_linearReg(theta,X,y,lamda):


   theta_trained=fmin_cg(cost,x0=theta,fprime=gradient,args=(X,y,lamda))
   print theta_trained
   return theta_trained

def linearing_curves(X,y,Xval,yval,lamda):
    m=X.size
    j_train=np.zeros(m)
    j_val=np.zeros(m)
    theta_init= np.asarray([0,0])
    for i in range(m):
        theta=train_linearReg(theta_init,X[:i+1],y[:i+1],lamda)
        j_train[i]=cost(theta,X[:0+1],y[:0+1],lamda)
        j_val[i]=cost(theta,Xval,yval,lamda)


    return j_train,j_val



def plot_learing_curves(X,y,Xval,yval,lamda):
    j_train,j_val=linearing_curves(X,y,Xval,yval,lamda)
    plt.plot(np.arange(1,13), j_train, label='Training error')
    plt.plot(np.arange(1,13), j_val, label='Validation error')
    plt.title('Learning curve for linear regression')
    plt.xlabel('Number of training examples')
    plt.ylabel('Error')
    plt.legend();
    plt.show()





def poly_feature(theta,X,y,p,lamda):
    X = np.array(X)
    '''
    theta = np.asarray([1, 1, 1, 1, 1, 1, 1, 1, 1])
    #X = np.insert(X, 0, np.ones(X.size), axis=1)
    X = np.insert(X, 1,np.power(X[:,0],2), axis=1)
    X = np.insert(X, 2,np.power(X[:,0],3), axis=1)
    X = np.insert(X, 3,np.power(X[:,0],4), axis=1)
    X = np.insert(X, 4,np.power(X[:,0],5), axis=1)
    X = np.insert(X, 5,np.power(X[:,0],6), axis=1)
    X = np.insert(X, 6,np.power(X[:,0],7), axis=1)
    X = np.insert(X, 7,np.power(X[:,0],8), axis=1)
    '''
    #X, mu, sigma = featureNormalize(X)
    theta=np.asarray(np.ones(p+1))
    for i in range(1,p):
      X = np.insert(X, i, np.power(X[:, 0], i+1), axis=1)




    #X = normalize(X)
   # X,mu, sigma =featureNormalize(X)


    return X,theta#,mu,sigma

def plot_poly_feature(theta_trained,X,y,p,lamda):
    from sklearn.preprocessing import PolynomialFeatures

    X = np.insert(X, 0, np.ones(X.shape[0]), axis=1)
    poly = PolynomialFeatures(degree=p)

    plt.scatter(np.array(data['X']), np.array(y))

    #p = np.poly1d(theta_trained[::-1])
    #x = np.arange(-10, 10)
    print theta_trained

    plot_x = np.linspace(-40, 40)

    #for i in range(1,p):
     #   plot_x = np.insert(plot_x, i, np.power(X[:, 0], 1), axis=1)
    #print poly.fit_transform(plot_x.reshape(-1, 1))
    plot_y=np.sum(theta_trained * poly.fit_transform(plot_x.reshape(-1, 1)), axis=1)

    #y = p(x)
    #y=normalize(np.array(y).reshape(-1, 1))
    #y=X.dot(theta_trained)
    #x=X.dot(theta_trained)
    #plt.plot(x, y)
    #plot_y=(plot_y-mu)/sigma
    plt.plot(plot_x,plot_y)
    #plt.plot(data['X'],x)
    plt.show()

def single_featue(X):
    X=np.array(X)
    theta = np.asarray([1, 1])
    return X,theta
def featureNormalize(X):
    mu = np.mean(X,axis=0)
    sigma = np.std(X,axis=0,ddof=1)
    X_norm = (X-mu)/sigma

    return X_norm,mu,sigma





'''
print (X)
print '\n'
X_norm,mu,sigma=featureNormalize(X)
#X_norm=normalize(X,norm='l1')
print X_norm
print mu
print sigma

'''


p=2

X,theta=poly_feature(theta,X,y,p,lamda)
print X
theta_trained=train_linearReg(theta,X,y,lamda)
plot_poly_feature(theta_trained,X,y,p,lamda)


'''
#print X.shape
#print theta.shape
#plot_learing_curves(X,y,Xval,yval,lamda)

#plot_learing_curves(X,y,Xval,yval,lamda)
'''
'''
X_train= np.insert(X, 0, np.ones(X.size), axis=1)
y_train=y
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression,Ridge

poly = PolynomialFeatures(degree=8)
X_train_poly = poly.fit_transform(X_train[:,1].reshape(-1,1))

regr2 = LinearRegression()
regr2.fit(X_train_poly, y_train)
#regr3 = Ridge(alpha=20)
#regr3.fit(X_train_poly, y_train)
# plot range for x
plot_x = np.linspace(-60,45)
# using coefficients to calculate y
plot_y = regr2.intercept_+ np.sum(regr2.coef_*poly.fit_transform(plot_x.reshape(-1,1)), axis=1)
#plot_y2 = regr3.intercept_ + np.sum(regr3.coef_*poly.fit_transform(plot_x.reshape(-1,1)), axis=1)
plt.plot(plot_x, plot_y, label='Scikit-learn LinearRegression')
#plt.plot(plot_x, plot_y2, label='Scikit-learn Ridge (alpha={})'.format(regr3.alpha))
plt.scatter(X_train[:,1], y_train, s=50, c='r', marker='x', linewidths=1)
plt.xlabel('Change in water level (x)')
plt.ylabel('Water flowing out of the dam (y)')
plt.title('Polynomial regression degree 8')
plt.legend(loc=4);
plt.show()

'''
'''
print X
print '\n'
X_norm,mu,sigm=featureNormalize(X)
print mu,sigm,'\n'
print X_norm
'''