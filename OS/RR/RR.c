#include <stdio.h>
#include <stdlib.h>
#include<unistd.h>
 #define dim 8
 #define q 3
 int v=0;//counter
 int process=1;//the process time;
 int n=2;
 int size=dim;
 int m[8][3]={
                {1,10,3},
                {2,1,1},
                {3,2,4},
                {4,1,5},
                {5,5,2},
                {6,7,6},
                {7,10,8},
                {8,3,7}


            };

int s[dim]={0,0,0,0,0,0,0,0};// array that shows the finished processes

struct u{//stuct that store the information of each process
int nop;//nuber of process
int bt;//the cbu burst of process
int at;//arriaval time of the proces

};





struct r{//struct that stores the sequence of processes that the scheduler have  chosen
int nop;
int bt;
int pro;
int at;

};
void Gantt(struct r* t)//the function that prints the output of thre scheduler
{for(int i=0;i<v;i++)
{printf(" %d ",t[i].nop);
for(int j=0;j<t[i].bt;j++)
{
printf(" #" );
sleep(1);
fflush(stdout);
}

}
}



void print(struct u* a){// the function that prints the struct u
for(int i=0;i<dim ;i++)
{
printf("%d\t%d\t%d\n",a[i].nop,a[i].bt,a[i].at);


}


}


int mini(struct u* a )//the function that return the process with minimum arriaval time
{ int min=50;
int imin;
for(int i=0;i<dim;i++)
{if(a[i].at<=min && s[i] !=1 && a[i].at<=process)
{
min=a[i].at;
imin=i;
}
}

return imin;
}

void scheduler(int k,int boo,struct r* t,struct u*a)
{

if(boo==0)
{
t[v].bt=a[k].bt;
t[v].nop=k+1;
t[v].pro=process;
t[v].at=a[k].at;
process=process+a[k].bt;
printf("%d\t",k+1);
printf("%d\t",process);

a[k].bt=0;

s[k]=1;

}
else if(boo==1)
{
t[v].bt=q;
t[v].nop=k+1;
t[v].pro=process;
t[v].at=a[k].at;
a[k].bt=a[k].bt-q;
process=process+q;

a[k].at=process;

}
v++;
/*if(v>size)
{
t= realloc(t, n*size *sizeof(struct r));
n++;
}*/
}
void calculation(struct r* t)//calculate the waiting time and turnaround time
{
int wait=0;
int tob=0;
for(int i=0;i<v;i++)
{

wait=wait+t[i].pro-t[i].at;
tob=tob+t[i].bt;
}
printf("\n");
printf("The Waiting Time = %f\n",1.0*wait/dim);
printf("The Turnaround Time = %f\n",1.0*(wait+tob)/dim);



}

int main()
{struct u* a=(struct u*)malloc(dim*sizeof(struct u));
struct r* t=(struct r*)malloc(3*dim*sizeof(struct r));

for(int i=0;i<dim;i++)
{a[i].nop=m[i][0];
a[i].bt=m[i][1];
a[i].at=m[i][2];

}
print(a);

int flag;
do{
 int k;
 flag=0;

 k=mini(a);
//printf("%d",k);


if(a[k].bt<=q)
{/*if(v>size)
{
t= realloc(t, n*size*sizeof(struct r));
size=size*n;
n++;
}*/
scheduler(k,0,t,a);


}
else{
/*
if(v>size)
{
t= realloc(t, n*size*sizeof(struct r));
size=size*n;
n++;
}*/
scheduler(k,1,t,a);

}
for(int i=0;i<dim;i++)
{
if(s[i]==0)
{
flag=1;

}
}

}while(flag==1);

printf("\n");

printf("\n");
Gantt(t);
calculation(t);

return 0;




}
