#include "wordle.h"
#include <stdio.h>

guess parse_guess(char *line) {
	int i = 0;
	guess g;
	int j = 0;
	while (j < 5){
		if (line[i] == '['){
			g.letters[j] = line[i + 1];
			g.feedback[j] = EXACT_HIT;
			i += 3;
		}
		else if(line[i] == '('){
			g.letters[j] = line[i+1];
			g.feedback[j] = PARTIAL_HIT;
			i += 3;
		}
		else{
			g.letters[j] = line[i];
			g.feedback[j] = MISS;
			i++;
		}
		j++;
	}g.letters[j] = '\0';
	return g;
}
