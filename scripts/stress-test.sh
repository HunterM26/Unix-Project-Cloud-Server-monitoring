#!/bin/bash

echo "03/14/2025 00:20:41: Starting stress test..." >> /var/log/stress_test.log
stress-ng --cpu 2 --timeout 30s &
stress-ng --vm 1 --vm-bytes 512M --timeout 30s &
stress-ng --io 1 --timeout 30s &
echo "03/14/2025 00:20:41: Stress test completed." >> /var/log/stress_test.log
