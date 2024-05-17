# Trabajo Práctico 3: Modo Protegido

Este trabajo fue realizado por los alumnos:

- Dalla Fontana, Facundo
- Gallardo, Nicolas
- Villar, Federico Ignacio

## Teorico

### UEFI

UEFI (Interfaz de Firmware Extensible Unificada) es una especificación de firmware de computadora que reemplaza al tradicional BIOS (Sistema Básico de Entrada/Salida) en las computadoras actuales. Proporciona una interfaz entre el sistema operativo y el firmware de la computadora, permitiendo un arranque más rápido, una mayor seguridad y una mejor gestión de los dispositivos de hardware.

Para utilizar UEFI, generalmente se necesita acceder a la configuración del firmware de la computadora durante el arranque. Esto se hace típicamente presionando una tecla específica (como F2, F10, Esc o Del) justo después de encender o reiniciar la misma. Desde la interfaz de configuración de UEFI, puedes realizar varias acciones, como configurar la secuencia de arranque, ajustar la configuración del hardware y habilitar o deshabilitar características como Secure Boot.

Una función a la que se podría llamar usando la dinámica de UEFI es la de configurar el Secure Boot. Esta función permite al usuario habilitar o deshabilitar Secure Boot, así como gestionar las claves de arranque seguro que se utilizan para verificar la autenticidad de los componentes del sistema operativo durante el proceso de arranque.

### Bug en UEFI: vulnerabilidades en el firmware UEFI de Lenovo

#### Resumen

Lenovo ha emitido un aviso de seguridad sobre tres vulnerabilidades críticas que afectan el firmware UEFI de más de 100 modelos de sus portátiles. Estas vulnerabilidades permiten a los atacantes desactivar la protección de la memoria flash SPI y desactivar la función Secure Boot, además de ejecutar código arbitrario con privilegios elevados. Los investigadores de ESET descubrieron estos fallos y los reportaron a Lenovo en octubre del año pasado. Las vulnerabilidades afectan a modelos como IdeaPad 3, Legion 5 Pro-16ACH6 H y Yoga Slim 9-14ITL05, poniendo en riesgo potencialmente a millones de usuarios.

#### Descripcion de las vulnerabilidades

- **CVE-2021-3971**: un controlador usado en procesos de fabricación antiguos se incluyó erróneamente en la imagen del BIOS. Permite a un atacante con privilegios elevados modificar la región de protección del firmware mediante la modificación de una variable NVRAM.
- **CVE-2021-3972**: un controlador utilizado en el proceso de fabricación no fue desactivado correctamente. Esto permite a un atacante con privilegios elevados modificar la configuración de Secure Boot mediante la modificación de una variable NVRAM.
- **CVE-2021-3970**: permite a un atacante local ejecutar código arbitrario con privilegios elevados.

#### Impacto y riesgos

Las dos primeras vulnerabilidades relacionadas con UEFI (CVE-2021-3971 y CVE-2021-3972) permiten a los atacantes desplegar implantes en la memoria flash SPI o en la ESP, lo que los hace extremadamente peligrosos y difíciles de detectar. Estos implantes pueden ejecutarse tempranamente en el proceso de arranque, antes de que el sistema operativo tome control, evadiendo así la mayoría de las soluciones de seguridad.

#### Historia de amenazas en UEFI

ESET (empresa de seguridad informatica, desarrolladora de soluciones de software de seguridad) identifico dos implantes UEFI en el pasado:

- **Lojax**: descubierto en 2018, usado por actores respaldados por el gobierno ruso.
- **ESPecter**: identificado en 2021, activo desde 2012 como bootkit para sistemas basados en BIOS.

Otros actores de seguridad sencontraron amenazas similares, como:

- **MosaicRegressor** (Kaspersky, 2020)
- **FinSpy** (Kaspersky, 2021)
- **MoonBounce** (Kaspersky, 2022)

#### Medidas de mitigacion

Lenovo recomienda actualizar el firmware del sistema a la versión más reciente para protegerse contra estas vulnerabilidades. Las actualizaciones pueden realizarse manualmente desde la página de soporte del dispositivo o mediante utilidades proporcionadas por la compañía para la actualización de controladores del sistema.

### Intel Converged Security and Management Engine (CSME)

Intel® CSME es un subsistema embebido y dispositivo PCIe que actúa como controlador de seguridad y gestión dentro del PCH. Está diseñado para operar en un entorno aislado del software principal del sistema, como el BIOS, el sistema operativo y las aplicaciones. Accede a interfaces limitadas como GPIO y LAN/WLAN para sus funciones, y su firmware y configuración se almacenan en memoria NVRAM, típicamente en memoria flash en el bus SPI.

ntel® CSME está presente en la mayoría de las plataformas de Intel, incluyendo sistemas de consumo y comerciales para clientes, estaciones de trabajo, servidores y productos de IoT (Internet de las Cosas). Para la seguridad basada en hardware, usuarios como proveedores de contenido u organizaciones de TI (Tecnología de la Información) pueden gestionar, por ejemplo, la gestión de derechos digitales (DRM) y la Tecnología de Gestión Activa de Intel® (Intel® AMT), la cual requiere que la seguridad a nivel de hardware esté disponible cuando el sistema anfitrión no responde o está apagado.

La siguiente imagen ilustra la ubicacion de CSME en el sistema.

<img src="../assets/csme_system.png" alt="CSME in the System">


