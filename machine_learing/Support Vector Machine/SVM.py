import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from scipy.io import loadmat
from sklearn import svm

'''
raw_data = loadmat('data/ex6data1.mat')
#print raw_data
data = pd.DataFrame(raw_data['X'], columns=['X1', 'X2'])
#print data['X1']
data['y'] = raw_data['y']
data_x1=np.array(data['X1'])
data_x2=np.array(data['X2'])
data_y=np.array(data['y'])
positive = data[data['y'].isin([1])]
negative = data[data['y'].isin([0])]

fig, ax = plt.subplots(figsize=(12,8))
ax.scatter(positive['X1'], positive['X2'], s=50, marker='x', label='Positive')
ax.scatter(negative['X1'], negative['X2'], s=50, marker='o', label='Negative')
ax.legend()
#plt.show()

svc = svm.LinearSVC(C=100, loss='hinge', max_iter=1000)
svc.fit(data[['X1','X1']],data['y'])
print svc.score(data[['X1','X1']],data['y'])

svc2 = svm.LinearSVC(C=100, loss='hinge', max_iter=1000)
svc2.fit(data[['X1', 'X2']], data['y'])
print svc2.score(data[['X1', 'X2']], data['y'])

data['SVM 1 Confidence'] = svc2.decision_function(data[['X1', 'X2']])
print 'ok'
print data['SVM 1 Confidence'].shape
print data_x1.shape
#print data_x1

fig, ax = plt.subplots(figsize=(12,8))

#print t.shape
ax.scatter(data_x1, data_x2, s=50,c=data['SVM 1 Confidence'], cmap='seismic')
ax.set_title('SVM (C=1) Decision Confidence')
plt.show()
'''
'''
raw_data = loadmat('data/ex6data2.mat')

data = pd.DataFrame(raw_data['X'], columns=['X1', 'X2'])
data['y'] = raw_data['y']

positive = data[data['y'].isin([1])]
negative = data[data['y'].isin([0])]

fig, ax = plt.subplots(figsize=(12,8))
ax.scatter(positive['X1'], positive['X2'], s=30, marker='x', label='Positive')
ax.scatter(negative['X1'], negative['X2'], s=30, marker='o', label='Negative')
ax.legend()

svc = svm.SVC(C=1000, gamma=10, probability=True)
svc.fit(data[['X1', 'X2']], data['y'])
data['Probability'] = svc.predict_proba(data[['X1', 'X2']])[:,0]
#print np.array( svc.predict_proba(data[['X1', 'X2']]))
fig, ax = plt.subplots(figsize=(12,8))
ax.scatter(data['X1'], data['X2'], s=30, c=data['Probability'], cmap='Reds')
plt.show()
'''
'''
raw_data = loadmat('data/ex6data3.mat')
#print raw_data['Xval']
X = raw_data['X']
Xval = raw_data['Xval']
y = raw_data['y'].ravel()
yval = raw_data['yval'].ravel()

C_values = [0.01, 0.03, 0.1, 0.3, 1, 3, 10, 30, 100]
gamma_values = [0.01, 0.03, 0.1, 0.3, 1, 3, 10, 30, 100]
best_score=0
optimal={
    'gamma':None,
    'C':None

}
for c in C_values:
    for gamma in gamma_values:
        svc=svm.SVC(C=c,gamma=gamma)
        svc.fit(X,y)
        score=svc.score(Xval,yval)
        if score>best_score:
           best_score=score
           optimal['gamma']=gamma
           optimal['C']=c


print 'best score=',best_score
print 'gamma=',optimal['gamma']
print 'C',optimal['C']
'''

spam_train = loadmat('data/spamTrain.mat')
spam_test = loadmat('data/spamTest.mat')


X = spam_train['X']
Xtest = spam_test['Xtest']
y = spam_train['y'].ravel()
ytest = spam_test['ytest'].ravel()
'''
count=np.array(np.zeros(X.shape[0]))
for i in range(X.shape[0]):
  for j in range(X.shape[1]):
    if X[i,j]==1:
       count[i]+=1


plt.scatter(count,y)
plt.show()
'''
svc=svm.SVC()
svc.fit(X,y)
print "accuracy= " ,svc.score(Xtest,ytest)*100


