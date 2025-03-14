#!/bin/bash
if ! pgrep -f monitoring_api.py > /dev/null; then
    echo "03/14/2025 00:20:47: API is down. Restarting..." >> /var/log/api_monitor.log
    python3 /path/to/api/monitoring_api.py &
fi
