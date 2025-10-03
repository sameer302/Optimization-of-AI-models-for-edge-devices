1) It is a virtual filesystem in Linux (usually mounted at /sys).
2) It exposes kernel objects, attributes and their relationships in a file-like structure.
3) It lets us see and control kernel internals (like devices, drivers, power, thermal zones, CPU frequency, etc.) from user space - just by reading/writing files.
4) Each attribute (like fan speed, CPU frequency, device ID) is shown as a simple text file. We can either read a file to get kernel state or write to a file to change the kernel state.
5) Its not a real filesystem, no disk storage, it's created dynamically by kernel.
6) Everything is a plain text file. 
7) It is an interface to access kernel-managed hardware states which tell the firmware what to do.