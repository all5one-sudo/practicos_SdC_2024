#include <linux/init.h>
#include <linux/module.h>
#include <linux/kernel.h>
#include <linux/utsname.h>

MODULE_LICENSE("GPL");
MODULE_AUTHOR("Facundo Dalla Fontana - Nicolas Gallardo - Villar Federico");
MODULE_DESCRIPTION("Un simple módulo de kernel que imprime el nombre del equipo.");

static int __init mymodule_init(void) {
    struct new_utsname *u = init_utsname();
    printk(KERN_INFO "Equipo: %s\n", u->nodename);
    return 0;
}

static void __exit mymodule_exit(void) {
    printk(KERN_INFO "Módulo descargado\n");
}

module_init(mymodule_init);
module_exit(mymodule_exit);
