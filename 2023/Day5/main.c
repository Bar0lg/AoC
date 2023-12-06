#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#include "utils.h"
#include "lists_long.h"

#define TEST_FILENAME "./inputtest.txt"
#define INPUT_FILENAME "./input.txt"

long long part1(char* filepath){
    FILE* fp = fopen(filepath, "r");
    char* saveptr;
    char line[BUFF_SIZE_MAX];
    char buf[BUFF_SIZE_MAX];
    fgets(line,BUFF_SIZE_MAX,fp);
    strcpy(buf, line);
    linked_list_long* seeds = NULL;
    char* tok = strtok_r(buf, "seeds: ", &saveptr);
    while (tok){
        seeds = cons_long(atoll(tok), seeds);
        tok = strtok_r(NULL, "seeds: ", &saveptr);
    }
    long long dest,source,range;
    //printf("SEEDS:");print_list_long(seeds);
    dict* changed = init_dict(30);
    while (!feof(fp)){
        if (!str_contain(line[0], "1234567890")){
            fgets(line, BUFF_SIZE_MAX, fp);
            free_dict(changed);
            changed = init_dict(30);
            continue;
        }
        //printf("%s\n",line);
        strcpy(buf, line);
        tok = strtok_r(buf, " ", &saveptr);
        dest = atoll(tok);
        tok = strtok_r(NULL, " ", &saveptr);
        source = atoll(tok);
        tok = strtok_r(NULL, " ", &saveptr);
        range = atoll(tok);
        linked_list_long* seed_cpy = seeds;
        //printf("\nLINE:%s\n",line);
        while (seed_cpy){
            if (seed_cpy->val >= source && seed_cpy->val < source + range){
                //printf("Olld:%lld NEW::%lld \n",seed_cpy->val, seed_cpy->val - source + dest);
                if (!exists(changed, (long)seed_cpy->val) || find(changed, (long)seed_cpy->val) == 0){
                    seed_cpy->val = (seed_cpy->val - source) + dest;
                    add_replace(changed, (long)seed_cpy->val, (long)1);
                }
            }
            seed_cpy = seed_cpy->next;
        }
        fgets(line, BUFF_SIZE_MAX, fp);
        //printf("\n");
        //print_list_long(seeds);

    }
    //print_list(seeds);
    //printf("\n");
    linked_list_long* seed_cpy = seeds;
    long long res = seeds->val;
    while (seed_cpy){
        res = min_long(res, seed_cpy->val);
        seed_cpy = seed_cpy->next;
    }
    //print_list_long(seeds);
    free_linked_list_long(seeds);
    free_dict(changed);
    return res;
}

