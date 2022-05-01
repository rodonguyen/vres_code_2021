#!/bin/bash



# Clean vPython.txt in current directory
rm -f vpython*.txt

# Create directories to store traces
mkdir linear_regression_real/trace_car_only
mkdir linear_regression_real/trace_diabetes_only

# Prompt filename and execute the file using vPython / python3.9
# Make sure the files are in consecutively-numbered ascending order to have the renaming done correctly. 
# Otherwise, the renaming will be a mess.

################################ CAR #################################
for i in {1..100}
do
    begin=$(printf "Executing car.py (%03d)" "$i")
    echo
    echo "_____________________"
    echo "$begin"
    python3.9 ./linear_regression_real/code_decor/car.py
    killall -9 python3.9

    # Renaming
    new=$(printf "vpython_car_%03d.txt" "$i")
    mv vpython.txt "$new"
    echo "Renamed to $new"
    echo 
done
# Move all trace files to a folder
mv vpython*.txt linear_regression_real/trace_car_only


############################### DIABETES #################################
for i in {1..100}
do
    begin=$(printf "Executing diabetes.py (%03d)" "$i")
    echo
    echo "_____________________"
    echo "$begin"
    python3.9 ./linear_regression_real/code_decor/diabetes.py
    killall -9 python3.9

    # Renaming
    new=$(printf "vpython_diabetes_%03d.txt" "$i")
    mv vpython.txt "$new"
    echo "Renamed to $new"
    echo 
done
# Move all trace files to a folder
mv vpython*.txt linear_regression_real/trace_diabetes_only




spd-say done