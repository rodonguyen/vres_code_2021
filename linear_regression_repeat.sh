#!/bin/bash

rm -f vpython*.txt

# Prompt filename and execute the file using vPython / python3.9
# Make sure the files are in consecutively-numbered ascending order to have the renaming done correctly. 
# Otherwise, the renaming will be a mess.

################################ CAR #################################
# for i in {1..200}
# do
#     begin=$(printf "Executing car.py (%03d)" "$i")
#     echo
#     echo "_____________________"
#     echo "$begin"
#     python3.9 ./linear_regression_additional/code/car.py
#     killall -9 python3.9

#     # Renaming
#     new=$(printf "vpython_car_%03d.txt" "$i")
#     mv vpython.txt "$new"
#     echo "Renamed to $new"
#     echo 
# done
# # Move all trace files to a folder
# mv vpython*.txt linear_regression_additional/trace_car_only

################################ DIABETES #################################
for i in {1..200}
do
    begin=$(printf "Executing diabetes.py (%03d)" "$i")
    echo
    echo "_____________________"
    echo "$begin"
    python3.9 ./linear_regression_additional/code/diabetes.py
    killall -9 python3.9

    # Renaming
    new=$(printf "vpython_diabetes_%03d.txt" "$i")
    mv vpython.txt "$new"
    echo "Renamed to $new"
    echo 
done
# Move all trace files to a folder
mv vpython*.txt linear_regression_additional/trace_diabetes_only


################################ ENERGY #################################
for i in {1..200}
do
    begin=$(printf "Executing energy.py (%03d)" "$i")
    echo
    echo "_____________________"
    echo "$begin"
    python3.9 ./linear_regression_additional/code/energy.py
    killall -9 python3.9

    # Renaming
    new=$(printf "vpython_energy_%03d.txt" "$i")
    mv vpython.txt "$new"
    echo "Renamed to $new"
    echo 
done
# Move all trace files to a folder
mv vpython*.txt linear_regression_additional/trace_energy_only


############################## HOUSE ###################################
for i in {1..200}
do
    begin=$(printf "Executing house.py (%03d)" "$i")
    echo
    echo "_____________________"
    echo "$begin"
    python3.9 ./linear_regression_additional/code/house.py
    killall -9 python3.9

    # Renaming
    new=$(printf "vpython_house_%03d.txt" "$i")
    mv vpython.txt "$new"
    echo "Renamed to $new"
    echo 
done
# Move all trace files to a folder
mv vpython*.txt linear_regression_additional/trace_house_only


############################# MEDICAL ####################################
for i in {1..200}
do
    begin=$(printf "Executing medical.py (%03d)" "$i")
    echo
    echo "_____________________"
    echo "$begin"
    python3.9 ./linear_regression_additional/code/medical.py
    killall -9 python3.9

    # Renaming
    new=$(printf "vpython_medical_%03d.txt" "$i")
    mv vpython.txt "$new"
    echo "Renamed to $new"
    echo 
done
# Move all trace files to a folder
mv vpython*.txt linear_regression_additional/trace_medical_only



spd-say done