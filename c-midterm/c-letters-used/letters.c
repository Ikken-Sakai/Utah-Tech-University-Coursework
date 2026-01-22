#include "letters.h"
#include <stdio.h>
#include <ctype.h>
#include <stdbool.h>
#include <string.h>

void letters_used(char *line) {
	int n, count, i, lletter;
	char current;
	bool letters[128] = {false};
	bool alphaornot;

	count = 0;

	while (line[count] != '\0'){
		n = sscanf(line, "%c", &current);
		if (n == 1){
			alphaornot = isalpha(line[count]);
			if (alphaornot == true){
				lletter = tolower(line[count]);
				if (letters[lletter] == false){
					letters[lletter] = true;
			}
		}
			count ++;
	}
}
	for (i = 97; i<123; i++){
		if (letters[i] == true)
			printf("%c", i);
	}
	printf("\n");
}
