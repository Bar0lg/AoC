#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#include "lists_long.h"



long long min_long(long long i1,long long i2){
    if (i1 > i2){
        return i2;
    }
    return i1;
}

linked_list_long* cons_long(long long val, linked_list_long* tail){
    linked_list_long* res = malloc(sizeof(linked_list_long));
    res->val = val;
    res->next = tail;
    return res;
}


void free_linked_list_long(linked_list_long* l){
    if (l->next != NULL){
        free_linked_list_long(l->next);
    }
    free(l);
}

void print_list_long(linked_list_long* l){
    if (l != NULL){
        printf("%lld ",l->val);
        print_list_long(l->next);
    }
}