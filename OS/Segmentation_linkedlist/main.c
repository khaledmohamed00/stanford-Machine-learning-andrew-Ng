#include <stdio.h>
#include <stdlib.h>
#include<stdio.h>
//#include<conio.h>
typedef struct node
{
int seg;
int base;
int limit;
struct node *next;
} seg_table;

seg_table*entry=NULL;

seg_table* create_new_row(int seg_num ,int base,int limit){

seg_table *row=malloc(sizeof(seg_table));
row->base=base;
row->limit=limit;
row->seg=seg_num;
row->next=NULL;


return row;

}


void insert (seg_table * row,int seg_num ,int base,int limit)
{ static int entry_num=0;
if(entry==NULL)
{

entry=malloc(sizeof(seg_table));
entry->base=base;
entry->limit=limit;
entry->seg=seg_num;
entry->next=NULL;

}
else{

while(row->next!=NULL)
{
row=row->next;
}
row->next=create_new_row( seg_num , base,limit);
row=row->next;


}

entry_num++;


}

void print(seg_table * row){
if(row==NULL)
printf("is empty");
else{
do{

printf("%d\n",row->seg);
row=row->next;

}while(row!=NULL);





}



}

int search_segment_base(seg_table* row,int seg_num)
{
while(row->seg!=seg_num)
{
row=row->next;

}
return row->base;


}
 int search_segment_limit(seg_table* row,int seg_num)
{
while(row->seg!=seg_num)
{
row=row->next;

}
return row->limit;


}





int main()
{
entry=NULL;
int flag=0;
while(1){
int seg,limit,base;
flag=0;
printf("enter segment number = ");
scanf("%d",&seg);
if(seg<0)
break;
printf("enter base for the segment %d: ",seg);
scanf("%d",&base);
printf("enter limit for the segment %d: ",seg);
scanf("%d",&limit);
insert(entry,seg,base,limit);

}
/*insert(entry,1,100,500);
insert(entry,2,700,300);
insert(entry,3,900,200);
*/

int seg_base,seg_limit,seg_num,offset,physical;
printf("enter segment number for the process = ");
scanf("%d",&seg_num);

printf("enter offset number = ");
scanf("%d",&offset);

seg_base=search_segment_base(entry,seg_num);
seg_limit=search_segment_limit(entry,seg_num);

if(offset>seg_limit)
{
printf("the offset value is greater than the limit");
}
else{
physical=seg_base+offset;
printf("phsical= %d",physical);

}
//print(entry);




/*int value = 123;
while (value > 10) {
 int digit = value % 10;

 printf("%d\n",digit);
 // do something with digit
 value /= 10;
}

printf("%d",value);
*/

   // printf("Hello world!\n");
    return 0;
}
