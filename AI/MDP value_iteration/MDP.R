reward=-2
#convergence=FALSE
epslion=0.0001
rows=3
cols=4
counter=0
action_list=c('N','S','E','W')
gama=1
history=array(0,dim=c(rows,cols))
values<-array(-1,dim=c(rows,cols))
policy=array(0,dim=c(rows,cols))
divergence=array(0,dim=c(rows,cols))
a<-c(0,0,0,0)

set_reward<-function(r){
  reward<<-r
}

get_reward<-function(state){
  if(state[1]==1&&state[2]==4)
    return(1)
  else if(state[1]==2&&state[2]==4)
    return(-1)
  else if(state[1]==2&&state[2]==2)
    return(0)
  else
    return(reward)
}

max_action<-function(actions){
  return(which.max(actions))
}

check_convergence<-function(epslion){
  divergence=abs(values-history)
  flag=TRUE
  for(row in 1:rows){
    for(col in 1:cols){
    
      if(divergence[row,col]>epslion)
        flag=FALSE        
       
      }}
return(flag)
  }

  utility<-function(state,action){
    #state[1]
    #state[2]
    #print(state[1])  
    if(state[1]==1&&state[2]==4)
      return(0)
    if(state[1]==2&&state[2]==4)
      return(0)
    if(state[1]==2&&state[2]==2)
      return(0)
    if (action=='N' &&state[1]==1)
    {
      
      return(history[state[1],state[2]])
      
    }
    if (action=='S' &&state[1]==3)
    {
      
      return(history[state[1],state[2]])
      
    }
    
    if(action=='E'&&state[2]==4){
      return(history[state[1],state[2]])
    }
    
    if(action=='W'&&state[2]==1){
      return(history[state[1],state[2]])
    }
    if(action=='N'){
      if (state[1]-1==2&&state[2]==2)
        return(history[state[1],state[2]])
      else(return(history[state[1]-1,state[2]]))
    }
    if(action=='S'){
      if (state[1]+1==2&&state[2]==2)
        return(history[state[1],state[2]])
      else(return(history[state[1]+1,state[2]]))
    }
    if(action=='E'){
      if (state[1]==2&&state[2]+1==2)
        return(history[state[1],state[2]])
      else(return(history[state[1],state[2]+1]))
      
    }
    
    if(action=='W'){
      if (state[1]==2&&state[2]-1==2)
        return(history[state[1],state[2]])
      else(return(history[state[1],state[2]-1]))
      
    }
    
  }

  
value_iteration<-function(){
  while (!check_convergence(epslion)) {
    history<<-values
    for(row in 1:rows){
      for(col in 1:cols){
      a[1]=0.8*((get_reward(c(row,col)))+gama*utility(c(row,col),'N'))+
        0.1*((get_reward(c(row,col)))+gama*utility(c(row,col),'E'))+
        0.1*((get_reward(c(row,col)))+gama*utility(c(row,col),'W'))
      
      a[2]=0.8*((get_reward(c(row,col)))+gama*utility(c(row,col),'S'))+
        0.1*((get_reward(c(row,col)))+gama*utility(c(row,col),'E'))+
        0.1*((get_reward(c(row,col)))+gama*utility(c(row,col),'W'))
      
      a[3]=0.8*((get_reward(c(row,col)))+gama*utility(c(row,col),'E'))+
        0.1*((get_reward(c(row,col)))+gama*utility(c(row,col),'N'))+
        0.1*((get_reward(c(row,col)))+gama*utility(c(row,col),'S'))
      
      a[4]=0.8*((get_reward(c(row,col)))+gama*utility(c(row,col),'W'))+
        0.1*((get_reward(c(row,col)))+gama*utility(c(row,col),'N'))+
        0.1*((get_reward(c(row,col)))+gama*utility(c(row,col),'S'))
      index=max_action(a)
      values[row,col]<<-a[index]
      policy[row,col]<<-action_list[index]
      }
    }
    #history<<-values
    counter<<-counter+1
    print(values)
    print(policy)
    #if(counter==100)
     # convergence<-TRUE
  }  
}

value_iteration()
policy[2,2]='#'
policy[2,4]='#'
#policy[1,4]='#'
#print(values)
print(policy)
counter

