#!/bin/bash
echo Monitoring CPU and memory usage.....

# Get both timestamp and cpu usage of python3.9
top -bd 0.5 -o +%CPU | grep "top - \|python3.9" > cpu_usage.log

# top -bd 0.5 -o +%CPU | grep "load average" -A 9 > memory_cpu_usage.log