#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#include "utils.h"

#define TEST_FILENAME "./inputtest.txt"
#define INPUT_FILENAME "./input.txt"

int part1(char* filepath){
    FILE* fp = fopen(filepath, "r");
    char line[BUFF_SIZE_MAX];
    linked_list* winnings = NULL;
    linked_list* connus = NULL;
    int res = 0;
    while(!feof(fp)){
        fgets(line,BUFF_SIZE_MAX,fp);
        char* tok = strtok(line + 9, "|");
        char tok_cpy[BUFF_SIZE_MAX];
        strcpy(tok_cpy, tok);
        char* saveptr;
        char* tok_2 = strtok_r(tok_cpy, " ", &saveptr);
        while (tok_2){
            winnings = cons(atoi(tok_2),winnings);
            tok_2 = strtok_r(NULL, " ", &saveptr);
        }
        tok = strtok(NULL, "|");
        strcpy(tok_cpy, tok);
        tok_2 = strtok_r(tok_cpy, " ", &saveptr);
        while (tok_2){
            connus= cons(atoi(tok_2),connus);
            tok_2 = strtok_r(NULL, " ", &saveptr);
        }

        linked_list* win_cpy = winnings;
        int tmp = 0;
        while (win_cpy){
            linked_list* conn_cpy = connus;
            while (conn_cpy){
                if (conn_cpy->val == win_cpy->val){
                    if (tmp == 0){
                        tmp = 1;
                    }
                    else {
                        tmp *= 2;
                    }
                }
                conn_cpy = conn_cpy->next;
            }
            win_cpy = win_cpy->next;

        }
        res += tmp;
        free_linked_list(winnings);
        free_linked_list(connus);
        winnings = NULL;
        connus = NULL;
    }
        return res;
}
int part2(char* filepath){
    FILE* fp = fopen(filepath, "r");
    int num_grids = 0;
    char line[BUFF_SIZE_MAX];
    while (!feof(fp)){
        fgets(line,BUFF_SIZE_MAX,fp);
        num_grids++;
    }
    rewind(fp);
    int* num_of_each = (int*)calloc(num_grids, sizeof(int));
    for (int i=0;i<num_grids;i++){
        num_of_each[i] = 1;
    }
    linked_list* winnings = NULL;
    linked_list* connus = NULL;
    int res = 0;
    int game_curr = 0;
    while(!feof(fp)){
        fgets(line,BUFF_SIZE_MAX,fp);
        char* tok = strtok(line + 9, "|");
        char tok_cpy[BUFF_SIZE_MAX];
        strcpy(tok_cpy, tok);
        char* saveptr;
        char* tok_2 = strtok_r(tok_cpy, " ", &saveptr);
        while (tok_2){
            winnings = cons(atoi(tok_2),winnings);
            tok_2 = strtok_r(NULL, " ", &saveptr);
        }
        tok = strtok(NULL, "|");
        strcpy(tok_cpy, tok);
        tok_2 = strtok_r(tok_cpy, " ", &saveptr);
        while (tok_2){
            connus= cons(atoi(tok_2),connus);
            tok_2 = strtok_r(NULL, " ", &saveptr);
        }

        linked_list* win_cpy = winnings;
        int tmp = 0;
        while (win_cpy){
            linked_list* conn_cpy = connus;
            while (conn_cpy){
                if (conn_cpy->val == win_cpy->val){
                    tmp++;
                }
                conn_cpy = conn_cpy->next;
            }
            win_cpy = win_cpy->next;

        }
        //print_int_arr(num_of_each, num_grids);
        for (int i=game_curr +1;i<game_curr+tmp+1;i++){
            num_of_each[i] += num_of_each[game_curr];
        }
        free_linked_list(winnings);
        free_linked_list(connus);
        winnings = NULL;
        connus = NULL;
        game_curr++;
    }
    for (int i =0;i<num_grids;i++){
        res += num_of_each[i];
    }
    free(num_of_each);
    return res;
}

int main(int argc, char** argv){
    int real_input = 0;
    if (argc > 1 && !strcmp(argv[1], "-i")){
        real_input = 1;
    }
    if (!real_input){
        printf("Resultat du test pour jour 4:\n");
        int res1 = part1(TEST_FILENAME);
        printf("Resultat part 1: %d\n",res1);
        int res2 = part2(TEST_FILENAME);
        printf("Resultat part 2: %d\n",res2);
    }
    else{
        printf("Resultat de l'input pour jour 4:\n");
        int res1 = part1(INPUT_FILENAME);
        printf("Resultat part 1: %d\n",res1);
        int res2 = part2(INPUT_FILENAME);
        printf("Resultat part 2: %d\n",res2);
    }
    return 0;
}
