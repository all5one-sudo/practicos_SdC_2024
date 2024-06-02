# Trabajo Practico 5: Modulos de Kernel

## Preparacion

Para este trabajo, se usa un SO Debian, virtualizado en una MacBook Air M1, las caracteristicas principales del computador se listan a continuacion en la captura de pantalla de `neofetch`.

<img src="./assets/neofetch.png">

Se hace fork de un repositorio de GitLab, luego se lo clona, y se lo inserta como submodulo al repositorio actual, cargado en GitHub. Ademas, se instalan las siguientes dependencias:

```bash
sudo apt-get install build-essential checkinstall 
```

## Primera parte

Para esta primera parte, al navegar a la carpeta `module`, se debe instanciar el modulo propuesto, y para ello se corre el siguiente comando:

```bash
sudo insmod mimodulo.ko
```

Y luego, al ejecutar `sudo dmesg > dmesg_output.txt` se obtiene lo siguiente:

```bash
[    0.000000] Booting Linux on physical CPU 0x0000000000 [0x610f0000]
[    0.000000] Linux version 6.1.0-21-arm64 (debian-kernel@lists.debian.org) (gcc-12 (Debian 12.2.0-14) 12.2.0, GNU ld (GNU Binutils for Debian) 2.40) #1 SMP Debian 6.1.90-1 (2024-05-03)
[    0.000000] efi: EFI v2.70 by EDK II
[    0.000000] efi: ACPI 2.0=0x16fc90018 SMBIOS=0xfffff000 SMBIOS 3.0=0x16fcb4000 MOKvar=0x16fc40000 MEMRESERVE=0x16e572798
[    0.000000] secureboot: Secure boot disabled
[    0.000000] ACPI: Early table checksum verification disabled
[    0.000000] ACPI: RSDP 0x000000016FC90018 000024 (v02 APPLE )
[    0.000000] ACPI: XSDT 0x000000016FC9FE98 000044 (v01 APPLE  Apple Vz 00000001      01000013)
[    0.000000] ACPI: FACP 0x000000016FC9FA98 000114 (v06 APPLE  Apple Vz 00000001 AAPL 20180427)
[    0.000000] ACPI: DSDT 0x000000016FC9F698 000394 (v02 APPLE  Apple Vz 00000001 AAPL 20180427)
[    0.000000] ACPI: GTDT 0x000000016FC9FC18 000068 (v03 APPLE  Apple Vz 00000001 AAPL 20180427)
[    0.000000] ACPI: APIC 0x000000016FC9E998 0001AC (v05 APPLE  Apple Vz 00000001 AAPL 20180427)
[    0.000000] ACPI: MCFG 0x000000016FC9FF98 00003C (v01 APPLE  Apple Vz 00000001 AAPL 20180427)
[    0.000000] NUMA: Failed to initialise from firmware
[    0.000000] NUMA: Faking a node at [mem 0x0000000070000000-0x000000016fffffff]
[    0.000000] NUMA: NODE_DATA [mem 0x16f713380-0x16f715fff]
[    0.000000] Zone ranges:
[    0.000000]   DMA      [mem 0x0000000070000000-0x00000000ffffffff]
[    0.000000]   DMA32    empty
[    0.000000]   Normal   [mem 0x0000000100000000-0x000000016fffffff]
[    0.000000] Movable zone start for each node
[    0.000000] Early memory node ranges
[    0.000000]   node   0: [mem 0x0000000070000000-0x00000000ffffdfff]
[    0.000000]   node   0: [mem 0x00000000ffffe000-0x00000000ffffffff]
[    0.000000]   node   0: [mem 0x0000000100000000-0x000000016e64ffff]
[    0.000000]   node   0: [mem 0x000000016e650000-0x000000016e79ffff]
[    0.000000]   node   0: [mem 0x000000016e7a0000-0x000000016fb9ffff]
[    0.000000]   node   0: [mem 0x000000016fba0000-0x000000016fc2ffff]
[    0.000000]   node   0: [mem 0x000000016fc30000-0x000000016fc3ffff]
[    0.000000]   node   0: [mem 0x000000016fc40000-0x000000016fc7ffff]
[    0.000000]   node   0: [mem 0x000000016fc80000-0x000000016fcb2fff]
[    0.000000]   node   0: [mem 0x000000016fcb3000-0x000000016fcb4fff]
[    0.000000]   node   0: [mem 0x000000016fcb5000-0x000000016fffffff]
[    0.000000] Initmem setup node 0 [mem 0x0000000070000000-0x000000016fffffff]
[    0.000000] cma: Reserved 64 MiB at 0x00000000fbe00000
[    0.000000] psci: probing for conduit method from ACPI.
[    0.000000] psci: PSCIv1.1 detected in firmware.
[    0.000000] psci: Using standard PSCI v0.2 function IDs
[    0.000000] psci: Trusted OS migration not required
[    0.000000] psci: SMC Calling Convention v1.0
[    0.000000] percpu: Embedded 31 pages/cpu s86632 r8192 d32152 u126976
[    0.000000] pcpu-alloc: s86632 r8192 d32152 u126976 alloc=31*4096
[    0.000000] pcpu-alloc: [0] 0 [0] 1 [0] 2 [0] 3
[    0.000000] Detected PIPT I-cache on CPU0
[    0.000000] CPU features: detected: Address authentication (IMP DEF algorithm)
[    0.000000] CPU features: detected: GIC system register CPU interface
[    0.000000] CPU features: detected: Spectre-v4
[    0.000000] alternatives: applying boot alternatives
[    0.000000] Fallback order for Node 0: 0
[    0.000000] Built 1 zonelists, mobility grouping on.  Total pages: 1032192
[    0.000000] Policy zone: Normal
[    0.000000] Kernel command line: BOOT_IMAGE=/boot/vmlinuz-6.1.0-21-arm64 root=UUID=8886428d-e9f6-4f33-883f-467ee75a767e ro quiet
[    0.000000] Unknown kernel command line parameters "BOOT_IMAGE=/boot/vmlinuz-6.1.0-21-arm64", will be passed to user space.
[    0.000000] Dentry cache hash table entries: 524288 (order: 10, 4194304 bytes, linear)
[    0.000000] Inode-cache hash table entries: 262144 (order: 9, 2097152 bytes, linear)
[    0.000000] mem auto-init: stack:all(zero), heap alloc:on, heap free:off
[    0.000000] software IO TLB: area num 4.
[    0.000000] software IO TLB: mapped [mem 0x00000000f7e00000-0x00000000fbe00000] (64MB)
[    0.000000] Memory: 2359288K/4194304K available (13056K kernel code, 2800K rwdata, 9452K rodata, 6464K init, 626K bss, 227036K reserved, 65536K cma-reserved)
[    0.000000] SLUB: HWalign=64, Order=0-3, MinObjects=0, CPUs=4, Nodes=1
[    0.000000] ftrace: allocating 43954 entries in 172 pages
[    0.000000] ftrace: allocated 172 pages with 4 groups
[    0.000000] trace event string verifier disabled
[    0.000000] rcu: Hierarchical RCU implementation.
[    0.000000] rcu: 	RCU restricting CPUs from NR_CPUS=256 to nr_cpu_ids=4.
[    0.000000] 	Rude variant of Tasks RCU enabled.
[    0.000000] 	Tracing variant of Tasks RCU enabled.
[    0.000000] rcu: RCU calculated value of scheduler-enlistment delay is 25 jiffies.
[    0.000000] rcu: Adjusting geometry for rcu_fanout_leaf=16, nr_cpu_ids=4
[    0.000000] NR_IRQS: 64, nr_irqs: 64, preallocated irqs: 0
[    0.000000] GICv3: 224 SPIs implemented
[    0.000000] GICv3: 0 Extended SPIs implemented
[    0.000000] Root IRQ handler: gic_handle_irq
[    0.000000] GICv3: GICv3 features: 16 PPIs, RSS
[    0.000000] GICv3: CPU0: found redistributor 0 region 0:0x0000000010010000
[    0.000000] GICv2m: range[mem 0x1fff0000-0x1fff0fff], SPI[128:255]
[    0.000000] rcu: srcu_init: Setting srcu_struct sizes based on contention.
[    0.000000] arch_timer: cp15 timer(s) running at 24.00MHz (virt).
[    0.000000] clocksource: arch_sys_counter: mask: 0xffffffffffffff max_cycles: 0x588fe9dc0, max_idle_ns: 440795202592 ns
[    0.000000] sched_clock: 56 bits at 24MHz, resolution 41ns, wraps every 4398046511097ns
[    0.000025] Console: colour dummy device 80x25
[    0.000030] printk: console [tty0] enabled
[    0.000052] ACPI: Core revision 20220331
[    0.000082] Calibrating delay loop (skipped), value calculated using timer frequency.. 48.00 BogoMIPS (lpj=96000)
[    0.000083] pid_max: default: 32768 minimum: 301
[    0.000118] LSM: Security Framework initializing
[    0.000125] landlock: Up and running.
[    0.000126] Yama: disabled by default; enable with sysctl kernel.yama.*
[    0.000147] AppArmor: AppArmor initialized
[    0.000148] TOMOYO Linux initialized
[    0.000154] LSM support for eBPF active
[    0.000192] Mount-cache hash table entries: 8192 (order: 4, 65536 bytes, linear)
[    0.000208] Mountpoint-cache hash table entries: 8192 (order: 4, 65536 bytes, linear)
[    0.000457] ACPI PPTT: No PPTT table found, CPU and cache topology may be inaccurate
[    0.000616] cblist_init_generic: Setting adjustable number of callback queues.
[    0.000617] cblist_init_generic: Setting shift to 2 and lim to 1.
[    0.000627] cblist_init_generic: Setting adjustable number of callback queues.
[    0.000627] cblist_init_generic: Setting shift to 2 and lim to 1.
[    0.000652] rcu: Hierarchical SRCU implementation.
[    0.000653] rcu: 	Max phase no-delay instances is 1000.
[    0.000860] Remapping and enabling EFI services.
[    0.000971] smp: Bringing up secondary CPUs ...
[    0.001147] Detected PIPT I-cache on CPU1
[    0.001162] GICv3: CPU1: found redistributor 1 region 0:0x0000000010030000
[    0.001216] CPU1: Booted secondary processor 0x0000000001 [0x610f0000]
[    0.001455] Detected PIPT I-cache on CPU2
[    0.001469] GICv3: CPU2: found redistributor 2 region 0:0x0000000010050000
[    0.001523] CPU2: Booted secondary processor 0x0000000002 [0x610f0000]
[    0.001718] Detected PIPT I-cache on CPU3
[    0.001733] GICv3: CPU3: found redistributor 3 region 0:0x0000000010070000
[    0.001786] CPU3: Booted secondary processor 0x0000000003 [0x610f0000]
[    0.001833] smp: Brought up 1 node, 4 CPUs
[    0.001834] SMP: Total of 4 processors activated.
[    0.001835] CPU features: detected: ARMv8.4 Translation Table Level
[    0.001836] CPU features: detected: Data cache clean to the PoU not required for I/D coherence
[    0.001836] CPU features: detected: Common not Private translations
[    0.001836] CPU features: detected: CRC32 instructions
[    0.001837] CPU features: detected: Data cache clean to Point of Deep Persistence
[    0.001837] CPU features: detected: Data cache clean to Point of Persistence
[    0.001837] CPU features: detected: E0PD
[    0.001838] CPU features: detected: Generic authentication (IMP DEF algorithm)
[    0.001838] CPU features: detected: RCpc load-acquire (LDAPR)
[    0.001838] CPU features: detected: LSE atomic instructions
[    0.001839] CPU features: detected: Privileged Access Never
[    0.001839] CPU features: detected: RAS Extension Support
[    0.001839] CPU features: detected: Speculation barrier (SB)
[    0.001840] CPU features: detected: TLB range maintenance instructions
[    0.001840] CPU features: detected: Speculative Store Bypassing Safe (SSBS)
[    0.001898] CPU: All CPU(s) started at EL1
[    0.001901] alternatives: applying system-wide alternatives
[    0.009052] node 0 deferred pages initialised in 4ms
[    0.010174] devtmpfs: initialized
[    0.010526] Registered cp15_barrier emulation handler
[    0.010527] setend instruction emulation is not supported on this system
[    0.010566] clocksource: jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 7645041785100000 ns
[    0.010582] futex hash table entries: 1024 (order: 4, 65536 bytes, linear)
[    0.010684] pinctrl core: initialized pinctrl subsystem
[    0.010762] SMBIOS 3.3.0 present.
[    0.010764] DMI: Apple Inc. Apple Virtualization Generic Platform, BIOS 2022.100.22.0.0 02/09/2024
[    0.010915] NET: Registered PF_NETLINK/PF_ROUTE protocol family
[    0.011640] DMA: preallocated 512 KiB GFP_KERNEL pool for atomic allocations
[    0.011663] DMA: preallocated 512 KiB GFP_KERNEL|GFP_DMA pool for atomic allocations
[    0.011695] DMA: preallocated 512 KiB GFP_KERNEL|GFP_DMA32 pool for atomic allocations
[    0.011701] audit: initializing netlink subsys (disabled)
[    0.011791] audit: type=2000 audit(0.008:1): state=initialized audit_enabled=0 res=1
[    0.011847] thermal_sys: Registered thermal governor 'fair_share'
[    0.011847] thermal_sys: Registered thermal governor 'bang_bang'
[    0.011848] thermal_sys: Registered thermal governor 'step_wise'
[    0.011848] thermal_sys: Registered thermal governor 'user_space'
[    0.011848] thermal_sys: Registered thermal governor 'power_allocator'
[    0.011853] cpuidle: using governor ladder
[    0.011854] cpuidle: using governor menu
[    0.011869] hw-breakpoint: found 6 breakpoint and 4 watchpoint registers.
[    0.011945] ASID allocator initialised with 256 entries
[    0.011967] acpiphp: ACPI Hot Plug PCI Controller Driver version: 0.5
[    0.012034] Serial: AMBA PL011 UART driver
[    0.012087] KASLR enabled
[    0.012835] HugeTLB: registered 1.00 GiB page size, pre-allocated 0 pages
[    0.012836] HugeTLB: 0 KiB vmemmap can be freed for a 1.00 GiB page
[    0.012837] HugeTLB: registered 32.0 MiB page size, pre-allocated 0 pages
[    0.012837] HugeTLB: 0 KiB vmemmap can be freed for a 32.0 MiB page
[    0.012838] HugeTLB: registered 2.00 MiB page size, pre-allocated 0 pages
[    0.012838] HugeTLB: 0 KiB vmemmap can be freed for a 2.00 MiB page
[    0.012838] HugeTLB: registered 64.0 KiB page size, pre-allocated 0 pages
[    0.012838] HugeTLB: 0 KiB vmemmap can be freed for a 64.0 KiB page
[    0.013405] ACPI: Added _OSI(Module Device)
[    0.013406] ACPI: Added _OSI(Processor Device)
[    0.013406] ACPI: Added _OSI(3.0 _SCP Extensions)
[    0.013407] ACPI: Added _OSI(Processor Aggregator Device)
[    0.013481] ACPI: 1 ACPI AML tables successfully acquired and loaded
[    0.013570] ACPI: Interpreter enabled
[    0.013571] ACPI: Using GIC for interrupt routing
[    0.013575] ACPI: MCFG table detected, 1 entries
[    0.013784] ACPI: PCI Root Bridge [PCI0] (domain 0000 [bus 00-ff])
[    0.013787] acpi PNP0A08:00: _OSC: OS supports [ExtendedConfig ASPM ClockPM Segments MSI HPX-Type3]
[    0.013789] acpi PNP0A08:00: _OSC: OS requested [PCIeHotplug SHPCHotplug PME AER PCIeCapability LTR]
[    0.013790] acpi PNP0A08:00: _OSC: platform willing to grant [PCIeHotplug SHPCHotplug PME AER PCIeCapability LTR]
[    0.013790] acpi PNP0A08:00: _OSC: platform retains control of PCIe features (AE_NOT_FOUND)
[    0.013797] acpi PNP0A08:00: ECAM area [mem 0x40000000-0x4fffffff] reserved by PNP0C02:00
[    0.013802] acpi PNP0A08:00: ECAM at [mem 0x40000000-0x4fffffff] for [bus 00-ff]
[    0.013806] ACPI: Remapped I/O 0x000000006fff0000 to [io  0x0000-0xffff window]
[    0.013823] PCI host bridge to bus 0000:00
[    0.013824] pci_bus 0000:00: root bus resource [mem 0x50000000-0x6ffdffff window]
[    0.013824] pci_bus 0000:00: root bus resource [mem 0x180000000-0x1bfffffff window]
[    0.013825] pci_bus 0000:00: root bus resource [io  0x0000-0xffff window]
[    0.013826] pci_bus 0000:00: root bus resource [bus 00-ff]
[    0.013843] pci 0000:00:00.0: [106b:1a05] type 00 class 0x060000
[    0.013975] pci 0000:00:01.0: [1af4:1041] type 00 class 0x020000
[    0.014008] pci 0000:00:01.0: reg 0x10: [mem 0x180020000-0x180023fff 64bit]
[    0.014022] pci 0000:00:01.0: reg 0x18: [mem 0x5000a000-0x5000a03f]
[    0.014201] pci 0000:00:05.0: [1af4:1042] type 00 class 0x018000
[    0.014229] pci 0000:00:05.0: reg 0x10: [mem 0x18001c000-0x18001ffff 64bit]
[    0.014242] pci 0000:00:05.0: reg 0x18: [mem 0x50009000-0x5000903f]
[    0.014418] pci 0000:00:06.0: [1af4:105a] type 00 class 0x018000
[    0.014446] pci 0000:00:06.0: reg 0x10: [mem 0x180018000-0x18001bfff 64bit]
[    0.014459] pci 0000:00:06.0: reg 0x18: [mem 0x50008000-0x5000803f]
[    0.014628] pci 0000:00:07.0: [1af4:1050] type 00 class 0x038000
[    0.014657] pci 0000:00:07.0: reg 0x10: [mem 0x180014000-0x180017fff 64bit]
[    0.014670] pci 0000:00:07.0: reg 0x18: [mem 0x50007000-0x5000703f]
[    0.014843] pci 0000:00:08.0: [1af4:1059] type 00 class 0x040100
[    0.014870] pci 0000:00:08.0: reg 0x10: [mem 0x180010000-0x180013fff 64bit]
[    0.014882] pci 0000:00:08.0: reg 0x18: [mem 0x50004000-0x5000407f]
[    0.015090] pci 0000:00:09.0: [1af4:1059] type 00 class 0x040100
[    0.015117] pci 0000:00:09.0: reg 0x10: [mem 0x18000c000-0x18000ffff 64bit]
[    0.015130] pci 0000:00:09.0: reg 0x18: [mem 0x50003000-0x5000307f]
[    0.015309] pci 0000:00:0a.0: [1af4:1044] type 00 class 0x100000
[    0.015336] pci 0000:00:0a.0: reg 0x10: [mem 0x180008000-0x18000bfff 64bit]
[    0.015349] pci 0000:00:0a.0: reg 0x18: [mem 0x50006000-0x5000603f]
[    0.015509] pci 0000:00:0b.0: [1af4:1045] type 00 class 0x058000
[    0.015536] pci 0000:00:0b.0: reg 0x10: [mem 0x180004000-0x180007fff 64bit]
[    0.015549] pci 0000:00:0b.0: reg 0x18: [mem 0x50005000-0x5000503f]
[    0.015711] pci 0000:00:0c.0: [1af4:1043] type 00 class 0x078000
[    0.015738] pci 0000:00:0c.0: reg 0x10: [mem 0x180000000-0x180003fff 64bit]
[    0.015751] pci 0000:00:0c.0: reg 0x18: [mem 0x50002000-0x5000207f]
[    0.015904] pci 0000:00:0d.0: [106b:1a06] type 00 class 0x0c0330
[    0.015921] pci 0000:00:0d.0: reg 0x10: [mem 0x50001000-0x50001fff]
[    0.015928] pci 0000:00:0d.0: reg 0x14: [mem 0x50000000-0x500003ff]
[    0.016057] pci 0000:00:01.0: BAR 0: assigned [mem 0x180000000-0x180003fff 64bit]
[    0.016071] pci 0000:00:05.0: BAR 0: assigned [mem 0x180004000-0x180007fff 64bit]
[    0.016084] pci 0000:00:06.0: BAR 0: assigned [mem 0x180008000-0x18000bfff 64bit]
[    0.016097] pci 0000:00:07.0: BAR 0: assigned [mem 0x18000c000-0x18000ffff 64bit]
[    0.016110] pci 0000:00:08.0: BAR 0: assigned [mem 0x180010000-0x180013fff 64bit]
[    0.016123] pci 0000:00:09.0: BAR 0: assigned [mem 0x180014000-0x180017fff 64bit]
[    0.016137] pci 0000:00:0a.0: BAR 0: assigned [mem 0x180018000-0x18001bfff 64bit]
[    0.016150] pci 0000:00:0b.0: BAR 0: assigned [mem 0x18001c000-0x18001ffff 64bit]
[    0.016164] pci 0000:00:0c.0: BAR 0: assigned [mem 0x180020000-0x180023fff 64bit]
[    0.016177] pci 0000:00:0d.0: BAR 0: assigned [mem 0x50000000-0x50000fff]
[    0.016180] pci 0000:00:0d.0: BAR 1: assigned [mem 0x50001000-0x500013ff]
[    0.016184] pci 0000:00:08.0: BAR 2: assigned [mem 0x50001400-0x5000147f]
[    0.016188] pci 0000:00:09.0: BAR 2: assigned [mem 0x50001480-0x500014ff]
[    0.016193] pci 0000:00:0c.0: BAR 2: assigned [mem 0x50001500-0x5000157f]
[    0.016197] pci 0000:00:01.0: BAR 2: assigned [mem 0x50001580-0x500015bf]
[    0.016202] pci 0000:00:05.0: BAR 2: assigned [mem 0x500015c0-0x500015ff]
[    0.016206] pci 0000:00:06.0: BAR 2: assigned [mem 0x50001600-0x5000163f]
[    0.016211] pci 0000:00:07.0: BAR 2: assigned [mem 0x50001640-0x5000167f]
[    0.016215] pci 0000:00:0a.0: BAR 2: assigned [mem 0x50001680-0x500016bf]
[    0.016220] pci 0000:00:0b.0: BAR 2: assigned [mem 0x500016c0-0x500016ff]
[    0.016225] pci_bus 0000:00: resource 4 [mem 0x50000000-0x6ffdffff window]
[    0.016226] pci_bus 0000:00: resource 5 [mem 0x180000000-0x1bfffffff window]
[    0.016227] pci_bus 0000:00: resource 6 [io  0x0000-0xffff window]
[    0.016349] iommu: Default domain type: Translated
[    0.016350] iommu: DMA domain TLB invalidation policy: strict mode
[    0.016394] pps_core: LinuxPPS API ver. 1 registered
[    0.016395] pps_core: Software ver. 5.3.6 - Copyright 2005-2007 Rodolfo Giometti <giometti@linux.it>
[    0.016396] PTP clock support registered
[    0.016404] EDAC MC: Ver: 3.0.0
[    0.016562] Registered efivars operations
[    0.016809] NetLabel: Initializing
[    0.016809] NetLabel:  domain hash size = 128
[    0.016810] NetLabel:  protocols = UNLABELED CIPSOv4 CALIPSO
[    0.016817] NetLabel:  unlabeled traffic allowed by default
[    0.016883] vgaarb: loaded
[    0.017008] clocksource: Switched to clocksource arch_sys_counter
[    0.017109] VFS: Disk quotas dquot_6.6.0
[    0.017116] VFS: Dquot-cache hash table entries: 512 (order 0, 4096 bytes)
[    0.017200] AppArmor: AppArmor Filesystem Enabled
[    0.017205] pnp: PnP ACPI init
[    0.017226] system 00:00: [mem 0x40000000-0x4fffffff] could not be reserved
[    0.017230] pnp: PnP ACPI: found 1 devices
[    0.020276] NET: Registered PF_INET protocol family
[    0.020414] IP idents hash table entries: 65536 (order: 7, 524288 bytes, linear)
[    0.020951] tcp_listen_portaddr_hash hash table entries: 2048 (order: 3, 32768 bytes, linear)
[    0.021037] Table-perturb hash table entries: 65536 (order: 6, 262144 bytes, linear)
[    0.021105] TCP established hash table entries: 32768 (order: 6, 262144 bytes, linear)
[    0.021332] TCP bind hash table entries: 32768 (order: 8, 1048576 bytes, linear)
[    0.021371] TCP: Hash tables configured (established 32768 bind 32768)
[    0.021468] MPTCP token hash table entries: 4096 (order: 4, 98304 bytes, linear)
[    0.021490] UDP hash table entries: 2048 (order: 4, 65536 bytes, linear)
[    0.021509] UDP-Lite hash table entries: 2048 (order: 4, 65536 bytes, linear)
[    0.021534] NET: Registered PF_UNIX/PF_LOCAL protocol family
[    0.021542] NET: Registered PF_XDP protocol family
[    0.021570] pci 0000:00:0d.0: enabling device (0010 -> 0012)
[    0.021606] PCI: CLS 0 bytes, default 64
[    0.021728] Trying to unpack rootfs image as initramfs...
[    0.021760] kvm [1]: HYP mode not available
[    0.022459] Initialise system trusted keyrings
[    0.022469] Key type blacklist registered
[    0.022548] workingset: timestamp_bits=42 max_order=20 bucket_order=0
[    0.023153] zbud: loaded
[    0.023317] integrity: Platform Keyring initialized
[    0.023323] integrity: Machine keyring initialized
[    0.023324] Key type asymmetric registered
[    0.023324] Asymmetric key parser 'x509' registered
[    0.225301] Freeing initrd memory: 45352K
[    0.229371] alg: self-tests for CTR-KDF (hmac(sha256)) passed
[    0.229430] Block layer SCSI generic (bsg) driver version 0.4 loaded (major 247)
[    0.229500] io scheduler mq-deadline registered
[    0.230496] pl061_gpio ARMH0061:00: PL061 GPIO chip registered
[    0.230550] shpchp: Standard Hot Plug PCI Controller Driver version: 0.4
[    0.230604] input: Power Button as /devices/LNXSYSTM:00/PNP0C0C:00/input/input0
[    0.230611] ACPI: button: Power Button [PWRB]
[    0.230957] Serial: 8250/16550 driver, 4 ports, IRQ sharing enabled
[    0.231194] Serial: AMBA driver
[    0.231196] SuperH (H)SCI(F) driver initialized
[    0.231206] msm_serial: driver initialized
[    0.231408] mousedev: PS/2 mouse device common for all mice
[    0.231581] rtc-efi rtc-efi.0: registered as rtc0
[    0.231611] rtc-efi rtc-efi.0: setting system clock to 2024-06-02T18:45:13 UTC (1717353913)
[    0.231756] ledtrig-cpu: registered to indicate activity on CPUs
[    0.237868] NET: Registered PF_INET6 protocol family
[    0.240156] Segment Routing with IPv6
[    0.240164] In-situ OAM (IOAM) with IPv6
[    0.240173] mip6: Mobile IPv6
[    0.240175] NET: Registered PF_PACKET protocol family
[    0.240223] mpls_gso: MPLS GSO support
[    0.240348] registered taskstats version 1
[    0.240352] Loading compiled-in X.509 certificates
[    0.249580] Loaded X.509 cert 'Debian Secure Boot CA: 6ccece7e4c6c0d1f6149f3dd27dfcc5cbb419ea1'
[    0.249587] Loaded X.509 cert 'Debian Secure Boot Signer 2022 - linux: 14011249c2675ea8e5148542202005810584b25f'
[    0.249817] zswap: loaded using pool lzo/zbud
[    0.249948] Key type .fscrypt registered
[    0.249949] Key type fscrypt-provisioning registered
[    0.251838] Key type encrypted registered
[    0.251840] AppArmor: AppArmor sha1 policy hashing enabled
[    0.251964] ima: secureboot mode disabled
[    0.251967] ima: No TPM chip found, activating TPM-bypass!
[    0.251968] ima: Allocated hash algorithm: sha256
[    0.251973] ima: No architecture policies found
[    0.251979] evm: Initialising EVM extended attributes:
[    0.251979] evm: security.selinux
[    0.251980] evm: security.SMACK64 (disabled)
[    0.251980] evm: security.SMACK64EXEC (disabled)
[    0.251980] evm: security.SMACK64TRANSMUTE (disabled)
[    0.251980] evm: security.SMACK64MMAP (disabled)
[    0.251981] evm: security.apparmor
[    0.251981] evm: security.ima
[    0.251981] evm: security.capability
[    0.251982] evm: HMAC attrs: 0x1
[    0.302636] clk: Disabling unused clocks
[    0.303201] Freeing unused kernel memory: 6464K
[    0.306914] Checked W+X mappings: passed, no W+X pages found
[    0.306917] Run /init as init process
[    0.306918]   with arguments:
[    0.306919]     /init
[    0.306919]   with environment:
[    0.306920]     HOME=/
[    0.306920]     TERM=linux
[    0.306920]     BOOT_IMAGE=/boot/vmlinuz-6.1.0-21-arm64
[    0.380455] ACPI: bus type USB registered
[    0.380466] usbcore: registered new interface driver usbfs
[    0.380470] usbcore: registered new interface driver hub
[    0.380474] usbcore: registered new device driver usb
[    0.386685] xhci_hcd 0000:00:0d.0: xHCI Host Controller
[    0.386688] xhci_hcd 0000:00:0d.0: new USB bus registered, assigned bus number 1
[    0.386792] xhci_hcd 0000:00:0d.0: hcc params 0x02600001 hci version 0x110 quirks 0x0000000000000010
[    0.387070] xhci_hcd 0000:00:0d.0: xHCI Host Controller
[    0.387071] xhci_hcd 0000:00:0d.0: new USB bus registered, assigned bus number 2
[    0.387074] xhci_hcd 0000:00:0d.0: Host supports USB 3.1 Enhanced SuperSpeed
[    0.387098] usb usb1: New USB device found, idVendor=1d6b, idProduct=0002, bcdDevice= 6.01
[    0.387099] usb usb1: New USB device strings: Mfr=3, Product=2, SerialNumber=1
[    0.387099] usb usb1: Product: xHCI Host Controller
[    0.387100] usb usb1: Manufacturer: Linux 6.1.0-21-arm64 xhci-hcd
[    0.387100] usb usb1: SerialNumber: 0000:00:0d.0
[    0.387179] hub 1-0:1.0: USB hub found
[    0.387194] hub 1-0:1.0: 8 ports detected
[    0.387344] usb usb2: We don't know the algorithms for LPM for this host, disabling LPM.
[    0.387354] usb usb2: New USB device found, idVendor=1d6b, idProduct=0003, bcdDevice= 6.01
[    0.387355] usb usb2: New USB device strings: Mfr=3, Product=2, SerialNumber=1
[    0.387355] usb usb2: Product: xHCI Host Controller
[    0.387356] usb usb2: Manufacturer: Linux 6.1.0-21-arm64 xhci-hcd
[    0.387357] usb usb2: SerialNumber: 0000:00:0d.0
[    0.387426] hub 2-0:1.0: USB hub found
[    0.387440] hub 2-0:1.0: 8 ports detected
[    0.485612] virtio_blk virtio1: 1/0/0 default/read/poll queues
[    0.486071] virtio_blk virtio1: [vda] 134217728 512-byte logical blocks (68.7 GB/64.0 GiB)
[    0.487425]  vda: vda1 vda2 vda3
[    0.501824] ACPI: bus type drm_connector registered
[    0.512043] [drm] pci: virtio-gpu-pci detected at 0000:00:07.0
[    0.512080] [drm] features: -virgl -edid -resource_blob -host_visible
[    0.512081] [drm] features: -context_init
[    0.512476] [drm] number of scanouts: 1
[    0.512479] [drm] number of cap sets: 0
[    0.512705] [drm] Initialized virtio_gpu 0.1.0 0 for 0000:00:07.0 on minor 0
[    0.515388] virtio-pci 0000:00:07.0: [drm] drm_plane_enable_fb_damage_clips() not called
[    0.515393] Console: switching to colour frame buffer device 167x47
[    0.518745] virtio-pci 0000:00:07.0: [drm] fb0: virtio_gpudrmfb frame buffer device
[    0.521286] virtio_net virtio0 enp0s1: renamed from eth0
[    0.593579] PM: Image not found (code -22)
[    0.649161] usb 1-1: new full-speed USB device number 2 using xhci_hcd
[    0.652816] EXT4-fs (vda2): mounted filesystem with ordered data mode. Quota mode: none.
[    0.682652] Not activating Mandatory Access Control as /sbin/tomoyo-init does not exist.
[    0.728739] systemd[1]: Inserted module 'autofs4'
[    0.734746] random: crng init done
[    0.752441] systemd[1]: systemd 252.22-1~deb12u1 running in system mode (+PAM +AUDIT +SELINUX +APPARMOR +IMA +SMACK +SECCOMP +GCRYPT -GNUTLS +OPENSSL +ACL +BLKID +CURL +ELFUTILS +FIDO2 +IDN2 -IDN +IPTC +KMOD +LIBCRYPTSETUP +LIBFDISK +PCRE2 -PWQUALITY +P11KIT +QRENCODE +TPM2 +BZIP2 +LZ4 +XZ +ZLIB +ZSTD -BPF_FRAMEWORK -XKBCOMMON +UTMP +SYSVINIT default-hierarchy=unified)
[    0.752444] systemd[1]: Detected virtualization apple.
[    0.752446] systemd[1]: Detected architecture arm64.
[    0.753848] systemd[1]: Hostname set to <debian>.
[    0.797340] usb 1-1: New USB device found, idVendor=05ac, idProduct=8105, bcdDevice= 0.00
[    0.797343] usb 1-1: New USB device strings: Mfr=2, Product=3, SerialNumber=0
[    0.797344] usb 1-1: Product: Virtual USB Keyboard
[    0.797345] usb 1-1: Manufacturer: Apple Inc.
[    0.848726] systemd[1]: Queued start job for default target graphical.target.
[    0.878296] systemd[1]: Created slice system-getty.slice - Slice /system/getty.
[    0.878487] systemd[1]: Created slice system-modprobe.slice - Slice /system/modprobe.
[    0.878626] systemd[1]: Created slice system-systemd\x2dfsck.slice - Slice /system/systemd-fsck.
[    0.878715] systemd[1]: Created slice user.slice - User and Session Slice.
[    0.878752] systemd[1]: Started systemd-ask-password-wall.path - Forward Password Requests to Wall Directory Watch.
[    0.878845] systemd[1]: Set up automount proc-sys-fs-binfmt_misc.automount - Arbitrary Executable File Formats File System Automount Point.
[    0.878858] systemd[1]: Expecting device dev-disk-by\x2duuid-C685\x2d1D26.device - /dev/disk/by-uuid/C685-1D26...
[    0.878863] systemd[1]: Expecting device dev-disk-by\x2duuid-cba290a0\x2da937\x2d4ae6\x2d837b\x2d33b49c86020e.device - /dev/disk/by-uuid/cba290a0-a937-4ae6-837b-33b49c86020e...
[    0.878881] systemd[1]: Reached target integritysetup.target - Local Integrity Protected Volumes.
[    0.878899] systemd[1]: Reached target nss-user-lookup.target - User and Group Name Lookups.
[    0.878908] systemd[1]: Reached target remote-fs.target - Remote File Systems.
[    0.878914] systemd[1]: Reached target slices.target - Slice Units.
[    0.878938] systemd[1]: Reached target veritysetup.target - Local Verity Protected Volumes.
[    0.879001] systemd[1]: Listening on systemd-fsckd.socket - fsck to fsckd communication Socket.
[    0.879027] systemd[1]: Listening on systemd-initctl.socket - initctl Compatibility Named Pipe.
[    0.879217] systemd[1]: Listening on systemd-journald-audit.socket - Journal Audit Socket.
[    0.879280] systemd[1]: Listening on systemd-journald-dev-log.socket - Journal Socket (/dev/log).
[    0.879336] systemd[1]: Listening on systemd-journald.socket - Journal Socket.
[    0.879605] systemd[1]: Listening on systemd-udevd-control.socket - udev Control Socket.
[    0.879654] systemd[1]: Listening on systemd-udevd-kernel.socket - udev Kernel Socket.
[    0.880037] systemd[1]: Mounting dev-hugepages.mount - Huge Pages File System...
[    0.880484] systemd[1]: Mounting dev-mqueue.mount - POSIX Message Queue File System...
[    0.880969] systemd[1]: Mounting sys-kernel-debug.mount - Kernel Debug File System...
[    0.881436] systemd[1]: Mounting sys-kernel-tracing.mount - Kernel Trace File System...
[    0.882735] systemd[1]: Starting keyboard-setup.service - Set the console keyboard layout...
[    0.883247] systemd[1]: Starting kmod-static-nodes.service - Create List of Static Device Nodes...
[    0.883774] systemd[1]: Starting modprobe@configfs.service - Load Kernel Module configfs...
[    0.884512] systemd[1]: Starting modprobe@dm_mod.service - Load Kernel Module dm_mod...
[    0.885881] systemd[1]: Starting modprobe@drm.service - Load Kernel Module drm...
[    0.886358] systemd[1]: Starting modprobe@efi_pstore.service - Load Kernel Module efi_pstore...
[    0.887777] systemd[1]: Starting modprobe@fuse.service - Load Kernel Module fuse...
[    0.888212] systemd[1]: Starting modprobe@loop.service - Load Kernel Module loop...
[    0.888275] systemd[1]: systemd-fsck-root.service - File System Check on Root Device was skipped because of an unmet condition check (ConditionPathExists=!/run/initramfs/fsck-root).
[    0.888512] pstore: Using crash dump compression: deflate
[    0.889354] systemd[1]: Starting systemd-journald.service - Journal Service...
[    0.890584] systemd[1]: Starting systemd-modules-load.service - Load Kernel Modules...
[    0.890924] systemd[1]: Starting systemd-remount-fs.service - Remount Root and Kernel File Systems...
[    0.891257] systemd[1]: Starting systemd-udev-trigger.service - Coldplug All udev Devices...
[    0.891875] systemd[1]: Mounted dev-hugepages.mount - Huge Pages File System.
[    0.891982] systemd[1]: Mounted dev-mqueue.mount - POSIX Message Queue File System.
[    0.892064] systemd[1]: Mounted sys-kernel-debug.mount - Kernel Debug File System.
[    0.892188] systemd[1]: Mounted sys-kernel-tracing.mount - Kernel Trace File System.
[    0.892468] systemd[1]: Finished kmod-static-nodes.service - Create List of Static Device Nodes.
[    0.892665] systemd[1]: modprobe@configfs.service: Deactivated successfully.
[    0.892715] systemd[1]: Finished modprobe@configfs.service - Load Kernel Module configfs.
[    0.892866] systemd[1]: modprobe@drm.service: Deactivated successfully.
[    0.892913] systemd[1]: Finished modprobe@drm.service - Load Kernel Module drm.
[    0.893398] systemd[1]: Mounting sys-kernel-config.mount - Kernel Configuration File System...
[    0.894467] device-mapper: core: CONFIG_IMA_DISABLE_HTABLE is disabled. Duplicate IMA measurements will not be recorded in the IMA log.
[    0.894485] device-mapper: uevent: version 1.0.3
[    0.894547] device-mapper: ioctl: 4.47.0-ioctl (2022-07-28) initialised: dm-devel@redhat.com
[    0.894731] fuse: init (API version 7.37)
[    0.894940] systemd[1]: modprobe@dm_mod.service: Deactivated successfully.
[    0.895015] systemd[1]: Finished modprobe@dm_mod.service - Load Kernel Module dm_mod.
[    0.895486] systemd[1]: modprobe@fuse.service: Deactivated successfully.
[    0.895547] systemd[1]: Finished modprobe@fuse.service - Load Kernel Module fuse.
[    0.896011] systemd[1]: Mounting sys-fs-fuse-connections.mount - FUSE Control File System...
[    0.896897] systemd[1]: Mounted sys-kernel-config.mount - Kernel Configuration File System.
[    0.898759] loop: module loaded
[    0.899019] systemd[1]: modprobe@loop.service: Deactivated successfully.
[    0.899092] systemd[1]: Finished modprobe@loop.service - Load Kernel Module loop.
[    0.899234] systemd[1]: Finished systemd-modules-load.service - Load Kernel Modules.
[    0.899415] systemd[1]: systemd-repart.service - Repartition Root Disk was skipped because no trigger condition checks were met.
[    0.899860] systemd[1]: Starting systemd-sysctl.service - Apply Kernel Variables...
[    0.901426] pstore: Registered efi as persistent store backend
[    0.901686] systemd[1]: modprobe@efi_pstore.service: Deactivated successfully.
[    0.901765] systemd[1]: Finished modprobe@efi_pstore.service - Load Kernel Module efi_pstore.
[    0.901866] systemd[1]: Mounted sys-fs-fuse-connections.mount - FUSE Control File System.
[    0.903891] EXT4-fs (vda2): re-mounted. Quota mode: none.
[    0.904388] systemd[1]: Finished systemd-remount-fs.service - Remount Root and Kernel File Systems.
[    0.904505] systemd[1]: systemd-firstboot.service - First Boot Wizard was skipped because of an unmet condition check (ConditionFirstBoot=yes).
[    0.904526] systemd[1]: systemd-pstore.service - Platform Persistent Storage Archival was skipped because of an unmet condition check (ConditionDirectoryNotEmpty=/sys/fs/pstore).
[    0.905005] systemd[1]: Starting systemd-random-seed.service - Load/Save Random Seed...
[    0.905531] systemd[1]: Starting systemd-sysusers.service - Create System Users...
[    0.915051] systemd[1]: Started systemd-journald.service - Journal Service.
[    0.925211] usb 1-2: new full-speed USB device number 3 using xhci_hcd
[    0.927319] systemd-journald[239]: Received client request to flush runtime journal.
[    1.058790] Adding 999420k swap on /dev/vda3.  Priority:-2 extents:1 across:999420k FS
[    1.077329] usb 1-2: New USB device found, idVendor=05ac, idProduct=8106, bcdDevice= 0.00
[    1.077332] usb 1-2: New USB device strings: Mfr=2, Product=3, SerialNumber=0
[    1.077333] usb 1-2: Product: Virtual USB Digitizer
[    1.077334] usb 1-2: Manufacturer: Apple Inc.
[    1.106562] usbcore: registered new device driver apple-mfi-fastcharge
[    1.109099] hid: raw HID events driver (C) Jiri Kosina
[    1.111061] usbcore: registered new interface driver usbhid
[    1.111062] usbhid: USB HID core driver
[    1.112104] input: Apple Inc. Virtual USB Keyboard as /devices/pci0000:00/0000:00:0d.0/usb1/1-1/1-1:1.0/0003:05AC:8105.0001/input/input1
[    1.169988] hid-generic 0003:05AC:8105.0001: input,hidraw0: USB HID v1.10 Keyboard [Apple Inc. Virtual USB Keyboard] on usb-0000:00:0d.0-1/input0
[    1.170102] input: Apple Inc. Virtual USB Digitizer as /devices/pci0000:00/0000:00:0d.0/usb1/1-2/1-2:1.0/0003:05AC:8106.0002/input/input2
[    1.170270] hid-generic 0003:05AC:8106.0002: input,hidraw1: USB HID v1.10 Mouse [Apple Inc. Virtual USB Digitizer] on usb-0000:00:0d.0-2/input0
[    1.930390] virtio-fs: tag <share> not found
[    1.971376] audit: type=1400 audit(1717353915.236:2): apparmor="STATUS" operation="profile_load" profile="unconfined" name="lsb_release" pid=433 comm="apparmor_parser"
[    1.971463] audit: type=1400 audit(1717353915.236:3): apparmor="STATUS" operation="profile_load" profile="unconfined" name="nvidia_modprobe" pid=434 comm="apparmor_parser"
[    1.971467] audit: type=1400 audit(1717353915.236:4): apparmor="STATUS" operation="profile_load" profile="unconfined" name="nvidia_modprobe//kmod" pid=434 comm="apparmor_parser"
[    1.979248] audit: type=1400 audit(1717353915.240:5): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/bin/man" pid=439 comm="apparmor_parser"
[    1.979253] audit: type=1400 audit(1717353915.240:6): apparmor="STATUS" operation="profile_load" profile="unconfined" name="man_filter" pid=439 comm="apparmor_parser"
[    1.979254] audit: type=1400 audit(1717353915.240:7): apparmor="STATUS" operation="profile_load" profile="unconfined" name="man_groff" pid=439 comm="apparmor_parser"
[    1.979824] audit: type=1400 audit(1717353915.244:8): apparmor="STATUS" operation="profile_load" profile="unconfined" name="libreoffice-senddoc" pid=441 comm="apparmor_parser"
[    1.979849] audit: type=1400 audit(1717353915.244:9): apparmor="STATUS" operation="profile_load" profile="unconfined" name="libreoffice-oosplash" pid=440 comm="apparmor_parser"
[    1.982282] audit: type=1400 audit(1717353915.248:10): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/lib/NetworkManager/nm-dhcp-client.action" pid=435 comm="apparmor_parser"
[    2.202129] NET: Registered PF_QIPCRTR protocol family
[   14.138349] rfkill: input handler disabled
[   14.530099] input: spice vdagent tablet as /devices/virtual/input/input3
[   21.731657] rfkill: input handler enabled
[   22.462605] rfkill: input handler disabled
[   23.237412] input: spice vdagent tablet as /devices/virtual/input/input4
[  495.394085] mimodulo: loading out-of-tree module taints kernel.
[  495.394594] mimodulo: module verification failed: signature and/or required key missing - tainting kernel
[  495.395847] Modulo cargado en el kernel.

```

