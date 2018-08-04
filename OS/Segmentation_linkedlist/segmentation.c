#include <stdlib.h>
#include <stdio.h>
#define tableSize 5
static int index;

typedef struct {
int base;
int limit;
}Segment;

Segment segmentTable[tableSize];

void init(){
index=0;
for(int i=0;i<tableSize;i++){
segmentTable[i].base=-1;
segmentTable[i].limit=-1;
}

}

typedef struct{
int segmentNumber;
int offset;
}Logical ;

int setSegment(int base,int limit){

if((segmentTable[index].base==-1)&&(segmentTable[index].limit=-1)){

segmentTable[index].base=base;
segmentTable[index].limit=limit;
index=index+1%tableSize;
return 1;

}
else{

printf("There is already a segment here");

return 0;
}
}

/*
int getBase(int seg){

return segmentTable[seg].base;
}

int getLimit(int seg)
{
return segmentTable[seg].limit;
}
*/
int checkLimit(Logical* logical){
if(segmentTable[logical->segmentNumber].limit < logical->offset){
return -1;                                                            //return -1 as indication of segment fault
}
else{
return (segmentTable[logical->segmentNumber].base + logical->offset);//return physical
}

}


int insertLogical(int segmentNumber,int offset){
Logical logical;

logical.segmentNumber=segmentNumber;
logical.offset=offset;
int result=checkLimit(&logical);
if(result==-1){

return -1;

}

else{
return result;

}

}

void main(void){
init();
setSegment(1400,1000);
setSegment(6300,400);
setSegment(4300,400);
setSegment(3200,1100);
setSegment(4700,1000);
int physical=insertLogical(1,600);
if(physical==-1){
printf("ERROR: Segmentation Fault\n");
}
else{
printf("Physical address = %d",physical);
}
}










