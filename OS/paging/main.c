#include <stdio.h>
#include <stdlib.h>
#include<stdio.h>
//#include<conio.h>
typedef struct node
{
int frame;
int page;
struct node* next;
}page_table;

int entry_num=0;
page_table* entry=NULL;

page_table* create_new_row(int page,int frame){

page_table *row=malloc(sizeof(page_table));
row->page=page;
row->frame=frame;

row->next=NULL;


return row;

}


void insert (page_table * row,int page,int frame)
{ //static int entry_num=0;
if(entry==NULL)
{

entry=malloc(sizeof(page_table));
entry->page=page;
entry->frame=frame;
entry->next=NULL;

}
else{

while(row->next!=NULL)
{
row=row->next;
}
row->next=create_new_row( page,frame);
row=row->next;


}

entry_num++;


}

void print(page_table * row){
if(row==NULL)
printf("is empty");
else{
do{

printf("%d\n",row->page);
row=row->next;

}while(row!=NULL);





}



}

int search_page_frame(page_table* row,int page_num)
{int i=0;int flag=0;
while(row->page!=page_num)
{i++;
if(i<entry_num)
{row=row->next;

//printf("%d ",entry_num);
//printf("%d\n",i);
}
else{
flag=1;
break;
}


}
if(flag==1)
{
return -1;
}
else{
return row->frame;
}

}






int main()
{
entry=NULL;
//int flag=0;
int page_size;
printf("enter page size= ");
scanf("%d",&page_size);
while(1){
int page,frame;

printf("enter page number = ");
scanf("%d",&page);
if(page<0)
break;
printf("enter frame for the page %d: ",page);
scanf("%d",&frame);

insert(entry,page,frame);

}


int page_num,offset,physical,logical,frame_num;
printf("enter the logical address of the process = ");
scanf("%d",&logical);

page_num=logical/page_size;
offset=logical%page_size;
if(offset>page_size)
{
printf("the logical address is not correct because offset >page size %d > %d",offset,page_size);
}
else{
frame_num=search_page_frame(entry,page_num);
//printf("%d",frame_num);
if(frame_num <0){
printf("this page does not exist");

}
else{
physical=frame_num*page_size+offset;
printf("phsical= %d",physical);
}
}

//print(entry);




int value = 123;
while (value > 10) {
 int digit = value % 10;

 printf("%d\n",digit);
 // do something with digit
/ value /= 10;
}

printf("%d",value);


   // printf("Hello world!\n");
    return 0;
}
