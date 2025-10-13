1) middle layer that sits between hardware and higher-level software like OS.
2) Firmware translates software instructions into low-level hardware operations.
3) whenever we power on any device firmware is the first code that runs, it initializes the hardware and also loads the operating system (bootloader is also a type of firmware)
4) In raspberry pi, firmware controls the fan speed, power management, camera interface, GPU initialization before linux starts, etc.
5) Each piece of hardware has its own firmware tailored to its job. 
6) primary firmware (boot firmware) present on EEPROM to load OS, GPU/VideoCore Firmware sets up the CPU, device specific firmwares (Wi-fi, fan, camera, PMIC, etc.)

So firmware is the permanent software inside hardware that tells it how to work and talk to the OS. Its not easily changed as apps/OS, but not as fixed as pure hardware. 