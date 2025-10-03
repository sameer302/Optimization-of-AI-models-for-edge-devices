1) Full form: VideoCore General Command
2) Talks to VideoCore GPU Firmware which is a low-level controller that manages Pi's hardware.
3) Using this we can query hardware state and settings that are not always exposed via Linux sysfs.
4) sysfs is like kernel interface but vcgencmd is like firmware interface and it gives extra info like throttling status, voltage rails, clock speeds, that sysfs does not expose.