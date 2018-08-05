#ifndef HEADER_H_   /* Include guard */
#define HEADER_H


void *writer(void *param); /* the producer thread */
void *reader(void *param); /* the consumer thread */

void wait(int *m);
void signal(int *m);
void initializeData();
#endif
