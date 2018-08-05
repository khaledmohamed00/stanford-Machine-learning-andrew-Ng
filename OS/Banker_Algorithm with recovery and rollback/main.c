#include <stdio.h>
#include <stdlib.h>
#define row 5
#define col 3
int allocation[row][col] = {
   {0, 1, 0} ,
   {2, 0, 0} ,
   {3, 0, 2},
   {2, 1, 1} ,
   {0, 0, 2}

};
int Max[row][col] = {
   {7, 5, 3} ,
   {3, 2, 2} ,
   {9, 0, 2},
   {2, 2, 2} ,
   {4, 3, 3}

};
int *c;
int avaialable [1][col]={{3,0,2}};//3,3,2 safe
int temp[1][col]={{0,0,0}};//temp matrix
int finish[row]={0,0,0,0,0};//0=not finished 1=finished -1=resource preempted
int process[row];//array that store processes order
int deadlock;
/*********************************************************************/
//check rescourse preemption

int test_preemption()
{
for(int i=0;i<row;i++)
{if(finish[i]==-1)
return 1;
}
return 0;

}
/*****************************************************************************/
//check finished or unfinished
int test(){

for(int i=0;i<row;i++)
{
    if(finish[i]==0)
    return 0;


}

return 1;
}
/******************************************************************/
//check if allocation+available>=max
int test_max(int i){
int count=0;
//c=&count;
for(int k=0;k<col;k++)
{if(temp[0][k]>=Max[i][k])
count++;
}
if(count==3)
return 1;

else return 0;
}
/*******************************************************************/
void set_available(){
deadlock=0;
for(int k=0;k<col;k++)
avaialable[0][k]=temp[0][k];


}
/******************************************************************/
void set_temp(int i)
{//printf("lol");
for(int k=0;k<col;k++)
{
temp[0][k]=avaialable[0][k]+allocation[i][k];


}

}
/********************************************************************/
void print_preemption(){
for(int i=0;i<row;i++)
{
if(finish[i]==-1)
{
printf("p%d ",i);
}

}


}
/*************************************************************************/
void process_order(int i)
{ static int count=0;
c=&count;
process[count]=i;
count++;


}
/************************************************************************/
void print()
{ printf("the system in a safe state in sequence\n");
for(int k=0;k<*c ;k++)
printf("p%d ",process[k]);

if(test_preemption()==1)
{printf("and processes are resource preempted ");
print_preemption();
}
}
/*****************************************************************************/
void print_deadlock_processes()
{
for(int i=0;i<row;i++)
{
if(finish[i]==0)
printf(" deadlock : p%d ",i);
if(finish[i]==-1)
printf(" resource preemption : p%d ",i);
}


}
/************************************************************************************/
int flag=0;
void Banker(){

//printf("%d,%d,%d\n",avaialable[0][0],avaialable[0][1],avaialable[0][2]);

//for(int y=0;y<row;y++)
 do{
 deadlock=1;

    for(int i=0;i<row;i++)
{
if(finish[i]==0)
{set_temp(i);

if(test_max(i)==1)

    {set_available();

    finish[i]=1;
    process_order(i);
    }




}
if(test()==1)
{
print();
flag=1;
printf("\n");
printf("available resources= %d,%d,%d\n",avaialable[0][0],avaialable[0][1],avaialable[0][2]);
break;

}

}

if(test()==1||deadlock==1)
break;

}while(1);
if(test()==0)
printf("the system is in unsafe state and the processes are\n");
print_deadlock_processes();
printf("\n");
printf("available resources= %d,%d,%d\n",avaialable[0][0],avaialable[0][1],avaialable[0][2]);
//print();
//printf("%d,%d,%d\n",avaialable[0][0],avaialable[0][1],avaialable[0][2]);



}
/***********************************************************************/
//the method that makes resource preemption
void resource_preemption()
{int i;
for( i=0;i<row;i++)
{
if(finish[i]==0)
break;
}
finish[i]=-1;
for(int k=0;k<col;k++)
{avaialable[0][k]=avaialable[0][k]+allocation[i][k];
allocation[i][k]=0;
}

}
/***********************************************************************/
//change the state of the process from resource preemption to unfinished
void recovery()
{
for(int i=0;i<row;i++)
{if(finish[i]==-1)
finish[i]=0;
break;
}


}
/**********************************************************************/
//test if available >=max
int test_max_available(int i)
{

int count=0;
//c=&count;
for(int k=0;k<col;k++)
{if(avaialable[0][k]>=Max[i][k])
count++;
}
if(count==3)
return 1;

else return 0;

}
/***********************************************************************/
//test the possiability of rollback
int test_rollback(){
for(int i=0;i<row;i++)
{
if(finish[i]==-1&&test_max_available(i)==1)
return 1;

}
return 0;

}

/**************************************************************************/
int main()
{//printf("%d,%d,%d\n",avaialable[0][0],avaialable[0][1],avaialable[0][2]);

 Banker();
while(test()==0)
{resource_preemption();
Banker();
 }
 while(test_rollback()==1)
 {recovery();
 Banker();
}

 for(int i=0;i<row;i++)
 printf("%d ",finish[i]);

  return 0;




}
