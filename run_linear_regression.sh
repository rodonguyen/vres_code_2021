#!/bin/bash


# Clean vPython.txt in current directory and targeted trace dirs
rm -f vpython*.txt
rm -r programs/linear_regression/trace_*

# Create directories to store traces
dir001="programs/linear_regression/trace_car"
dir002="programs/linear_regression/trace_energy"
dir003="programs/linear_regression/trace_house"
dir004="programs/linear_regression/trace_medical"

program001="./programs/linear_regression/code_shortened_data/car.py"
program002="./programs/linear_regression/code_shortened_data/energy.py"
program003="./programs/linear_regression/code_shortened_data/house.py"
program004="./programs/linear_regression/code_shortened_data/medical.py"

mkdir $dir001
mkdir $dir002
mkdir $dir003
mkdir $dir004

run_num=5

# Prompt filename and execute the file using vPython / python3.9
# Make sure the files are in consecutively-numbered ascending order to have the renaming done correctly. 
# Otherwise, the renaming will be a mess.

################################ 1 #################################
for (( i=1; i<=$run_num; i++ ))
do
    begin=$(printf "Executing $program001 (%03d)" "$i")
    echo "_____________________"
    echo "$begin"
    python3.9 $program001
    killall -9 python3.9

    # Renaming
    new=$(printf "vpython1_%03d.txt" "$i")
    mv vpython.txt "$new"
    echo "Renamed to $new"
    echo 
done
# Move all trace files to a folder
mv vpython*.txt $dir001

# ############################### 2 #################################
for (( i=1; i<=$run_num; i++ ))
do
    begin=$(printf "Executing $program002 (%03d)" "$i")
    echo "_____________________"
    echo "$begin"
    python3.9 $program002
    killall -9 python3.9

    # Renaming
    new=$(printf "vpython2_%03d.txt" "$i")
    mv vpython.txt "$new"
    echo "Renamed to $new"
    echo 
done
# Move all trace files to a folder
mv vpython*.txt $dir002

# ############################### 3 #################################
for (( i=1; i<=$run_num; i++ ))
do
    begin=$(printf "Executing $program003 (%03d)" "$i")
    echo "_____________________"
    echo "$begin"
    python3.9 $program003
    killall -9 python3.9

    # Renaming
    new=$(printf "vpython3_%03d.txt" "$i")
    mv vpython.txt "$new"
    echo "Renamed to $new"
    echo 
done
# Move all trace files to a folder
mv vpython*.txt $dir003


# ################################ 4 #################################
for (( i=1; i<=$run_num; i++ ))
do
    begin=$(printf "Executing $program004 (%03d)" "$i")
    echo "_____________________"
    echo "$begin"
    python3.9 $program004
    killall -9 python3.9

    # Renaming
    new=$(printf "vpython4_%03d.txt" "$i")
    mv vpython.txt "$new"
    echo "Renamed to $new"
    echo 
done
# Move all trace files to a folder
mv vpython*.txt $dir004


# python programs/run_analysis_script.py
spd-say done