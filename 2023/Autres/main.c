#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "utils.h"

#define TEST_FILENAME "./inputtest.txt"
#define INPUT_FILENAME "./input.txt"

int part1(char* filepath){
    return -1;
}
int part2(char* filepath){
    return -1;
}

int main(int argc, char** argv){
    int real_input = 0;
    if (argc > 1 && !strcmp(argv[1], "-i")){
        real_input = 1;
    }
    if (!real_input){
        printf("Resultat du test:\n");
        int res1 = part1(TEST_FILENAME);
        printf("Resultat part 1: %d\n",res1);
        int res2 = part2(TEST_FILENAME);
        printf("Resultat part 2: %d\n",res2);
    }
    else{
        printf("Resultat de l'input:\n");
        int res1 = part1(INPUT_FILENAME);
        printf("Resultat part 1: %d\n",res1);
        int res2 = part2(INPUT_FILENAME);
        printf("Resultat part 2: %d\n",res2);
    }
    return 0;
}