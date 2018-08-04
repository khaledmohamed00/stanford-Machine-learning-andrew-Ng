import numpy as np
import random
import pandas as pd


R=[ [-1,0,-1,-1,0,-1,-1,-1,-1,-1,-1,-1],
    [0,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,0,-1,0,-1,-1,0,-1,-1,-1,-1,-1],
    [-1,-1,0,-1,-1,-1,-1,-10,-1,-1,-1,-1],
    [0,-1,-1,-1,-1,-1,-1,-1,0,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,0,-1,-1,-1,-1,-10,-1,-1,0,-1],
    [-1,-1,-1,0,-1,-1,0,-10,-1,-1,-1,-1],
    [-1,-1,-1,-1,0,-1,-1,-1,-1,0,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,0,-1,0,-1],
    [-1,-1,-1,-1,-1,-1,0,-1,-1,0,-1,10],
    [-1,-1,-1,-1,-1,-1,-1,-10,-1,-1,0,10]

   ]
grid=[[0 ,0 ,0 ,0],
      [0, 0, 0, 0],
      [0, 0, 0, 0],]

policy_board=[[0 ,0 ,0 ,0],
              [0, 0, 0, 0],
              [0, 0, 0, 0],]
R=np.array(R)#the reward matrix which gives the reward if you are in some state and take some action
Q=np.zeros((12,12)) #Q matrix it can be viewed as the memory that stores what the agent has learned in each epsiode
#grid=np.array((12,12))
#Q=np.array(pd.read_csv('Q.csv', sep=',',header=None))
#Q=np.delete(Q, 0, 0)
#Q=np.delete(Q,0,1)
history=[]#list that store each state the aent has visited in each episode
Q_history=-1*np.ones((12,12))#matrix that helps me to check for convergence

count=0#counter that counts how many times the Q matrix does not change
def convergence(Q):#function that check for convergence which means has the agent learned enough
    global Q_history
    global count
    divergence=Q-Q_history
    flag=1
    for i in range(12):
        for j in range(12):
            if abs(divergence[i][j])>0:
                flag=0
    Q_history = Q
    if flag==1:
     count+=1

     if count > 8:
         return 1
     else :
         return 0

    #return flag

def max_Q(state):#the fuction that takes state and return the max Q value and coresonding action for the state

    max_value=-999
    availabe=[]
    max_action=-1
    if state==7:
        return -10,7
    if state==11:
        return 10,11
    for action in range(12):
        if R[state][action]!=-1:
            availabe.append((state, action))

    for ava in availabe:
        if Q[ava[0]][ava[1]]>max_value and ava[1] not in history:
            max_value=Q[ava[0]][ava[1]]
            max_action=ava[1]
    '''
    if max_action==7:
        return -10,7
    '''
    return max_value,max_action

def choose_action(state):#the function that choose the action for state and it chooses randomly
    if state==7:
        return 7
    if state==11:
        return 11
    availabe = []
    for action in range(12):
        if R[state][action]!=-1:
            availabe.append((state, action))
    #print len(availabe)
    r = random.randint(0, len(availabe) - 1)
    while availabe[r][1]  in history:
     r=random.randint(0,len(availabe)-1)

    #print r
    return availabe[r][1]






#count=0

def Q_learning(state,gamma,alpha):#the function that implement the Q_learing algorithm
                                  #sample(state,action)=R(state,action)+gamma*Max(Q(nextstate,all actions))
                                  #Q(state,action)=(1-alpha)*Q(state,action)+alpha*sample(state,action)

    history.append(state)
    action=choose_action(state)
    Max_Q,nex_state=max_Q(action)
    if nex_state==-1:
        return
    sample=R[state][action]+gamma*Max_Q
    Q[state][action]=(1-alpha)*Q[state][action]+alpha*sample
    history.append(action)
    if state==7 or state==11:
        return
    Q_learning(nex_state,gamma,alpha)


def optimal_path(state,path=None):#the function that takes state and returns the optimal path after the agent has learned the the environment
    if path==None:
        path=[]

    max_value=-999
    best_action=-1
    path.append(state)
    if state ==11:
        return #path
    for action in range(12):
        if Q[state][action]>max_value:
            max_value=Q[state][action]
            best_action=action

    optimal_path(best_action,path)
    return path

