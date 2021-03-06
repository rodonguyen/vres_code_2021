#!/bin/bash

# Clean vPython.txt in current directory and traces
rm -f vpython*.txt
rm -r linear_regression_real/trace*

# Create directories to store traces
mkdir linear_regression_real/trace_car_testResult
# mkdir linear_regression_real/trace_diabetes_only
# mkdir linear_regression_real/trace_energy_only
# mkdir linear_regression_real/trace_house_only
# mkdir linear_regression_real/trace_medical_only

run_num=10

# Prompt filename and execute the file using vPython / python3.9
# Make sure the files are in consecutively-numbered ascending order to have the renaming done correctly. 
# Otherwise, the renaming will be a mess.

################################ CAR #################################
for (( i=1; i<=$run_num; i++ ))
do
    begin=$(printf "Executing car.py (%03d)" "$i")
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
mv vpython*.txt linear_regression_real/trace_car_testResult


# ############################### DIABETES #################################
# for (( i=1; i<=$run_num; i++ ))
# do
#     begin=$(printf "Executing diabetes.py (%03d)" "$i")
#     echo "_____________________"
#     echo "$begin"
#     python3.9 ./linear_regression_real/code_decor/diabetes.py
#     killall -9 python3.9

#     # Renaming
#     new=$(printf "vpython_diabetes_%03d.txt" "$i")
#     mv vpython.txt "$new"
#     echo "Renamed to $new"
#     echo 
# done
# # Move all trace files to a folder
# mv vpython*.txt linear_regression_real/trace_diabetes_only


# ################################ ENERGY #################################
# for (( i=1; i<=$run_num; i++ ))
# do
#     begin=$(printf "Executing energy.py (%03d)" "$i")
#     echo "_____________________"
#     echo "$begin"
#     python3.9 ./linear_regression_real/code_decor/energy.py
#     killall -9 python3.9

#     # Renaming
#     new=$(printf "vpython_energy_%03d.txt" "$i")
#     mv vpython.txt "$new"
#     echo "Renamed to $new"
#     echo 
# done
# # Move all trace files to a folder
# mv vpython*.txt linear_regression_real/trace_energy_only


# ############################## HOUSE ###################################
# for (( i=1; i<=$run_num; i++ ))
# do
#     begin=$(printf "Executing house.py (%03d)" "$i")
#     echo "_____________________"
#     echo "$begin"
#     python3.9 ./linear_regression_real/code_decor/house.py
#     killall -9 python3.9

#     # Renaming
#     new=$(printf "vpython_house_%03d.txt" "$i")
#     mv vpython.txt "$new"
#     echo "Renamed to $new"
#     echo 
# done
# # Move all trace files to a folder
# mv vpython*.txt linear_regression_real/trace_house_only


# ############################# MEDICAL ####################################
# for (( i=1; i<=$run_num; i++ ))
# do
#     begin=$(printf "Executing medical.py (%03d)" "$i")
#     echo "_____________________"
#     echo "$begin"
#     python3.9 ./linear_regression_real/code_decor/medical.py
#     killall -9 python3.9

#     # Renaming
#     new=$(printf "vpython_medical_%03d.txt" "$i")
#     mv vpython.txt "$new"
#     echo "Renamed to $new"
#     echo 
# done
# # Move all trace files to a folder
# mv vpython*.txt linear_regression_real/trace_medical_only

python3.8 utils/run_analysis_script.py

spd-say done