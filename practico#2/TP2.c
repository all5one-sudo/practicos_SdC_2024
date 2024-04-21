#include <stdio.h>
#include <stdlib.h>

extern int float_2_int(float data);

int process_data(float data) {
    // return (int) (data+1);
    return float_2_int(data);
}

int main() {
    return 0;
}

// para compilar: gcc -m32 -o convert TP2.c TP2.o