def index_max(actions):
    max_value=-999
    max_index=-1
    for i in range(len(actions)):
        if actions[i] >max_value:
            max_value=actions[i]
            max_index=i

    return max_value,max_index

indexes=[]
max_values=[]
def find_max(Q):
    actions=[]
    global indexs
    global max_values
    for state in range(12):
        actions=Q[state][:]
        max_value,max_index=index_max(actions)
        indexes.append(max_index)
        max_values.append(max_value)



def grid_world(Q,grid):#the function that print the grid world with their utilities

    grid_no=0

    for i in range(12):
        for j in range(12):
            if Q[i][j]==0 :
                if i==6 and j==2:
                    continue
                Q[i][j]=-9999
    Q_list=[]

    for i in range(12):
     if i !=5:
        Q_list.append( max(Q[i][:]))

    for i in range(3):
        for j in range(4):
            if i ==1 and j==1:
                continue

            else:
                grid[2-i][j]=Q_list[grid_no]

                grid_no+=1
    grid=np.array(grid)
    grid = grid / 15
    grid = grid * 10
    print '\n'
    print "Grid world : "
    for grid_row in grid:
        print grid_row

def Q_run(Q):
    global history

    gamma=0.5
    alpha=0.5

    while convergence(Q)!=1:
        for state in range(11):
            if state !=5:
                Q_learning(10-state,gamma,alpha)

                #Q_learning(state, gamma, alpha)

                history=[]

    #Q=np.array(Q)
    Q=Q/15
    Q=Q*10
    df = pd.DataFrame(Q)
    df.to_csv("Q.csv")
    '''
    for i in range(12):
        for j in range(12):
            if Q[i][j]!=0:
                print "Q[", i,"]","[",j,"]=",Q[i][j]
    '''

def direction(state0,state1):
    if state0==0 and state1==4 :
        return 'N'
    if state0==4 and state1==8:
        return 'N'
    if state0==8 and state1==9:
        return 'E'
    if state0==9 and state1==10:
        return 'E'
    if state0==6 and state1==2:
        return 'S'
    if state0==1 and state1==0:
        return 'W'
    if state0==2 and state1==1:
        return 'W'
    if state0==3 and state1==2:
        return 'W'
    if state0==9 and state1==10:
        return 'E'
    if state0==10 and state1==11:
        return 'E'
    if state0 == 4 and state1 == 0:
        return 'S'
    if state0 == 8 and state1 == 4:
        return 'S'
    if state0 == 9 and state1 == 8:
        return 'W'
    if state0 == 10 and state1 == 9:
        return 'W'
    if state0 == 2 and state1 == 6:
        return 'N'
    if state0 == 0 and state1 == 1:
        return 'E'
    if state0 == 1 and state1 == 2:
        return 'E'
    if state0 == 2 and state1 == 3:
        return 'E'
    if state0 == 10 and state1 == 9:
        return 'W'
    if state0 == 11 and state1 == 10:
        return 'W'
    if state0 == 6 and state1 == 10:
        return 'N'
    if state0 == 10 and state1 == 6:
        return 'N'

def find_policy(indexes):
    policy=[]
    for index in range(len(indexes)):
        if index==5 :
            continue
        policy.append(direction(index,indexes[index]))

    return policy

def policy_grid(policy_board,policy):
    grid_no=0
    for i in range(3):
        for j in range(4):
            if i == 1 and j == 1 :
                continue

            else:
                policy_board[2 - i][j] = policy[grid_no]
                grid_no += 1

    policy_board[0][3] = '#'
    policy_board[1][3] = '#'
    policy_board[1][1] = '#'
    print '\n'
    print "Policy: "
    for pol in policy_board:
        print pol



Q_run(Q)
print '\n'
print "the optimal path from state : 0"
opt=optimal_path(0)
print opt
grid_world(Q,grid)
find_max(Q)
policy=[]
policy=find_policy(indexes)
policy_grid(policy_board,policy)


