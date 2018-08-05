#include <sys/types.h>
#include <sys/syscall.h>
#include <stdlib.h>
#include <stdio.h>
#include <pthread.h>
#include <semaphore.h>
#include<unistd.h>
#include "header.h"
#include <stdlib.h>
#include <time.h>

int main(int argc, char *argv[]) {
   /* Loop counter */
   //int  n;
 //srand((unsigned int)time(NULL));
srand((unsigned int)time(NULL));
int * a = malloc(atoi(argv[2])*sizeof(int));
//int x;
for(int i=0;i<atoi(argv[2]);i++)

a[i]=rand();

   int i;
pthread_t tid;
//    Verify the correct number of arguments were passed in */
   if(argc != 4) {
      printf( "(sleeptime) (noproducer) (noconsumer)\n");
   return 0;
   }

   int Sleeptime = atoi(argv[1]); /* Time in seconds for main to sleep */
   int noProd = atoi(argv[2]); /* Number of producer threads */
   int noCons = atoi(argv[3]); /* Number of consumer threads */


   initial();

   /* Create the producer threads */
   for(i = 0; i < noProd; i++) {
      /* Create the thread */
      pthread_create(&tid,NULL,producer,a);
    }

   /* Create the consumer threads */
   for(i = 0; i < noCons; i++) {
      /* Create the thread */
      pthread_create(&tid,NULL,consumer,NULL);
   }


   sleep(Sleeptime);


   return 0;
}
