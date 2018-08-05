#include <pthread.h>
#include <stdio.h>
#include <sys/types.h>
#include <sys/syscall.h>
#include<unistd.h>
//#include "header.h"
#include "synclib.h"
int main()
{ int lock=0;
     pthread_t threads[2];
for(int i=0;i<2;i++)
{pthread_create(&threads[i], NULL, test_set,&lock);
//sleep(1);
//sleep(1);
//fflush(stdout);
}
for(int i=0;i<2;i++)
pthread_join(threads[i], NULL);

    return 0;
}
