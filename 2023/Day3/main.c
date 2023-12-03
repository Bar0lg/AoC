#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "utils.h"

#define TEST_FILENAME "./inputtest.txt"
#define INPUT_FILENAME "./input.txt"

int part1(char* filepath){
    //Part 1.1 Capture all specials charaters
    FILE* fp = fopen(filepath, "r");
    int num_lines = 1;
    int len_in_line = 0;
    char c;
    char spe_chars[BUFF_SIZE_MAX];
    spe_chars[0] = '\0';
    char spe_char[2];
    while (!feof(fp)){
        c = fgetc(fp);
        if (c == EOF){
            continue;
        }
        if (c == '\n'){
            num_lines++;
        }
        spe_char[0] = c;
        spe_char[1] = '\0';
        if (str_contain(c, "\n.12345678990", FALSE)){
            if (str_contain(c, spe_chars, FALSE)){
                //printf("%s %s\n",spe_chars,spe_char);
                strcat(spe_chars,spe_char);
            }
        }
    }
    rewind(fp);
    //Part 1.2 Capture all vals:
    linked_list* all_vals = NULL;
    char line[BUFF_SIZE_MAX];
    char delimiters[BUFF_SIZE_MAX+3];
    delimiters[0] = '.';
    delimiters[1] = '\n';
    delimiters[2] = '\0';
    strcat(delimiters, spe_chars);
    //printf("DELIMITERS = %s \n",delimiters);
    while (!feof(fp)){
        fgets(line,BUFF_SIZE_MAX,fp);
        len_in_line = strlen(line);
        char* tok = strtok(line, delimiters);
        while (tok){
            //printf("TOK:%s %d\n",tok,atoi(tok));
            all_vals = cons(atoi(tok),all_vals);
            tok = strtok(NULL, delimiters);
        }
    }
    all_vals = rev_linked(all_vals);
    rewind(fp);
    //Part 1.3 get all positions
    int** pos = init_int_tab(len_in_line, num_lines,0);
    //printf("%d %d\n",len_in_line,num_lines);
    int i = 0;
    int j = 0;
    while (!feof(fp)){
        c = fgetc(fp);
        if (c == EOF){
            continue;
        }
        //printf("%d %d %d\n",c,j,i);
        if (str_contain(c, spe_chars, TRUE)){
            pos[i][j] = 2;
        }
        if (str_contain(c, "1234567890", TRUE)){
            pos[i][j] = 1;
        }
        j++;
        if (c == '\n'){
            i++;
            j = 0;
        }
    }
    fclose(fp);
    //Part 1.4 finally get result
    int res = 0;
    int already_seen = FALSE;
    linked_list* val_curr = all_vals;
    //print_int_tab(pos, num_lines, len_in_line);
    //print_list(all_vals);
    //printf("ALL VALS\n");
    for (int i=0;i<num_lines;i++){
        for (int j=0;j<len_in_line;j++){

            if (pos[i][j] == 0 || pos[i][j] == 2){
                if (j == 0 || pos[i][j-1] == 1){
                    already_seen = FALSE;
                    if (j != 0){
                        val_curr = val_curr->next;
                    }
                    else if (i != 0 && pos[i-1][len_in_line-1]) {
                        val_curr = val_curr->next;
                    }
                }
            }
            if (already_seen){
                continue;
            }
            if (pos[i][j] == 1){
                int next_to_spe = FALSE;
                // if not at top
                if (i != 0){
                    next_to_spe = next_to_spe || (pos[i-1][j] == 2);
                    if (j != 0){
                        next_to_spe = next_to_spe || (pos[i-1][j-1] == 2);
                    }
                    if (j != len_in_line -1){
                        next_to_spe = next_to_spe || (pos[i-1][j+1] == 2);
                    }
                }
                if (i != num_lines-1){
                    next_to_spe = next_to_spe || (pos[i+1][j] == 2);
                    if (j != 0){
                        next_to_spe = next_to_spe || (pos[i+1][j-1] == 2);
                    }
                    if (j != len_in_line -1){
                        next_to_spe = next_to_spe || (pos[i+1][j+1] == 2);
                    }
                }
                if (j != 0){
                        next_to_spe = next_to_spe || (pos[i][j-1] == 2);
                    }
                if (j != len_in_line -1){
                        next_to_spe = next_to_spe || (pos[i][j+1] == 2);
                }

                if (next_to_spe){
                    //printf("%d %d %d\n",i,j,val_curr->val);
                    res += val_curr->val;
                    already_seen = TRUE;
                }
            }
        }
    }
    free_linked_list(all_vals);
    free_int_tab(pos, num_lines);
    return res;
}

