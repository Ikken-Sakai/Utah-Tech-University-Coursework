#include <assert.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

#define MAX_N 10000
void sieve(bool *array, int size){
	for (int i=2; i<size; i++){
		array[i] = true;
	}

	for (int i=2; i*i<=size; i++){
		if(array[i]){
			for (int j=i*2; j<=size; j=j+i){
				array[j]=false;
			}
		}

	}
}
