#ifndef LISTS_CHAR_H
#define LISTS_CHAR_H

typedef struct duo_char {
    char* x;
    int y;
} duo_char ;

typedef struct linked_list_char{
    duo_char val;
    struct linked_list_char* next;
} linked_list_char;

void free_linked_list_char(linked_list_char* l);
linked_list_char* cons_duo_char(duo_char val, linked_list_char* tail);

void print_duoc(duo_char d);
void print_list_char(linked_list_char* l);
#endif