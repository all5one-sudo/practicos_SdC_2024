#include <stdio.h>

extern int _float_2_int(float data);

int process_data(float data) {
    // return (int) (data+1);
    return _float_2_int(data);
}

int main() {
    return 0;
}

// gcc -shared -W -m32 -o TP2_asm_lib TP2.c TP2.o
