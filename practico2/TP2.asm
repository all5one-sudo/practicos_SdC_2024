section .data
    num dd 0

global _float_2_int
section .text

_float_2_int:
    push ebp
    mov ebp, esp
    fld dword [ebp + 8]
    fistp dword [num]
    mov eax, [num]
    add eax, 1
    mov [num], eax
    mov esp, ebp
    pop ebp
    ret

; para compilar nasm -f elf32 TP2.asm
