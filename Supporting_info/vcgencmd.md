- Full form: VideoCore General Command

- Talks to VideoCore GPU Firmware which is a low-level controller that manages Pi's hardware.

- Using this we can query hardware state and settings that are not always exposed via Linux sysfs.

- sysfs is like kernel interface but vcgencmd is like firmware interface and it gives extra info like throttling status, voltage rails, clock speeds, that sysfs does not expose.