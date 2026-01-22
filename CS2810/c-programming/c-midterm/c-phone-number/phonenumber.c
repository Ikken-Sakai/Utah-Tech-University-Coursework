#include "phonenumber.h"
#include <stdio.h>
#include <ctype.h>

void format_phone_number(char *line) {
	int count;
	char area[2] = {0};
	char last[3] = {0};

	count = 0;
	while (line[count] != '\0'){
		if (isdigit(line[count]) && isdigit(line[count+1]) && isdigit(line[count+2])){
			area[0] = line[count];
			area[1] = line[count + 1];
			area[2] = line[count + 2];
			printf("%c%c%c", area[0], area[1], area[2]);
		}
		else if (isdigit(line[count]) && isdigit(line[count+1]) && isdigit(line[count+2]) && isdigit(line[count+3])){
			last[0] = line[count];
			last[1] = line[count+1];
			last[2] = line[count+2];
			last[3] = line[count+3];
			printf("%c%c%c%c", last[0], last[1], last[2], last[3]);
		}
	count ++;
	}
}
