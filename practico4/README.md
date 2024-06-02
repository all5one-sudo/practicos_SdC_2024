# Trabajo Practico 5: Modulos de Kernel

## Preparacion

Para este trabajo, se usa un SO Linux Mint, las caracteristicas principales del computador se listan a continuacion en la captura de pantalla de `neofetch`.

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
[    0.000000] microcode: microcode updated early to revision 0xf4, date = 2023-02-23
[    0.000000] Linux version 5.15.0-107-generic (buildd@lcy02-amd64-012) (gcc (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0, GNU ld (GNU Binutils for Ubuntu) 2.38) #117-Ubuntu SMP Fri Apr 26 12:26:49 UTC 2024 (Ubuntu 5.15.0-107.117-generic 5.15.149)
[    0.000000] Command line: BOOT_IMAGE=/boot/vmlinuz-5.15.0-107-generic root=UUID=609f9f04-f21d-4aef-9d3a-c34a32a53aa4 ro quiet splash
[    0.000000] KERNEL supported cpus:
[    0.000000]   Intel GenuineIntel
[    0.000000]   AMD AuthenticAMD
[    0.000000]   Hygon HygonGenuine
[    0.000000]   Centaur CentaurHauls
[    0.000000]   zhaoxin   Shanghai  
[    0.000000] BIOS-provided physical RAM map:
[    0.000000] BIOS-e820: [mem 0x0000000000000000-0x000000000009c7ff] usable
[    0.000000] BIOS-e820: [mem 0x000000000009c800-0x000000000009ffff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000000e0000-0x00000000000fffff] reserved
[    0.000000] BIOS-e820: [mem 0x0000000000100000-0x00000000a28d9fff] usable
[    0.000000] BIOS-e820: [mem 0x00000000a28da000-0x00000000a28dafff] ACPI NVS
[    0.000000] BIOS-e820: [mem 0x00000000a28db000-0x00000000a28dbfff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000a28dc000-0x00000000a9d6afff] usable
[    0.000000] BIOS-e820: [mem 0x00000000a9d6b000-0x00000000aa0c8fff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000aa0c9000-0x00000000aa260fff] usable
[    0.000000] BIOS-e820: [mem 0x00000000aa261000-0x00000000aa90ffff] ACPI NVS
[    0.000000] BIOS-e820: [mem 0x00000000aa910000-0x00000000aaefefff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000aaeff000-0x00000000aaefffff] usable
[    0.000000] BIOS-e820: [mem 0x00000000aaf00000-0x00000000afffffff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000f0000000-0x00000000f7ffffff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000fe000000-0x00000000fe010fff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000fec00000-0x00000000fec00fff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000fee00000-0x00000000fee00fff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000ff000000-0x00000000ffffffff] reserved
[    0.000000] BIOS-e820: [mem 0x0000000100000000-0x000000064effffff] usable
[    0.000000] NX (Execute Disable) protection: active
[    0.000000] SMBIOS 3.0.0 present.
[    0.000000] DMI: Gigabyte Technology Co., Ltd. H110M-H/H110M-H-CF, BIOS F22a 07/06/2017
[    0.000000] tsc: Detected 3000.000 MHz processor
[    0.000647] e820: update [mem 0x00000000-0x00000fff] usable ==> reserved
[    0.000650] e820: remove [mem 0x000a0000-0x000fffff] usable
[    0.000658] last_pfn = 0x64f000 max_arch_pfn = 0x400000000
[    0.000783] x86/PAT: Configuration [0-7]: WB  WC  UC- UC  WB  WP  UC- WT  
[    0.001396] last_pfn = 0xaaf00 max_arch_pfn = 0x400000000
[    0.008283] found SMP MP-table at [mem 0x000fcc70-0x000fcc7f]
[    0.008297] Using GB pages for direct mapping
[    0.008770] RAMDISK: [mem 0x28fb5000-0x307d1fff]
[    0.008775] ACPI: Early table checksum verification disabled
[    0.008778] ACPI: RSDP 0x00000000000F05B0 000024 (v02 ALASKA)
[    0.008782] ACPI: XSDT 0x00000000AA5610A0 0000BC (v01 ALASKA A M I    01072009 AMI  00010013)
[    0.008786] ACPI: FACP 0x00000000AA5892A8 000114 (v06 ALASKA A M I    01072009 AMI  00010013)
[    0.008791] ACPI: DSDT 0x00000000AA5611F0 0280B7 (v02 ALASKA A M I    01072009 INTL 20160422)
[    0.008794] ACPI: FACS 0x00000000AA90FC40 000040
[    0.008797] ACPI: APIC 0x00000000AA5893C0 000084 (v03 ALASKA A M I    01072009 AMI  00010013)
[    0.008800] ACPI: FPDT 0x00000000AA589448 000044 (v01 ALASKA A M I    01072009 AMI  00010013)
[    0.008802] ACPI: MCFG 0x00000000AA589490 00003C (v01 ALASKA A M I    01072009 MSFT 00000097)
[    0.008805] ACPI: FIDT 0x00000000AA5894D0 00009C (v01 ALASKA A M I    01072009 AMI  00010013)
[    0.008808] ACPI: SSDT 0x00000000AA589570 003154 (v02 SaSsdt SaSsdt   00003000 INTL 20160422)
[    0.008811] ACPI: SSDT 0x00000000AA58C6C8 002544 (v02 PegSsd PegSsdt  00001000 INTL 20160422)
[    0.008814] ACPI: HPET 0x00000000AA58EC10 000038 (v01 INTEL  KBL      00000001 MSFT 0000005F)
[    0.008816] ACPI: SSDT 0x00000000AA58EC48 000E3B (v02 INTEL  Ther_Rvp 00001000 INTL 20160422)
[    0.008819] ACPI: SSDT 0x00000000AA58FA88 002AD7 (v02 INTEL  xh_rvp10 00000000 INTL 20160422)
[    0.008822] ACPI: UEFI 0x00000000AA592560 000042 (v01 INTEL  EDK2     00000002      01000013)
[    0.008825] ACPI: SSDT 0x00000000AA5925A8 000EDE (v02 CpuRef CpuSsdt  00003000 INTL 20160422)
[    0.008828] ACPI: LPIT 0x00000000AA593488 000094 (v01 INTEL  KBL      00000000 MSFT 0000005F)
[    0.008830] ACPI: WSMT 0x00000000AA593520 000028 (v01 INTEL  KBL      00000000 MSFT 0000005F)
[    0.008833] ACPI: SSDT 0x00000000AA593548 00029F (v02 INTEL  sensrhub 00000000 INTL 20160422)
[    0.008836] ACPI: SSDT 0x00000000AA5937E8 003002 (v02 INTEL  PtidDevc 00001000 INTL 20160422)
[    0.008839] ACPI: DBGP 0x00000000AA5967F0 000034 (v01 INTEL           00000002 MSFT 0000005F)
[    0.008841] ACPI: DBG2 0x00000000AA596828 000054 (v00 INTEL           00000002 MSFT 0000005F)
[    0.008844] ACPI: DMAR 0x00000000AA596880 0000A8 (v01 INTEL  KBL      00000001 INTL 00000001)
[    0.008846] ACPI: Reserving FACP table memory at [mem 0xaa5892a8-0xaa5893bb]
[    0.008848] ACPI: Reserving DSDT table memory at [mem 0xaa5611f0-0xaa5892a6]
[    0.008849] ACPI: Reserving FACS table memory at [mem 0xaa90fc40-0xaa90fc7f]
[    0.008850] ACPI: Reserving APIC table memory at [mem 0xaa5893c0-0xaa589443]
[    0.008851] ACPI: Reserving FPDT table memory at [mem 0xaa589448-0xaa58948b]
[    0.008851] ACPI: Reserving MCFG table memory at [mem 0xaa589490-0xaa5894cb]
[    0.008852] ACPI: Reserving FIDT table memory at [mem 0xaa5894d0-0xaa58956b]
[    0.008853] ACPI: Reserving SSDT table memory at [mem 0xaa589570-0xaa58c6c3]
[    0.008854] ACPI: Reserving SSDT table memory at [mem 0xaa58c6c8-0xaa58ec0b]
[    0.008855] ACPI: Reserving HPET table memory at [mem 0xaa58ec10-0xaa58ec47]
[    0.008856] ACPI: Reserving SSDT table memory at [mem 0xaa58ec48-0xaa58fa82]
[    0.008856] ACPI: Reserving SSDT table memory at [mem 0xaa58fa88-0xaa59255e]
[    0.008857] ACPI: Reserving UEFI table memory at [mem 0xaa592560-0xaa5925a1]
[    0.008858] ACPI: Reserving SSDT table memory at [mem 0xaa5925a8-0xaa593485]
[    0.008859] ACPI: Reserving LPIT table memory at [mem 0xaa593488-0xaa59351b]
[    0.008860] ACPI: Reserving WSMT table memory at [mem 0xaa593520-0xaa593547]
[    0.008861] ACPI: Reserving SSDT table memory at [mem 0xaa593548-0xaa5937e6]
[    0.008862] ACPI: Reserving SSDT table memory at [mem 0xaa5937e8-0xaa5967e9]
[    0.008863] ACPI: Reserving DBGP table memory at [mem 0xaa5967f0-0xaa596823]
[    0.008863] ACPI: Reserving DBG2 table memory at [mem 0xaa596828-0xaa59687b]
[    0.008864] ACPI: Reserving DMAR table memory at [mem 0xaa596880-0xaa596927]
[    0.009017] No NUMA configuration found
[    0.009018] Faking a node at [mem 0x0000000000000000-0x000000064effffff]
[    0.009026] NODE_DATA(0) allocated [mem 0x64efd6000-0x64effffff]
[    0.009340] Zone ranges:
[    0.009341]   DMA      [mem 0x0000000000001000-0x0000000000ffffff]
[    0.009343]   DMA32    [mem 0x0000000001000000-0x00000000ffffffff]
[    0.009345]   Normal   [mem 0x0000000100000000-0x000000064effffff]
[    0.009346]   Device   empty
[    0.009347] Movable zone start for each node
[    0.009350] Early memory node ranges
[    0.009350]   node   0: [mem 0x0000000000001000-0x000000000009bfff]
[    0.009351]   node   0: [mem 0x0000000000100000-0x00000000a28d9fff]
[    0.009353]   node   0: [mem 0x00000000a28dc000-0x00000000a9d6afff]
[    0.009353]   node   0: [mem 0x00000000aa0c9000-0x00000000aa260fff]
[    0.009354]   node   0: [mem 0x00000000aaeff000-0x00000000aaefffff]
[    0.009355]   node   0: [mem 0x0000000100000000-0x000000064effffff]
[    0.009358] Initmem setup node 0 [mem 0x0000000000001000-0x000000064effffff]
[    0.009362] On node 0, zone DMA: 1 pages in unavailable ranges
[    0.009386] On node 0, zone DMA: 100 pages in unavailable ranges
[    0.013345] On node 0, zone DMA32: 2 pages in unavailable ranges
[    0.013363] On node 0, zone DMA32: 862 pages in unavailable ranges
[    0.013408] On node 0, zone DMA32: 3230 pages in unavailable ranges
[    0.045657] On node 0, zone Normal: 20736 pages in unavailable ranges
[    0.045714] On node 0, zone Normal: 4096 pages in unavailable ranges
[    0.045924] ACPI: PM-Timer IO Port: 0x1808
[    0.045930] ACPI: LAPIC_NMI (acpi_id[0x01] high edge lint[0x1])
[    0.045931] ACPI: LAPIC_NMI (acpi_id[0x02] high edge lint[0x1])
[    0.045932] ACPI: LAPIC_NMI (acpi_id[0x03] high edge lint[0x1])
[    0.045933] ACPI: LAPIC_NMI (acpi_id[0x04] high edge lint[0x1])
[    0.045958] IOAPIC[0]: apic_id 2, version 32, address 0xfec00000, GSI 0-119
[    0.045961] ACPI: INT_SRC_OVR (bus 0 bus_irq 0 global_irq 2 dfl dfl)
[    0.045962] ACPI: INT_SRC_OVR (bus 0 bus_irq 9 global_irq 9 high level)
[    0.045966] ACPI: Using ACPI (MADT) for SMP configuration information
[    0.045967] ACPI: HPET id: 0x8086a201 base: 0xfed00000
[    0.045970] TSC deadline timer available
[    0.045971] smpboot: Allowing 4 CPUs, 0 hotplug CPUs
[    0.045985] PM: hibernation: Registered nosave memory: [mem 0x00000000-0x00000fff]
[    0.045987] PM: hibernation: Registered nosave memory: [mem 0x0009c000-0x0009cfff]
[    0.045988] PM: hibernation: Registered nosave memory: [mem 0x0009d000-0x0009ffff]
[    0.045989] PM: hibernation: Registered nosave memory: [mem 0x000a0000-0x000dffff]
[    0.045989] PM: hibernation: Registered nosave memory: [mem 0x000e0000-0x000fffff]
[    0.045991] PM: hibernation: Registered nosave memory: [mem 0xa28da000-0xa28dafff]
[    0.045992] PM: hibernation: Registered nosave memory: [mem 0xa28db000-0xa28dbfff]
[    0.045993] PM: hibernation: Registered nosave memory: [mem 0xa9d6b000-0xaa0c8fff]
[    0.045994] PM: hibernation: Registered nosave memory: [mem 0xaa261000-0xaa90ffff]
[    0.045995] PM: hibernation: Registered nosave memory: [mem 0xaa910000-0xaaefefff]
[    0.045997] PM: hibernation: Registered nosave memory: [mem 0xaaf00000-0xafffffff]
[    0.045997] PM: hibernation: Registered nosave memory: [mem 0xb0000000-0xefffffff]
[    0.045998] PM: hibernation: Registered nosave memory: [mem 0xf0000000-0xf7ffffff]
[    0.045999] PM: hibernation: Registered nosave memory: [mem 0xf8000000-0xfdffffff]
[    0.045999] PM: hibernation: Registered nosave memory: [mem 0xfe000000-0xfe010fff]
[    0.046000] PM: hibernation: Registered nosave memory: [mem 0xfe011000-0xfebfffff]
[    0.046001] PM: hibernation: Registered nosave memory: [mem 0xfec00000-0xfec00fff]
[    0.046001] PM: hibernation: Registered nosave memory: [mem 0xfec01000-0xfedfffff]
[    0.046002] PM: hibernation: Registered nosave memory: [mem 0xfee00000-0xfee00fff]
[    0.046003] PM: hibernation: Registered nosave memory: [mem 0xfee01000-0xfeffffff]
[    0.046003] PM: hibernation: Registered nosave memory: [mem 0xff000000-0xffffffff]
[    0.046005] [mem 0xb0000000-0xefffffff] available for PCI devices
[    0.046006] Booting paravirtualized kernel on bare hardware
[    0.046008] clocksource: refined-jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 7645519600211568 ns
[    0.046014] setup_percpu: NR_CPUS:8192 nr_cpumask_bits:4 nr_cpu_ids:4 nr_node_ids:1
[    0.046134] percpu: Embedded 61 pages/cpu s212992 r8192 d28672 u524288
[    0.046140] pcpu-alloc: s212992 r8192 d28672 u524288 alloc=1*2097152
[    0.046142] pcpu-alloc: [0] 0 1 2 3 
[    0.046165] Built 1 zonelists, mobility grouping on.  Total pages: 6164421
[    0.046166] Policy zone: Normal
[    0.046168] Kernel command line: BOOT_IMAGE=/boot/vmlinuz-5.15.0-107-generic root=UUID=609f9f04-f21d-4aef-9d3a-c34a32a53aa4 ro quiet splash
[    0.046227] Unknown kernel command line parameters "splash BOOT_IMAGE=/boot/vmlinuz-5.15.0-107-generic", will be passed to user space.
[    0.047442] Dentry cache hash table entries: 4194304 (order: 13, 33554432 bytes, linear)
[    0.048124] Inode-cache hash table entries: 2097152 (order: 12, 16777216 bytes, linear)
[    0.048184] mem auto-init: stack:off, heap alloc:on, heap free:off
[    0.106136] Memory: 24358516K/25049716K available (16393K kernel code, 4395K rwdata, 10944K rodata, 3356K init, 18712K bss, 690940K reserved, 0K cma-reserved)
[    0.107260] SLUB: HWalign=64, Order=0-3, MinObjects=0, CPUs=4, Nodes=1
[    0.107300] Kernel/User page tables isolation: enabled
[    0.107354] ftrace: allocating 50710 entries in 199 pages
[    0.130229] ftrace: allocated 199 pages with 5 groups
[    0.130408] rcu: Hierarchical RCU implementation.
[    0.130410] rcu: 	RCU restricting CPUs from NR_CPUS=8192 to nr_cpu_ids=4.
[    0.130411] 	Rude variant of Tasks RCU enabled.
[    0.130412] 	Tracing variant of Tasks RCU enabled.
[    0.130412] rcu: RCU calculated value of scheduler-enlistment delay is 25 jiffies.
[    0.130413] rcu: Adjusting geometry for rcu_fanout_leaf=16, nr_cpu_ids=4
[    0.135224] NR_IRQS: 524544, nr_irqs: 1024, preallocated irqs: 16
[    0.135541] random: crng init done
[    0.135564] Console: colour dummy device 80x25
[    0.135577] printk: console [tty0] enabled
[    0.135593] ACPI: Core revision 20210730
[    0.135807] clocksource: hpet: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 79635855245 ns
[    0.135874] APIC: Switch to symmetric I/O mode setup
[    0.135876] DMAR: Host address width 39
[    0.135877] DMAR: DRHD base: 0x000000fed90000 flags: 0x0
[    0.135882] DMAR: dmar0: reg_base_addr fed90000 ver 1:0 cap 1c0000c40660462 ecap 19e2ff0505e
[    0.135884] DMAR: DRHD base: 0x000000fed91000 flags: 0x1
[    0.135887] DMAR: dmar1: reg_base_addr fed91000 ver 1:0 cap d2008c40660462 ecap f050da
[    0.135888] DMAR: RMRR base: 0x000000aa043000 end: 0x000000aa062fff
[    0.135890] DMAR: RMRR base: 0x000000ab800000 end: 0x000000afffffff
[    0.135891] DMAR-IR: IOAPIC id 2 under DRHD base  0xfed91000 IOMMU 1
[    0.135892] DMAR-IR: HPET id 0 under DRHD base 0xfed91000
[    0.135893] DMAR-IR: Queued invalidation will be enabled to support x2apic and Intr-remapping.
[    0.137437] DMAR-IR: Enabled IRQ remapping in x2apic mode
[    0.137438] x2apic enabled
[    0.137451] Switched APIC routing to cluster x2apic.
[    0.141422] ..TIMER: vector=0x30 apic1=0 pin1=2 apic2=-1 pin2=-1
[    0.159847] clocksource: tsc-early: mask: 0xffffffffffffffff max_cycles: 0x2b3e459bf4c, max_idle_ns: 440795289890 ns
[    0.159853] Calibrating delay loop (skipped), value calculated using timer frequency.. 6000.00 BogoMIPS (lpj=12000000)
[    0.159870] x86/cpu: SGX disabled by BIOS.
[    0.159877] CPU0: Thermal monitoring enabled (TM1)
[    0.159935] process: using mwait in idle threads
[    0.159937] Last level iTLB entries: 4KB 128, 2MB 8, 4MB 8
[    0.159938] Last level dTLB entries: 4KB 64, 2MB 0, 4MB 0, 1GB 4
[    0.159942] Spectre V1 : Mitigation: usercopy/swapgs barriers and __user pointer sanitization
[    0.159944] Spectre V2 : Mitigation: IBRS
[    0.159945] Spectre V2 : Spectre v2 / SpectreRSB mitigation: Filling RSB on context switch
[    0.159945] Spectre V2 : Spectre v2 / SpectreRSB : Filling RSB on VMEXIT
[    0.159946] RETBleed: Mitigation: IBRS
[    0.159948] Spectre V2 : mitigation: Enabling conditional Indirect Branch Prediction Barrier
[    0.159949] Speculative Store Bypass: Mitigation: Speculative Store Bypass disabled via prctl and seccomp
[    0.159956] MDS: Mitigation: Clear CPU buffers
[    0.159957] MMIO Stale Data: Mitigation: Clear CPU buffers
[    0.159963] SRBDS: Mitigation: Microcode
[    0.159972] GDS: Mitigation: Microcode
[    0.159981] x86/fpu: Supporting XSAVE feature 0x001: 'x87 floating point registers'
[    0.159983] x86/fpu: Supporting XSAVE feature 0x002: 'SSE registers'
[    0.159984] x86/fpu: Supporting XSAVE feature 0x004: 'AVX registers'
[    0.159985] x86/fpu: Supporting XSAVE feature 0x008: 'MPX bounds registers'
[    0.159985] x86/fpu: Supporting XSAVE feature 0x010: 'MPX CSR'
[    0.159988] x86/fpu: xstate_offset[2]:  576, xstate_sizes[2]:  256
[    0.159989] x86/fpu: xstate_offset[3]:  832, xstate_sizes[3]:   64
[    0.159991] x86/fpu: xstate_offset[4]:  896, xstate_sizes[4]:   64
[    0.159992] x86/fpu: Enabled xstate features 0x1f, context size is 960 bytes, using 'compacted' format.
[    0.185789] Freeing SMP alternatives memory: 44K
[    0.185792] pid_max: default: 32768 minimum: 301
[    0.185816] LSM: Security Framework initializing
[    0.185826] landlock: Up and running.
[    0.185826] Yama: becoming mindful.
[    0.185843] AppArmor: AppArmor initialized
[    0.185894] Mount-cache hash table entries: 65536 (order: 7, 524288 bytes, linear)
[    0.185920] Mountpoint-cache hash table entries: 65536 (order: 7, 524288 bytes, linear)
[    0.186407] smpboot: Estimated ratio of average max frequency by base frequency (times 1024): 1126
[    0.186419] smpboot: CPU0: Intel(R) Core(TM) i5-7400 CPU @ 3.00GHz (family: 0x6, model: 0x9e, stepping: 0x9)
[    0.186533] Performance Events: PEBS fmt3+, Skylake events, 32-deep LBR, full-width counters, Intel PMU driver.
[    0.186544] ... version:                4
[    0.186545] ... bit width:              48
[    0.186545] ... generic registers:      8
[    0.186546] ... value mask:             0000ffffffffffff
[    0.186547] ... max period:             00007fffffffffff
[    0.186548] ... fixed-purpose events:   3
[    0.186548] ... event mask:             00000007000000ff
[    0.186623] signal: max sigframe size: 2032
[    0.186641] rcu: Hierarchical SRCU implementation.
[    0.187252] NMI watchdog: Enabled. Permanently consumes one hw-PMU counter.
[    0.187289] smp: Bringing up secondary CPUs ...
[    0.187366] x86: Booting SMP configuration:
[    0.187367] .... node  #0, CPUs:      #1 #2 #3
[    0.189671] smp: Brought up 1 node, 4 CPUs
[    0.189671] smpboot: Max logical packages: 1
[    0.189671] smpboot: Total of 4 processors activated (24000.00 BogoMIPS)
[    0.192879] devtmpfs: initialized
[    0.192879] x86/mm: Memory block size: 128MB
[    0.193509] ACPI: PM: Registering ACPI NVS region [mem 0xa28da000-0xa28dafff] (4096 bytes)
[    0.193509] ACPI: PM: Registering ACPI NVS region [mem 0xaa261000-0xaa90ffff] (7008256 bytes)
[    0.193509] clocksource: jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 7645041785100000 ns
[    0.193509] futex hash table entries: 1024 (order: 4, 65536 bytes, linear)
[    0.193509] pinctrl core: initialized pinctrl subsystem
[    0.193509] PM: RTC time: 13:03:13, date: 2024-05-20
[    0.193509] NET: Registered PF_NETLINK/PF_ROUTE protocol family
[    0.193509] DMA: preallocated 4096 KiB GFP_KERNEL pool for atomic allocations
[    0.193509] DMA: preallocated 4096 KiB GFP_KERNEL|GFP_DMA pool for atomic allocations
[    0.193509] DMA: preallocated 4096 KiB GFP_KERNEL|GFP_DMA32 pool for atomic allocations
[    0.193509] audit: initializing netlink subsys (disabled)
[    0.195863] audit: type=2000 audit(1716210193.060:1): state=initialized audit_enabled=0 res=1
[    0.195986] thermal_sys: Registered thermal governor 'fair_share'
[    0.195987] thermal_sys: Registered thermal governor 'bang_bang'
[    0.195988] thermal_sys: Registered thermal governor 'step_wise'
[    0.195989] thermal_sys: Registered thermal governor 'user_space'
[    0.195989] thermal_sys: Registered thermal governor 'power_allocator'
[    0.195995] EISA bus registered
[    0.196003] cpuidle: using governor ladder
[    0.196006] cpuidle: using governor menu
[    0.196038] ACPI FADT declares the system doesn't support PCIe ASPM, so disable it
[    0.196038] ACPI: bus type PCI registered
[    0.196038] acpiphp: ACPI Hot Plug PCI Controller Driver version: 0.5
[    0.196038] PCI: MMCONFIG for domain 0000 [bus 00-7f] at [mem 0xf0000000-0xf7ffffff] (base 0xf0000000)
[    0.196038] PCI: MMCONFIG at [mem 0xf0000000-0xf7ffffff] reserved in E820
[    0.196038] PCI: Using configuration type 1 for base access
[    0.197678] kprobes: kprobe jump-optimization is enabled. All kprobes are optimized if possible.
[    0.197683] HugeTLB registered 1.00 GiB page size, pre-allocated 0 pages
[    0.197683] HugeTLB registered 2.00 MiB page size, pre-allocated 0 pages
[    0.197683] fbcon: Taking over console
[    0.197683] ACPI: Added _OSI(Module Device)
[    0.197683] ACPI: Added _OSI(Processor Device)
[    0.197683] ACPI: Added _OSI(3.0 _SCP Extensions)
[    0.197683] ACPI: Added _OSI(Processor Aggregator Device)
[    0.197683] ACPI: Added _OSI(Linux-Dell-Video)
[    0.197683] ACPI: Added _OSI(Linux-Lenovo-NV-HDMI-Audio)
[    0.197683] ACPI: Added _OSI(Linux-HPI-Hybrid-Graphics)
[    0.237543] ACPI: 8 ACPI AML tables successfully acquired and loaded
[    0.240688] ACPI: [Firmware Bug]: BIOS _OSI(Linux) query ignored
[    0.248527] ACPI: Dynamic OEM Table Load:
[    0.248533] ACPI: SSDT 0xFFFF98B381204800 000693 (v02 PmRef  Cpu0Ist  00003000 INTL 20160422)
[    0.250151] ACPI: \_PR_.CPU0: _OSC native thermal LVT Acked
[    0.251851] ACPI: Dynamic OEM Table Load:
[    0.251851] ACPI: SSDT 0xFFFF98B3811B7C00 0003FF (v02 PmRef  Cpu0Cst  00003001 INTL 20160422)
[    0.251851] ACPI: Dynamic OEM Table Load:
[    0.251851] ACPI: SSDT 0xFFFF98B381206800 00065C (v02 PmRef  ApIst    00003000 INTL 20160422)
[    0.256003] ACPI: Dynamic OEM Table Load:
[    0.256008] ACPI: SSDT 0xFFFF98B380F07A00 00018A (v02 PmRef  ApCst    00003000 INTL 20160422)
[    0.260523] ACPI: Interpreter enabled
[    0.260560] ACPI: PM: (supports S0 S3 S4 S5)
[    0.260561] ACPI: Using IOAPIC for interrupt routing
[    0.260599] PCI: Using host bridge windows from ACPI; if necessary, use "pci=nocrs" and report a bug
[    0.260600] PCI: Using E820 reservations for host bridge windows
[    0.261849] ACPI: Enabled 6 GPEs in block 00 to 7F
[    0.264721] ACPI: PM: Power Resource [PG00]
[    0.265136] ACPI: PM: Power Resource [PG01]
[    0.265543] ACPI: PM: Power Resource [PG02]
[    0.267849] ACPI: PM: Power Resource [WRST]
[    0.268180] ACPI: PM: Power Resource [WRST]
[    0.268507] ACPI: PM: Power Resource [WRST]
[    0.268834] ACPI: PM: Power Resource [WRST]
[    0.269161] ACPI: PM: Power Resource [WRST]
[    0.269492] ACPI: PM: Power Resource [WRST]
[    0.269819] ACPI: PM: Power Resource [WRST]
[    0.270146] ACPI: PM: Power Resource [WRST]
[    0.270473] ACPI: PM: Power Resource [WRST]
[    0.270801] ACPI: PM: Power Resource [WRST]
[    0.271157] ACPI: PM: Power Resource [WRST]
[    0.271489] ACPI: PM: Power Resource [WRST]
[    0.271819] ACPI: PM: Power Resource [WRST]
[    0.272156] ACPI: PM: Power Resource [WRST]
[    0.272482] ACPI: PM: Power Resource [WRST]
[    0.272809] ACPI: PM: Power Resource [WRST]
[    0.273140] ACPI: PM: Power Resource [WRST]
[    0.274647] ACPI: PM: Power Resource [WRST]
[    0.274977] ACPI: PM: Power Resource [WRST]
[    0.275307] ACPI: PM: Power Resource [WRST]
[    0.288195] ACPI: PM: Power Resource [FN00]
[    0.288292] ACPI: PM: Power Resource [FN01]
[    0.288386] ACPI: PM: Power Resource [FN02]
[    0.288478] ACPI: PM: Power Resource [FN03]
[    0.288572] ACPI: PM: Power Resource [FN04]
[    0.290144] ACPI: PCI Root Bridge [PCI0] (domain 0000 [bus 00-7e])
[    0.290151] acpi PNP0A08:00: _OSC: OS supports [ExtendedConfig ASPM ClockPM Segments MSI EDR HPX-Type3]
[    0.290202] acpi PNP0A08:00: _OSC: platform retains control of PCIe features (AE_ERROR)
[    0.291173] PCI host bridge to bus 0000:00
[    0.291175] pci_bus 0000:00: root bus resource [bus 00-7e]
[    0.291177] pci_bus 0000:00: root bus resource [io  0x0000-0x0cf7 window]
[    0.291179] pci_bus 0000:00: root bus resource [io  0x0d00-0xffff window]
[    0.291180] pci_bus 0000:00: root bus resource [mem 0x000a0000-0x000bffff window]
[    0.291182] pci_bus 0000:00: root bus resource [mem 0xb0000000-0xefffffff window]
[    0.291183] pci_bus 0000:00: root bus resource [mem 0xfd000000-0xfe7fffff window]
[    0.291346] pci 0000:00:00.0: [8086:591f] type 00 class 0x060000
[    0.291730] pci 0000:00:01.0: [8086:1901] type 01 class 0x060400
[    0.291793] pci 0000:00:01.0: PME# supported from D0 D3hot D3cold
[    0.292410] pci 0000:00:02.0: [8086:5912] type 00 class 0x038000
[    0.292430] pci 0000:00:02.0: reg 0x10: [mem 0xed000000-0xedffffff 64bit]
[    0.292443] pci 0000:00:02.0: reg 0x18: [mem 0xc0000000-0xcfffffff 64bit pref]
[    0.292453] pci 0000:00:02.0: reg 0x20: [io  0xf000-0xf03f]
[    0.292856] pci 0000:00:14.0: [8086:a12f] type 00 class 0x0c0330
[    0.292886] pci 0000:00:14.0: reg 0x10: [mem 0xef210000-0xef21ffff 64bit]
[    0.292977] pci 0000:00:14.0: PME# supported from D3hot D3cold
[    0.293860] pci 0000:00:16.0: [8086:a13a] type 00 class 0x078000
[    0.293889] pci 0000:00:16.0: reg 0x10: [mem 0xef22d000-0xef22dfff 64bit]
[    0.293966] pci 0000:00:16.0: PME# supported from D3hot
[    0.294418] pci 0000:00:17.0: [8086:a102] type 00 class 0x010601
[    0.294441] pci 0000:00:17.0: reg 0x10: [mem 0xef228000-0xef229fff]
[    0.294454] pci 0000:00:17.0: reg 0x14: [mem 0xef22c000-0xef22c0ff]
[    0.294467] pci 0000:00:17.0: reg 0x18: [io  0xf090-0xf097]
[    0.294479] pci 0000:00:17.0: reg 0x1c: [io  0xf080-0xf083]
[    0.294492] pci 0000:00:17.0: reg 0x20: [io  0xf060-0xf07f]
[    0.294504] pci 0000:00:17.0: reg 0x24: [mem 0xef22b000-0xef22b7ff]
[    0.294548] pci 0000:00:17.0: PME# supported from D3hot
[    0.295007] pci 0000:00:1c.0: [8086:a114] type 01 class 0x060400
[    0.295102] pci 0000:00:1c.0: PME# supported from D0 D3hot D3cold
[    0.295948] pci 0000:00:1c.5: [8086:a115] type 01 class 0x060400
[    0.296043] pci 0000:00:1c.5: PME# supported from D0 D3hot D3cold
[    0.296865] pci 0000:00:1c.6: [8086:a116] type 01 class 0x060400
[    0.296960] pci 0000:00:1c.6: PME# supported from D0 D3hot D3cold
[    0.297783] pci 0000:00:1c.7: [8086:a117] type 01 class 0x060400
[    0.297877] pci 0000:00:1c.7: PME# supported from D0 D3hot D3cold
[    0.298702] pci 0000:00:1d.0: [8086:a118] type 01 class 0x060400
[    0.298803] pci 0000:00:1d.0: PME# supported from D0 D3hot D3cold
[    0.299625] pci 0000:00:1d.1: [8086:a119] type 01 class 0x060400
[    0.299726] pci 0000:00:1d.1: PME# supported from D0 D3hot D3cold
[    0.300570] pci 0000:00:1f.0: [8086:a143] type 00 class 0x060100
[    0.301131] pci 0000:00:1f.2: [8086:a121] type 00 class 0x058000
[    0.301156] pci 0000:00:1f.2: reg 0x10: [mem 0xef224000-0xef227fff]
[    0.301652] pci 0000:00:1f.3: [8086:a170] type 00 class 0x040300
[    0.301688] pci 0000:00:1f.3: reg 0x10: [mem 0xef220000-0xef223fff 64bit]
[    0.301739] pci 0000:00:1f.3: reg 0x20: [mem 0xef200000-0xef20ffff 64bit]
[    0.301793] pci 0000:00:1f.3: PME# supported from D3hot D3cold
[    0.302612] pci 0000:00:1f.4: [8086:a123] type 00 class 0x0c0500
[    0.302674] pci 0000:00:1f.4: reg 0x10: [mem 0xef22a000-0xef22a0ff 64bit]
[    0.302746] pci 0000:00:1f.4: reg 0x20: [io  0xf040-0xf05f]
[    0.303120] pci 0000:01:00.0: [10de:1c03] type 00 class 0x030000
[    0.303142] pci 0000:01:00.0: reg 0x10: [mem 0xee000000-0xeeffffff]
[    0.303159] pci 0000:01:00.0: reg 0x14: [mem 0xd0000000-0xdfffffff 64bit pref]
[    0.303177] pci 0000:01:00.0: reg 0x1c: [mem 0xe0000000-0xe1ffffff 64bit pref]
[    0.303188] pci 0000:01:00.0: reg 0x24: [io  0xe000-0xe07f]
[    0.303200] pci 0000:01:00.0: reg 0x30: [mem 0xef000000-0xef07ffff pref]
[    0.303225] pci 0000:01:00.0: Video device with shadowed ROM at [mem 0x000c0000-0x000dffff]
[    0.303293] pci 0000:01:00.0: 32.000 Gb/s available PCIe bandwidth, limited by 2.5 GT/s PCIe x16 link at 0000:00:01.0 (capable of 126.016 Gb/s with 8.0 GT/s PCIe x16 link)
[    0.303363] pci 0000:01:00.1: [10de:10f1] type 00 class 0x040300
[    0.303384] pci 0000:01:00.1: reg 0x10: [mem 0xef080000-0xef083fff]
[    0.303530] pci 0000:00:01.0: ASPM: current common clock configuration is inconsistent, reconfiguring
[    0.311895] pci 0000:00:01.0: PCI bridge to [bus 01]
[    0.311919] pci 0000:00:01.0:   bridge window [io  0xe000-0xefff]
[    0.311921] pci 0000:00:01.0:   bridge window [mem 0xee000000-0xef0fffff]
[    0.311924] pci 0000:00:01.0:   bridge window [mem 0xd0000000-0xe1ffffff 64bit pref]
[    0.312064] pci 0000:02:00.0: [10ec:8168] type 00 class 0x020000
[    0.312094] pci 0000:02:00.0: reg 0x10: [io  0xd000-0xd0ff]
[    0.312133] pci 0000:02:00.0: reg 0x18: [mem 0xef100000-0xef100fff 64bit]
[    0.312157] pci 0000:02:00.0: reg 0x20: [mem 0xe2100000-0xe2103fff 64bit pref]
[    0.312264] pci 0000:02:00.0: supports D1 D2
[    0.312266] pci 0000:02:00.0: PME# supported from D0 D1 D2 D3hot D3cold
[    0.312701] pci 0000:00:1c.0: PCI bridge to [bus 02]
[    0.312704] pci 0000:00:1c.0:   bridge window [io  0xd000-0xdfff]
[    0.312706] pci 0000:00:1c.0:   bridge window [mem 0xef100000-0xef1fffff]
[    0.312710] pci 0000:00:1c.0:   bridge window [mem 0xe2100000-0xe21fffff 64bit pref]
[    0.312809] pci 0000:00:1c.5: PCI bridge to [bus 03]
[    0.312910] pci 0000:00:1c.6: PCI bridge to [bus 04]
[    0.313014] pci 0000:00:1c.7: PCI bridge to [bus 05]
[    0.313117] pci 0000:00:1d.0: PCI bridge to [bus 06]
[    0.313221] pci 0000:00:1d.1: PCI bridge to [bus 07]
[    0.315539] ACPI: PCI: Interrupt link LNKA configured for IRQ 11
[    0.315609] ACPI: PCI: Interrupt link LNKB configured for IRQ 10
[    0.315678] ACPI: PCI: Interrupt link LNKC configured for IRQ 11
[    0.315748] ACPI: PCI: Interrupt link LNKD configured for IRQ 11
[    0.315817] ACPI: PCI: Interrupt link LNKE configured for IRQ 11
[    0.315887] ACPI: PCI: Interrupt link LNKF configured for IRQ 11
[    0.315957] ACPI: PCI: Interrupt link LNKG configured for IRQ 11
[    0.316025] ACPI: PCI: Interrupt link LNKH configured for IRQ 11
[    0.324290] iommu: Default domain type: Translated 
[    0.324290] iommu: DMA domain TLB invalidation policy: lazy mode 
[    0.324290] SCSI subsystem initialized
[    0.324290] libata version 3.00 loaded.
[    0.324290] pci 0000:01:00.0: vgaarb: setting as boot VGA device
[    0.324290] pci 0000:01:00.0: vgaarb: VGA device added: decodes=io+mem,owns=io+mem,locks=none
[    0.324290] pci 0000:01:00.0: vgaarb: bridge control possible
[    0.324290] vgaarb: loaded
[    0.324290] ACPI: bus type USB registered
[    0.324290] usbcore: registered new interface driver usbfs
[    0.324290] usbcore: registered new interface driver hub
[    0.324290] usbcore: registered new device driver usb
[    0.324290] pps_core: LinuxPPS API ver. 1 registered
[    0.324290] pps_core: Software ver. 5.3.6 - Copyright 2005-2007 Rodolfo Giometti <giometti@linux.it>
[    0.324290] PTP clock support registered
[    0.324290] EDAC MC: Ver: 3.0.0
[    0.324290] NetLabel: Initializing
[    0.324290] NetLabel:  domain hash size = 128
[    0.324290] NetLabel:  protocols = UNLABELED CIPSOv4 CALIPSO
[    0.324290] NetLabel:  unlabeled traffic allowed by default
[    0.324290] PCI: Using ACPI for IRQ routing
[    0.338184] PCI: pci_cache_line_size set to 64 bytes
[    0.338228] e820: reserve RAM buffer [mem 0x0009c800-0x0009ffff]
[    0.338230] e820: reserve RAM buffer [mem 0xa28da000-0xa3ffffff]
[    0.338231] e820: reserve RAM buffer [mem 0xa9d6b000-0xabffffff]
[    0.338233] e820: reserve RAM buffer [mem 0xaa261000-0xabffffff]
[    0.338234] e820: reserve RAM buffer [mem 0xaaf00000-0xabffffff]
[    0.338235] e820: reserve RAM buffer [mem 0x64f000000-0x64fffffff]
[    0.338237] hpet0: at MMIO 0xfed00000, IRQs 2, 8, 0, 0, 0, 0, 0, 0
[    0.338237] hpet0: 8 comparators, 64-bit 24.000000 MHz counter
[    0.340882] clocksource: Switched to clocksource tsc-early
[    0.349627] VFS: Disk quotas dquot_6.6.0
[    0.349641] VFS: Dquot-cache hash table entries: 512 (order 0, 4096 bytes)
[    0.349741] AppArmor: AppArmor Filesystem Enabled
[    0.349773] pnp: PnP ACPI init
[    0.350123] system 00:00: [io  0x0a00-0x0a2f] has been reserved
[    0.350126] system 00:00: [io  0x0a30-0x0a3f] has been reserved
[    0.350128] system 00:00: [io  0x0a40-0x0a4f] has been reserved
[    0.350357] system 00:01: [io  0x0680-0x069f] has been reserved
[    0.350359] system 00:01: [io  0xffff] has been reserved
[    0.350363] system 00:01: [io  0xffff] has been reserved
[    0.350365] system 00:01: [io  0xffff] has been reserved
[    0.350366] system 00:01: [io  0x1800-0x18fe] has been reserved
[    0.350368] system 00:01: [io  0x164e-0x164f] has been reserved
[    0.350461] system 00:02: [io  0x0800-0x087f] has been reserved
[    0.350522] system 00:04: [io  0x1854-0x1857] has been reserved
[    0.350813] system 00:05: [mem 0xfed10000-0xfed17fff] has been reserved
[    0.350815] system 00:05: [mem 0xfed18000-0xfed18fff] has been reserved
[    0.350816] system 00:05: [mem 0xfed19000-0xfed19fff] has been reserved
[    0.350818] system 00:05: [mem 0xf0000000-0xf7ffffff] has been reserved
[    0.350819] system 00:05: [mem 0xfed20000-0xfed3ffff] has been reserved
[    0.350821] system 00:05: [mem 0xfed90000-0xfed93fff] could not be reserved
[    0.350822] system 00:05: [mem 0xfed45000-0xfed8ffff] has been reserved
[    0.350824] system 00:05: [mem 0xff000000-0xffffffff] has been reserved
[    0.350826] system 00:05: [mem 0xfee00000-0xfeefffff] could not be reserved
[    0.350827] system 00:05: [mem 0xeffe0000-0xefffffff] has been reserved
[    0.350870] system 00:06: [mem 0xfd000000-0xfdabffff] has been reserved
[    0.350872] system 00:06: [mem 0xfdad0000-0xfdadffff] has been reserved
[    0.350873] system 00:06: [mem 0xfdb00000-0xfdffffff] has been reserved
[    0.350875] system 00:06: [mem 0xfe000000-0xfe01ffff] could not be reserved
[    0.350876] system 00:06: [mem 0xfe036000-0xfe03bfff] has been reserved
[    0.350878] system 00:06: [mem 0xfe03d000-0xfe3fffff] has been reserved
[    0.350879] system 00:06: [mem 0xfe410000-0xfe7fffff] has been reserved
[    0.351205] system 00:07: [io  0xff00-0xfffe] has been reserved
[    0.352635] system 00:08: [mem 0xfdaf0000-0xfdafffff] has been reserved
[    0.352637] system 00:08: [mem 0xfdae0000-0xfdaeffff] has been reserved
[    0.352639] system 00:08: [mem 0xfdac0000-0xfdacffff] has been reserved
[    0.353701] pnp: PnP ACPI: found 9 devices
[    0.359256] clocksource: acpi_pm: mask: 0xffffff max_cycles: 0xffffff, max_idle_ns: 2085701024 ns
[    0.359308] NET: Registered PF_INET protocol family
[    0.359419] IP idents hash table entries: 262144 (order: 9, 2097152 bytes, linear)
[    0.360941] tcp_listen_portaddr_hash hash table entries: 16384 (order: 6, 262144 bytes, linear)
[    0.360972] Table-perturb hash table entries: 65536 (order: 6, 262144 bytes, linear)
[    0.361074] TCP established hash table entries: 262144 (order: 9, 2097152 bytes, linear)
[    0.361286] TCP bind hash table entries: 65536 (order: 8, 1048576 bytes, linear)
[    0.361341] TCP: Hash tables configured (established 262144 bind 65536)
[    0.361424] MPTCP token hash table entries: 32768 (order: 7, 786432 bytes, linear)
[    0.361509] UDP hash table entries: 16384 (order: 7, 524288 bytes, linear)
[    0.361573] UDP-Lite hash table entries: 16384 (order: 7, 524288 bytes, linear)
[    0.361639] NET: Registered PF_UNIX/PF_LOCAL protocol family
[    0.361644] NET: Registered PF_XDP protocol family
[    0.361656] pci 0000:00:01.0: PCI bridge to [bus 01]
[    0.361660] pci 0000:00:01.0:   bridge window [io  0xe000-0xefff]
[    0.361667] pci 0000:00:01.0:   bridge window [mem 0xee000000-0xef0fffff]
[    0.361672] pci 0000:00:01.0:   bridge window [mem 0xd0000000-0xe1ffffff 64bit pref]
[    0.361681] pci 0000:00:1c.0: PCI bridge to [bus 02]
[    0.361683] pci 0000:00:1c.0:   bridge window [io  0xd000-0xdfff]
[    0.361690] pci 0000:00:1c.0:   bridge window [mem 0xef100000-0xef1fffff]
[    0.361695] pci 0000:00:1c.0:   bridge window [mem 0xe2100000-0xe21fffff 64bit pref]
[    0.361705] pci 0000:00:1c.5: PCI bridge to [bus 03]
[    0.361724] pci 0000:00:1c.6: PCI bridge to [bus 04]
[    0.361744] pci 0000:00:1c.7: PCI bridge to [bus 05]
[    0.361763] pci 0000:00:1d.0: PCI bridge to [bus 06]
[    0.361783] pci 0000:00:1d.1: PCI bridge to [bus 07]
[    0.361804] pci_bus 0000:00: resource 4 [io  0x0000-0x0cf7 window]
[    0.361806] pci_bus 0000:00: resource 5 [io  0x0d00-0xffff window]
[    0.361807] pci_bus 0000:00: resource 6 [mem 0x000a0000-0x000bffff window]
[    0.361808] pci_bus 0000:00: resource 7 [mem 0xb0000000-0xefffffff window]
[    0.361810] pci_bus 0000:00: resource 8 [mem 0xfd000000-0xfe7fffff window]
[    0.361811] pci_bus 0000:01: resource 0 [io  0xe000-0xefff]
[    0.361812] pci_bus 0000:01: resource 1 [mem 0xee000000-0xef0fffff]
[    0.361813] pci_bus 0000:01: resource 2 [mem 0xd0000000-0xe1ffffff 64bit pref]
[    0.361815] pci_bus 0000:02: resource 0 [io  0xd000-0xdfff]
[    0.361816] pci_bus 0000:02: resource 1 [mem 0xef100000-0xef1fffff]
[    0.361817] pci_bus 0000:02: resource 2 [mem 0xe2100000-0xe21fffff 64bit pref]
[    0.362906] pci 0000:01:00.1: D0 power state depends on 0000:01:00.0
[    0.362915] PCI: CLS 64 bytes, default 64
[    0.362972] PCI-DMA: Using software bounce buffering for IO (SWIOTLB)
[    0.362973] software IO TLB: mapped [mem 0x00000000a5d6b000-0x00000000a9d6b000] (64MB)
[    0.363004] Trying to unpack rootfs image as initramfs...
[    0.363493] Initialise system trusted keyrings
[    0.363501] Key type blacklist registered
[    0.363522] workingset: timestamp_bits=36 max_order=23 bucket_order=0
[    0.364790] zbud: loaded
[    0.365022] squashfs: version 4.0 (2009/01/31) Phillip Lougher
[    0.365137] fuse: init (API version 7.34)
[    0.365263] integrity: Platform Keyring initialized
[    0.371866] Key type asymmetric registered
[    0.371867] Asymmetric key parser 'x509' registered
[    0.371883] Block layer SCSI generic (bsg) driver version 0.4 loaded (major 243)
[    0.371908] io scheduler mq-deadline registered
[    0.373417] shpchp: Standard Hot Plug PCI Controller Driver version: 0.4
[    0.373771] input: Sleep Button as /devices/LNXSYSTM:00/LNXSYBUS:00/PNP0C0E:00/input/input0
[    0.373792] ACPI: button: Sleep Button [SLPB]
[    0.373818] input: Power Button as /devices/LNXSYSTM:00/LNXSYBUS:00/PNP0C0C:00/input/input1
[    0.373831] ACPI: button: Power Button [PWRB]
[    0.373855] input: Power Button as /devices/LNXSYSTM:00/LNXPWRBN:00/input/input2
[    0.373878] ACPI: button: Power Button [PWRF]
[    0.374627] thermal LNXTHERM:00: registered as thermal_zone0
[    0.374629] ACPI: thermal: Thermal Zone [TZ00] (28 C)
[    0.374819] thermal LNXTHERM:01: registered as thermal_zone1
[    0.374821] ACPI: thermal: Thermal Zone [TZ01] (30 C)
[    0.375043] Serial: 8250/16550 driver, 32 ports, IRQ sharing enabled
[    0.376707] Linux agpgart interface v0.103
[    0.378351] loop: module loaded
[    0.378554] tun: Universal TUN/TAP device driver, 1.6
[    0.378574] PPP generic driver version 2.4.2
[    0.378608] VFIO - User Level meta-driver version: 0.3
[    0.378695] ehci_hcd: USB 2.0 'Enhanced' Host Controller (EHCI) Driver
[    0.378697] ehci-pci: EHCI PCI platform driver
[    0.378703] ehci-platform: EHCI generic platform driver
[    0.378710] ohci_hcd: USB 1.1 'Open' Host Controller (OHCI) Driver
[    0.378712] ohci-pci: OHCI PCI platform driver
[    0.378718] ohci-platform: OHCI generic platform driver
[    0.378723] uhci_hcd: USB Universal Host Controller Interface driver
[    0.378773] i8042: PNP: No PS/2 controller found.
[    0.378806] mousedev: PS/2 mouse device common for all mice
[    0.378888] rtc_cmos 00:03: RTC can wake from S4
[    0.379502] rtc_cmos 00:03: registered as rtc0
[    0.379627] rtc_cmos 00:03: setting system clock to 2024-05-20T13:03:13 UTC (1716210193)
[    0.379649] rtc_cmos 00:03: alarms up to one month, y3k, 242 bytes nvram
[    0.379656] i2c_dev: i2c /dev entries driver
[    0.379989] device-mapper: core: CONFIG_IMA_DISABLE_HTABLE is disabled. Duplicate IMA measurements will not be recorded in the IMA log.
[    0.380010] device-mapper: uevent: version 1.0.3
[    0.380101] device-mapper: ioctl: 4.45.0-ioctl (2021-03-22) initialised: dm-devel@redhat.com
[    0.380118] platform eisa.0: Probing EISA bus 0
[    0.380119] platform eisa.0: EISA: Cannot allocate resource for mainboard
[    0.380121] platform eisa.0: Cannot allocate resource for EISA slot 1
[    0.380122] platform eisa.0: Cannot allocate resource for EISA slot 2
[    0.380123] platform eisa.0: Cannot allocate resource for EISA slot 3
[    0.380124] platform eisa.0: Cannot allocate resource for EISA slot 4
[    0.380125] platform eisa.0: Cannot allocate resource for EISA slot 5
[    0.380126] platform eisa.0: Cannot allocate resource for EISA slot 6
[    0.380127] platform eisa.0: Cannot allocate resource for EISA slot 7
[    0.380128] platform eisa.0: Cannot allocate resource for EISA slot 8
[    0.380129] platform eisa.0: EISA: Detected 0 cards
[    0.380132] intel_pstate: Intel P-state driver initializing
[    0.380274] intel_pstate: Disabling energy efficiency optimization
[    0.380275] intel_pstate: HWP enabled
[    0.380450] ledtrig-cpu: registered to indicate activity on CPUs
[    0.380485] vesafb: mode is 1920x1080x32, linelength=7680, pages=0
[    0.380486] vesafb: scrolling: redraw
[    0.380487] vesafb: Truecolor: size=8:8:8:8, shift=24:16:8:0
[    0.380499] vesafb: framebuffer at 0xe1000000, mapped to 0x00000000ea95e1c7, using 8128k, total 8128k
[    0.380567] Console: switching to colour frame buffer device 240x67
[    0.512456] fb0: VESA VGA frame buffer device
[    0.512592] resource sanity check: requesting [mem 0xfdffe800-0xfe0007ff], which spans more than pnp 00:06 [mem 0xfdb00000-0xfdffffff]
[    0.512595] caller pmc_core_probe+0xb3/0x250 mapping multiple BARs
[    0.512628] intel_pmc_core INT33A1:00:  initialized
[    0.512746] drop_monitor: Initializing network drop monitor service
[    0.512929] NET: Registered PF_INET6 protocol family
[    0.986668] Freeing initrd memory: 122996K
[    0.992487] Segment Routing with IPv6
[    0.992499] In-situ OAM (IOAM) with IPv6
[    0.992523] NET: Registered PF_PACKET protocol family
[    0.992624] Key type dns_resolver registered
[    0.993174] microcode: sig=0x906e9, pf=0x2, revision=0xf4
[    0.993273] microcode: Microcode Update Driver: v2.2.
[    0.993278] IPI shorthand broadcast: enabled
[    0.993307] sched_clock: Marking stable (992762696, 339528)->(998156016, -5053792)
[    0.993521] registered taskstats version 1
[    0.993843] Loading compiled-in X.509 certificates
[    0.994487] Loaded X.509 cert 'Build time autogenerated kernel key: 51c8d42d691c9bd960c7b21eb177ba4d2ddc4d38'
[    0.994927] Loaded X.509 cert 'Canonical Ltd. Live Patch Signing: 14df34d1a87cf37625abec039ef2bf521249b969'
[    0.995358] Loaded X.509 cert 'Canonical Ltd. Kernel Module Signing: 88f752e560a1e0737e31163a466ad7b70a850c19'
[    0.995360] blacklist: Loading compiled-in revocation X.509 certificates
[    0.995374] Loaded X.509 cert 'Canonical Ltd. Secure Boot Signing: 61482aa2830d0ab2ad5af10b7250da9033ddcef0'
[    0.995386] Loaded X.509 cert 'Canonical Ltd. Secure Boot Signing (2017): 242ade75ac4a15e50d50c84b0d45ff3eae707a03'
[    0.995399] Loaded X.509 cert 'Canonical Ltd. Secure Boot Signing (ESM 2018): 365188c1d374d6b07c3c8f240f8ef722433d6a8b'
[    0.995411] Loaded X.509 cert 'Canonical Ltd. Secure Boot Signing (2019): c0746fd6c5da3ae827864651ad66ae47fe24b3e8'
[    0.995423] Loaded X.509 cert 'Canonical Ltd. Secure Boot Signing (2021 v1): a8d54bbb3825cfb94fa13c9f8a594a195c107b8d'
[    0.995437] Loaded X.509 cert 'Canonical Ltd. Secure Boot Signing (2021 v2): 4cf046892d6fd3c9a5b03f98d845f90851dc6a8c'
[    0.995449] Loaded X.509 cert 'Canonical Ltd. Secure Boot Signing (2021 v3): 100437bb6de6e469b581e61cd66bce3ef4ed53af'
[    0.995462] Loaded X.509 cert 'Canonical Ltd. Secure Boot Signing (Ubuntu Core 2019): c1d57b8f6b743f23ee41f4f7ee292f06eecadfb9'
[    0.995535] zswap: loaded using pool lzo/zbud
[    0.996051] Key type .fscrypt registered
[    0.996053] Key type fscrypt-provisioning registered
[    0.998898] Key type encrypted registered
[    0.998901] AppArmor: AppArmor sha1 policy hashing enabled
[    0.998910] ima: No TPM chip found, activating TPM-bypass!
[    0.998912] Loading compiled-in module X.509 certificates
[    0.999358] Loaded X.509 cert 'Build time autogenerated kernel key: 51c8d42d691c9bd960c7b21eb177ba4d2ddc4d38'
[    0.999360] ima: Allocated hash algorithm: sha1
[    0.999364] ima: No architecture policies found
[    0.999374] evm: Initialising EVM extended attributes:
[    0.999374] evm: security.selinux
[    0.999376] evm: security.SMACK64
[    0.999377] evm: security.SMACK64EXEC
[    0.999377] evm: security.SMACK64TRANSMUTE
[    0.999378] evm: security.SMACK64MMAP
[    0.999378] evm: security.apparmor
[    0.999379] evm: security.ima
[    0.999379] evm: security.capability
[    0.999380] evm: HMAC attrs: 0x1
[    0.999719] PM:   Magic number: 8:388:79
[    0.999964] RAS: Correctable Errors collector initialized.
[    1.001063] Freeing unused decrypted memory: 2036K
[    1.001551] Freeing unused kernel image (initmem) memory: 3356K
[    1.032559] Write protecting the kernel read-only data: 30720k
[    1.033148] Freeing unused kernel image (text/rodata gap) memory: 2036K
[    1.033496] Freeing unused kernel image (rodata/data gap) memory: 1344K
[    1.079148] x86/mm: Checked W+X mappings: passed, no W+X pages found.
[    1.079149] x86/mm: Checking user space page tables
[    1.120938] x86/mm: Checked W+X mappings: passed, no W+X pages found.
[    1.120942] Run /init as init process
[    1.120943]   with arguments:
[    1.120944]     /init
[    1.120945]     splash
[    1.120946]   with environment:
[    1.120946]     HOME=/
[    1.120947]     TERM=linux
[    1.120948]     BOOT_IMAGE=/boot/vmlinuz-5.15.0-107-generic
[    1.227056] ACPI: video: Video Device [GFX0] (multi-head: yes  rom: no  post: no)
[    1.228888] input: Video Bus as /devices/LNXSYSTM:00/LNXSYBUS:00/PNP0A08:00/LNXVIDEO:00/input/input3
[    1.242439] xhci_hcd 0000:00:14.0: xHCI Host Controller
[    1.242445] xhci_hcd 0000:00:14.0: new USB bus registered, assigned bus number 1
[    1.243512] xhci_hcd 0000:00:14.0: hcc params 0x200077c1 hci version 0x100 quirks 0x0000000001109810
[    1.243937] xhci_hcd 0000:00:14.0: xHCI Host Controller
[    1.243941] xhci_hcd 0000:00:14.0: new USB bus registered, assigned bus number 2
[    1.243944] xhci_hcd 0000:00:14.0: Host supports USB 3.0 SuperSpeed
[    1.244609] usb usb1: New USB device found, idVendor=1d6b, idProduct=0002, bcdDevice= 5.15
[    1.244613] usb usb1: New USB device strings: Mfr=3, Product=2, SerialNumber=1
[    1.244615] usb usb1: Product: xHCI Host Controller
[    1.244616] usb usb1: Manufacturer: Linux 5.15.0-107-generic xhci-hcd
[    1.244617] usb usb1: SerialNumber: 0000:00:14.0
[    1.244858] hub 1-0:1.0: USB hub found
[    1.244873] hub 1-0:1.0: 10 ports detected
[    1.247193] usb usb2: New USB device found, idVendor=1d6b, idProduct=0003, bcdDevice= 5.15
[    1.247196] usb usb2: New USB device strings: Mfr=3, Product=2, SerialNumber=1
[    1.247198] usb usb2: Product: xHCI Host Controller
[    1.247199] usb usb2: Manufacturer: Linux 5.15.0-107-generic xhci-hcd
[    1.247200] usb usb2: SerialNumber: 0000:00:14.0
[    1.247285] hub 2-0:1.0: USB hub found
[    1.247300] hub 2-0:1.0: 4 ports detected
[    1.282995] ahci 0000:00:17.0: version 3.0
[    1.283540] ahci 0000:00:17.0: AHCI 0001.0301 32 slots 4 ports 6 Gbps 0xf impl SATA mode
[    1.283549] ahci 0000:00:17.0: flags: 64bit ncq sntf pm led clo only pio slum part ems deso sadm sds apst 
[    1.289404] cryptd: max_cpu_qlen set to 1000
[    1.289574] i801_smbus 0000:00:1f.4: SPD Write Disable is set
[    1.289622] i801_smbus 0000:00:1f.4: SMBus using PCI interrupt
[    1.295880] i2c i2c-0: 2/4 memory slots populated (from DMI)
[    1.302775] AVX2 version of gcm_enc/dec engaged.
[    1.302813] AES CTR mode by8 optimization enabled
[    1.306746] i2c i2c-0: Successfully instantiated SPD at 0x50
[    1.307727] r8169 0000:02:00.0 eth0: RTL8168g/8111g, 1c:1b:0d:cb:11:c8, XID 4c0, IRQ 131
[    1.307732] r8169 0000:02:00.0 eth0: jumbo features [frames: 9194 bytes, tx checksumming: ko]
[    1.308181] i2c i2c-0: Successfully instantiated SPD at 0x52
[    1.317224] r8169 0000:02:00.0 enp2s0: renamed from eth0
[    1.317278] scsi host0: ahci
[    1.317518] scsi host1: ahci
[    1.320485] scsi host2: ahci
[    1.324025] scsi host3: ahci
[    1.324066] ata1: SATA max UDMA/133 abar m2048@0xef22b000 port 0xef22b100 irq 130
[    1.324069] ata2: SATA max UDMA/133 abar m2048@0xef22b000 port 0xef22b180 irq 130
[    1.324071] ata3: SATA max UDMA/133 abar m2048@0xef22b000 port 0xef22b200 irq 130
[    1.324072] ata4: SATA max UDMA/133 abar m2048@0xef22b000 port 0xef22b280 irq 130
[    1.348206] Console: switching to colour dummy device 80x25
[    1.348242] nouveau 0000:01:00.0: vgaarb: deactivate vga console
[    1.348298] nouveau 0000:01:00.0: NVIDIA GP106 (136000a1)
[    1.371513] i915 0000:00:02.0: [drm] Finished loading DMC firmware i915/kbl_dmc_ver1_04.bin (v1.4)
[    1.380677] tsc: Refined TSC clocksource calibration: 2999.999 MHz
[    1.380680] clocksource: tsc: mask: 0xffffffffffffffff max_cycles: 0x2b3e44b2357, max_idle_ns: 440795324996 ns
[    1.380689] clocksource: Switched to clocksource tsc
[    1.455187] nouveau 0000:01:00.0: bios: version 86.06.0e.00.a5
[    1.455745] nouveau 0000:01:00.0: pmu: firmware unavailable
[    1.456261] nouveau 0000:01:00.0: fb: 6144 MiB GDDR5
[    1.469163] nouveau 0000:01:00.0: DRM: VRAM: 6144 MiB
[    1.469165] nouveau 0000:01:00.0: DRM: GART: 536870912 MiB
[    1.469167] nouveau 0000:01:00.0: DRM: BIT table 'A' not found
[    1.469169] nouveau 0000:01:00.0: DRM: BIT table 'L' not found
[    1.469170] nouveau 0000:01:00.0: DRM: TMDS table version 2.0
[    1.469171] nouveau 0000:01:00.0: DRM: DCB version 4.1
[    1.469173] nouveau 0000:01:00.0: DRM: DCB outp 00: 01000f42 04620030
[    1.469175] nouveau 0000:01:00.0: DRM: DCB outp 04: 04022f82 00020030
[    1.469177] nouveau 0000:01:00.0: DRM: DCB outp 06: 02033f62 04620010
[    1.469178] nouveau 0000:01:00.0: DRM: DCB outp 07: 02844f76 04600020
[    1.469179] nouveau 0000:01:00.0: DRM: DCB outp 08: 02044f72 00020020
[    1.469181] nouveau 0000:01:00.0: DRM: DCB conn 00: 00001031
[    1.469182] nouveau 0000:01:00.0: DRM: DCB conn 02: 01000231
[    1.469183] nouveau 0000:01:00.0: DRM: DCB conn 03: 00010361
[    1.469185] nouveau 0000:01:00.0: DRM: DCB conn 04: 00020446
[    1.469492] nouveau 0000:01:00.0: DRM: MM: using COPY for buffer copies
[    1.580344] usb 1-1: new high-speed USB device number 2 using xhci_hcd
[    1.638415] ata2: SATA link up 6.0 Gbps (SStatus 133 SControl 300)
[    1.638430] ata3: SATA link down (SStatus 4 SControl 300)
[    1.638452] ata1: SATA link up 6.0 Gbps (SStatus 133 SControl 300)
[    1.638484] ata2.00: ATA-11: KINGSTON SA400S37480G, SBFKB1D1, max UDMA/133
[    1.638505] ata2.00: 937703088 sectors, multi 16: LBA48 NCQ (depth 32), AA
[    1.638595] ata2.00: configured for UDMA/133
[    1.638888] ata1.00: ATA-9: WDC WD10EURX-63C57Y0, 01.01A01, max UDMA/133
[    1.639105] ata1.00: ATA Identify Device Log not supported
[    1.639106] ata1.00: 1953525168 sectors, multi 16: LBA48 NCQ (depth 32), AA
[    1.639818] ata1.00: ATA Identify Device Log not supported
[    1.639821] ata1.00: configured for UDMA/133
[    1.639893] scsi 0:0:0:0: Direct-Access     ATA      WDC WD10EURX-63C 1A01 PQ: 0 ANSI: 5
[    1.640022] sd 0:0:0:0: Attached scsi generic sg0 type 0
[    1.640070] sd 0:0:0:0: [sda] 1953525168 512-byte logical blocks: (1.00 TB/932 GiB)
[    1.640072] sd 0:0:0:0: [sda] 4096-byte physical blocks
[    1.640081] sd 0:0:0:0: [sda] Write Protect is off
[    1.640084] sd 0:0:0:0: [sda] Mode Sense: 00 3a 00 00
[    1.640098] sd 0:0:0:0: [sda] Write cache: enabled, read cache: enabled, doesn't support DPO or FUA
[    1.640106] scsi 1:0:0:0: Direct-Access     ATA      KINGSTON SA400S3 B1D1 PQ: 0 ANSI: 5
[    1.640224] sd 1:0:0:0: Attached scsi generic sg1 type 0
[    1.640296] sd 1:0:0:0: [sdb] 937703088 512-byte logical blocks: (480 GB/447 GiB)
[    1.640306] sd 1:0:0:0: [sdb] Write Protect is off
[    1.640308] sd 1:0:0:0: [sdb] Mode Sense: 00 3a 00 00
[    1.640326] sd 1:0:0:0: [sdb] Write cache: enabled, read cache: enabled, doesn't support DPO or FUA
[    1.640800]  sdb: sdb1 sdb2
[    1.640833] i915 0000:00:02.0: [drm] failed to retrieve link info, disabling eDP
[    1.640944] i915 0000:00:02.0: [drm] [ENCODER:73:DDI B/PHY B] is disabled/in DSI mode with an ungated DDI clock, gate it
[    1.640947] i915 0000:00:02.0: [drm] [ENCODER:83:DDI C/PHY C] is disabled/in DSI mode with an ungated DDI clock, gate it
[    1.640949] i915 0000:00:02.0: [drm] [ENCODER:87:DDI D/PHY D] is disabled/in DSI mode with an ungated DDI clock, gate it
[    1.640956] sd 1:0:0:0: [sdb] Attached SCSI disk
[    1.642773] [drm] Initialized i915 1.6.0 20201103 for 0000:00:02.0 on minor 0
[    1.646524] ata4: SATA link down (SStatus 4 SControl 300)
[    1.726537]  sda: sda1 sda2 sda3 sda4 < sda5 sda6 sda7 sda8 >
[    1.728291] sd 0:0:0:0: [sda] Attached SCSI disk
[    1.728938] usb 1-1: New USB device found, idVendor=2357, idProduct=0115, bcdDevice= 2.10
[    1.728949] usb 1-1: New USB device strings: Mfr=1, Product=2, SerialNumber=3
[    1.728955] usb 1-1: Product: 802.11ac NIC
[    1.728961] usb 1-1: Manufacturer: Realtek
[    1.728966] usb 1-1: SerialNumber: 123456
[    1.845088] i915 0000:00:02.0: [drm] Cannot find any crtc or sizes
[    1.856380] usb 1-5: new full-speed USB device number 3 using xhci_hcd
[    2.005950] usb 1-5: New USB device found, idVendor=03f0, idProduct=058f, bcdDevice=21.06
[    2.005954] usb 1-5: New USB device strings: Mfr=1, Product=2, SerialNumber=0
[    2.005956] usb 1-5: Product: HyperX Alloy Elite 2
[    2.005958] usb 1-5: Manufacturer: HP, Inc
[    2.010638] hid: raw HID events driver (C) Jiri Kosina
[    2.013750] usbhid 1-5:1.3: couldn't find an input interrupt endpoint
[    2.013763] usbcore: registered new interface driver usbhid
[    2.013764] usbhid: USB HID core driver
[    2.015826] input: HP, Inc HyperX Alloy Elite 2 as /devices/pci0000:00/0000:00:14.0/usb1/1-5/1-5:1.0/0003:03F0:058F.0001/input/input4
[    2.048986] i915 0000:00:02.0: [drm] Cannot find any crtc or sizes
[    2.076595] hid-generic 0003:03F0:058F.0001: input,hidraw0: USB HID v1.11 Keyboard [HP, Inc HyperX Alloy Elite 2] on usb-0000:00:14.0-5/input0
[    2.077164] input: HP, Inc HyperX Alloy Elite 2 Mouse as /devices/pci0000:00/0000:00:14.0/usb1/1-5/1-5:1.1/0003:03F0:058F.0002/input/input5
[    2.077431] input: HP, Inc HyperX Alloy Elite 2 System Control as /devices/pci0000:00/0000:00:14.0/usb1/1-5/1-5:1.1/0003:03F0:058F.0002/input/input6
[    2.136392] usb 1-6: new full-speed USB device number 4 using xhci_hcd
[    2.136598] input: HP, Inc HyperX Alloy Elite 2 Consumer Control as /devices/pci0000:00/0000:00:14.0/usb1/1-5/1-5:1.1/0003:03F0:058F.0002/input/input7
[    2.152572] input: HP, Inc HyperX Alloy Elite 2 as /devices/pci0000:00/0000:00:14.0/usb1/1-5/1-5:1.1/0003:03F0:058F.0002/input/input8
[    2.164612] hid-generic 0003:03F0:058F.0002: input,hiddev0,hidraw1: USB HID v1.11 Mouse [HP, Inc HyperX Alloy Elite 2] on usb-0000:00:14.0-5/input1
[    2.164725] input: HP, Inc HyperX Alloy Elite 2 as /devices/pci0000:00/0000:00:14.0/usb1/1-5/1-5:1.2/0003:03F0:058F.0003/input/input9
[    2.210107] nouveau 0000:01:00.0: DRM: allocated 1920x1080 fb: 0x200000, bo 00000000f417da2e
[    2.210159] fbcon: nouveaudrmfb (fb0) is primary device
[    2.248489] hid-generic 0003:03F0:058F.0003: input,hidraw2: USB HID v1.11 Keyboard [HP, Inc HyperX Alloy Elite 2] on usb-0000:00:14.0-5/input2
[    2.253580] i915 0000:00:02.0: [drm] Cannot find any crtc or sizes
[    2.293520] usb 1-6: New USB device found, idVendor=046d, idProduct=c08b, bcdDevice=27.03
[    2.293538] usb 1-6: New USB device strings: Mfr=1, Product=2, SerialNumber=3
[    2.293539] usb 1-6: Product: G502 HERO Gaming Mouse
[    2.293540] usb 1-6: Manufacturer: Logitech
[    2.293541] usb 1-6: SerialNumber: 0A6B316A3534
[    2.295022] input: Logitech G502 HERO Gaming Mouse as /devices/pci0000:00/0000:00:14.0/usb1/1-6/1-6:1.0/0003:046D:C08B.0004/input/input10
[    2.295081] hid-generic 0003:046D:C08B.0004: input,hidraw3: USB HID v1.11 Mouse [Logitech G502 HERO Gaming Mouse] on usb-0000:00:14.0-6/input0
[    2.295947] input: Logitech G502 HERO Gaming Mouse Keyboard as /devices/pci0000:00/0000:00:14.0/usb1/1-6/1-6:1.1/0003:046D:C08B.0005/input/input11
[    2.352520] hid-generic 0003:046D:C08B.0005: input,hiddev1,hidraw4: USB HID v1.11 Keyboard [Logitech G502 HERO Gaming Mouse] on usb-0000:00:14.0-6/input1
[    2.497146] Console: switching to colour frame buffer device 240x67
[    2.717107] nouveau 0000:01:00.0: [drm] fb0: nouveaudrmfb frame buffer device
[    2.740604] [drm] Initialized nouveau 1.3.1 20120801 for 0000:01:00.0 on minor 1
[    2.740618] nouveau 0000:01:00.0: DRM: Disabling PCI power management to avoid bug
[    3.792378] raid6: avx2x4   gen() 27448 MB/s
[    3.860398] raid6: avx2x4   xor() 13765 MB/s
[    3.928379] raid6: avx2x2   gen() 37439 MB/s
[    3.996378] raid6: avx2x2   xor() 22622 MB/s
[    4.064378] raid6: avx2x1   gen() 23331 MB/s
[    4.132374] raid6: avx2x1   xor() 15051 MB/s
[    4.200376] raid6: sse2x4   gen() 15812 MB/s
[    4.268378] raid6: sse2x4   xor()  9241 MB/s
[    4.336379] raid6: sse2x2   gen() 16158 MB/s
[    4.404378] raid6: sse2x2   xor()  9739 MB/s
[    4.472381] raid6: sse2x1   gen() 13589 MB/s
[    4.540378] raid6: sse2x1   xor()  6761 MB/s
[    4.540379] raid6: using algorithm avx2x2 gen() 37439 MB/s
[    4.540380] raid6: .... xor() 22622 MB/s, rmw enabled
[    4.540381] raid6: using avx2x2 recovery algorithm
[    4.543530] xor: automatically using best checksumming function   avx       
[    4.569281] Btrfs loaded, crc32c=crc32c-intel, zoned=yes, fsverity=yes
[    5.422717] EXT4-fs (sda8): mounted filesystem with ordered data mode. Opts: (null). Quota mode: none.
[    8.573178] systemd[1]: Inserted module 'autofs4'
[    8.972612] systemd[1]: systemd 249.11-0ubuntu3.12 running in system mode (+PAM +AUDIT +SELINUX +APPARMOR +IMA +SMACK +SECCOMP +GCRYPT +GNUTLS +OPENSSL +ACL +BLKID +CURL +ELFUTILS +FIDO2 +IDN2 -IDN +IPTC +KMOD +LIBCRYPTSETUP +LIBFDISK +PCRE2 -PWQUALITY -P11KIT -QRENCODE +BZIP2 +LZ4 +XZ +ZLIB +ZSTD -XKBCOMMON +UTMP +SYSVINIT default-hierarchy=unified)
[    8.992806] systemd[1]: Detected architecture x86-64.
[   17.664426] systemd[1]: Queued start job for default target Graphical Interface.
[   17.667914] systemd[1]: Created slice Slice /system/modprobe.
[   17.669036] systemd[1]: Created slice Slice /system/systemd-fsck.
[   17.669870] systemd[1]: Created slice User and Session Slice.
[   17.670153] systemd[1]: Started Forward Password Requests to Wall Directory Watch.
[   17.670726] systemd[1]: Set up automount Arbitrary Executable File Formats File System Automount Point.
[   17.670963] systemd[1]: Reached target User and Group Name Lookups.
[   17.671027] systemd[1]: Reached target Remote File Systems.
[   17.671081] systemd[1]: Reached target Slice Units.
[   17.671189] systemd[1]: Reached target Local Verity Protected Volumes.
[   17.671492] systemd[1]: Listening on Device-mapper event daemon FIFOs.
[   17.671875] systemd[1]: Listening on LVM2 poll daemon socket.
[   17.672219] systemd[1]: Listening on Syslog Socket.
[   17.675927] systemd[1]: Listening on Process Core Dump Socket.
[   17.676276] systemd[1]: Listening on fsck to fsckd communication Socket.
[   17.676508] systemd[1]: Listening on initctl Compatibility Named Pipe.
[   17.677248] systemd[1]: Listening on Journal Audit Socket.
[   17.677651] systemd[1]: Listening on Journal Socket (/dev/log).
[   17.678084] systemd[1]: Listening on Journal Socket.
[   17.693156] systemd[1]: Listening on udev Control Socket.
[   17.693504] systemd[1]: Listening on udev Kernel Socket.
[   17.695533] systemd[1]: Mounting Huge Pages File System...
[   17.697335] systemd[1]: Mounting POSIX Message Queue File System...
[   17.699158] systemd[1]: Mounting Kernel Debug File System...
[   17.700954] systemd[1]: Mounting Kernel Trace File System...
[   17.704557] systemd[1]: Starting Journal Service...
[   17.704893] systemd[1]: Finished Availability of block devices.
[   17.707936] systemd[1]: Starting Set the console keyboard layout...
[   17.709626] systemd[1]: Starting Create List of Static Device Nodes...
[   17.710271] systemd[1]: Starting Monitoring of LVM2 mirrors, snapshots etc. using dmeventd or progress polling...
[   17.711011] systemd[1]: Starting Load Kernel Module configfs...
[   17.711741] systemd[1]: Starting Load Kernel Module drm...
[   17.712469] systemd[1]: Starting Load Kernel Module efi_pstore...
[   17.713230] systemd[1]: Starting Load Kernel Module fuse...
[   17.713335] systemd[1]: Condition check resulted in File System Check on Root Device being skipped.
[   17.903202] systemd[1]: Starting Load Kernel Modules...
[   17.905711] systemd[1]: Starting Remount Root and Kernel File Systems...
[   17.908258] systemd[1]: Starting Coldplug All udev Devices...
[   17.914106] systemd[1]: Mounted Huge Pages File System.
[   17.914495] systemd[1]: Mounted POSIX Message Queue File System.
[   17.914844] systemd[1]: Mounted Kernel Debug File System.
[   17.915181] systemd[1]: Mounted Kernel Trace File System.
[   17.916181] systemd[1]: Finished Create List of Static Device Nodes.
[   17.917162] systemd[1]: modprobe@configfs.service: Deactivated successfully.
[   17.917840] systemd[1]: Finished Load Kernel Module configfs.
[   17.918693] systemd[1]: modprobe@drm.service: Deactivated successfully.
[   17.919348] systemd[1]: Finished Load Kernel Module drm.
[   17.920204] systemd[1]: modprobe@fuse.service: Deactivated successfully.
[   17.920888] systemd[1]: Finished Load Kernel Module fuse.
[   17.923755] systemd[1]: Mounting FUSE Control File System...
[   17.926472] systemd[1]: Mounting Kernel Configuration File System...
[   17.929788] systemd[1]: Mounted FUSE Control File System.
[   17.930388] systemd[1]: Mounted Kernel Configuration File System.
[   18.235305] systemd[1]: Started Journal Service.
[   18.286940] EXT4-fs (sda8): re-mounted. Opts: errors=remount-ro. Quota mode: none.
[   18.392635] systemd-journald[378]: Received client request to flush runtime journal.
[   18.964352] Adding 1130884k swap on /swapfile.  Priority:-2 extents:5 across:1163652k FS
[   19.387492] lp: driver loaded but no devices found
[   19.539603] ppdev: user-space parallel port driver
[   23.116059] mei_me 0000:00:16.0: enabling device (0000 -> 0002)
[   23.346417] ee1004 0-0050: 512 byte EE1004-compliant SPD EEPROM, read-only
[   23.346432] ee1004 0-0052: 512 byte EE1004-compliant SPD EEPROM, read-only
[   24.912097] mei_hdcp 0000:00:16.0-b638ab7e-94e2-4ea2-a552-d1c54b627f04: bound 0000:00:02.0 (ops i915_hdcp_component_ops [i915])
[   25.018482] RAPL PMU: API unit is 2^-32 Joules, 4 fixed counters, 655360 ms ovfl timer
[   25.018486] RAPL PMU: hw unit of domain pp0-core 2^-14 Joules
[   25.018487] RAPL PMU: hw unit of domain package 2^-14 Joules
[   25.018488] RAPL PMU: hw unit of domain dram 2^-14 Joules
[   25.018489] RAPL PMU: hw unit of domain pp1-gpu 2^-14 Joules
[   25.026389] cfg80211: Loading compiled-in X.509 certificates for regulatory database
[   25.026631] cfg80211: Loaded X.509 cert 'sforshee: 00b28ddf47aef9cea7'
[   25.026783] cfg80211: Loaded X.509 cert 'wens: 61c038651aabdcf94bd0ac7ff06c7248db18c600'
[   25.948703] 88x2bu: loading out-of-tree module taints kernel.
[   25.949426] 88x2bu: module verification failed: signature and/or required key missing - tainting kernel
[   26.087481] snd_hda_intel 0000:00:1f.3: bound 0000:00:02.0 (ops i915_audio_component_bind_ops [i915])
[   26.088011] snd_hda_intel 0000:01:00.1: Disabling MSI
[   26.088015] snd_hda_intel 0000:01:00.1: Handle vga_switcheroo audio client
[   26.266723] snd_hda_codec_realtek hdaudioC0D0: autoconfig for ALC887-VD: line_outs=1 (0x14/0x0/0x0/0x0/0x0) type:line
[   26.266739] snd_hda_codec_realtek hdaudioC0D0:    speaker_outs=0 (0x0/0x0/0x0/0x0/0x0)
[   26.266747] snd_hda_codec_realtek hdaudioC0D0:    hp_outs=1 (0x1b/0x0/0x0/0x0/0x0)
[   26.266754] snd_hda_codec_realtek hdaudioC0D0:    mono: mono_out=0x0
[   26.266759] snd_hda_codec_realtek hdaudioC0D0:    dig-out=0x11/0x0
[   26.266764] snd_hda_codec_realtek hdaudioC0D0:    inputs:
[   26.266769] snd_hda_codec_realtek hdaudioC0D0:      Front Mic=0x19
[   26.266775] snd_hda_codec_realtek hdaudioC0D0:      Rear Mic=0x18
[   26.266780] snd_hda_codec_realtek hdaudioC0D0:      Line=0x1a
[   26.320401] snd_hda_intel 0000:01:00.1: bound 0000:01:00.0 (ops nv50_audio_component_bind_ops [nouveau])
[   26.330412] input: HDA NVidia HDMI/DP,pcm=3 as /devices/pci0000:00/0000:00:01.0/0000:01:00.1/sound/card1/input19
[   26.330571] input: HDA NVidia HDMI/DP,pcm=7 as /devices/pci0000:00/0000:00:01.0/0000:01:00.1/sound/card1/input20
[   26.331506] input: HDA NVidia HDMI/DP,pcm=8 as /devices/pci0000:00/0000:00:01.0/0000:01:00.1/sound/card1/input21
[   26.331667] input: HDA NVidia HDMI/DP,pcm=9 as /devices/pci0000:00/0000:00:01.0/0000:01:00.1/sound/card1/input22
[   26.331907] input: HDA NVidia HDMI/DP,pcm=10 as /devices/pci0000:00/0000:00:01.0/0000:01:00.1/sound/card1/input23
[   26.331970] input: HDA NVidia HDMI/DP,pcm=11 as /devices/pci0000:00/0000:00:01.0/0000:01:00.1/sound/card1/input24
[   26.332033] input: HDA NVidia HDMI/DP,pcm=12 as /devices/pci0000:00/0000:00:01.0/0000:01:00.1/sound/card1/input25
[   26.341700] input: HDA Intel PCH Front Mic as /devices/pci0000:00/0000:00:1f.3/sound/card0/input14
[   26.350347] input: HDA Intel PCH Rear Mic as /devices/pci0000:00/0000:00:1f.3/sound/card0/input15
[   26.357042] input: HDA Intel PCH Line as /devices/pci0000:00/0000:00:1f.3/sound/card0/input16
[   26.363455] input: HDA Intel PCH Line Out as /devices/pci0000:00/0000:00:1f.3/sound/card0/input17
[   26.366533] input: HDA Intel PCH Front Headphone as /devices/pci0000:00/0000:00:1f.3/sound/card0/input18
[   26.367359] input: HDA Intel PCH HDMI/DP,pcm=3 as /devices/pci0000:00/0000:00:1f.3/sound/card0/input26
[   26.367567] input: HDA Intel PCH HDMI/DP,pcm=7 as /devices/pci0000:00/0000:00:1f.3/sound/card0/input27
[   26.367761] input: HDA Intel PCH HDMI/DP,pcm=8 as /devices/pci0000:00/0000:00:1f.3/sound/card0/input28
[   26.367949] input: HDA Intel PCH HDMI/DP,pcm=9 as /devices/pci0000:00/0000:00:1f.3/sound/card0/input29
[   26.368145] input: HDA Intel PCH HDMI/DP,pcm=10 as /devices/pci0000:00/0000:00:1f.3/sound/card0/input30
[   26.452028] usbcore: registered new interface driver rtl88x2bu
[   26.773996] rtl88x2bu 1-1:1.0 wlxc006c39f8358: renamed from wlan0
[   27.108858] intel_tcc_cooling: Programmable TCC Offset detected
[   27.685720] intel_rapl_common: Found RAPL domain package
[   27.685728] intel_rapl_common: Found RAPL domain core
[   27.685733] intel_rapl_common: Found RAPL domain uncore
[   27.685737] intel_rapl_common: Found RAPL domain dram
[   32.792194] znvpair: module license 'CDDL' taints kernel.
[   32.792202] Disabling lock debugging due to kernel taint
[   33.366935] ZFS: Loaded module v2.1.5-1ubuntu6~22.04.3, ZFS pool version 5000, ZFS filesystem version 5
[   34.970329] audit: type=1400 audit(1716210228.085:2): apparmor="STATUS" operation="profile_load" profile="unconfined" name="lsb_release" pid=688 comm="apparmor_parser"
[   34.970857] audit: type=1400 audit(1716210228.085:3): apparmor="STATUS" operation="profile_load" profile="unconfined" name="nvidia_modprobe" pid=689 comm="apparmor_parser"
[   34.970861] audit: type=1400 audit(1716210228.085:4): apparmor="STATUS" operation="profile_load" profile="unconfined" name="nvidia_modprobe//kmod" pid=689 comm="apparmor_parser"
[   34.975011] audit: type=1400 audit(1716210228.089:5): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/bin/man" pid=692 comm="apparmor_parser"
[   34.975015] audit: type=1400 audit(1716210228.089:6): apparmor="STATUS" operation="profile_load" profile="unconfined" name="man_filter" pid=692 comm="apparmor_parser"
[   34.975017] audit: type=1400 audit(1716210228.089:7): apparmor="STATUS" operation="profile_load" profile="unconfined" name="man_groff" pid=692 comm="apparmor_parser"
[   34.979548] audit: type=1400 audit(1716210228.093:8): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/bin/redshift" pid=693 comm="apparmor_parser"
[   34.981280] audit: type=1400 audit(1716210228.097:9): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/lib/NetworkManager/nm-dhcp-client.action" pid=690 comm="apparmor_parser"
[   34.981284] audit: type=1400 audit(1716210228.097:10): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/lib/NetworkManager/nm-dhcp-helper" pid=690 comm="apparmor_parser"
[   34.981286] audit: type=1400 audit(1716210228.097:11): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/lib/connman/scripts/dhclient-script" pid=690 comm="apparmor_parser"
[   50.469655] kauditd_printk_skb: 19 callbacks suppressed
[   50.469663] audit: type=1400 audit(1716210243.585:31): apparmor="DENIED" operation="capable" profile="/usr/sbin/cupsd" pid=902 comm="cupsd" capability=12  capname="net_admin"
[   50.696502] Generic FE-GE Realtek PHY r8169-0-200:00: attached PHY driver (mii_bus:phy_addr=r8169-0-200:00, irq=MAC)
[   50.900601] r8169 0000:02:00.0 enp2s0: Link is Down
[   51.568966] start_addr=(0x20000), end_addr=(0x40000), buffer_size=(0x20000), smp_number_max=(16384)
[   55.666229] start_addr=(0x20000), end_addr=(0x40000), buffer_size=(0x20000), smp_number_max=(16384)
[   60.222318] start_addr=(0x20000), end_addr=(0x40000), buffer_size=(0x20000), smp_number_max=(16384)
[   60.404702] IPv6: ADDRCONF(NETDEV_CHANGE): wlxc006c39f8358: link becomes ready
[   62.772803] audit: type=1400 audit(1716210255.889:32): apparmor="DENIED" operation="capable" profile="/usr/sbin/cups-browsed" pid=975 comm="cups-browsed" capability=23  capname="sys_nice"
[   94.569046] rfkill: input handler disabled
[  655.618408] PM: suspend entry (deep)
[  656.279649] Filesystems sync: 0.661 seconds
[  656.779966] Freezing user space processes ... (elapsed 0.002 seconds) done.
[  656.782685] OOM killer disabled.
[  656.782688] Freezing remaining freezable tasks ... (elapsed 0.001 seconds) done.
[  656.784039] printk: Suspending console(s) (use no_console_suspend to debug)
[  656.805824] sd 1:0:0:0: [sdb] Synchronizing SCSI cache
[  656.805889] sd 0:0:0:0: [sda] Synchronizing SCSI cache
[  656.806047] sd 1:0:0:0: [sdb] Stopping disk
[  656.857512] sd 0:0:0:0: [sda] Stopping disk
[  657.852638] ACPI: PM: Preparing to enter system sleep state S3
[  657.854555] ACPI: PM: Saving platform NVS memory
[  657.854626] Disabling non-boot CPUs ...
[  657.856206] smpboot: CPU 1 is now offline
[  657.858201] smpboot: CPU 2 is now offline
[  657.860327] smpboot: CPU 3 is now offline
[  657.864364] ACPI: PM: Low-level resume complete
[  657.864407] ACPI: PM: Restoring platform NVS memory
[  657.865060] Enabling non-boot CPUs ...
[  657.865094] x86: Booting SMP configuration:
[  657.865095] smpboot: Booting Node 0 Processor 1 APIC 0x2
[  657.867125] CPU1 is up
[  657.867149] smpboot: Booting Node 0 Processor 2 APIC 0x4
[  657.869203] CPU2 is up
[  657.869226] smpboot: Booting Node 0 Processor 3 APIC 0x6
[  657.871313] CPU3 is up
[  657.872285] ACPI: PM: Waking up from system sleep state S3
[  657.921092] i915 0000:00:02.0: [drm] [ENCODER:73:DDI B/PHY B] is disabled/in DSI mode with an ungated DDI clock, gate it
[  657.921105] i915 0000:00:02.0: [drm] [ENCODER:83:DDI C/PHY C] is disabled/in DSI mode with an ungated DDI clock, gate it
[  657.921112] i915 0000:00:02.0: [drm] [ENCODER:87:DDI D/PHY D] is disabled/in DSI mode with an ungated DDI clock, gate it
[  657.928788] sd 0:0:0:0: [sda] Starting disk
[  657.928898] sd 1:0:0:0: [sdb] Starting disk
[  658.251062] ata3: SATA link down (SStatus 4 SControl 300)
[  658.274994] ata4: SATA link down (SStatus 4 SControl 300)
[  658.278907] ata2: SATA link up 6.0 Gbps (SStatus 133 SControl 300)
[  658.279386] ata2.00: configured for UDMA/133
[  658.790234] start_addr=(0x20000), end_addr=(0x40000), buffer_size=(0x20000), smp_number_max=(16384)
[  658.802156] OOM killer enabled.
[  658.802157] Restarting tasks ... done.
[  658.812938] video LNXVIDEO:00: Restoring backlight state
[  658.812945] PM: suspend exit
[  658.818711] mei_hdcp 0000:00:16.0-b638ab7e-94e2-4ea2-a552-d1c54b627f04: bound 0000:00:02.0 (ops i915_hdcp_component_ops [i915])
[  663.316668] ata1: link is slow to respond, please be patient (ready=0)
[  664.156694] ata1: SATA link up 6.0 Gbps (SStatus 133 SControl 300)
[  664.277522] ata1.00: ATA Identify Device Log not supported
[  664.278885] ata1.00: ATA Identify Device Log not supported
[  664.278903] ata1.00: configured for UDMA/133
[  664.536543] Generic FE-GE Realtek PHY r8169-0-200:00: attached PHY driver (mii_bus:phy_addr=r8169-0-200:00, irq=MAC)
[  664.736625] r8169 0000:02:00.0 enp2s0: Link is Down
[  664.836160] ------------[ cut here ]------------
[  664.836162] URB ffff98b386314600 submitted while active
[  664.836172] WARNING: CPU: 1 PID: 748 at drivers/usb/core/urb.c:378 usb_submit_urb+0x618/0x6d0
[  664.836177] Modules linked in: binfmt_misc zfs(PO) zunicode(PO) zzstd(O) zlua(O) zavl(PO) icp(PO) zcommon(PO) znvpair(PO) spl(O) nls_iso8859_1 intel_rapl_msr intel_rapl_common intel_tcc_cooling x86_pkg_temp_thermal intel_powerclamp coretemp snd_hda_codec_hdmi snd_hda_codec_realtek snd_hda_codec_generic ledtrig_audio snd_hda_intel kvm_intel 88x2bu(OE) snd_intel_dspcfg kvm snd_intel_sdw_acpi snd_seq_midi snd_seq_midi_event snd_rawmidi joydev input_leds snd_hda_codec snd_seq cfg80211 snd_hda_core rapl mei_hdcp snd_seq_device intel_cstate snd_hwdep snd_pcm snd_timer ee1004 snd mei_me mac_hid soundcore mei intel_wmi_thunderbolt acpi_pad sch_fq_codel msr parport_pc ppdev lp parport efi_pstore ip_tables x_tables autofs4 btrfs blake2b_generic xor zstd_compress raid6_pq libcrc32c dm_mirror dm_region_hash dm_log hid_generic usbhid hid i915 nouveau mxm_wmi i2c_algo_bit drm_ttm_helper ttm crct10dif_pclmul crc32_pclmul drm_kms_helper ghash_clmulni_intel syscopyarea sha256_ssse3 sha1_ssse3
[  664.836231]  aesni_intel sysfillrect sysimgblt fb_sys_fops cec crypto_simd i2c_i801 rc_core r8169 cryptd i2c_smbus realtek ahci libahci drm xhci_pci xhci_pci_renesas wmi video
[  664.836242] CPU: 1 PID: 748 Comm: wpa_supplicant Tainted: P           OE     5.15.0-107-generic #117-Ubuntu
[  664.836245] Hardware name: Gigabyte Technology Co., Ltd. H110M-H/H110M-H-CF, BIOS F22a 07/06/2017
[  664.836246] RIP: 0010:usb_submit_urb+0x618/0x6d0
[  664.836248] Code: bd 3e 00 83 e3 01 b8 f0 ff ff ff 0f 85 55 fc ff ff 4c 89 f6 48 c7 c7 60 65 4a a6 89 45 d0 c6 05 65 ab 84 01 01 e8 d8 4f 37 00 <0f> 0b 8b 45 d0 e9 32 fc ff ff b8 ed ff ff ff e9 28 fc ff ff 66 90
[  664.836250] RSP: 0018:ffffab6f810cb348 EFLAGS: 00010286
[  664.836252] RAX: 0000000000000000 RBX: 0000000000000000 RCX: 0000000000000027
[  664.836254] RDX: ffff98b8b6ca0588 RSI: 0000000000000001 RDI: ffff98b8b6ca0580
[  664.836255] RBP: ffffab6f810cb398 R08: 0000000000000003 R09: fffffffffffd1898
[  664.836256] R10: ffffffffa8048010 R11: 000000000000000f R12: ffff98b38c018000
[  664.836257] R13: ffff98b38b180000 R14: ffff98b386314600 R15: ffff98b39abb5000
[  664.836258] FS:  00007fbef1251800(0000) GS:ffff98b8b6c80000(0000) knlGS:0000000000000000
[  664.836259] CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033
[  664.836261] CR2: 000018b300d03528 CR3: 0000000113cb8001 CR4: 00000000003706e0
[  664.836262] Call Trace:
[  664.836263]  <TASK>
[  664.836265]  ? show_trace_log_lvl+0x1d6/0x2ea
[  664.836268]  ? show_trace_log_lvl+0x1d6/0x2ea
[  664.836271]  ? usb_read_port+0x15b/0x200 [88x2bu]
[  664.836331]  ? show_regs.part.0+0x23/0x29
[  664.836333]  ? show_regs.cold+0x8/0xd
[  664.836334]  ? usb_submit_urb+0x618/0x6d0
[  664.836336]  ? __warn+0x8c/0x100
[  664.836338]  ? usb_submit_urb+0x618/0x6d0
[  664.836340]  ? report_bug+0xa4/0xd0
[  664.836344]  ? handle_bug+0x39/0x90
[  664.836347]  ? exc_invalid_op+0x19/0x70
[  664.836350]  ? asm_exc_invalid_op+0x1b/0x20
[  664.836353]  ? usb_submit_urb+0x618/0x6d0
[  664.836354]  ? usb_submit_urb+0x618/0x6d0
[  664.836356]  ? usb_write16+0x3b/0x60 [88x2bu]
[  664.836412]  usb_read_port+0x15b/0x200 [88x2bu]
[  664.836463]  ? usb_recv_tasklet+0xe0/0xe0 [88x2bu]
[  664.836537]  rtl8822bu_inirp_init+0x53/0x80 [88x2bu]
[  664.836593]  rtw_hal_inirp_init+0x12/0x20 [88x2bu]
[  664.836675]  usb_intf_start+0x16/0x30 [88x2bu]
[  664.836739]  rtw_intf_start+0x17/0x30 [88x2bu]
[  664.836790]  _halmac_init_hal+0xb7/0x160 [88x2bu]
[  664.836842]  rtw_halmac_init_hal_fw+0xe/0x20 [88x2bu]
[  664.836894]  rtl8822b_init+0x34/0xb0 [88x2bu]
[  664.836946]  rtl8822bu_init+0x1a/0x60 [88x2bu]
[  664.836998]  rtw_hal_init+0x39/0x130 [88x2bu]
[  664.837050]  rtw_ips_pwr_up+0x3b/0x80 [88x2bu]
[  664.837101]  _ips_leave+0x50/0x90 [88x2bu]
[  664.837142]  _rtw_pwr_wakeup+0x1ea/0x230 [88x2bu]
[  664.837184]  cfg80211_rtw_scan+0x401/0x870 [88x2bu]
[  664.837236]  ? update_load_avg+0x82/0x660
[  664.837239]  ? set_next_entity+0xe9/0x230
[  664.837242]  ? pick_next_task_fair+0x242/0x510
[  664.837245]  ? save_fpregs_to_fpstate+0x3f/0xa0
[  664.837249]  ? finish_task_switch.isra.0+0x7e/0x280
[  664.837251]  ? timerqueue_del+0x31/0x50
[  664.837254]  ? __remove_hrtimer+0x48/0xa0
[  664.837257]  ? hrtimer_try_to_cancel.part.0+0x54/0xe0
[  664.837260]  ? schedule_hrtimeout_range_clock+0xc3/0x140
[  664.837262]  ? remove_wait_queue+0x47/0x50
[  664.837264]  ? fput+0x13/0x20
[  664.837266]  ? _raw_spin_unlock_bh+0x1e/0x30
[  664.837268]  ? packet_poll+0xee/0x170
[  664.837271]  ? do_select+0x5de/0x850
[  664.837274]  rdev_scan+0x2a/0xb0 [cfg80211]
[  664.837301]  cfg80211_scan+0xf6/0x120 [cfg80211]
[  664.837320]  nl80211_trigger_scan+0x47e/0x930 [cfg80211]
[  664.837342]  genl_family_rcv_msg_doit+0xe4/0x150
[  664.837346]  genl_rcv_msg+0xe2/0x1f0
[  664.837347]  ? nl80211_send_scan_start+0xb0/0xb0 [cfg80211]
[  664.837368]  ? genl_get_cmd+0xe0/0xe0
[  664.837370]  netlink_rcv_skb+0x53/0x100
[  664.837372]  genl_rcv+0x29/0x40
[  664.837374]  netlink_unicast+0x220/0x340
[  664.837376]  netlink_sendmsg+0x24b/0x4c0
[  664.837378]  __sock_sendmsg+0x66/0x70
[  664.837380]  ____sys_sendmsg+0x252/0x290
[  664.837382]  ? import_iovec+0x31/0x40
[  664.837385]  ? sendmsg_copy_msghdr+0x7f/0xa0
[  664.837388]  ___sys_sendmsg+0x81/0xc0
[  664.837390]  ? sock_getsockopt+0x110/0xdb0
[  664.837392]  ? sock_do_ioctl+0x42/0x100
[  664.837394]  ? sock_do_ioctl+0x42/0x100
[  664.837396]  ? unix_ioctl+0x168/0x1e0
[  664.837398]  ? __cond_resched+0x1a/0x50
[  664.837401]  ? aa_sk_perm+0x43/0x1c0
[  664.837404]  ? _copy_from_user+0x31/0x70
[  664.837405]  ? netlink_setsockopt+0x345/0x440
[  664.837407]  ? __cond_resched+0x1a/0x50
[  664.837409]  ? aa_sk_perm+0x43/0x1c0
[  664.837412]  __sys_sendmsg+0x62/0xc0
[  664.837414]  ? probe_wakeup+0x150/0x400
[  664.837418]  __x64_sys_sendmsg+0x1d/0x30
[  664.837420]  x64_sys_call+0x1bf7/0x1fa0
[  664.837423]  do_syscall_64+0x56/0xb0
[  664.837426]  ? exit_to_user_mode_prepare+0x37/0xb0
[  664.837429]  ? syscall_exit_to_user_mode+0x35/0x50
[  664.837431]  ? x64_sys_call+0x1e5f/0x1fa0
[  664.837433]  ? do_syscall_64+0x63/0xb0
[  664.837435]  entry_SYSCALL_64_after_hwframe+0x67/0xd1
[  664.837437] RIP: 0033:0x7fbef16cf967
[  664.837440] Code: 0f 00 f7 d8 64 89 02 48 c7 c0 ff ff ff ff eb b9 0f 1f 00 f3 0f 1e fa 64 8b 04 25 18 00 00 00 85 c0 75 10 b8 2e 00 00 00 0f 05 <48> 3d 00 f0 ff ff 77 51 c3 48 83 ec 28 89 54 24 1c 48 89 74 24 10
[  664.837441] RSP: 002b:00007fff1b6ac7c8 EFLAGS: 00000246 ORIG_RAX: 000000000000002e
[  664.837443] RAX: ffffffffffffffda RBX: 00005637fb618ac0 RCX: 00007fbef16cf967
[  664.837445] RDX: 0000000000000000 RSI: 00007fff1b6ac800 RDI: 0000000000000006
[  664.837446] RBP: 00005637fb618da0 R08: 0000000000000004 R09: 00005637fb6f8b80
[  664.837447] R10: 00007fff1b6ac8e0 R11: 0000000000000246 R12: 00005637fb6fad00
[  664.837448] R13: 00007fff1b6ac800 R14: 0000000000000000 R15: 0000000000000000
[  664.837450]  </TASK>
[  664.837463] ---[ end trace b7e4b275285f8f85 ]---
[  665.451043] start_addr=(0x20000), end_addr=(0x40000), buffer_size=(0x20000), smp_number_max=(16384)
[  673.120054] start_addr=(0x20000), end_addr=(0x40000), buffer_size=(0x20000), smp_number_max=(16384)
[  673.290793] IPv6: ADDRCONF(NETDEV_CHANGE): wlxc006c39f8358: link becomes ready
[  673.337290] rfkill: input handler enabled
[  682.651935] rfkill: input handler disabled
[  857.118819] start_addr=(0x20000), end_addr=(0x40000), buffer_size=(0x20000), smp_number_max=(16384)
[  858.922847] start_addr=(0x20000), end_addr=(0x40000), buffer_size=(0x20000), smp_number_max=(16384)
[  863.679065] start_addr=(0x20000), end_addr=(0x40000), buffer_size=(0x20000), smp_number_max=(16384)
[  867.393911] IPv6: ADDRCONF(NETDEV_CHANGE): wlxc006c39f8358: link becomes ready
[ 2007.770586] Modulo cargado en el kernel.
```

Luego, se ejecuta la instruccion `modinfo mimodulo.ko > info_module.txt`, obteniendose:

```
filename:       /home/fedefedev/Documents/practicos_SdC_2024/practico4/kernel-modules/part1/module/mimodulo.ko
author:         Catedra de SdeC
description:    Primer modulo ejemplo
license:        GPL
srcversion:     C6390D617B2101FB1B600A9
depends:        
retpoline:      Y
name:           mimodulo
vermagic:       5.15.0-107-generic SMP mod_unload modversions 
```