Para corroborar que el modulo se cargo correctamente, se ejecuta la instruccion `lsmod | grep mod`, encontrandose lo siguiente:

```bash
mimodulo               16384  0
dm_mod                143360  0
dax                    32768  1 dm_mod
virtio_pci_modern_dev    16384  1 virtio_pci
```

Ahora, se ejecuta la instruccion `sudo rmmod mimodulo`, cuyo objetivo es quitar el modulo del kernel, y se obtiene entonces asi:

```bash
[    0.000000] Booting Linux on physical CPU 0x0000000000 [0x610f0000]
[    0.000000] Linux version 6.1.0-21-arm64 (debian-kernel@lists.debian.org) (gcc-12 (Debian 12.2.0-14) 12.2.0, GNU ld (GNU Binutils for Debian) 2.40) #1 SMP Debian 6.1.90-1 (2024-05-03)
[    0.000000] efi: EFI v2.70 by EDK II
[    0.000000] efi: ACPI 2.0=0x16fc90018 SMBIOS=0xfffff000 SMBIOS 3.0=0x16fcb4000 MOKvar=0x16fc40000 MEMRESERVE=0x16e572798
[    0.000000] secureboot: Secure boot disabled
[    0.000000] ACPI: Early table checksum verification disabled
[    0.000000] ACPI: RSDP 0x000000016FC90018 000024 (v02 APPLE )
[    0.000000] ACPI: XSDT 0x000000016FC9FE98 000044 (v01 APPLE  Apple Vz 00000001      01000013)
[    0.000000] ACPI: FACP 0x000000016FC9FA98 000114 (v06 APPLE  Apple Vz 00000001 AAPL 20180427)
[    0.000000] ACPI: DSDT 0x000000016FC9F698 000394 (v02 APPLE  Apple Vz 00000001 AAPL 20180427)
[    0.000000] ACPI: GTDT 0x000000016FC9FC18 000068 (v03 APPLE  Apple Vz 00000001 AAPL 20180427)
[    0.000000] ACPI: APIC 0x000000016FC9E998 0001AC (v05 APPLE  Apple Vz 00000001 AAPL 20180427)
[    0.000000] ACPI: MCFG 0x000000016FC9FF98 00003C (v01 APPLE  Apple Vz 00000001 AAPL 20180427)
[    0.000000] NUMA: Failed to initialise from firmware
[    0.000000] NUMA: Faking a node at [mem 0x0000000070000000-0x000000016fffffff]
[    0.000000] NUMA: NODE_DATA [mem 0x16f713380-0x16f715fff]
[    0.000000] Zone ranges:
[    0.000000]   DMA      [mem 0x0000000070000000-0x00000000ffffffff]
[    0.000000]   DMA32    empty
[    0.000000]   Normal   [mem 0x0000000100000000-0x000000016fffffff]
[    0.000000] Movable zone start for each node
[    0.000000] Early memory node ranges
[    0.000000]   node   0: [mem 0x0000000070000000-0x00000000ffffdfff]
[    0.000000]   node   0: [mem 0x00000000ffffe000-0x00000000ffffffff]
[    0.000000]   node   0: [mem 0x0000000100000000-0x000000016e64ffff]
[    0.000000]   node   0: [mem 0x000000016e650000-0x000000016e79ffff]
[    0.000000]   node   0: [mem 0x000000016e7a0000-0x000000016fb9ffff]
[    0.000000]   node   0: [mem 0x000000016fba0000-0x000000016fc2ffff]
[    0.000000]   node   0: [mem 0x000000016fc30000-0x000000016fc3ffff]
[    0.000000]   node   0: [mem 0x000000016fc40000-0x000000016fc7ffff]
[    0.000000]   node   0: [mem 0x000000016fc80000-0x000000016fcb2fff]
[    0.000000]   node   0: [mem 0x000000016fcb3000-0x000000016fcb4fff]
[    0.000000]   node   0: [mem 0x000000016fcb5000-0x000000016fffffff]
[    0.000000] Initmem setup node 0 [mem 0x0000000070000000-0x000000016fffffff]
[    0.000000] cma: Reserved 64 MiB at 0x00000000fbe00000
[    0.000000] psci: probing for conduit method from ACPI.
[    0.000000] psci: PSCIv1.1 detected in firmware.
[    0.000000] psci: Using standard PSCI v0.2 function IDs
[    0.000000] psci: Trusted OS migration not required
[    0.000000] psci: SMC Calling Convention v1.0
[    0.000000] percpu: Embedded 31 pages/cpu s86632 r8192 d32152 u126976
[    0.000000] pcpu-alloc: s86632 r8192 d32152 u126976 alloc=31*4096
[    0.000000] pcpu-alloc: [0] 0 [0] 1 [0] 2 [0] 3
[    0.000000] Detected PIPT I-cache on CPU0
[    0.000000] CPU features: detected: Address authentication (IMP DEF algorithm)
[    0.000000] CPU features: detected: GIC system register CPU interface
[    0.000000] CPU features: detected: Spectre-v4
[    0.000000] alternatives: applying boot alternatives
[    0.000000] Fallback order for Node 0: 0
[    0.000000] Built 1 zonelists, mobility grouping on.  Total pages: 1032192
[    0.000000] Policy zone: Normal
[    0.000000] Kernel command line: BOOT_IMAGE=/boot/vmlinuz-6.1.0-21-arm64 root=UUID=8886428d-e9f6-4f33-883f-467ee75a767e ro quiet
[    0.000000] Unknown kernel command line parameters "BOOT_IMAGE=/boot/vmlinuz-6.1.0-21-arm64", will be passed to user space.
[    0.000000] Dentry cache hash table entries: 524288 (order: 10, 4194304 bytes, linear)
[    0.000000] Inode-cache hash table entries: 262144 (order: 9, 2097152 bytes, linear)
[    0.000000] mem auto-init: stack:all(zero), heap alloc:on, heap free:off
[    0.000000] software IO TLB: area num 4.
[    0.000000] software IO TLB: mapped [mem 0x00000000f7e00000-0x00000000fbe00000] (64MB)
[    0.000000] Memory: 2359288K/4194304K available (13056K kernel code, 2800K rwdata, 9452K rodata, 6464K init, 626K bss, 227036K reserved, 65536K cma-reserved)
[    0.000000] SLUB: HWalign=64, Order=0-3, MinObjects=0, CPUs=4, Nodes=1
[    0.000000] ftrace: allocating 43954 entries in 172 pages
[    0.000000] ftrace: allocated 172 pages with 4 groups
[    0.000000] trace event string verifier disabled
[    0.000000] rcu: Hierarchical RCU implementation.
[    0.000000] rcu: 	RCU restricting CPUs from NR_CPUS=256 to nr_cpu_ids=4.
[    0.000000] 	Rude variant of Tasks RCU enabled.
[    0.000000] 	Tracing variant of Tasks RCU enabled.
[    0.000000] rcu: RCU calculated value of scheduler-enlistment delay is 25 jiffies.
[    0.000000] rcu: Adjusting geometry for rcu_fanout_leaf=16, nr_cpu_ids=4
[    0.000000] NR_IRQS: 64, nr_irqs: 64, preallocated irqs: 0
[    0.000000] GICv3: 224 SPIs implemented
[    0.000000] GICv3: 0 Extended SPIs implemented
[    0.000000] Root IRQ handler: gic_handle_irq
[    0.000000] GICv3: GICv3 features: 16 PPIs, RSS
[    0.000000] GICv3: CPU0: found redistributor 0 region 0:0x0000000010010000
[    0.000000] GICv2m: range[mem 0x1fff0000-0x1fff0fff], SPI[128:255]
[    0.000000] rcu: srcu_init: Setting srcu_struct sizes based on contention.
[    0.000000] arch_timer: cp15 timer(s) running at 24.00MHz (virt).
[    0.000000] clocksource: arch_sys_counter: mask: 0xffffffffffffff max_cycles: 0x588fe9dc0, max_idle_ns: 440795202592 ns
[    0.000000] sched_clock: 56 bits at 24MHz, resolution 41ns, wraps every 4398046511097ns
[    0.000025] Console: colour dummy device 80x25
[    0.000030] printk: console [tty0] enabled
[    0.000052] ACPI: Core revision 20220331
[    0.000082] Calibrating delay loop (skipped), value calculated using timer frequency.. 48.00 BogoMIPS (lpj=96000)
[    0.000083] pid_max: default: 32768 minimum: 301
[    0.000118] LSM: Security Framework initializing
[    0.000125] landlock: Up and running.
[    0.000126] Yama: disabled by default; enable with sysctl kernel.yama.*
[    0.000147] AppArmor: AppArmor initialized
[    0.000148] TOMOYO Linux initialized
[    0.000154] LSM support for eBPF active
[    0.000192] Mount-cache hash table entries: 8192 (order: 4, 65536 bytes, linear)
[    0.000208] Mountpoint-cache hash table entries: 8192 (order: 4, 65536 bytes, linear)
[    0.000457] ACPI PPTT: No PPTT table found, CPU and cache topology may be inaccurate
[    0.000616] cblist_init_generic: Setting adjustable number of callback queues.
[    0.000617] cblist_init_generic: Setting shift to 2 and lim to 1.
[    0.000627] cblist_init_generic: Setting adjustable number of callback queues.
[    0.000627] cblist_init_generic: Setting shift to 2 and lim to 1.
[    0.000652] rcu: Hierarchical SRCU implementation.
[    0.000653] rcu: 	Max phase no-delay instances is 1000.
[    0.000860] Remapping and enabling EFI services.
[    0.000971] smp: Bringing up secondary CPUs ...
[    0.001147] Detected PIPT I-cache on CPU1
[    0.001162] GICv3: CPU1: found redistributor 1 region 0:0x0000000010030000
[    0.001216] CPU1: Booted secondary processor 0x0000000001 [0x610f0000]
[    0.001455] Detected PIPT I-cache on CPU2
[    0.001469] GICv3: CPU2: found redistributor 2 region 0:0x0000000010050000
[    0.001523] CPU2: Booted secondary processor 0x0000000002 [0x610f0000]
[    0.001718] Detected PIPT I-cache on CPU3
[    0.001733] GICv3: CPU3: found redistributor 3 region 0:0x0000000010070000
[    0.001786] CPU3: Booted secondary processor 0x0000000003 [0x610f0000]
[    0.001833] smp: Brought up 1 node, 4 CPUs
[    0.001834] SMP: Total of 4 processors activated.
[    0.001835] CPU features: detected: ARMv8.4 Translation Table Level
[    0.001836] CPU features: detected: Data cache clean to the PoU not required for I/D coherence
[    0.001836] CPU features: detected: Common not Private translations
[    0.001836] CPU features: detected: CRC32 instructions
[    0.001837] CPU features: detected: Data cache clean to Point of Deep Persistence
[    0.001837] CPU features: detected: Data cache clean to Point of Persistence
[    0.001837] CPU features: detected: E0PD
[    0.001838] CPU features: detected: Generic authentication (IMP DEF algorithm)
[    0.001838] CPU features: detected: RCpc load-acquire (LDAPR)
[    0.001838] CPU features: detected: LSE atomic instructions
[    0.001839] CPU features: detected: Privileged Access Never
[    0.001839] CPU features: detected: RAS Extension Support
[    0.001839] CPU features: detected: Speculation barrier (SB)
[    0.001840] CPU features: detected: TLB range maintenance instructions
[    0.001840] CPU features: detected: Speculative Store Bypassing Safe (SSBS)
[    0.001898] CPU: All CPU(s) started at EL1
[    0.001901] alternatives: applying system-wide alternatives
[    0.009052] node 0 deferred pages initialised in 4ms
[    0.010174] devtmpfs: initialized
[    0.010526] Registered cp15_barrier emulation handler
[    0.010527] setend instruction emulation is not supported on this system
[    0.010566] clocksource: jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 7645041785100000 ns
[    0.010582] futex hash table entries: 1024 (order: 4, 65536 bytes, linear)
[    0.010684] pinctrl core: initialized pinctrl subsystem
[    0.010762] SMBIOS 3.3.0 present.
[    0.010764] DMI: Apple Inc. Apple Virtualization Generic Platform, BIOS 2022.100.22.0.0 02/09/2024
[    0.010915] NET: Registered PF_NETLINK/PF_ROUTE protocol family
[    0.011640] DMA: preallocated 512 KiB GFP_KERNEL pool for atomic allocations
[    0.011663] DMA: preallocated 512 KiB GFP_KERNEL|GFP_DMA pool for atomic allocations
[    0.011695] DMA: preallocated 512 KiB GFP_KERNEL|GFP_DMA32 pool for atomic allocations
[    0.011701] audit: initializing netlink subsys (disabled)
[    0.011791] audit: type=2000 audit(0.008:1): state=initialized audit_enabled=0 res=1
[    0.011847] thermal_sys: Registered thermal governor 'fair_share'
[    0.011847] thermal_sys: Registered thermal governor 'bang_bang'
[    0.011848] thermal_sys: Registered thermal governor 'step_wise'
[    0.011848] thermal_sys: Registered thermal governor 'user_space'
[    0.011848] thermal_sys: Registered thermal governor 'power_allocator'
[    0.011853] cpuidle: using governor ladder
[    0.011854] cpuidle: using governor menu
[    0.011869] hw-breakpoint: found 6 breakpoint and 4 watchpoint registers.
[    0.011945] ASID allocator initialised with 256 entries
[    0.011967] acpiphp: ACPI Hot Plug PCI Controller Driver version: 0.5
[    0.012034] Serial: AMBA PL011 UART driver
[    0.012087] KASLR enabled
[    0.012835] HugeTLB: registered 1.00 GiB page size, pre-allocated 0 pages
[    0.012836] HugeTLB: 0 KiB vmemmap can be freed for a 1.00 GiB page
[    0.012837] HugeTLB: registered 32.0 MiB page size, pre-allocated 0 pages
[    0.012837] HugeTLB: 0 KiB vmemmap can be freed for a 32.0 MiB page
[    0.012838] HugeTLB: registered 2.00 MiB page size, pre-allocated 0 pages
[    0.012838] HugeTLB: 0 KiB vmemmap can be freed for a 2.00 MiB page
[    0.012838] HugeTLB: registered 64.0 KiB page size, pre-allocated 0 pages
[    0.012838] HugeTLB: 0 KiB vmemmap can be freed for a 64.0 KiB page
[    0.013405] ACPI: Added _OSI(Module Device)
[    0.013406] ACPI: Added _OSI(Processor Device)
[    0.013406] ACPI: Added _OSI(3.0 _SCP Extensions)
[    0.013407] ACPI: Added _OSI(Processor Aggregator Device)
[    0.013481] ACPI: 1 ACPI AML tables successfully acquired and loaded
[    0.013570] ACPI: Interpreter enabled
[    0.013571] ACPI: Using GIC for interrupt routing
[    0.013575] ACPI: MCFG table detected, 1 entries
[    0.013784] ACPI: PCI Root Bridge [PCI0] (domain 0000 [bus 00-ff])
[    0.013787] acpi PNP0A08:00: _OSC: OS supports [ExtendedConfig ASPM ClockPM Segments MSI HPX-Type3]
[    0.013789] acpi PNP0A08:00: _OSC: OS requested [PCIeHotplug SHPCHotplug PME AER PCIeCapability LTR]
[    0.013790] acpi PNP0A08:00: _OSC: platform willing to grant [PCIeHotplug SHPCHotplug PME AER PCIeCapability LTR]
[    0.013790] acpi PNP0A08:00: _OSC: platform retains control of PCIe features (AE_NOT_FOUND)
[    0.013797] acpi PNP0A08:00: ECAM area [mem 0x40000000-0x4fffffff] reserved by PNP0C02:00
[    0.013802] acpi PNP0A08:00: ECAM at [mem 0x40000000-0x4fffffff] for [bus 00-ff]
[    0.013806] ACPI: Remapped I/O 0x000000006fff0000 to [io  0x0000-0xffff window]
[    0.013823] PCI host bridge to bus 0000:00
[    0.013824] pci_bus 0000:00: root bus resource [mem 0x50000000-0x6ffdffff window]
[    0.013824] pci_bus 0000:00: root bus resource [mem 0x180000000-0x1bfffffff window]
[    0.013825] pci_bus 0000:00: root bus resource [io  0x0000-0xffff window]
[    0.013826] pci_bus 0000:00: root bus resource [bus 00-ff]
[    0.013843] pci 0000:00:00.0: [106b:1a05] type 00 class 0x060000
[    0.013975] pci 0000:00:01.0: [1af4:1041] type 00 class 0x020000
[    0.014008] pci 0000:00:01.0: reg 0x10: [mem 0x180020000-0x180023fff 64bit]
[    0.014022] pci 0000:00:01.0: reg 0x18: [mem 0x5000a000-0x5000a03f]
[    0.014201] pci 0000:00:05.0: [1af4:1042] type 00 class 0x018000
[    0.014229] pci 0000:00:05.0: reg 0x10: [mem 0x18001c000-0x18001ffff 64bit]
[    0.014242] pci 0000:00:05.0: reg 0x18: [mem 0x50009000-0x5000903f]
[    0.014418] pci 0000:00:06.0: [1af4:105a] type 00 class 0x018000
[    0.014446] pci 0000:00:06.0: reg 0x10: [mem 0x180018000-0x18001bfff 64bit]
[    0.014459] pci 0000:00:06.0: reg 0x18: [mem 0x50008000-0x5000803f]
[    0.014628] pci 0000:00:07.0: [1af4:1050] type 00 class 0x038000
[    0.014657] pci 0000:00:07.0: reg 0x10: [mem 0x180014000-0x180017fff 64bit]
[    0.014670] pci 0000:00:07.0: reg 0x18: [mem 0x50007000-0x5000703f]
[    0.014843] pci 0000:00:08.0: [1af4:1059] type 00 class 0x040100
[    0.014870] pci 0000:00:08.0: reg 0x10: [mem 0x180010000-0x180013fff 64bit]
[    0.014882] pci 0000:00:08.0: reg 0x18: [mem 0x50004000-0x5000407f]
[    0.015090] pci 0000:00:09.0: [1af4:1059] type 00 class 0x040100
[    0.015117] pci 0000:00:09.0: reg 0x10: [mem 0x18000c000-0x18000ffff 64bit]
[    0.015130] pci 0000:00:09.0: reg 0x18: [mem 0x50003000-0x5000307f]
[    0.015309] pci 0000:00:0a.0: [1af4:1044] type 00 class 0x100000
[    0.015336] pci 0000:00:0a.0: reg 0x10: [mem 0x180008000-0x18000bfff 64bit]
[    0.015349] pci 0000:00:0a.0: reg 0x18: [mem 0x50006000-0x5000603f]
[    0.015509] pci 0000:00:0b.0: [1af4:1045] type 00 class 0x058000
[    0.015536] pci 0000:00:0b.0: reg 0x10: [mem 0x180004000-0x180007fff 64bit]
[    0.015549] pci 0000:00:0b.0: reg 0x18: [mem 0x50005000-0x5000503f]
[    0.015711] pci 0000:00:0c.0: [1af4:1043] type 00 class 0x078000
[    0.015738] pci 0000:00:0c.0: reg 0x10: [mem 0x180000000-0x180003fff 64bit]
[    0.015751] pci 0000:00:0c.0: reg 0x18: [mem 0x50002000-0x5000207f]
[    0.015904] pci 0000:00:0d.0: [106b:1a06] type 00 class 0x0c0330
[    0.015921] pci 0000:00:0d.0: reg 0x10: [mem 0x50001000-0x50001fff]
[    0.015928] pci 0000:00:0d.0: reg 0x14: [mem 0x50000000-0x500003ff]
[    0.016057] pci 0000:00:01.0: BAR 0: assigned [mem 0x180000000-0x180003fff 64bit]
[    0.016071] pci 0000:00:05.0: BAR 0: assigned [mem 0x180004000-0x180007fff 64bit]
[    0.016084] pci 0000:00:06.0: BAR 0: assigned [mem 0x180008000-0x18000bfff 64bit]
[    0.016097] pci 0000:00:07.0: BAR 0: assigned [mem 0x18000c000-0x18000ffff 64bit]
[    0.016110] pci 0000:00:08.0: BAR 0: assigned [mem 0x180010000-0x180013fff 64bit]
[    0.016123] pci 0000:00:09.0: BAR 0: assigned [mem 0x180014000-0x180017fff 64bit]
[    0.016137] pci 0000:00:0a.0: BAR 0: assigned [mem 0x180018000-0x18001bfff 64bit]
[    0.016150] pci 0000:00:0b.0: BAR 0: assigned [mem 0x18001c000-0x18001ffff 64bit]
[    0.016164] pci 0000:00:0c.0: BAR 0: assigned [mem 0x180020000-0x180023fff 64bit]
[    0.016177] pci 0000:00:0d.0: BAR 0: assigned [mem 0x50000000-0x50000fff]
[    0.016180] pci 0000:00:0d.0: BAR 1: assigned [mem 0x50001000-0x500013ff]
[    0.016184] pci 0000:00:08.0: BAR 2: assigned [mem 0x50001400-0x5000147f]
[    0.016188] pci 0000:00:09.0: BAR 2: assigned [mem 0x50001480-0x500014ff]
[    0.016193] pci 0000:00:0c.0: BAR 2: assigned [mem 0x50001500-0x5000157f]
[    0.016197] pci 0000:00:01.0: BAR 2: assigned [mem 0x50001580-0x500015bf]
[    0.016202] pci 0000:00:05.0: BAR 2: assigned [mem 0x500015c0-0x500015ff]
[    0.016206] pci 0000:00:06.0: BAR 2: assigned [mem 0x50001600-0x5000163f]
[    0.016211] pci 0000:00:07.0: BAR 2: assigned [mem 0x50001640-0x5000167f]
[    0.016215] pci 0000:00:0a.0: BAR 2: assigned [mem 0x50001680-0x500016bf]
[    0.016220] pci 0000:00:0b.0: BAR 2: assigned [mem 0x500016c0-0x500016ff]
[    0.016225] pci_bus 0000:00: resource 4 [mem 0x50000000-0x6ffdffff window]
[    0.016226] pci_bus 0000:00: resource 5 [mem 0x180000000-0x1bfffffff window]
[    0.016227] pci_bus 0000:00: resource 6 [io  0x0000-0xffff window]
[    0.016349] iommu: Default domain type: Translated
[    0.016350] iommu: DMA domain TLB invalidation policy: strict mode
[    0.016394] pps_core: LinuxPPS API ver. 1 registered
[    0.016395] pps_core: Software ver. 5.3.6 - Copyright 2005-2007 Rodolfo Giometti <giometti@linux.it>
[    0.016396] PTP clock support registered
[    0.016404] EDAC MC: Ver: 3.0.0
[    0.016562] Registered efivars operations
[    0.016809] NetLabel: Initializing
[    0.016809] NetLabel:  domain hash size = 128
[    0.016810] NetLabel:  protocols = UNLABELED CIPSOv4 CALIPSO
[    0.016817] NetLabel:  unlabeled traffic allowed by default
[    0.016883] vgaarb: loaded
[    0.017008] clocksource: Switched to clocksource arch_sys_counter
[    0.017109] VFS: Disk quotas dquot_6.6.0
[    0.017116] VFS: Dquot-cache hash table entries: 512 (order 0, 4096 bytes)
[    0.017200] AppArmor: AppArmor Filesystem Enabled
[    0.017205] pnp: PnP ACPI init
[    0.017226] system 00:00: [mem 0x40000000-0x4fffffff] could not be reserved
[    0.017230] pnp: PnP ACPI: found 1 devices
[    0.020276] NET: Registered PF_INET protocol family
[    0.020414] IP idents hash table entries: 65536 (order: 7, 524288 bytes, linear)
[    0.020951] tcp_listen_portaddr_hash hash table entries: 2048 (order: 3, 32768 bytes, linear)
[    0.021037] Table-perturb hash table entries: 65536 (order: 6, 262144 bytes, linear)
[    0.021105] TCP established hash table entries: 32768 (order: 6, 262144 bytes, linear)
[    0.021332] TCP bind hash table entries: 32768 (order: 8, 1048576 bytes, linear)
[    0.021371] TCP: Hash tables configured (established 32768 bind 32768)
[    0.021468] MPTCP token hash table entries: 4096 (order: 4, 98304 bytes, linear)
[    0.021490] UDP hash table entries: 2048 (order: 4, 65536 bytes, linear)
[    0.021509] UDP-Lite hash table entries: 2048 (order: 4, 65536 bytes, linear)
[    0.021534] NET: Registered PF_UNIX/PF_LOCAL protocol family
[    0.021542] NET: Registered PF_XDP protocol family
[    0.021570] pci 0000:00:0d.0: enabling device (0010 -> 0012)
[    0.021606] PCI: CLS 0 bytes, default 64
[    0.021728] Trying to unpack rootfs image as initramfs...
[    0.021760] kvm [1]: HYP mode not available
[    0.022459] Initialise system trusted keyrings
[    0.022469] Key type blacklist registered
[    0.022548] workingset: timestamp_bits=42 max_order=20 bucket_order=0
[    0.023153] zbud: loaded
[    0.023317] integrity: Platform Keyring initialized
[    0.023323] integrity: Machine keyring initialized
[    0.023324] Key type asymmetric registered
[    0.023324] Asymmetric key parser 'x509' registered
[    0.225301] Freeing initrd memory: 45352K
[    0.229371] alg: self-tests for CTR-KDF (hmac(sha256)) passed
[    0.229430] Block layer SCSI generic (bsg) driver version 0.4 loaded (major 247)
[    0.229500] io scheduler mq-deadline registered
[    0.230496] pl061_gpio ARMH0061:00: PL061 GPIO chip registered
[    0.230550] shpchp: Standard Hot Plug PCI Controller Driver version: 0.4
[    0.230604] input: Power Button as /devices/LNXSYSTM:00/PNP0C0C:00/input/input0
[    0.230611] ACPI: button: Power Button [PWRB]
[    0.230957] Serial: 8250/16550 driver, 4 ports, IRQ sharing enabled
[    0.231194] Serial: AMBA driver
[    0.231196] SuperH (H)SCI(F) driver initialized
[    0.231206] msm_serial: driver initialized
[    0.231408] mousedev: PS/2 mouse device common for all mice
[    0.231581] rtc-efi rtc-efi.0: registered as rtc0
[    0.231611] rtc-efi rtc-efi.0: setting system clock to 2024-06-02T18:45:13 UTC (1717353913)
[    0.231756] ledtrig-cpu: registered to indicate activity on CPUs
[    0.237868] NET: Registered PF_INET6 protocol family
[    0.240156] Segment Routing with IPv6
[    0.240164] In-situ OAM (IOAM) with IPv6
[    0.240173] mip6: Mobile IPv6
[    0.240175] NET: Registered PF_PACKET protocol family
[    0.240223] mpls_gso: MPLS GSO support
[    0.240348] registered taskstats version 1
[    0.240352] Loading compiled-in X.509 certificates
[    0.249580] Loaded X.509 cert 'Debian Secure Boot CA: 6ccece7e4c6c0d1f6149f3dd27dfcc5cbb419ea1'
[    0.249587] Loaded X.509 cert 'Debian Secure Boot Signer 2022 - linux: 14011249c2675ea8e5148542202005810584b25f'
[    0.249817] zswap: loaded using pool lzo/zbud
[    0.249948] Key type .fscrypt registered
[    0.249949] Key type fscrypt-provisioning registered
[    0.251838] Key type encrypted registered
[    0.251840] AppArmor: AppArmor sha1 policy hashing enabled
[    0.251964] ima: secureboot mode disabled
[    0.251967] ima: No TPM chip found, activating TPM-bypass!
[    0.251968] ima: Allocated hash algorithm: sha256
[    0.251973] ima: No architecture policies found
[    0.251979] evm: Initialising EVM extended attributes:
[    0.251979] evm: security.selinux
[    0.251980] evm: security.SMACK64 (disabled)
[    0.251980] evm: security.SMACK64EXEC (disabled)
[    0.251980] evm: security.SMACK64TRANSMUTE (disabled)
[    0.251980] evm: security.SMACK64MMAP (disabled)
[    0.251981] evm: security.apparmor
[    0.251981] evm: security.ima
[    0.251981] evm: security.capability
[    0.251982] evm: HMAC attrs: 0x1
[    0.302636] clk: Disabling unused clocks
[    0.303201] Freeing unused kernel memory: 6464K
[    0.306914] Checked W+X mappings: passed, no W+X pages found
[    0.306917] Run /init as init process
[    0.306918]   with arguments:
[    0.306919]     /init
[    0.306919]   with environment:
[    0.306920]     HOME=/
[    0.306920]     TERM=linux
[    0.306920]     BOOT_IMAGE=/boot/vmlinuz-6.1.0-21-arm64
[    0.380455] ACPI: bus type USB registered
[    0.380466] usbcore: registered new interface driver usbfs
[    0.380470] usbcore: registered new interface driver hub
[    0.380474] usbcore: registered new device driver usb
[    0.386685] xhci_hcd 0000:00:0d.0: xHCI Host Controller
[    0.386688] xhci_hcd 0000:00:0d.0: new USB bus registered, assigned bus number 1
[    0.386792] xhci_hcd 0000:00:0d.0: hcc params 0x02600001 hci version 0x110 quirks 0x0000000000000010
[    0.387070] xhci_hcd 0000:00:0d.0: xHCI Host Controller
[    0.387071] xhci_hcd 0000:00:0d.0: new USB bus registered, assigned bus number 2
[    0.387074] xhci_hcd 0000:00:0d.0: Host supports USB 3.1 Enhanced SuperSpeed
[    0.387098] usb usb1: New USB device found, idVendor=1d6b, idProduct=0002, bcdDevice= 6.01
[    0.387099] usb usb1: New USB device strings: Mfr=3, Product=2, SerialNumber=1
[    0.387099] usb usb1: Product: xHCI Host Controller
[    0.387100] usb usb1: Manufacturer: Linux 6.1.0-21-arm64 xhci-hcd
[    0.387100] usb usb1: SerialNumber: 0000:00:0d.0
[    0.387179] hub 1-0:1.0: USB hub found
[    0.387194] hub 1-0:1.0: 8 ports detected
[    0.387344] usb usb2: We don't know the algorithms for LPM for this host, disabling LPM.
[    0.387354] usb usb2: New USB device found, idVendor=1d6b, idProduct=0003, bcdDevice= 6.01
[    0.387355] usb usb2: New USB device strings: Mfr=3, Product=2, SerialNumber=1
[    0.387355] usb usb2: Product: xHCI Host Controller
[    0.387356] usb usb2: Manufacturer: Linux 6.1.0-21-arm64 xhci-hcd
[    0.387357] usb usb2: SerialNumber: 0000:00:0d.0
[    0.387426] hub 2-0:1.0: USB hub found
[    0.387440] hub 2-0:1.0: 8 ports detected
[    0.485612] virtio_blk virtio1: 1/0/0 default/read/poll queues
[    0.486071] virtio_blk virtio1: [vda] 134217728 512-byte logical blocks (68.7 GB/64.0 GiB)
[    0.487425]  vda: vda1 vda2 vda3
[    0.501824] ACPI: bus type drm_connector registered
[    0.512043] [drm] pci: virtio-gpu-pci detected at 0000:00:07.0
[    0.512080] [drm] features: -virgl -edid -resource_blob -host_visible
[    0.512081] [drm] features: -context_init
[    0.512476] [drm] number of scanouts: 1
[    0.512479] [drm] number of cap sets: 0
[    0.512705] [drm] Initialized virtio_gpu 0.1.0 0 for 0000:00:07.0 on minor 0
[    0.515388] virtio-pci 0000:00:07.0: [drm] drm_plane_enable_fb_damage_clips() not called
[    0.515393] Console: switching to colour frame buffer device 167x47
[    0.518745] virtio-pci 0000:00:07.0: [drm] fb0: virtio_gpudrmfb frame buffer device
[    0.521286] virtio_net virtio0 enp0s1: renamed from eth0
[    0.593579] PM: Image not found (code -22)
[    0.649161] usb 1-1: new full-speed USB device number 2 using xhci_hcd
[    0.652816] EXT4-fs (vda2): mounted filesystem with ordered data mode. Quota mode: none.
[    0.682652] Not activating Mandatory Access Control as /sbin/tomoyo-init does not exist.
[    0.728739] systemd[1]: Inserted module 'autofs4'
[    0.734746] random: crng init done
[    0.752441] systemd[1]: systemd 252.22-1~deb12u1 running in system mode (+PAM +AUDIT +SELINUX +APPARMOR +IMA +SMACK +SECCOMP +GCRYPT -GNUTLS +OPENSSL +ACL +BLKID +CURL +ELFUTILS +FIDO2 +IDN2 -IDN +IPTC +KMOD +LIBCRYPTSETUP +LIBFDISK +PCRE2 -PWQUALITY +P11KIT +QRENCODE +TPM2 +BZIP2 +LZ4 +XZ +ZLIB +ZSTD -BPF_FRAMEWORK -XKBCOMMON +UTMP +SYSVINIT default-hierarchy=unified)
[    0.752444] systemd[1]: Detected virtualization apple.
[    0.752446] systemd[1]: Detected architecture arm64.
[    0.753848] systemd[1]: Hostname set to <debian>.
[    0.797340] usb 1-1: New USB device found, idVendor=05ac, idProduct=8105, bcdDevice= 0.00
[    0.797343] usb 1-1: New USB device strings: Mfr=2, Product=3, SerialNumber=0
[    0.797344] usb 1-1: Product: Virtual USB Keyboard
[    0.797345] usb 1-1: Manufacturer: Apple Inc.
[    0.848726] systemd[1]: Queued start job for default target graphical.target.
[    0.878296] systemd[1]: Created slice system-getty.slice - Slice /system/getty.
[    0.878487] systemd[1]: Created slice system-modprobe.slice - Slice /system/modprobe.
[    0.878626] systemd[1]: Created slice system-systemd\x2dfsck.slice - Slice /system/systemd-fsck.
[    0.878715] systemd[1]: Created slice user.slice - User and Session Slice.
[    0.878752] systemd[1]: Started systemd-ask-password-wall.path - Forward Password Requests to Wall Directory Watch.
[    0.878845] systemd[1]: Set up automount proc-sys-fs-binfmt_misc.automount - Arbitrary Executable File Formats File System Automount Point.
[    0.878858] systemd[1]: Expecting device dev-disk-by\x2duuid-C685\x2d1D26.device - /dev/disk/by-uuid/C685-1D26...
[    0.878863] systemd[1]: Expecting device dev-disk-by\x2duuid-cba290a0\x2da937\x2d4ae6\x2d837b\x2d33b49c86020e.device - /dev/disk/by-uuid/cba290a0-a937-4ae6-837b-33b49c86020e...
[    0.878881] systemd[1]: Reached target integritysetup.target - Local Integrity Protected Volumes.
[    0.878899] systemd[1]: Reached target nss-user-lookup.target - User and Group Name Lookups.
[    0.878908] systemd[1]: Reached target remote-fs.target - Remote File Systems.
[    0.878914] systemd[1]: Reached target slices.target - Slice Units.
[    0.878938] systemd[1]: Reached target veritysetup.target - Local Verity Protected Volumes.
[    0.879001] systemd[1]: Listening on systemd-fsckd.socket - fsck to fsckd communication Socket.
[    0.879027] systemd[1]: Listening on systemd-initctl.socket - initctl Compatibility Named Pipe.
[    0.879217] systemd[1]: Listening on systemd-journald-audit.socket - Journal Audit Socket.
[    0.879280] systemd[1]: Listening on systemd-journald-dev-log.socket - Journal Socket (/dev/log).
[    0.879336] systemd[1]: Listening on systemd-journald.socket - Journal Socket.
[    0.879605] systemd[1]: Listening on systemd-udevd-control.socket - udev Control Socket.
[    0.879654] systemd[1]: Listening on systemd-udevd-kernel.socket - udev Kernel Socket.
[    0.880037] systemd[1]: Mounting dev-hugepages.mount - Huge Pages File System...
[    0.880484] systemd[1]: Mounting dev-mqueue.mount - POSIX Message Queue File System...
[    0.880969] systemd[1]: Mounting sys-kernel-debug.mount - Kernel Debug File System...
[    0.881436] systemd[1]: Mounting sys-kernel-tracing.mount - Kernel Trace File System...
[    0.882735] systemd[1]: Starting keyboard-setup.service - Set the console keyboard layout...
[    0.883247] systemd[1]: Starting kmod-static-nodes.service - Create List of Static Device Nodes...
[    0.883774] systemd[1]: Starting modprobe@configfs.service - Load Kernel Module configfs...
[    0.884512] systemd[1]: Starting modprobe@dm_mod.service - Load Kernel Module dm_mod...
[    0.885881] systemd[1]: Starting modprobe@drm.service - Load Kernel Module drm...
[    0.886358] systemd[1]: Starting modprobe@efi_pstore.service - Load Kernel Module efi_pstore...
[    0.887777] systemd[1]: Starting modprobe@fuse.service - Load Kernel Module fuse...
[    0.888212] systemd[1]: Starting modprobe@loop.service - Load Kernel Module loop...
[    0.888275] systemd[1]: systemd-fsck-root.service - File System Check on Root Device was skipped because of an unmet condition check (ConditionPathExists=!/run/initramfs/fsck-root).
[    0.888512] pstore: Using crash dump compression: deflate
[    0.889354] systemd[1]: Starting systemd-journald.service - Journal Service...
[    0.890584] systemd[1]: Starting systemd-modules-load.service - Load Kernel Modules...
[    0.890924] systemd[1]: Starting systemd-remount-fs.service - Remount Root and Kernel File Systems...
[    0.891257] systemd[1]: Starting systemd-udev-trigger.service - Coldplug All udev Devices...
[    0.891875] systemd[1]: Mounted dev-hugepages.mount - Huge Pages File System.
[    0.891982] systemd[1]: Mounted dev-mqueue.mount - POSIX Message Queue File System.
[    0.892064] systemd[1]: Mounted sys-kernel-debug.mount - Kernel Debug File System.
[    0.892188] systemd[1]: Mounted sys-kernel-tracing.mount - Kernel Trace File System.
[    0.892468] systemd[1]: Finished kmod-static-nodes.service - Create List of Static Device Nodes.
[    0.892665] systemd[1]: modprobe@configfs.service: Deactivated successfully.
[    0.892715] systemd[1]: Finished modprobe@configfs.service - Load Kernel Module configfs.
[    0.892866] systemd[1]: modprobe@drm.service: Deactivated successfully.
[    0.892913] systemd[1]: Finished modprobe@drm.service - Load Kernel Module drm.
[    0.893398] systemd[1]: Mounting sys-kernel-config.mount - Kernel Configuration File System...
[    0.894467] device-mapper: core: CONFIG_IMA_DISABLE_HTABLE is disabled. Duplicate IMA measurements will not be recorded in the IMA log.
[    0.894485] device-mapper: uevent: version 1.0.3
[    0.894547] device-mapper: ioctl: 4.47.0-ioctl (2022-07-28) initialised: dm-devel@redhat.com
[    0.894731] fuse: init (API version 7.37)
[    0.894940] systemd[1]: modprobe@dm_mod.service: Deactivated successfully.
[    0.895015] systemd[1]: Finished modprobe@dm_mod.service - Load Kernel Module dm_mod.
[    0.895486] systemd[1]: modprobe@fuse.service: Deactivated successfully.
[    0.895547] systemd[1]: Finished modprobe@fuse.service - Load Kernel Module fuse.
[    0.896011] systemd[1]: Mounting sys-fs-fuse-connections.mount - FUSE Control File System...
[    0.896897] systemd[1]: Mounted sys-kernel-config.mount - Kernel Configuration File System.
[    0.898759] loop: module loaded
[    0.899019] systemd[1]: modprobe@loop.service: Deactivated successfully.
[    0.899092] systemd[1]: Finished modprobe@loop.service - Load Kernel Module loop.
[    0.899234] systemd[1]: Finished systemd-modules-load.service - Load Kernel Modules.
[    0.899415] systemd[1]: systemd-repart.service - Repartition Root Disk was skipped because no trigger condition checks were met.
[    0.899860] systemd[1]: Starting systemd-sysctl.service - Apply Kernel Variables...
[    0.901426] pstore: Registered efi as persistent store backend
[    0.901686] systemd[1]: modprobe@efi_pstore.service: Deactivated successfully.
[    0.901765] systemd[1]: Finished modprobe@efi_pstore.service - Load Kernel Module efi_pstore.
[    0.901866] systemd[1]: Mounted sys-fs-fuse-connections.mount - FUSE Control File System.
[    0.903891] EXT4-fs (vda2): re-mounted. Quota mode: none.
[    0.904388] systemd[1]: Finished systemd-remount-fs.service - Remount Root and Kernel File Systems.
[    0.904505] systemd[1]: systemd-firstboot.service - First Boot Wizard was skipped because of an unmet condition check (ConditionFirstBoot=yes).
[    0.904526] systemd[1]: systemd-pstore.service - Platform Persistent Storage Archival was skipped because of an unmet condition check (ConditionDirectoryNotEmpty=/sys/fs/pstore).
[    0.905005] systemd[1]: Starting systemd-random-seed.service - Load/Save Random Seed...
[    0.905531] systemd[1]: Starting systemd-sysusers.service - Create System Users...
[    0.915051] systemd[1]: Started systemd-journald.service - Journal Service.
[    0.925211] usb 1-2: new full-speed USB device number 3 using xhci_hcd
[    0.927319] systemd-journald[239]: Received client request to flush runtime journal.
[    1.058790] Adding 999420k swap on /dev/vda3.  Priority:-2 extents:1 across:999420k FS
[    1.077329] usb 1-2: New USB device found, idVendor=05ac, idProduct=8106, bcdDevice= 0.00
[    1.077332] usb 1-2: New USB device strings: Mfr=2, Product=3, SerialNumber=0
[    1.077333] usb 1-2: Product: Virtual USB Digitizer
[    1.077334] usb 1-2: Manufacturer: Apple Inc.
[    1.106562] usbcore: registered new device driver apple-mfi-fastcharge
[    1.109099] hid: raw HID events driver (C) Jiri Kosina
[    1.111061] usbcore: registered new interface driver usbhid
[    1.111062] usbhid: USB HID core driver
[    1.112104] input: Apple Inc. Virtual USB Keyboard as /devices/pci0000:00/0000:00:0d.0/usb1/1-1/1-1:1.0/0003:05AC:8105.0001/input/input1
[    1.169988] hid-generic 0003:05AC:8105.0001: input,hidraw0: USB HID v1.10 Keyboard [Apple Inc. Virtual USB Keyboard] on usb-0000:00:0d.0-1/input0
[    1.170102] input: Apple Inc. Virtual USB Digitizer as /devices/pci0000:00/0000:00:0d.0/usb1/1-2/1-2:1.0/0003:05AC:8106.0002/input/input2
[    1.170270] hid-generic 0003:05AC:8106.0002: input,hidraw1: USB HID v1.10 Mouse [Apple Inc. Virtual USB Digitizer] on usb-0000:00:0d.0-2/input0
[    1.930390] virtio-fs: tag <share> not found
[    1.971376] audit: type=1400 audit(1717353915.236:2): apparmor="STATUS" operation="profile_load" profile="unconfined" name="lsb_release" pid=433 comm="apparmor_parser"
[    1.971463] audit: type=1400 audit(1717353915.236:3): apparmor="STATUS" operation="profile_load" profile="unconfined" name="nvidia_modprobe" pid=434 comm="apparmor_parser"
[    1.971467] audit: type=1400 audit(1717353915.236:4): apparmor="STATUS" operation="profile_load" profile="unconfined" name="nvidia_modprobe//kmod" pid=434 comm="apparmor_parser"
[    1.979248] audit: type=1400 audit(1717353915.240:5): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/bin/man" pid=439 comm="apparmor_parser"
[    1.979253] audit: type=1400 audit(1717353915.240:6): apparmor="STATUS" operation="profile_load" profile="unconfined" name="man_filter" pid=439 comm="apparmor_parser"
[    1.979254] audit: type=1400 audit(1717353915.240:7): apparmor="STATUS" operation="profile_load" profile="unconfined" name="man_groff" pid=439 comm="apparmor_parser"
[    1.979824] audit: type=1400 audit(1717353915.244:8): apparmor="STATUS" operation="profile_load" profile="unconfined" name="libreoffice-senddoc" pid=441 comm="apparmor_parser"
[    1.979849] audit: type=1400 audit(1717353915.244:9): apparmor="STATUS" operation="profile_load" profile="unconfined" name="libreoffice-oosplash" pid=440 comm="apparmor_parser"
[    1.982282] audit: type=1400 audit(1717353915.248:10): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/lib/NetworkManager/nm-dhcp-client.action" pid=435 comm="apparmor_parser"
[    2.202129] NET: Registered PF_QIPCRTR protocol family
[   14.138349] rfkill: input handler disabled
[   14.530099] input: spice vdagent tablet as /devices/virtual/input/input3
[   21.731657] rfkill: input handler enabled
[   22.462605] rfkill: input handler disabled
[   23.237412] input: spice vdagent tablet as /devices/virtual/input/input4
[  495.394085] mimodulo: loading out-of-tree module taints kernel.
[  495.394594] mimodulo: module verification failed: signature and/or required key missing - tainting kernel
[  495.395847] Modulo cargado en el kernel.
[ 1585.745148] Modulo descargado del kernel.
```

En donde puede corroborarse en el ultimo print la correcta ejecucion de la sentencia. No es posible ejecutar `modinfo` desde Debian, incluso con este comando instalado. Se busco informacion en foros, y parece ser un bug comun.

Al ejecutar `cat /proc/modules | grep mod` se encuentra:

```bash
dm_mod 143360 0 - Live 0x0000000000000000
dax 32768 1 dm_mod, Live 0x0000000000000000
virtio_pci_modern_dev 16384 1 virtio_pci, Live 0x0000000000000000
```

Lo que corrobora que el modulo se descargo del kernel correctamente.
