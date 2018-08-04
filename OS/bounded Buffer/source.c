#include <pthread.h>
#include <stdio.h>
#include <sys/types.h>
#include <sys/syscall.h>
#include<unistd.h>
#include <time.h>
#include <semaphore.h>

typedef int buffer_item;
#define BUFFER_SIZE 5
/* The mutex lock */
pthread_mutex_t mutex;

/* the semaphores */
sem_t full, empty;
buffer_item buffer[BUFFER_SIZE];
//int *mutex ;
//int * empty ;
//int * full;
int counter;
//srand((unsigned int)time(NULL));
void wait(int *S) {
while (*S <= 0 )
/*{
sleep(3);
fflush(stdout);
}//*/; // busy wait
--*S;
}
//The definition of signal() is as follows:



void signal(int *S) {
++*S;
}
/* Producer Thread */
/* Add an item to the buffer */
int insert_item(buffer_item item) {

   if(counter < BUFFER_SIZE) {
      buffer[counter] = item;
      counter++;
      return 0;
   }
   else {
      return -1;
   }
}


int remove_item(buffer_item *item) {

   if(counter > 0) {
      *item = buffer[(counter-1)];
      counter--;
      return 0;
   }
   else {
      return -1;
   }
}

void *producer(void *param) {
static int  i=0;
int * a=(int*)param;
buffer_item item;
//srand((unsigned int)time(NULL));
 //  while(1) {


      /* acquire the empty lock */
     sem_wait(&empty);
      /* acquire the mutex lock */
      pthread_mutex_lock(&mutex);
item=a[i];
i++;
      if(insert_item(item)) {
         printf( " error \n");
      }
      else {
         printf("producer produced %d\n", item);
      }
      /* release the mutex lock */
      pthread_mutex_unlock(&mutex);
      /* signal full */
      sem_post(&full);
  // }
return NULL;
}

/* Consumer Thread */
void *consumer(void *param) {
   buffer_item item;

   //while(1) {


      /* aquire the full lock */
      /* acquire the empty lock */
       sem_wait(&full);
      /* aquire the mutex lock */
      pthread_mutex_lock(&mutex);
      if(remove_item(&item)) {
         printf( "Consumer error \n");
      }
      else {
         printf("consumer consumed %d\n", item);
      }
      /* release the mutex lock */
      pthread_mutex_unlock(&mutex);
      /* signal empty */
      sem_post(&empty);
   //}
return NULL;
}

void initial() {
//srand((unsigned int)time(NULL));

   pthread_mutex_init(&mutex, NULL);


   sem_init(&full, 0, 0);


   sem_init(&empty, 0, BUFFER_SIZE);


   counter = 0;
}

