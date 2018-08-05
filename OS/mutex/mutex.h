#ifndef MUTEX_H_INCLUDED
#define MUTEX_H_INCLUDED

void acquire();
void release();
void sum(int x,int y);
void *increase_x(void *x_void_ptr);
#endif // MUTEX_H_INCLUDED
