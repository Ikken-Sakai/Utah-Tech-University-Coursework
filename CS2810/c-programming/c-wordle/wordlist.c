#include "wordle.h"
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

char **read_word_list(char *filename) {
	FILE *fp = fopen(filename, "r");
	int max = 32;
	char **list = malloc(max*sizeof(char*));
	int numberOfElm = 0;
	char line[16];
	while (fgets(line, 16, fp) != NULL){
		if (numberOfElm == max){
			max *= 2;
			list = realloc(list, max*sizeof(char*));
		}
		int i = 0;
		while (line[i] != '\n'){
			i++;
		}
		if (i != 5){ printf("ahhhhhhhhhhhhhhh"); }
		char* word = malloc(6*sizeof(char));
		list[numberOfElm] = strncpy(word, line, 5);
		list[numberOfElm][5] = '\0';
		numberOfElm++;
	}
	fclose(fp);
	return list;
}

void free_word_list(char **list) {
	int i = 0;
	while (list [i] != NULL) {
		free(list[i]);
		i ++;
	}
	free(list);
}
