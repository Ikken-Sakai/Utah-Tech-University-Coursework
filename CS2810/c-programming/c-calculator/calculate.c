#include <stdio.h>

void calculate(char *line){
	int a, b, n;
	char nl;
	n = sscanf(line, "What is %d added to %d?%c", &a, &b, &nl);

	if (n == 3){
		if (nl =='\n') {
			printf("%d + %d = %d\n", a, b, a+b);
			return;
		}
	}
		
	n = sscanf(line, "What is %d subtracted from %d?%c", &a, &b, &nl);

	if (n == 3){
		if (nl =='\n') {
			printf("%d - %d = %d\n", b, a, b-a);
			return;
		}
	}

	n = sscanf(line, "What is %d times %d?%c", &a, &b, &nl);

	if (n == 3){
		if (nl =='\n') {
			printf("%d * %d = %d\n", a, b, a*b);
			return;
		}
	}

	n = sscanf(line, "What is %d divided by %d?%c", &a, &b, &nl);

	if (n == 3){
		if (nl =='\n') {
			if (b != 0){
				printf("%d / %d = %d\n", a, b, a/b);
				return;
			}else{
				printf("Division by zero is undefined\n");
				return;
			}
		}
	}

	n = sscanf(line, "What is the remainder of %d divided by %d?%c", &a, &b, &nl);

	if (n == 3){
		if (nl =='\n') {
			if (b != 0){
				printf("%d %% %d = %d\n", a, b, a%b);
				return;
			}else{
				printf("Division by zero is undefined\n");
				return;
			}
		}
	}

	n = sscanf(line, "What is %d negated?%c", &a, &nl);

	if (n == 2){
		if (nl =='\n') {
			printf("-(%d) = %d\n", a, -1*a);
			return;
		}
	}

	n = sscanf(line, "What is %d squared?%c", &a, &nl);

	if (n == 2){
		if (nl =='\n') {
			printf("(%d)^2 = %d\n", a, a*a);
			return;
		}
	}

	n = sscanf(line, "Which is larger: %d or %d?%c", &a, &b, &nl);

	if (n == 3){
		if (nl =='\n') {
			if (a>b){
				printf("%d is larger than %d\n", a, b);
				return;
			}else if (b>a){
				printf("%d is larger than %d\n", b, a);
				return;
			}else{
				printf("Both values are the same\n");
				return;
			}
		}
	}

	printf("I do not understand the question, sorry!\n");

}
