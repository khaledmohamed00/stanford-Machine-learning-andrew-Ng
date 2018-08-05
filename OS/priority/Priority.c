#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
enum bool{true,false};
enum bool preemptive;
int headP=0,tailP=0,headR=0,tailR=0,timer=0,totalWaiting=0,totalBurst=0;
struct process
{
    int burstTime;
    int arrivalTime;
    int priority;
    int id;
};
void insertion_sort_pool(struct process* pool,int i)
{
    if(i>0)
    {
        int hole;
        struct process nextItem;

        nextItem.burstTime=pool[i].burstTime;
        nextItem.arrivalTime=pool[i].arrivalTime;
        nextItem.id=pool[i].id;
        nextItem.priority=pool[i].priority;
        hole=i;
        while(hole>0&&nextItem.arrivalTime<pool[hole-1].arrivalTime)
        {
            pool[hole].arrivalTime=pool[hole-1].arrivalTime;
            pool[hole].burstTime=pool[hole-1].burstTime;
            pool[hole].id=pool[hole-1].id;
            pool[hole].priority=pool[hole-1].priority;
            hole--;
        }
        pool[hole].arrivalTime=nextItem.arrivalTime;
        pool[hole].burstTime=nextItem.burstTime;
        pool[hole].id=nextItem.id;
        pool[hole].priority=nextItem.priority;
    }
}
void insertion_sort_ready(struct process* ready,int i)
{
    if(i>0)
    {
        int hole;
        struct process nextItem;

        nextItem.burstTime=ready[i].burstTime;
        nextItem.arrivalTime=ready[i].arrivalTime;
        nextItem.id=ready[i].id;
        nextItem.priority=ready[i].priority;
        hole=i;
        while(hole>0&&nextItem.priority>ready[hole-1].priority)
        {
            ready[hole].arrivalTime=ready[hole-1].arrivalTime;
            ready[hole].burstTime=ready[hole-1].burstTime;
            ready[hole].id=ready[hole-1].id;
            ready[hole].priority=ready[hole-1].priority;
            hole--;
        }
        ready[hole].arrivalTime=nextItem.arrivalTime;
        ready[hole].burstTime=nextItem.burstTime;
        ready[hole].id=nextItem.id;
        ready[hole].priority=nextItem.priority;
        if(hole==0)
            preemptive=true;
    }
}
void enqueue (struct process* a,int burst,int arrival,int id,int priority,int* tail)
{
    a[*tail].arrivalTime=arrival;
    a[*tail].burstTime=burst;
    a[*tail].id=id;
    a[*tail].priority=priority;
    (*tail)++;
   // printf("%d",*tail);
}
void readd(struct process* pool,int n)
{
    int i,burst,arrival,id,priority;
    for(i=0; i<n; i++)
    {
        printf("Enter Process ID ");
        scanf("%d",&id);
        printf("Enter Burst time of process %d ",id);
        scanf("%d",&burst);
        totalBurst+=burst;
        printf("Enter Arrival time of process %d ",id);
        scanf("%d",&arrival);
        printf("Enter Priority of process %d ",id);
        scanf("%d",&priority);
        enqueue(pool,burst,arrival,id,priority,&tailP);
        insertion_sort_pool(pool,tailP-1);
    }
}
void dequeue(int* head)
{
    (*head)++;
}
void check(struct process* pool,struct process* ready)
{
    if(pool[headP].arrivalTime==timer)
    {
        enqueue(ready,pool[headP].burstTime,pool[headP].arrivalTime,pool[headP].id,pool[headP].priority,&tailR);
        dequeue(&headP);
        insertion_sort_ready(ready,tailR-1);
        check(pool,ready);
    }
}

void execute(struct process* pool,struct process* ready)
{
    while(headP<tailP||headR<tailR)
    {
        if(headP!=tailP)
            check(pool,ready);
        if(headR!=tailR)
        {
            if(ready[headR].burstTime>0)
            {
                if(preemptive==true)
                {
                    printf("p%d",ready[headR].id);
                    preemptive=false;
                }
                printf("*");
                fflush(stdout);

                ready[headR].burstTime--;
            }
            else
            {
                 dequeue(&headR);
                 preemptive=true;
                 continue;
            }
            totalWaiting+=tailR-headR-1;
        }
        sleep (1);

        timer++;
    }
}
void calculate(int n)
{
    double avgWaiting=totalWaiting*1.0/n;
    double avgTurn=(totalBurst+totalWaiting)*1.0/n;
    printf("Average Waiting Time = %f\n",avgWaiting);
    printf("Average Turn Around Time = %f",avgTurn);

}
int main()
{
    printf("Enter Number of processes: ");
    int n;
    scanf("%d",&n);
    struct process* pool=(struct process *)malloc(n*sizeof(struct process));
    struct process* ready=(struct process *)malloc(n*sizeof(struct process));
    //int* waiting=(int*)malloc(n*sizeof(int));
    readd(pool,n);
   // print(pool,headP,tailP);
    execute(pool,ready);
    calculate(n);
    return 0;
}