int part2(char* filepath){
    //Part 1.1 Capture all specials charaters
    FILE* fp = fopen(filepath, "r");
    int num_lines = 1;
    int len_in_line = 0;
    char c;
    char spe_chars[BUFF_SIZE_MAX];
    spe_chars[0] = '\0';
    char spe_char[2];
    while (!feof(fp)){
        c = fgetc(fp);
        if (c == EOF){
            continue;
        }
        if (c == '\n'){
            num_lines++;
        }
        spe_char[0] = c;
        spe_char[1] = '\0';
        if (str_contain(c, "\n.12345678990", FALSE)){
            if (str_contain(c, spe_chars, FALSE)){
                //printf("%s %s\n",spe_chars,spe_char);
                strcat(spe_chars,spe_char);
            }
        }
    }
    rewind(fp);
    //Part 1.2 Capture all vals:
    linked_list* all_vals = NULL;
    char line[BUFF_SIZE_MAX];
    char delimiters[BUFF_SIZE_MAX+3];
    delimiters[0] = '.';
    delimiters[1] = '\n';
    delimiters[2] = '\0';
    strcat(delimiters, spe_chars);
    //printf("DELIMITERS = %s \n",delimiters);
    while (!feof(fp)){
        fgets(line,BUFF_SIZE_MAX,fp);
        len_in_line = strlen(line);
        char* tok = strtok(line, delimiters);
        while (tok){
            //printf("TOK:%s %d\n",tok,atoi(tok));
            all_vals = cons(atoi(tok),all_vals);
            tok = strtok(NULL, delimiters);
        }
    }
    all_vals = rev_linked(all_vals);
    rewind(fp);
    //Part 1.3 get all positions
    int** pos = init_int_tab(len_in_line, num_lines,0);
    //printf("%d %d\n",len_in_line,num_lines);
    int i = 0;
    int j = 0;
    while (!feof(fp)){
        c = fgetc(fp);
        if (c == EOF){
            continue;
        }
        //printf("%d %d %d\n",c,j,i);
        if (str_contain(c, spe_chars, TRUE)){
            pos[i][j] = 2;
        }
        if (str_contain(c, "1234567890", TRUE)){
            pos[i][j] = 1;
        }
        j++;
        if (c == '\n'){
            i++;
            j = 0;
        }
    }
    fclose(fp);
    //Part 1.4 finally get result
    int res = 0;
    int already_seen = FALSE;
    linked_list* val_curr = all_vals;
    linked_duo_list* binded = NULL;
    long link_co;
    //print_int_tab(pos, num_lines, len_in_line);
    //print_list(all_vals);
    //printf("ALL VALS\n");
    for (int i=0;i<num_lines;i++){
        for (int j=0;j<len_in_line;j++){

            if (pos[i][j] == 0 || pos[i][j] == 2){
                if (j == 0 || pos[i][j-1] == 1){
                    already_seen = FALSE;
                    if (j != 0){
                        val_curr = val_curr->next;
                    }
                    else if (i != 0 && pos[i-1][len_in_line-1]) {
                        val_curr = val_curr->next;
                    }
                }
            }
            if (already_seen){
                continue;
            }
            if (pos[i][j] == 1){
                int next_to_spe = FALSE;
                // if not at top
                if (i != 0) {
                    if (pos[i-1][j] == 2){
                        next_to_spe = TRUE;
                        link_co = two_to_one(i-1 , j);
                    }
                    if (j != 0 && (pos[i-1][j-1] == 2)){
                        next_to_spe = TRUE;
                        link_co = two_to_one(i-1 , j-1);
                    }
                    if (j != len_in_line -1 && (pos[i-1][j+1] == 2)){
                        next_to_spe = TRUE;
                        link_co = two_to_one(i-1 , j+1);
                    }
                }
                if (i != num_lines-1){
                    if (pos[i+1][j] == 2){
                        next_to_spe = TRUE ;
                        link_co = two_to_one(i+1 , j);
                    }
                    if (j != 0 && (pos[i+1][j-1] == 2)){
                        next_to_spe = TRUE;
                        link_co = two_to_one(i+1 , j-1);
                    }
                    if (j != len_in_line -1 && (pos[i+1][j+1] == 2)){
                        next_to_spe = TRUE;
                        link_co = two_to_one(i+1 , j+1);
                    }
                }
                if (j != 0 && (pos[i][j-1] == 2)){
                        next_to_spe = TRUE;
                        link_co = two_to_one(i , j-1);
                    }
                if (j != len_in_line -1 && (pos[i][j+1] == 2)){
                        next_to_spe = TRUE;
                        link_co = two_to_one(i , j+1);
                }

                if (next_to_spe){
                    //printf("%d %d %d\n",i,j,val_curr->val);
                    linked_duo_list* binded_copy = binded;
                    //print_duo_list(binded);
                    //printf("\n");
                    duo link = {.x = link_co, .y = (long)val_curr->val};
                    int changed = FALSE;
                    while(binded_copy){
                        //printf("%d %d\n",get_first(binded_copy->val.x),get_second(binded_copy->val.x));
                        if (link_co == binded_copy->val.x){
                            //printf("%d * %d\n",val_curr->val,(int)binded_copy->val.y);
                            res += (int)(val_curr->val * (int)binded_copy->val.y);
                            changed = TRUE;
                        }
                        binded_copy = binded_copy->next;
                    }
                    if (!changed){
                        binded = cons_duo(link, binded);
                    }
                    already_seen = TRUE;

                }
            }
        }
    }
    free_linked_duo_list(binded);
    free_linked_list(all_vals);
    free_int_tab(pos, num_lines);
    return res;
}

int main(int argc, char** argv){
    int real_input = 0;
    if (argc > 1 && !strcmp(argv[1], "-i")){
        real_input = 1;
    }
    if (!real_input){
        printf("Resultat du test pour jour 3:\n");
        int res1 = part1(TEST_FILENAME);
        printf("Resultat part 1: %d\n",res1);
        int res2 = part2(TEST_FILENAME);
        printf("Resultat part 2: %d\n",res2);
    }
    else{
        printf("Resultat de l'input pour jour 3:\n");
        int res1 = part1(INPUT_FILENAME);
        printf("Resultat part 1: %d\n",res1);
        int res2 = part2(INPUT_FILENAME);
        printf("Resultat part 2: %d\n",res2);
    }
    return 0;
}
