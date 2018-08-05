#include <stdio.h>
#include <stdlib.h>
int reference_string[20]={7,0,1,2,0,3,0,4,2,3,0,3,2,1,2,0,1,7,0,1};
int page_fault=0;
void clear_count(int *count,int num_frames)
{

for(int i=0;i<num_frames;i++)
{
count[i]=0;
}

}
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
void set_count(int *queue,int *count ,int num_frames,int place)
{ //int j=0;
for(int i=0;i<num_frames;i++)
{
for(int j=place+1;j<20;j++)
{
if(queue[i]==reference_string[j])
break;
else
count[i]++;

}


}



}
int max(int *count,int num_frames){


int max_num=0;
int index_max;
for(int i=0;i<num_frames;i++)
{

if(count[i]>max_num)
{max_num=count[i];
index_max=i;

}
}
return index_max;


}

//}
void print_queue(int *queue,int num_frames)
{
for(int i=0;i<num_frames;i++)
{
printf("%d\n",queue[i]);

}
printf("\n");
}
void print_count(int *count,int num_frames)
{

for(int i=0;i<num_frames;i++)
{
printf("%d\n",count[i]);

}
printf("\n");


}
void page_replacement(int *queue,int *count,int num_frames,int ref_string,int place)
{//printf("%d\n",ref_string);
page_fault++;
 set_count(queue,count,num_frames,place);
int j=max(count,num_frames);
queue[j]=ref_string;
//printf("queue\n");
//print_queue(queue,num_frames);
//printf("count\n");
//print_count(count,num_frames);
clear_count(count,num_frames);

}
void optimal_Page_Replacement(int num_frames)
{int * queue=malloc(num_frames*sizeof(int));
int *count=malloc(num_frames*sizeof(int));
for(int i=0;i<num_frames;i++)
{
count[i]=0;
}
for(int i=0;i<num_frames;i++){

    queue[i]=reference_string[i];
    page_fault++;
    //printf("%d\n",queue[i]);
    //printf("%d\n",page_fault);
    }
   // printf("queue\n");
    //print_queue(queue,num_frames);
for(int i=0;i<20;i++)
{
if(test_available(queue,reference_string[i],num_frames)==0)
page_replacement(queue,count,num_frames,reference_string[i],i);



}
    printf("page fault %d",page_fault);
free(queue);
free(count);



}






int main()
{/*int num_frames;
printf("enter number of frames = ");
scanf("%d",&num_frames);

int * queue=malloc(num_frames*sizeof(int));
int *count=malloc(num_frames*sizeof(int));
for(int i=0;i<num_frames;i++)
{
count[i]=0;
}
for(int i=0;i<num_frames;i++){

    queue[i]=reference_string[i];
    page_fault++;
    printf("%d\n",queue[i]);
    //printf("%d\n",page_fault);
    }
    printf("queue\n");
    print_queue(queue,num_frames);
for(int i=0;i<20;i++)
{
if(test_available(queue,reference_string[i],num_frames)==0)
page_replacement(queue,count,num_frames,reference_string[i],i);



}
    printf("page fault %d",page_fault);
*/
    int iteration;
    printf("enter number of iteration = ");
scanf("%d",&iteration);

for(int i=1;i<=iteration;i++)
{page_fault=0;
//index=0;
printf("number of frames %d ",i);
optimal_Page_Replacement(i);
printf("\n");
}


    return 0;
}
