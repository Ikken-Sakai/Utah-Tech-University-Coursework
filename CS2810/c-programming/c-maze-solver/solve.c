#include <stdio.h>
#include <stdbool.h>
#include "solve.h"


void print_maze(char field[SIZE_Y][SIZE_X]){
	int i, j;
	for (i = 0; i<SIZE_Y; i++){
		for(j=0; j<SIZE_X; j++){
			printf("%c", field[i][j]);
		}
		printf("\n");
	}
}
void solve_maze(char field[SIZE_Y][SIZE_X]){
	int x, y;
	bool done = false;
	while (!done){
		done = true;
		for (x = 1; x<SIZE_X-1; x++){
			for (y = 1; y<SIZE_Y-1; y++){
				if(field[y][x] != '@'){
					int count = 0;
					if(field[y + 1][x] == '@'){
						count += 1;
					}
					if(field[y][x+1] == '@'){
						count += 1;
					}
					if(field[y-1][x] == '@'){
						count += 1;
					}
					if(field[y][x-1]=='@'){
						count += 1;
					}
					if(count == 3){
						field[y][x] = '@';
						done = false;
					}
				}
			}
		}
	}return;
}
