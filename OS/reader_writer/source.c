#include <pthread.h>
#include <stdio.h>
#include <sys/types.h>
#include <sys/syscall.h>
#include<unistd.h>
#include <time.h>
#include <semaphore.h>

#define RAND_DIVISOR 100000000
typedef int buffer_item;
#define BUFFER_SIZE 5
/* The mutex lock */

/* the semaphores */
sem_t rw_mutex, mutex;

int read_count;
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


void *writer(void *param) {
//static int  i=0;
//int * a=(int*)param;

//sem_wait(rw_mutex);
//int x=500;
sem_wait(&rw_mutex);
/* writing is performed */
 /*FILE* fp = fopen( "file.txt", "w" );
fprintf(fp, "%d",x );
*/
//while(1){
printf("i am writing\n");
sleep(1);
fflush(stdout);
sem_post(&rw_mutex);



//}
return NULL;
}

/* reader Thread */
void *reader(void *param) {
//while(1){
//int x;
   sem_wait(&mutex);
read_count++;
if (read_count == 1)
sem_wait(&rw_mutex);
sem_post(&mutex);

/* reading is performed */
/*FILE* file= fopen( "file.txt", "r" );
 fscanf(file, "%d",&x);*/
 printf("i am reading\n");
sleep(1);
fflush(stdout);
sem_wait(&mutex);
read_count--;

if (read_count == 0)

sem_post(&rw_mutex);
sem_post(&mutex);
//}
return NULL;
}

void initializeData() {


   sem_init(&rw_mutex, 0, 1);


   sem_init(&mutex, 0, 1);




   read_count = 0;
}

