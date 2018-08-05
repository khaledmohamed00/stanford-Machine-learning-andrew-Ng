color_number=3
map={
    'WA':['NT','SA'],
    'NT':['WA','SA'],
    'SA':['WA','NT','Q','NSW','V'],
    'Q':['NT','SA'],
    'NSW':['SA','Q','V'],
    'V':['SA','NSW','T'],
    'T':['V']

}
color={
    0:'red',
    1:'green',
    2:'blue'

}
variable_domain={#(0,1,2)=(R,G,B)

    'WA':[-1,3],
    'NT':[-1,3],
    'SA':[-1,3],
    'Q':[-1,3],
    'NSW':[-1,3],
    'V':[-1,3],
    'T':[-1,3]
}



choice={
    'WA':[],
    'NT':[],
    'SA':[],
    'Q':[],
    'NSW':[],
    'V':[],
    'T':[],
}


states={
    0:'WA',
    1:'NT',
    2:'SA',
    3:'Q',
    4:'NSW',
    5:'V',
    6:'T'


}
flag=0


def availabe_domain(variable):
    num=0
    reserved=[]
    availabe=[]
    for child in map[variable]:

        reserved.append(variable_domain[child][0])

    for i in range(color_number):
        if i not in reserved:
            availabe.append(i)
            num+=1
    variable_domain[variable][1]=num
    return availabe





def next_successor():
    lis=[]
    lis=sorted(variable_domain.items(),key=lambda x:x[1][1])


    i=0;
    while i<7 and lis[i][1][0] !=-1 :
        i+=1
    if i==7:
        return -1
    else:
     return lis[i][0]




def set_color(variable):
    global flag

    while True:
        available=availabe_domain(variable)

        if not available:
            variable_domain[variable][0]=-1
            return
        color=available.pop(0)

        while color  in choice[variable]:
          if len(available)>0:

           color = available.pop()
          else:
              variable_domain[variable][0]=-1
              return

        choice[variable].append(color)
        variable_domain[variable][0]=color

        sucessor=next_successor()
        if sucessor==-1:
            flag=1
            break
        else:
         set_color(sucessor)
         available=availabe_domain(variable)

        if   flag==1:
             break



import random

i=random.randint(0,6)

print states[i]
set_color(states[i])
print variable_domain
value=[]
for key,value in variable_domain.iteritems():
      print key ,color[value[0]]

