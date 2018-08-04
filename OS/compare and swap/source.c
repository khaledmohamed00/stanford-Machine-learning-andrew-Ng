#include <pthread.h>
#include <stdio.h>
#include <sys/types.h>
#include <sys/syscall.h>
#include<unistd.h>



int compare_and_swap (int *value, int expected, int new_value)
{
int temp = *value;
if (*value == expected)
*value = new_value;

return temp;
}
void *comp(void * a /* *x_void_ptr*/)
{//int s=3;
int *lock = (int *)a;
static int x=0;
while (compare_and_swap(lock, 0, 1));
 printf("%d" "%d" "%d\n",x,*lock,getpid());
 printf("The ID of this thread is: %u\n", (unsigned int)pthread_self());
sleep(1);
fflush(stdout);
x++;
*lock = 0;

return NULL;


}
