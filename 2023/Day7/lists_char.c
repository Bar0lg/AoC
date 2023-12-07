#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#include "lists_char.h"


void free_linked_list_char(linked_list_char* l){
    if (l == NULL){
        return;
    }
    if (l->next != NULL){
        free_linked_list_char(l->next);
    }
    free(l->val.x);
    free(l);
}

linked_list_char* cons_duo_char(duo_char val, linked_list_char* tail){
    linked_list_char* res = malloc(sizeof(linked_list_char));
    res->val = val;
    res->next = tail;
    return res;
}

void print_duoc(duo_char d){
    printf("(%s %d)",d.x,d.y);
}

void print_list_char(linked_list_char* l){
    if (l != NULL){
        print_duoc(l->val);
        print_list_char(l->next);
    }
}