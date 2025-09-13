#!/bin/bash

# --- This script is designed to be run before and after a test ---

echo "=== Raspberry Pi Health Snapshot ==="
echo "Timestamp: $(date)"

echo -e "\n1. Core Temperature:"
vcgencmd measure_temp

echo -e "\n2. Throttling & Power Status:"
# This is the most critical check. 0x0 is a perfect score.
vcgencmd get_throttled

echo -e "\n3. Memory Usage:"
free -h

echo -e "\n4. New Kernel Warnings/Errors since boot:"
# This will show if any new hardware or driver issues have appeared.
dmesg -l err,warn

echo -e "\n--- Snapshot Complete ---"