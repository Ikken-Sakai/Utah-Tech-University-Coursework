#include <stdio.h>

void print_diamond(int n){
	for(int i=1;i<=n;i++){
		for(int j=1;j<=n-i;j++){
			printf(" ");
		}
		for (int j=1;j<=i*2-1;j++){
			printf("*");
		}
		printf("\n");
	}

	for(int i=n-1;i>0;i--){
		for(int j=1;j<=n-i;j++){
			printf(" ");
		}
		for(int j=1;j<=i*2-1;j++){
			printf("*");
		}
		printf("\n");
	}

}
