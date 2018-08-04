#include <sys/types.h>
#include <sys/syscall.h>
#include <stdlib.h>
#include <stdio.h>
#include <pthread.h>
#include <semaphore.h>
#include<unistd.h>
//#include "header.h"
#include <stdlib.h>
#include <time.h>
#include "synclib.h"

int main(int argc, char *argv[])
{
    int i;
pthread_t tid;
//    Verify the correct number of arguments were passed in */
   if(argc != 4) {
       printf( "<sleeptime> <noreader> <nowriter>\n");
   return 0;
   }

 //  int Sleeptime = atoi(argv[1]); /* Time in seconds for main to sleep */
   int numwriter = atoi(argv[1]); /* Number of writer threads */
   int numreader= atoi(argv[2]); /* Number of reader threads */


   initializeData();

   /* Create the writer threads */
   for(i = 0; i < numwriter; i++) {
      /* Create the thread */
      pthread_create(&tid,NULL,writer,NULL);
    }

   /* Create the reader threads */
   for(i = 0; i < numreader; i++) {
      /* Create the thread */
      pthread_create(&tid,NULL,reader,NULL);
   }


   sleep(numreader+numwriter);




    return 0;
}
