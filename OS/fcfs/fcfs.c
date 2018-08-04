#include <stdio.h>
#include <stdlib.h>
#include<unistd.h>
 #define dim 8
 #define inf 50;
 int m[8][3]={
                {1,8,3},
                {2,4,1},
                {3,9,4},
                {4,5,5},
                {5,3,2},
                {6,7,6},
                {7,1,8},
                {8,6,7}


            };
int v[dim-1];//array that stores process time after each process
int p[dim];//array that stores the sequence of processes in fcfs
int sum=1;
int s=0;
int c=0;
void gantt(int i){// draw the gantt chart
p[c]=i;
c++;
printf("%d",i+1);
for(int j=0;j<m[i][1];j++)
{printf("#");
printf(" ");
sleep(1);
fflush(stdout);
}

}
void calc(){//calculate the waiting time and turnaround time

for(int u=1;u<dim;u++)
{ sum=sum+m[p[u-1]][1];
 v[u-1]=sum;

}
printf("\n");

int y=0;int t=m[p[0]][1];
for(int i=0;i<dim-1;i++ )
{
y=y+v[i]-m[p[i+1]][2];
t=t+v[i]+m[p[i+1]][1]-m[p[i+1]][2];
}
printf("\n");

printf("Average Waiting Time = ");

double av=1.0*y/dim;
printf("%f\n",av);
double wt=1.0*t/dim;
printf("Average Turnaround Time = ");

printf("%f",wt);



}


int main()
{

  int s[dim]={0,0,0,0,0,0,0,0};
  int min;
  int imin;
   int flag;
   do{
   min=inf;
   flag=1;
    for(int i=0;i<dim;i++)
    {
    if(m[i][2]<min &&s[i]!=1)
    {
    min=m[i][2];
imin=i;
    }
}
    s[imin]=1;
   gantt(imin);

    for(int i=0;i<dim;i++)
    {
    if(s[i]==0)
    {flag=0;

    }

    }
    }while(flag==0);


calc();

    return 0;

}
