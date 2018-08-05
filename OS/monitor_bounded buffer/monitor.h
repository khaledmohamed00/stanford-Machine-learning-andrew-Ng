#ifndef MONITOR_H_
#define MONITOR_H_
#include <pthread.h>
#define max 3
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
#endif
