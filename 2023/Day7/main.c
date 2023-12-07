#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "lists_char.h"
#include "utils.h"

#define TEST_FILENAME "./inputtest.txt"
#define INPUT_FILENAME "./input.txt"

#define FIVE_OF_KIND 6
#define CARRE 5
#define FULL_HOUSE 4
#define BRELAN 3
#define TWO_PAIRS 2
#define PAIR 1
#define HIGH_CARD 0

int conv_val(char c){
    if (str_contain(c, "23456789")){
        char num[2];
        num[0] = c;
        num[1] = '\0';
        return atoi(num);
    }
    switch (c) {
        case 'T':
            return 10;
        case 'J':
            return 11;
        case 'Q':
            return 12;
        case 'K':
            return 13;
        case 'A':
            return 14;
    }
    return -1;
}
int conv_val_p2(char c){
    if (str_contain(c, "23456789")){
        char num[2];
        num[0] = c;
        num[1] = '\0';
        return atoi(num);
    }
    switch (c) {
        case 'T':
            return 10;
        case 'J':
            return 0;
        case 'Q':
            return 12;
        case 'K':
            return 13;
        case 'A':
            return 14;
    }
    return -1;
}

int occ(char c, char* s){
    int n = strlen(s);
    int res = 0;
    for (int i =0;i<n;i++){
        if (s[i] == c){
            res++;
        }
    }
    return res;
}
int occ_jok(char c, char* s){
    int n = strlen(s);
    int res = 0;
    for (int i =0;i<n;i++){
        if (s[i] == c || s[i] == 'J'){
            res++;
        }
    }
    return res;
}
char most_occ(char* s){
    int n = strlen(s);
    int max = 0;
    char c_max;
    for (int i=0;i<n;i++){
        if (occ(s[i],s) >= max){
        max = occ(s[i],s);
        c_max = s[i];
        }
    }
    return c_max;
}

char sec_most_occ(char* s){
    int n = strlen(s);
    int max = 0;
    char res = s[0];
    char most_occuring = most_occ(s);
    for (int i=0;i<n;i++){
        if (s[i] != most_occuring){
            if (occ(s[i],s) >= max){
            max = occ(s[i],s);
            res = s[i];
            }
        }
    }
    return res;
}



int classe(char* s){
    int most_occuring = occ(most_occ(s),s);
    int sec_most_occuring = occ(sec_most_occ(s),s);
    if (most_occuring == 5){
        return FIVE_OF_KIND;
    }
    if (most_occuring == 4){
        return CARRE;
    }
    if (most_occuring == 3 && sec_most_occuring == 2){
        return FULL_HOUSE;
    }
    if (most_occuring == 3){
        return BRELAN;
    }
    if (most_occuring == 2 && sec_most_occuring == 2){
        return TWO_PAIRS;
    }
    if (most_occuring == 2){
        return PAIR;
    }
    return HIGH_CARD;
}
int classe_p2(char* s){
    int most_occuring = occ_jok(most_occ(s),s);
    int sec_most_occuring = occ(sec_most_occ(s),s);
    if (occ('J',s) == most_occuring){
        most_occuring = occ_jok(sec_most_occ(s),s);
    }
    if (most_occuring == 5){
        return FIVE_OF_KIND;
    }
    if (most_occuring == 4){
        return CARRE;
    }
    if (most_occuring == 3 && sec_most_occuring == 2){
        return FULL_HOUSE;
    }
    if (most_occuring == 3){
        return BRELAN;
    }
    if (most_occuring == 2 && sec_most_occuring == 2){
        return TWO_PAIRS;
    }
    if (most_occuring == 2){
        return PAIR;
    }
    return HIGH_CARD;
}


int comp_hand(char* s1, char* s2){
    int n = strlen(s1);
    for (int i = 0;i<n;i++){
        if (conv_val(s1[i]) > conv_val(s2[i])){
            return 1;
        }
        if (conv_val(s1[i]) < conv_val(s2[i])){
            return -1;
        }
    }
    return 0;
}
int comp_hand_p2(char* s1, char* s2){
    int n = strlen(s1);
    for (int i = 0;i<n;i++){
        if (conv_val_p2(s1[i]) > conv_val_p2(s2[i])){
            return 1;
        }
        if (conv_val_p2(s1[i]) < conv_val_p2(s2[i])){
            return -1;
        }
    }
    return 0;
}


