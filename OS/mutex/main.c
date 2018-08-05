#include <stdio.h>
#include <stdlib.h>
#include "synclib.h"
#include <pthread.h>
int main()
{
int x=0;
   pthread_t inc_x_thread1,inc_x_thread2;
pthread_create(&inc_x_thread1, NULL, increase_x,&x);
pthread_create(&inc_x_thread2, NULL, increase_x,&x);
pthread_join(inc_x_thread1, NULL);
pthread_join(inc_x_thread2, NULL);
printf("counter= %d",x);
    return 0;
}
