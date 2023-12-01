#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#define BUFF_MAX 100
#define FILEPATH "./input.txt"

int min(int i1,int i2){
    if (i1 > i2){
        return i2;
    }
    return i1;
}

int cmp_strings(char* str1, char* str2){
    int res = 0;
    int max = min(strlen(str1),strlen(str2));

    for (int i = 0;i<max;i++){
        if (str1[i] != str2[i]){
            return res;
        }
        res++;
    }
    return res;

}

int is_anumber(char* str){
    if (cmp_strings(str, "one") >= 3){
        return 1;
    }
    if (cmp_strings(str, "two") >= 3){
        return 2;
    }
    if (cmp_strings(str, "three") >= 5){
        return 3;
    }
    if (cmp_strings(str, "four") >= 4){
        return 4;
    }
    if (cmp_strings(str, "five") >= 4){
        return 5;
    }
    if (cmp_strings(str, "six") >= 3){
        return 6;
    }
    if (cmp_strings(str, "seven") >= 5){
        return 7;
    }
    if (cmp_strings(str, "eight") >= 5){
        return 8;
    }
    if (cmp_strings(str, "nine") >= 4){
        return 9;
    }
    return -1;
}

int part1(char* filename){
    FILE* fp = fopen(filename, "r");
    int res = 0;
    int first = -1;
    int last = -1;
    char line[BUFF_MAX];
    while (!feof(fp)){
        fgets(line,BUFF_MAX,fp);
        int index = 0;
        while (line[index] != '\0'){
            char c = line[index];
            if ((int)c <= (int)'9' && (int)c >= (int)'0'){
                last = (int)c - (int)'0';
            }
            if (first == -1){
                first = last;
            }
            index++;
        }
        if (first != -1){
        res += 10*first + last;
        }
        first = -1;
        last = -1;
    }
    return res;
}

int part2(char* filename){
    FILE* fp = fopen(filename, "r");
    int res = 0;
    int first = -1;
    int last = -1;
    char line[BUFF_MAX];
    while (!feof(fp)){
        fgets(line,BUFF_MAX,fp);
        int index = 0;
        while (line[index] != '\0'){
            char c = line[index];
            if ((int)c <= (int)'9' && (int)c >= (int)'0'){
                last = (int)c - (int)'0';
            }
            else{
                if (is_anumber(line + index) != -1){
                    last = is_anumber(line + index);
                }
            }
            if (first == -1){
                first = last;
            }
            index++;
        }
        if (first != -1){
        res += 10*first + last;
        }
        first = -1;
        last = -1;
    }
    return res;
}

int main(){
    int res1 = part1(FILEPATH);
    int res2 = part2(FILEPATH);
    printf("PART1: %d\n",res1);
    printf("PART2: %d\n",res2);
    return 0;
}