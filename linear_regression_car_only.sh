#!/bin/bash
rm -f vpython*.txt

# Prompt filename and execute the file using vPython / python3.9
# Make sure the files are in consecutively-numbered ascending order to have the renaming done correctly. 
# Otherwise, the renaming will be a mess.

for i in {1..100}
do
    begin=$(printf "Executing car.py (%03d)" "$i")
    echo
    echo "_____________________"
    echo "$begin"
    python3.9 ./linear_regression_additional/code/car.py
    killall -9 python3.9

    # Renaming
    new=$(printf "vpython_LRcar_%03d.txt" "$i")
    mv vpython.txt "$new"
    echo "Renamed to $new"
    echo 
done


# Move all trace files to a folder
mv vpython*.txt linear_regression_additional/trace_car_only

spd-say done