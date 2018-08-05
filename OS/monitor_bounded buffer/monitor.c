#include "monitor.h"
#include <stdio.h>
int counter=0;
void monitor_constructor(struct monitor* m){
	//pthread_mutex_init(&m->mutex, 0);
	pthread_mutex_init(&m->lockk, 0);
	pthread_cond_init(&m->full, 0);
	pthread_cond_init(&m->empty, 0);

}
void* produce(void* ptr){
struct monitor* m=(struct monitor*)ptr;
	pthread_mutex_lock(&m->lockk);


			while(counter==max)
			{
				printf("buffer full\n");
				//pthread_cond_signal(&m->empty);
				pthread_cond_wait(&m->full,&m->lockk);//wait on full condition & release lock
				//pthread_mutex_lock(&m->lockk);
			}
			printf("buffer produced\n");
			counter++;
			printf("%d\n",counter);

	pthread_cond_signal(&m->empty);
	pthread_mutex_unlock(&m->lockk);
	//pthread_exit(0);
return NULL;
}
void* consume(void* ptr){
struct monitor* m=(struct monitor*)ptr;
	pthread_mutex_lock(&m->lockk);
	int i;

		while(counter==0)
		{
			printf("buffer empty\n");
			//pthread_cond_signal(&m->full);
			pthread_cond_wait(&m->empty,&m->lockk);
	 		//pthread_mutex_lock(&m->lockk);
		}
		printf("buffer consumed \n");
		counter--;
		printf("%d\n",counter);

	pthread_cond_signal(&m->full);
	pthread_mutex_unlock(&m->lockk);
return NULL;
//	pthread_exit(1);
}
