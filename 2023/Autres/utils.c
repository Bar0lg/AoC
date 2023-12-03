#include "utils.h"
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int min_int(int i1,int i2){
    if (i1 > i2){
        return i2;
    }
    return i1;
}

int max_int(int i1,int i2){
    if (i1 < i2){
        return i2;
    }
    return i1;
}

int cmp_strings(char* str1, char* str2){
    int res = 0;
    int max = min_int(strlen(str1),strlen(str2));

    for (int i = 0;i<max;i++){
        if (str1[i] != str2[i]){
            return res;
        }
        res++;
    }
    return res;

}

int equal_strings(char* str1, char* str2){
    int n_1 = strlen(str1);
    int n_2 = strlen(str1);
    if (n_1 == n_2){
        if (cmp_strings(str1,str2) == n_1){
            return 1;
        }
    }
    return 0;
}

int start_with(char* grand, char* petit){
    if (cmp_strings(grand, petit) >= (int)strlen(petit)){
        return 1;
    }
    return 0;
}

int is_in(char* grand, char* petit){
    int res = 0;
    for (int i =0;i<(int)(strlen(grand));i++){
        res = res || start_with(grand + i, petit);
    }
    return res;
}

int str_contain(char c, char* all_chars,int include){
    int res = 0;
    int n = strlen(all_chars);
    if (include){
        for (int i=0;i<n;i++){
            res = res || (c == all_chars[i]);
        }
    }
    else
    {
        res = 1;
        for (int i=0;i<n;i++){
            res = res && (c != all_chars[i]);
        }
    }
    return res;
}

linked_list* cons(int val, linked_list* tail){
    linked_list* res = malloc(sizeof(linked_list));
    res->val = val;
    res->next = tail;
    return res;
}

linked_list* rev_linked(linked_list* l){
    linked_list* res = NULL;
    linked_list* l_copy = l;
    while (l_copy){
        res = cons(l_copy->val, res);
        l_copy = l_copy->next; 
    }
    free_linked_list(l);
    return res;
}

void free_linked_list(linked_list* l){
    if (l->next != NULL){
        free_linked_list(l->next);
    }
    free(l);
}

void print_list(linked_list* l){
    if (l != NULL){
        printf("%d ",l->val);
        print_list(l->next);
    }
}

void print_duo(duo d){
    printf("(%ld %ld) ",d.x, d.y);
}

linked_duo_list* cons_duo(duo val, linked_duo_list* tail){
    linked_duo_list* res = malloc(sizeof(linked_duo_list));
    res->val = val;
    res->next = tail;
    return res;
}

linked_duo_list* rev_linked_duo(linked_duo_list* l){
    linked_duo_list* res = NULL;
    linked_duo_list* l_copy = l;
    while (l_copy){
        res = cons_duo(l_copy->val, res);
        l_copy = l_copy->next; 
    }
    free_linked_duo_list(l);
    return res;
}

void free_linked_duo_list(linked_duo_list* l){
    if (l->next != NULL){
        free_linked_duo_list(l->next);
    }
    free(l);
}

void print_duo_list(linked_duo_list* l){
    if (l != NULL){
        print_duo(l->val);
        print_duo_list(l->next);
    }
}


int** init_int_tab(int larg,int longe,int val){
    int** res = (int**)malloc(sizeof(int*)*longe);
    for (int i=0;i<longe;i++){
        int* res_bis = (int*)malloc(sizeof(int)*larg);
        for (int j=0;j<larg;j++){
            res_bis[j] = val;
        }
        res[i] = res_bis;
    }
    return res;
}

void print_int_arr(int* t, int size){
    for (int i=0;i<size;i++){
        printf("%d ",t[i]);
    }
    printf("\n");
}

void print_int_tab(int** t,int lg, int larg){
    for (int i=0;i<lg;i++){
        print_int_arr(t[i], larg);
    }
}

void free_int_tab(int** t, int size){
    for (int i=0;i<size;i++){
        free(t[i]);
    }
    free(t);
}

long two_to_one(int i1,int i2){
    return i1 << 16 | i2;
}
int get_first (int super_num){
    return super_num >> 16;
}
int get_second (int super_num){
    return super_num & 0xFFFF;
}