
#ifndef HEADER_H_   /* Include guard */
#define HEADER_H
typedef int buffer_item;
#define BUFFER_SIZE 5

void *producer(void *param); /* the producer thread */
void *consumer(void *param); /* the consumer thread */
int insert_item(buffer_item item);
int remove_item(buffer_item *item);
void wait(int *m);
void signal(int *m);
void initial();
#endif