long part2(char* filepath){
    FILE* fp = fopen(filepath, "r");
    char* saveptr;
    char line[BUFF_SIZE_MAX];
    char buf[BUFF_SIZE_MAX];
    fgets(line,BUFF_SIZE_MAX,fp);
    strcpy(buf, line);
    linked_duo_list* seeds_pairs = NULL;
    char* tok = strtok_r(buf, "seeds: ", &saveptr);
    //printf("%s\n",line);
    while (tok){
        long seed_start = atol(tok);
        tok = strtok_r(NULL, "seeds: ", &saveptr);
        long seed_range = atol(tok);
        duo pair = {.x = seed_start,.y = seed_start+seed_range -1};
        seeds_pairs = cons_duo(pair, seeds_pairs);
        tok = strtok_r(NULL, "seeds: ", &saveptr);
    }
    //printf("%s\n",line);
    //print_list_long(seeds);
    long dest,source,range;
    //printf("SEEDS:");print_list_long(seeds);
    linked_duo_list* new_list = NULL;
    fgets(line, BUFF_SIZE_MAX, fp);
    fgets(line, BUFF_SIZE_MAX, fp);
    fgets(line, BUFF_SIZE_MAX, fp);
    //printf("YOOO:%s",line);
    while (!feof(fp)){


        if (!str_contain(line[0], "1234567890")){
            //printf("Changed Line!!!\n");
            fgets(line, BUFF_SIZE_MAX, fp);
            linked_duo_list* seed_cpy = seeds_pairs;
            while (seed_cpy){
                if ((seed_cpy->val.x != -1)){
                    new_list = cons_duo(seed_cpy->val, new_list);
                }
                seed_cpy = seed_cpy->next;
            }
            free_linked_duo_list(seeds_pairs);
            seeds_pairs = new_list;
            new_list = NULL;
            continue;
        }


        strcpy(buf, line);
        tok = strtok_r(buf, " ", &saveptr);
        dest = atoll(tok);
        tok = strtok_r(NULL, " ", &saveptr);
        source = atoll(tok);
        tok = strtok_r(NULL, " ", &saveptr);
        range = atoll(tok);

        linked_duo_list* seed_cpy = seeds_pairs;

        while (seed_cpy){
            //linked_duo_list* next_cpy;
            //while (next_cpy){
            //    if (seed_cpy->val.x == next_cpy->val.x && seed_cpy->val.y == next_cpy->val.y ){
            //        seed_cpy = seed_cpy->next;
            //        continue;
            //    }
            //    next_cpy = next_cpy->next;
            //}
            if (seed_cpy->val.x == -1){
                ;
            }
            else if (seed_cpy->val.y < source|| seed_cpy->val.x >= source+range){
                //printf("Nothing\n");
                ;
            }
            else if (seed_cpy->val.x >= source && seed_cpy->val.y < source+range){
                duo new_pair = {.x = seed_cpy->val.x - source + dest, .y = seed_cpy->val.y - source + dest};
                //print_duo(seed_cpy->val);printf("-->");print_duo(new_pair);printf("\n");
                new_list = cons_duo(new_pair, new_list);
                seed_cpy->val.x = -1;seed_cpy->val.y = -1;
                //printf("All Included\n");
            }
            else if (seed_cpy->val.x >= source && seed_cpy->val.x < source+range  ){
                duo changed = {.x = seed_cpy->val.x - source + dest, .y = dest + range - 1};
                //print_duo(seed_cpy->val);printf("-->");print_duo(changed);printf("\n");
                seed_cpy->val.x = source+ range;
                new_list = cons_duo(changed, new_list);
                //printf("Over-right\n");
            }
            else if (seed_cpy->val.y >= source && seed_cpy->val.y < source+range  ){
                duo changed = {.x = dest, .y = seed_cpy->val.y - source + dest};
                //print_duo(seed_cpy->val);printf("-->");print_duo(changed);printf("\n");
                seed_cpy->val.y = source -1;
                new_list = cons_duo(changed, new_list);
                //printf("Over-left\n");
            }
            else if (seed_cpy->val.x <= source && seed_cpy->val.y >= source+range){
                duo unchanged2 = {.x = source + range, .y = seed_cpy->val.y};
                duo changed = {.x = dest, .y = dest + range -1};
                //print_duo(seed_cpy->val);printf("-->");print_duo(changed);printf("\n");
                //print_duo(seed_cpy->val);printf("-->");print_duo(unchanged2);printf("\n");
                seed_cpy->val.y = source -1;
                linked_duo_list* next = seed_cpy->next;
                linked_duo_list* to_add = cons_duo(unchanged2, NULL);
                seed_cpy->next = to_add;
                seed_cpy->next->next = next;
                new_list = cons_duo(changed, new_list);
                //printf("all-IN\n");
            }
            seed_cpy = seed_cpy->next;
        }
        //printf("LINE:%s",line);
        //printf("Dest: %ld Source: %ld range: %ld (%ld-%ld)\n",dest,source,range,source,source+range-1);
        //printf("seed_pair:");print_duo_list(seeds_pairs);
        //printf("\nnew_list:");print_duo_list(new_list);
        //printf("\n\n\n");
        //fgetc(stdin);


        fgets(line, BUFF_SIZE_MAX, fp);

    }
    linked_duo_list* last_cpy = seeds_pairs;
    while (last_cpy){
        if (last_cpy->val.x != -1){
            new_list = cons_duo(last_cpy->val, new_list);
        }
        last_cpy = last_cpy->next;
    }
    free_linked_duo_list(seeds_pairs);
    //print_duo_list(new_list);

    linked_duo_list* seed_cpy = new_list;
    long res = new_list->val.x;
    int is_ranged = 1;
    while (seed_cpy){
        is_ranged = is_ranged && (seed_cpy->val.x <= seed_cpy->val.y);
        res = min_long(res, seed_cpy->val.x);
        seed_cpy = seed_cpy->next;
    }
    //print_list_long(seeds);
    free_linked_duo_list(new_list);
    //printf("RNAGED%d\n",is_ranged);
    return res;
}

int main(int argc, char** argv){
    int real_input = 0;
    if (argc > 1 && !strcmp(argv[1], "-i")){
        real_input = 1;
    }
    if (!real_input){
        printf("Resultat du test pour jour 5:\n");
        long long res1 = part1(TEST_FILENAME);
        printf("Resultat part 1: %lld\n",res1);
        long long res2 = part2(TEST_FILENAME);
        printf("Resultat part 2: %lld\n",res2);
    }
    else{
        printf("Resultat de l'input pour jour 5:\n");
        long res1 = part1(INPUT_FILENAME);
        printf("Resultat part 1: %ld\n",res1);
        long res2 = part2(INPUT_FILENAME);
        printf("Resultat part 2: %ld\n",res2);
    }
    return 0;
}
