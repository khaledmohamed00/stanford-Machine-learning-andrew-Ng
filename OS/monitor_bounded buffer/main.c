#include <stdio.h>
#include <stdlib.h>
//#include "monitor.h"
#include <pthread.h>
#include <unistd.h>
#include "synclib.h"
int main()
{

  struct monitor m1;
   monitor_constructor(&m1);
   //int i;
pthread_t cons[10];
pthread_t prod[10];
   for(int i=0;i<10;i++)
   {
   // pthread_t prod[i];
    pthread_create(&prod[i],NULL,produce,&m1);
/*pthread_t cons[i];
 pthread_create(&cons[i],NULL,consume,&m1);*/
   }
for(int i=0;i<10;i++){
//pthread_t cons[i];
 pthread_create(&cons[i],NULL,consume,&m1);
}
for(int i=0;i<10;i++){
pthread_join(cons[i],0);
 pthread_join(prod[i],0);
}
/*for(int i=0;i<10;i++){
pthread_join(cons[i],0);
// pthread_join(prod[i],0);
}
//sleep(5);*/
    return 0;
}
