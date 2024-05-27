#include "stdio.h"

extern int _float_2_int (float num);

int main() {

    float num = 43.12;
    int int_num = _float_2_int(num);
    printf("%d\n",int_num);
    return 0;
}

// para compilar gcc -m32 -o -g convert test.c TP2.o

/*

nasm -f elf32 -o TP2.o TP2.asm
gcc -g -m32 -c -o test.o test.c
gcc -g -m32 -o convert test.o TP2.o

*/