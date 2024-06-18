### Firma de un modulo de kernel

#### Creacion del modulo del kernel

Se usa el archivo:

```c
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
```

Las herramientas necesarias para trabajar se pueden instalar con:

```
sudo apt update
sudo apt install build-essential linux-headers-$(uname -r)
```

Se crea un `makefile` con las siguientes instrucciones:

```
obj-m += myModule.o

all:
	make -C /lib/modules/$(shell uname -r)/build M=$(PWD) modules

clean:
	make -C /lib/modules/$(shell uname -r)/build M=$(PWD) clean
```

Ahora se lo compila con `make`, obteniendose la siguiente salida:

<img src='./assets/make_mod.png'>

Se procede ahora a generar las claves de firma. Primero una clave privada y un certificado X.509.

```
openssl req -new -x509 -newkey rsa:2048 -keyout MOK.priv -outform DER -out MOK.der -nodes -days 36500 -subj "/CN=myKernelModule/"
```

Ahora hay que importar la clave con:

```
sudo mokutil --import MOK.der
```

<img src='./assets/firm_sec.png'>

Puede verse que el Secure Boot no esta habilitado, esto es comun porque se esta trabajando en un sistema linux virtualizado. Esto significa que tecnicamente no es necesario firmar el modulo. Por lo tanto, se procede a llamar a `insmod`, obteniendose el siguiente mensaje desde `dmesg` (tail):

```
[    1.985585] audit: type=1400 audit(1718721706.252:10): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/lib/NetworkManager/nm-dhcp-helper" pid=428 comm="apparmor_parser"
[    2.212808] NET: Registered PF_QIPCRTR protocol family
[   14.214779] rfkill: input handler disabled
[   14.572739] input: spice vdagent tablet as /devices/virtual/input/input3
[   20.444800] rfkill: input handler enabled
[   21.157946] rfkill: input handler disabled
[   21.907784] input: spice vdagent tablet as /devices/virtual/input/input4
[  771.028068] myModule: loading out-of-tree module taints kernel.
[  771.028552] myModule: module verification failed: signature and/or required key missing - tainting kernel
[  771.029886] Equipo: debian
```

Puede verse que el modulo se carga correctamente. Finalmente, se procede a descargar el modulo con `rmmod`. Se tiene la siguiente salida.

```
[    2.212808] NET: Registered PF_QIPCRTR protocol family
[   14.214779] rfkill: input handler disabled
[   14.572739] input: spice vdagent tablet as /devices/virtual/input/input3
[   20.444800] rfkill: input handler enabled
[   21.157946] rfkill: input handler disabled
[   21.907784] input: spice vdagent tablet as /devices/virtual/input/input4
[  771.028068] myModule: loading out-of-tree module taints kernel.
[  771.028552] myModule: module verification failed: signature and/or required key missing - tainting kernel
[  771.029886] Equipo: debian
[  897.137815] Módulo descargado
```

De esta forma, puede comprobarse el proceso completo.

Ahora, si un colega tiene Secure Boot habilitado en su sistema, cualquier modulo de kernel que intente cargar debe estar firmado con una clave que su sistema reconozca como valida. Como mi firma no estaria verificada, el sistema rechazaria la carga del modulo.




