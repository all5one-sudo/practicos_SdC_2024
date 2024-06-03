.equ CODE_SEGMENT, gdt_code - gdt_start
.equ DATA_SEGMENT, gdt_data - gdt_start

/* Entrada al modo protegido */
.code16
switch_to_protected_mode:
    cli                                   /* Paso 0. Deshabilitar interrupciones */
    lgdt gdt_descriptor                   /* Paso 1. Cargar la Tabla de Descriptores Global (GDT) */
    
    /* Paso 2. Cargar el Registro de Control CR0 y establecer el bit de Habilitación de Protección (PE) en 1 */
    mov %cr0, %eax
    orl $0x1, %eax
    mov %eax, %cr0
    
    /* Paso 3. Saltar a la sección de código de 32 bits */
    ljmp $CODE_SEGMENT, $protected_mode


/* Tabla de Descriptores Global (GDT) */
gdt_start:
    /* Descriptor nulo */
    gdt_null:
        .long 0x0                         /* Descriptor de segmento nulo - límite */
        .long 0x0                         /* Dirección base */

    /* Descriptor de código */
    gdt_code:
        .word 0xffff                      /* Límite del segmento (16 bits inferiores) */
        .word 0x0                         /* Dirección base (16 bits inferiores) */
        .byte 0x0                         /* Dirección base (8 bits medios) */
        .byte 0b10011010                  /* Flags: Presente, Nivel de Privilegio 0, Segmento de Código, Ejecutable, Legible */
        .byte 0b11001111                  /* Flags: Granularidad (4KB), Modo de 32 bits, Límite (4 bits superiores) */
        .byte 0x0                         /* Dirección base (8 bits superiores) */

    /* Descriptor de datos (lectura solamente) */
    gdt_data:
        .word 0xffff                      /* Límite del segmento (16 bits inferiores) */
        .word 0x0                         /* Dirección base (16 bits inferiores) */
        .byte 0x0                         /* Dirección base (8 bits medios) */
        .byte 0b10010000                  /* Flags: Presente, Nivel de Privilegio 0, Segmento de Datos, Legible */
        .byte 0b11001111                  /* Flags: Granularidad (4KB), Modo de 32 bits, Límite (4 bits superiores) */
        .byte 0x0                         /* Dirección base (8 bits superiores) */

    gdt_end:

    /* Descriptor de GDT */
    gdt_descriptor:
        .word gdt_end - gdt_start - 1     /* Límite de GDT (tamaño - 1) */
        .long gdt_start                   /* Dirección base de GDT */


/* Inicialización del modo protegido */
.code32
protected_mode:
    /* Inicializar registros y puntero de pila */
    mov $DATA_SEGMENT, %ax
    mov %ax, %ds
    mov %ax, %es
    mov %ax, %fs
    mov %ax, %gs
    mov %ax, %ss
    mov $0x7000, %ebp
    mov %ebp, %esp

    mov $0x7000, %ebp
    mov %ebp, %esp
    
    /* Saltar a la función de comprobación del modo protegido */
    jmp check_protected_mode


/* Comprobar si está en modo protegido e imprimir mensaje */
check_protected_mode:
    mov %cr0, %eax                        /* Cargar Registro de Control CR0 */
    test $0x1, %eax                       /* Probar el bit PE (bit 0) */
    jnz protected_mode_detected           /* Saltar si el bit PE está establecido (en modo protegido) */
    jmp not_in_protected_mode
protected_mode_detected:
    /* El procesador está en modo protegido */
    call print_message
    jmp continue_execution
not_in_protected_mode:
    /* El procesador no está en modo protegido */
    hlt
continue_execution:
    /* Continuar con la ejecución del programa */
    hlt


/* Imprimir mensaje en VGA */
print_message:
    mov $message, %ecx                    /* Cargar la dirección del mensaje en ECX */
    mov vga, %eax                         /* Cargar la dirección del búfer VGA en EAX */
    
    /* Calcular dirección de memoria VGA */
    mov $160, %edx
    mul %edx
    lea 0xb8000(%eax), %edx
    mov $0x0f, %ah 
loop:
    mov (%ecx), %al                       /* Cargar el siguiente byte del mensaje en AL */
    cmp $0, %al                           /* Comprobar si hemos llegado al final del mensaje */
    je end
    
    mov %ax, (%edx)                       /* Escribir el carácter en el búfer VGA */
    
    /* Mover al siguiente carácter en el mensaje y en el búfer VGA */
    add $1, %ecx
    add $2, %edx
    jmp loop
end:
    ret

/* Mensaje a imprimir en VGA */
message:
    .asciz "Estamos en modo protegido gente."

/* Dirección del búfer VGA */
vga:
    .long 10
