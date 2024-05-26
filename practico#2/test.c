#include "stdio.h"

extern int _float_2_int (float num);

int main() {

    float num = 43.12;
    int int_num = _float_2_int(num);
    printf("%d\n",int_num);
    return 0;
}

// para compilar gcc -m32 -o convert test.c TP2.o