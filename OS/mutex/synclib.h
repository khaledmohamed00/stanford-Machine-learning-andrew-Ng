#include <pthread.h>
#define max 3
typedef int buffer_item;
#define BUFFER_SIZE 5
#ifndef SYNCLIB_H_   /* Include guard */
#define SYNCLIB_H

int test_and_set(int *target);
void *test_set(void * a /* *x_void_ptr*/);

void *writer(void *param); /* the producer thread */
void *reader(void *param); /* the consumer thread */


void *sem(void * a /* *x_void_ptr*/);

void wait(int *m);
void signal(int *m);
void initializeData();

void acquire();
void release();
void sum(int x,int y);
void *increase_x(void *x_void_ptr);

struct monitor
{
	pthread_mutex_t mutex;
	pthread_mutex_t lockk;
	pthread_cond_t full;
	pthread_cond_t empty;
	int buffer[max];


};
void monitor_constructor(struct monitor* m);
	void* produce(void* ptr);
	void* consume(void* ptr);

void * philospher(void *num);
void pickup_chopstick(int ph_num);
void putdown_chopstick(int ph_num);
void test(int ph_num);
void intial();

void *producer(void *param); /* the producer thread */
void *consumer(void *param); /* the consumer thread */
int insert_item(buffer_item item);
int remove_item(buffer_item *item);
void wait(int *m);
void signal(int *m);
void initial();

int compare_and_swap (int *value, int expected, int new_value);
void *comp(void * a /* *x_void_ptr*/);
#endif
