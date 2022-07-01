#!/bin/bash

# Clean vPython.txt in current directory and traces
rm -f vpython*.txt
rm -r linear_regression_real/trace*

# Create directories to store traces
mkdir neural_network/trace_car

run_num=100

# Prompt filename and execute the file using vPython / python3.9
# Make sure the files are in consecutively-numbered ascending order to have the renaming done correctly. 
# Otherwise, the renaming will be a mess.

################################ CAR #################################
for (( i=1; i<=$run_num; i++ ))
do
    begin=$(printf "Executing car.py (%03d)" "$i")
    echo "_____________________"
    echo "$begin"
    python3.9 ./neural_network/car.py
    killall -9 python3.9

    # Renaming
    new=$(printf "vpython_car_%03d.txt" "$i")
    mv vpython.txt "$new"
    echo "Renamed to $new"
    echo 
done
# Move all trace files to a folder
mv vpython*.txt neural_network/trace_car

python3.8 neural_network/run_analysis_script.py
spd-say done