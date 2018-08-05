#include <pthread.h>
#include <stdio.h>
#include <sys/types.h>
#include <sys/syscall.h>
#include<unistd.h>
#include <synclib.h>


int test_and_set(int *target) {
int rv = *target;
*target = 1;

return rv;
}

void *test_set(void * a /* *x_void_ptr*/)
{//int s=3;
int *lock = (int *)a;
static int x=0;
while (test_and_set(lock));
 printf("%d" "%d" "%d\n",x,*lock,getpid());
 printf("The ID of this thread is: %u\n", (unsigned int)pthread_self());
sleep(1);
fflush(stdout);
x++;
*lock = 0;


return NULL;

}