int part1(char* filepath){
    FILE* fp = fopen(filepath, "r");
    linked_list_char* scores = NULL;
    char line[BUFF_SIZE_MAX];

    while(!feof(fp)){
        char* hand = (char*)malloc(sizeof(char)*10);
        hand[0] = '\0';
        int bet = 0;


        fgets(line, BUFF_SIZE_MAX, fp);
        char* tok = strtok(line, " ");
        strcpy(hand, tok);
        tok = strtok(NULL, " ");
        bet = atoi(tok);
        duo_char to_add = {hand,bet};
        linked_list_char* scores_cpy = scores;
        linked_list_char* prev = NULL;
        while (TRUE){
            if (!scores){
                scores = cons_duo_char(to_add, NULL);
                break;
            }
            if (!scores_cpy){
                prev->next = cons_duo_char(to_add, NULL);
                break;
            }
            else if (classe(to_add.x) > classe(scores_cpy->val.x)){
                prev = scores_cpy;
                scores_cpy = scores_cpy->next;
            }
            else if (classe(to_add.x) < classe(scores_cpy->val.x)){
                if (prev == NULL){
                    scores = cons_duo_char(to_add, scores);
                }
                else {
                    prev->next = cons_duo_char(to_add, scores_cpy);
                }
                break;
            }
            else{
                if (comp_hand(to_add.x, scores_cpy->val.x) == 1){
                    prev = scores_cpy;
                    scores_cpy = scores_cpy->next;
                }else{
                    if (prev == NULL){
                        scores = cons_duo_char(to_add, scores);
                        }
                    else {
                        prev->next = cons_duo_char(to_add, scores_cpy);
                        }
                    break;
                }
            }
        }
    }
    int num_hand = 1;
    int res = 0;
    linked_list_char* res_cpy = scores;
    //print_list_char(scores);
    while (res_cpy){
        res += res_cpy->val.y * num_hand;
        num_hand++;
        res_cpy = res_cpy->next;
    }
    free_linked_list_char(scores);
    return res;
}
int part2(char* filepath){
    FILE* fp = fopen(filepath, "r");
    linked_list_char* scores = NULL;
    char line[BUFF_SIZE_MAX];

    while(!feof(fp)){
        char* hand = (char*)malloc(sizeof(char)*10);
        hand[0] = '\0';
        int bet = 0;


        fgets(line, BUFF_SIZE_MAX, fp);
        char* tok = strtok(line, " ");
        strcpy(hand, tok);
        tok = strtok(NULL, " ");
        bet = atoi(tok);
        duo_char to_add = {hand,bet};
        linked_list_char* scores_cpy = scores;
        linked_list_char* prev = NULL;
        //printf("%s Classe:%d \n",hand,classe_p2(hand));
        while (TRUE){
            if (!scores){
                scores = cons_duo_char(to_add, NULL);
                break;
            }
            if (!scores_cpy){
                prev->next = cons_duo_char(to_add, NULL);
                break;
            }
            else if (classe_p2(to_add.x) > classe_p2(scores_cpy->val.x)){
                prev = scores_cpy;
                scores_cpy = scores_cpy->next;
            }
            else if (classe_p2(to_add.x) < classe_p2(scores_cpy->val.x)){
                if (prev == NULL){
                    scores = cons_duo_char(to_add, scores);
                }
                else {
                    prev->next = cons_duo_char(to_add, scores_cpy);
                }
                break;
            }
            else{
                if (comp_hand_p2(to_add.x, scores_cpy->val.x) == 1){
                    prev = scores_cpy;
                    scores_cpy = scores_cpy->next;
                }else{
                    if (prev == NULL){
                        scores = cons_duo_char(to_add, scores);
                        }
                    else {
                        prev->next = cons_duo_char(to_add, scores_cpy);
                        }
                    break;
                }
            }
        }
    }
    int num_hand = 1;
    int res = 0;
    linked_list_char* res_cpy = scores;
    //print_list_char(scores);
    while (res_cpy){
        res += res_cpy->val.y * num_hand;
        num_hand++;
        res_cpy = res_cpy->next;
    }
    free_linked_list_char(scores);
    return res;
}

int main(int argc, char** argv){
    int real_input = 0;
    if (argc > 1 && !strcmp(argv[1], "-i")){
        real_input = 1;
    }
    if (!real_input){
        printf("Resultat du test pour jour 7:\n");
        int res1 = part1(TEST_FILENAME);
        printf("Resultat part 1: %d\n",res1);
        int res2 = part2(TEST_FILENAME);
        printf("Resultat part 2: %d\n",res2);
    }
    else{
        printf("Resultat de l'input pour jour 7:\n");
        int res1 = part1(INPUT_FILENAME);
        printf("Resultat part 1: %d\n",res1);
        int res2 = part2(INPUT_FILENAME);
        printf("Resultat part 2: %d\n",res2);
    }
    return 0;
}
