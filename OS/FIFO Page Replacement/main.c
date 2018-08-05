#include <stdio.h>
#include <stdlib.h>
int reference_string[20]={7,0,1,2,0,3,0,4,2,3,0,3,2,1,2,0,1,7,0,1};
//int *queue ;
  int index=0;
 int page_fault=0;
int test_available(int * queue,int x,int num_frames)
{
for(int i=0;i<num_frames;i++)
{if(queue[i]==x)
{
return 1;

}
}
return 0;


}
void print_queue(int *queue,int num_frames)
{//static int space=1;
for(int i=0;i<num_frames;i++)
{/*for(int j=0;j<space;j++)
{
printf("\t");
}*/

printf("%d\n",queue[i]);

}

//space++;

}
void page_replacement(int *queue,int x,int num_frames)
{ page_fault++;

//printf("%d\n",x);
//printf("%d\n",page_fault);
//static int index=0;
queue[index]=x;
index=(index+1)%num_frames;
if(page_fault>num_frames)
{//printf("\t");
//print_queue(queue,num_frames);
//printf("\n");
}
}

void fifo_page_replacement(int num_frames){
//int num_frames;


   // printf("enter number of frames = ");
   // scanf("%d",&num_frames);
   //num_frames=3;
   int * queue=malloc(num_frames*sizeof(int));

   for(int i=0;i<num_frames;i++){

    queue[i]=reference_string[i];
    page_fault++;
    //printf("%d\n",queue[i]);
    //printf("%d\n",page_fault);
    }
//printf("\n");
    int i;


    for( i=0;i<20;i++)
    {


    if(test_available(queue,reference_string[i],num_frames)==0)
    {
    page_replacement(queue,reference_string[i],num_frames);

    }


    }

    printf("page fault = %d",page_fault);
free(queue);
}

int main()
{

int iteration;
printf("enter number of iteration = ");
scanf("%d",&iteration);

for(int i=1;i<=iteration;i++)
{page_fault=0;
index=0;
printf("number of frames %d ",i);
fifo_page_replacement(i);
printf("\n");
}

    return 0;
}
