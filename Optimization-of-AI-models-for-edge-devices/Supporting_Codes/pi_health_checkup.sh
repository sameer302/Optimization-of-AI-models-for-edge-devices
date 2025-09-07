#!/bin/bash

echo "=== Raspberry Pi 5 Health Check ==="

echo -e "\n1. Temperature:"
vcgencmd measure_temp

echo -e "\n2. Throttling Status:"
vcgencmd get_throttled

echo -e "\n3. Power Supply Voltage Warnings:"
dmesg | grep -i "under-voltage"

echo -e "\n4. Storage Usage:"
df -h

echo -e "\n5. Memory Usage:"
free -h

echo -e "\n6. Kernel Messages (dmesg):"
dmesg -T | tail -n 20

echo -e "\n7. Critical System Service Logs:"
journalctl -p 3 -xb

echo -e "\n8. Top Processes (htop):"
echo "Tip: Run 'htop' manually for interactive view."

echo -e "\n9. System Updates Check:"
sudo apt update && sudo apt full-upgrade -y

echo -e "\n10. RPi-Monitor Installation (optional):"
echo "Tip: Run 'sudo apt install rpi-monitor' if desired."

echo -e "Give execute permission: chmod +x pi_health_check.sh"