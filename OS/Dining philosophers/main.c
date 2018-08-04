#include <sys/types.h>
#include <sys/syscall.h>
#include <stdlib.h>
#include <stdio.h>
#include <pthread.h>
#include <semaphore.h>
#include<unistd.h>
//#include "header.h"
#include "synclib.h"
#define N 5




int philospher_num[N]={0,1,2,3,4};
int main()
{
    int i;
    pthread_t thread_id[N];


    intial();


   for(i=0;i<N;i++)
    {
        pthread_create(&thread_id[i],NULL,philospher,&philospher_num[i]);
        printf("Philosopher %d is thinking\n",i+1);
    }
   for(i=0;i<N;i++)
        pthread_join(thread_id[i],NULL);
return 0;
}
