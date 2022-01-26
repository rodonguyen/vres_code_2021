#!/bin/bash
top -bd 0.5 -o +%MEM | grep "load average" -A 9 > memory_usage.log