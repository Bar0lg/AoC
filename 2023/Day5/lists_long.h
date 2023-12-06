#ifndef LIST_LONG_H
#define LIST_LONG_H

typedef struct linked_list_long{
    long long val;
    struct linked_list_long* next;
} linked_list_long;

long long min_long(long long i1,long long i2);
linked_list_long* cons_long(long long val, linked_list_long* tail);
void free_linked_list_long(linked_list_long* l);
void print_list_long(linked_list_long* l);
#endif