#include <sys/types.h>
#include <sys/syscall.h>
#include <stdlib.h>
#include <stdio.h>
#include <pthread.h>
#include <semaphore.h>
#include<unistd.h>
#define N 5
#define THINKING 0
#define HUNGRY 1
#define EATING 2
#define LEFT (philos_num+4)%N
#define RIGHT (philos_num+1)%N

sem_t mutex;
sem_t S[N];

//void * philospher(void *num);
void pickup_chopstick(int);
void putdown_chopstick(int);
void test(int);

int state[N];


void *philospher(void *num)
{
    while(1)
    {
        int *i =(int*) num;
        sleep(1);
       fflush(stdout);
        pickup_chopstick(*i);
        sleep(1);
       fflush(stdout);
        putdown_chopstick(*i);
    }
}

void pickup_chopstick(int philos_num)
{
    sem_wait(&mutex);
    state[philos_num] = HUNGRY;
    printf("Philosopher %d is Hungry\n",philos_num+1);
    sleep(1);
    test(philos_num);
    sem_post(&mutex);
    sem_wait(&S[philos_num]);
    sleep(1);
fflush(stdout);
}

void test(int philos_num)
{
    if (state[philos_num] == HUNGRY && state[LEFT] != EATING && state[RIGHT] != EATING)
    {
        state[philos_num] = EATING;
        sleep(2);
        fflush(stdout);
        printf("Philosopher %d takes chopstick %d and %d\n",philos_num+1,LEFT+1,philos_num+1);
        printf("Philosopher %d is Eating\n",philos_num+1);
        sleep(1);
        sem_post(&S[philos_num]);
    }
}

void putdown_chopstick(int philos_num)
{
    sem_wait(&mutex);
    state[philos_num] = THINKING;
    printf("Philosopher %d putting chopstick %d and %d down\n",philos_num+1,LEFT+1,philos_num+1);
    printf("Philosopher %d is thinking\n",philos_num+1);
    sleep(1);
    test(LEFT);
    test(RIGHT);
    sem_post(&mutex);
}
void intial()
{//int i;
sem_init(&mutex,0,1);
    for(int i=0;i<N;i++)
        sem_init(&S[i],0,0);


}
