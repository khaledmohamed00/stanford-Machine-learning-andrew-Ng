#include <pthread.h>
#include <stdio.h>
#include <sys/types.h>
#include <sys/syscall.h>
#include<unistd.h>
#include "synclib.h"
//#include "header.h"
//int *s;
//*s=1;
int s=3;
void wait(int *S) {

while (*S <= 0 );
//sleep(3);
//fflush(stdout);
/*{
sleep(3);
fflush(stdout);
}//*/// busy wait
(*S)--;
}
//The definition of signal() is as follows:



void signal(int *S) {
(*S)++;
}


void *sem(void * a /* *x_void_ptr*/)
{
int *aa = (int *)a;

static int x=0;
wait(&s);
x++;
//pthread_id_np_t   tid;
//pthread_t         self;
//self = pthread_self();
 //pid_t x = syscall(__NR_gettid);
printf("%d" "%d" "%d\n",x,*aa,getpid());
 printf("The ID of this thread is: %u\n", (unsigned int)pthread_self());
sleep(3);
fflush(stdout);
//pthread_getunique_np(&self, &tid);
signal(&s);


return NULL;
}
