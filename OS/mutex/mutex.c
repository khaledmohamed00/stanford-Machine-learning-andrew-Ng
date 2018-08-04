#include "synclib.h"
#include <stdio.h>
#include <unistd.h>
//enum bool{true,false};
//enum bool available=true;

int available=1;

void acquire(){
while(!available);
available=0;
}

void release(){
available=1;
}

void sum(int x,int y){
int summ=x+y;
printf("%d",summ);
}




void *increase_x(void *x_void_ptr)
{

int *x_ptr = (int *)x_void_ptr;
acquire();
(*x_ptr)++;
sleep(1);
release();
printf("x increment finished\n");

return NULL;
}

