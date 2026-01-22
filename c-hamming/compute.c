#include "compute.h"
#include <string.h>
#include <stddef.h>

int compute(char *a, char *b){
    int dif_count = 0;
    int i = 0;
    int n = strlen(a);
    int g = strlen(b);
    if (n!=g) return -1;
    while(a[i]!=0 && b[i]!=0){
        if (a[i]!=b[i]) dif_count+=1;
        i++;
    }
    return dif_count;
}
