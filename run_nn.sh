#!/bin/bash

# Clean vPython.txt in current directory and traces
rm -f vpython*.txt

# Create directories to store traces
dir010="programs/neural_network/trace_car"
dir020="programs/neural_network/trace_diabetes"
dir030="programs/neural_network/trace_energy"
dir040="programs/neural_network/trace_house"
dir050="programs/neural_network/trace_medical"

mkdir $dir010
mkdir $dir020
mkdir $dir030
mkdir $dir040
mkdir $dir050

run_num=10

# Prompt filename and execute the file using vPython / python3.9
# Make sure the files are in consecutively-numbered ascending order to have the renaming done correctly. 
# Otherwise, the renaming will be a mess.

# ################################ CAR #################################
for (( i=1; i<=$run_num; i++ ))
do
    begin=$(printf "Executing car.py (%03d)" "$i")
    echo "_____________________"
    echo "$begin"
    python3.9 ./programs/neural_network/car.py
    killall -9 python3.9

    # Renaming
    new=$(printf "vpython_car_%03d.txt" "$i")
    mv vpython.txt "$new"
    echo "Renamed to $new"
    echo 
done
# Move all trace files to a folder
mv vpython*.txt $dir010


############################### DIABETES #################################
for (( i=1; i<=$run_num; i++ ))
do
    begin=$(printf "Executing diabetes.py (%03d)" "$i")
    echo "_____________________"
    echo "$begin"
    python3.9 ./programs/neural_network/diabetes.py
    killall -9 python3.9

    # Renaming
    new=$(printf "vpython_diabetes_%03d.txt" "$i")
    mv vpython.txt "$new"
    echo "Renamed to $new"
    echo 
done
# Move all trace files to a folder
mv vpython*.txt $dir020


############################### ENERGY #################################
for (( i=1; i<=$run_num; i++ ))
do
    begin=$(printf "Executing energy.py (%03d)" "$i")
    echo "_____________________"
    echo "$begin"
    python3.9 ./programs/neural_network/energy.py
    killall -9 python3.9

    # Renaming
    new=$(printf "vpython_energy_%03d.txt" "$i")
    mv vpython.txt "$new"
    echo "Renamed to $new"
    echo 
done
# Move all trace files to a folder
mv vpython*.txt $dir030


############################## HOUSE ###################################
for (( i=1; i<=$run_num; i++ ))
do
    begin=$(printf "Executing house.py (%03d)" "$i")
    echo "_____________________"
    echo "$begin"
    python3.9 ./programs/neural_network/house.py
    killall -9 python3.9

    # Renaming
    new=$(printf "vpython_house_%03d.txt" "$i")
    mv vpython.txt "$new"
    echo "Renamed to $new"
    echo 
done
# Move all trace files to a folder
mv vpython*.txt $dir040



############################# MEDICAL ####################################
for (( i=1; i<=$run_num; i++ ))
do
    begin=$(printf "Executing medical.py (%03d)" "$i")
    echo "_____________________"
    echo "$begin"
    python3.9 ./programs/neural_network/medical.py
    killall -9 python3.9

    # Renaming
    new=$(printf "vpython_medical_%03d.txt" "$i")
    mv vpython.txt "$new"
    echo "Renamed to $new"
    echo 
done
# Move all trace files to a folder
mv vpython*.txt $dir050


python3.8 neural_network/run_analysis_script.py
spd-say done