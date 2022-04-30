#!/bin/bash


# Clean vPython.txt in current directory
rm -f vpython*.txt

# Create directories to store traces
mkdir linear_regression_real/trace_energy_only
mkdir linear_regression_real/trace_house_only
mkdir linear_regression_real/trace_medical_only


# Prompt filename and execute the file using vPython / python3.9
# Make sure the files are in consecutively-numbered ascending order to have the renaming done correctly. 
# Otherwise, the renaming will be a mess.


################################ ENERGY #################################
for i in {1..200}
do
    begin=$(printf "Executing energy.py (%03d)" "$i")
    echo
    echo "_____________________"
    echo "$begin"
    python3.9 ./linear_regression_real/code_decor/energy.py
    killall -9 python3.9

    # Renaming
    new=$(printf "vpython_energy_%03d.txt" "$i")
    mv vpython.txt "$new"
    echo "Renamed to $new"
    echo 
done
# Move all trace files to a folder
mv vpython*.txt linear_regression_real/trace_energy_only


############################## HOUSE ###################################
for i in {1..200}
do
    begin=$(printf "Executing house.py (%03d)" "$i")
    echo
    echo "_____________________"
    echo "$begin"
    python3.9 ./linear_regression_real/code_decor/house.py
    killall -9 python3.9

    # Renaming
    new=$(printf "vpython_house_%03d.txt" "$i")
    mv vpython.txt "$new"
    echo "Renamed to $new"
    echo 
done
# Move all trace files to a folder
mv vpython*.txt linear_regression_real/trace_house_only


############################# MEDICAL ####################################
for i in {1..200}
do
    begin=$(printf "Executing medical.py (%03d)" "$i")
    echo
    echo "_____________________"
    echo "$begin"
    python3.9 ./linear_regression_real/code_decor/medical.py
    killall -9 python3.9

    # Renaming
    new=$(printf "vpython_medical_%03d.txt" "$i")
    mv vpython.txt "$new"
    echo "Renamed to $new"
    echo 
done
# Move all trace files to a folder
mv vpython*.txt linear_regression_real/trace_medical_only



spd-say done