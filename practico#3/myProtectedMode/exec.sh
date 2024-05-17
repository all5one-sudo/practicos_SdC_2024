as -g -o main.o protectedMode_v2.S # se crea el ejecutable
ld --oformat binary -o main.img -T linker.ld main.o # se linkea
hyper -- qemu-system-i386 -fda main.img -boot a -s -S -monitor stdio # se lanza la vm con qemu
hyper -- gdb -x gdb.gdb # se lanza la sesion de gdb con sus breakpoints ya definidos en otra venta del terminal
