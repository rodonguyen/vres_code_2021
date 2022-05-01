#!/bin/bash


# Clean vPython.txt in current directory
rm -f vpython*.txt
rm -r simple_one/trace*

# Create directories to store traces
mkdir simple_one/trace_pandas_play
mkdir simple_one/trace_print_nothing


# Prompt filename and execute the file using vPython / python3.9
# Make sure the files are in consecutively-numbered ascending order to have the renaming done correctly. 
# Otherwise, the renaming will be a mess.

################################ CAR #################################
for i in {1..5}
do
    begin=$(printf "Executing pandas_play.py (%03d)" "$i")
    echo "_____________________"
    echo "$begin"
    python3.9 ./simple_one/pandas_play.py
    killall -9 python3.9

    # Renaming
    new=$(printf "vpython_pandas_play_%03d.txt" "$i")
    mv vpython.txt "$new"
    echo "Renamed to $new"
    echo 
done
# Move all trace files to a folder
mv vpython*.txt simple_one/trace_pandas_play


############################### DIABETES #################################
for i in {1..5}
do
    begin=$(printf "Executing print_nothing.py (%03d)" "$i")
    echo "_____________________"
    echo "$begin"
    python3.9 ./simple_one/print_nothing.py
    killall -9 python3.9

    # Renaming
    new=$(printf "vpython_print_nothing_%03d.txt" "$i")
    mv vpython.txt "$new"
    echo "Renamed to $new"
    echo 
done
# Move all trace files to a folder
mv vpython*.txt simple_one/trace_print_nothing


python3.8 utils/run_script.py

spd-say done