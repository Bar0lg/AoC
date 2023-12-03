#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#include "utils.h"

#define TEST_FILENAME "./inputtest.txt"
#define INPUT_FILENAME "./input.txt"

enum colors{
    ROUGE,
    BLEU,
    VERT,
};

int match_color(char* str){
    if (is_in(str, "red")){
        return ROUGE;
    }
    if (is_in(str, "blue")){
        return BLEU;
    }
    if (is_in(str, "green")){
        return VERT;
    }
    return -1;
}

int part1(char* filepath){
    FILE* fp = fopen(filepath, "r");
    char line[BUFF_SIZE_MAX];
    char buf[BUFF_SIZE_MAX];
    int res = 0;
    int game_id = 1;
    int num_red = 0;
    int num_blue = 0;
    int num_green = 0;
    while (!feof(fp)){
        fgets(line, BUFF_SIZE_MAX, fp);
        strcpy(buf, line + 6 + (int)floor(log10(abs(game_id))) +1 );
        char* tok = strtok(buf,",;");
        while (tok) {
            //printf("%s\n",tok);
            int num_marble;
            sscanf(tok, " %d %*[^\n]", &num_marble);
            int color_used = match_color(tok);
            switch (color_used) {
                case ROUGE:
                    if (num_red < num_marble){
                        num_red = num_marble;
                    }
                    break;
                case BLEU:
                    if (num_blue < num_marble){
                        num_blue = num_marble;
                    }
                    break;
                case VERT:
                    if (num_green < num_marble){
                        num_green = num_marble;
                    }
                    break;

            
            }
            tok = strtok(NULL, ",;");

        }
        if (num_red <= 12 && num_blue <= 14 && num_green <= 13){
            res += game_id;
        }
        //printf("%d %d %d %d\n",game_id,num_red,num_blue,num_green);
        num_red = 0;
        num_blue = 0;
        num_green = 0;
        game_id++;

    }
    return res;
}
int part2(char* filepath){
    FILE* fp = fopen(filepath, "r");
    char line[BUFF_SIZE_MAX];
    char buf[BUFF_SIZE_MAX];
    int res = 0;
    int game_id = 1;
    int num_red = 0;
    int num_blue = 0;
    int num_green = 0;
    while (!feof(fp)){
        fgets(line, BUFF_SIZE_MAX, fp);
        strcpy(buf, line + 6 + (int)floor(log10(abs(game_id))) +1 );
        char* tok = strtok(buf,",;");
        while (tok) {
            //printf("%s\n",tok);
            int num_marble;
            sscanf(tok, " %d %*[^\n]", &num_marble);
            int color_used = match_color(tok);
            switch (color_used) {
                case ROUGE:
                    if (num_red < num_marble){
                        num_red = num_marble;
                    }
                    break;
                case BLEU:
                    if (num_blue < num_marble){
                        num_blue = num_marble;
                    }
                    break;
                case VERT:
                    if (num_green < num_marble){
                        num_green = num_marble;
                    }
                    break;

            
            }
            tok = strtok(NULL, ",;");

        }
        res += num_blue * num_green * num_red;
        //printf("%d %d %d %d\n",game_id,num_red,num_blue,num_green);
        num_red = 0;
        num_blue = 0;
        num_green = 0;
        game_id++;

    }
    return res;
}

int main(int argc, char** argv){
    int real_input = 0;
    if (argc > 1 && !strcmp(argv[1], "-i")){
        real_input = 1;
    }
    if (!real_input){
        printf("Resultat du test pour jour 2:\n");
        int res1 = part1(TEST_FILENAME);
        printf("Resultat part 1: %d\n",res1);
        int res2 = part2(TEST_FILENAME);
        printf("Resultat part 2: %d\n",res2);
    }
    else{
        printf("Resultat de l'input pour jour 2:\n");
        int res1 = part1(INPUT_FILENAME);
        printf("Resultat part 1: %d\n",res1);
        int res2 = part2(INPUT_FILENAME);
        printf("Resultat part 2: %d\n",res2);
    }
    return 0;
}
