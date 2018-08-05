#include <pthread.h>
#include <stdio.h>
#include <sys/types.h>
#include <sys/syscall.h>
#include<unistd.h>
#include "header.h"
//#include <sys/types.h>
//pid_t tid = gettid();
//int i=0;
//int S=3;

int main()
{
    pthread_t threads[5];
for(int i=0;i<5;i++)
{pthread_create(&threads[i], NULL, sem,&i);
//sleep(1);
//sleep(1);
//fflush(stdout);
}
for(int i=0;i<5;i++)
pthread_join(threads[i], NULL);


return 0;
}
