#ifndef UTILS_H
#define UTILS_H

#define BUFF_SIZE_MAX 2000
#define FALSE 0
#define TRUE 1

int min_int(int i1,int i2);
int max_int(int i1,int i2);

int cmp_strings(char* str1, char* str2);
int equal_strings(char* str1, char* str2);
int start_with(char* grand, char* petit);
int is_in(char* grand, char* petit);
int str_contain(char c, char* all_chars);


typedef struct linked_list{
    int val;
    struct linked_list* next;
} linked_list;

linked_list* cons(int val, linked_list* tail);
linked_list* rev_linked(linked_list* l);
void free_linked_list(linked_list* l);
void print_list(linked_list* l);

typedef struct{
    long x;
    long y;
} duo;

typedef struct linked_duo_list{
    duo val;
    struct linked_duo_list* next;
} linked_duo_list;

void print_duo(duo d);

linked_duo_list* cons_duo(duo val, linked_duo_list* tail);
linked_duo_list* rev_linked_duo(linked_duo_list* l);
void free_linked_duo_list(linked_duo_list* l);
void print_duo_list(linked_duo_list* l);

int** init_int_tab(int larg,int longe,int val);
int* init_int_arr(int size, int val);
void print_int_arr(int* t, int size);
void print_int_tab(int** t,int lg, int larg);
void free_int_tab(int** t, int size);


long two_to_one(int i1,int i2);
int get_first (int super_num);
int get_second (int super_num);

typedef struct {
    linked_duo_list** table;
    int size;
} dict;

dict* init_dict(int size);
void free_dict(dict* dico);
int exists(dict* dico,long key);
long find(dict* dico, long key);
void replace(dict* dico, long key, long val);
void add_to(dict* dico, long key,long val);
void add_replace(dict* dico,long key, long val);

#endif