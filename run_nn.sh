#!/bin/bash

# Clean vPython.txt in current directory and traces
rm -f vpython*.txt

# Create directories to store traces

dir001="trace_car_withRandom"
dir002="trace_diabetes_withRandom"
# dir003="trace_energy_withRandom"
# dir004="trace_house_withRandom"
# dir005="trace_medical_withRandom"

# dir001="trace_car_noRandom"
# dir002="trace_diabetes_noRandom"
# dir003="trace_energy_noRandom"
# dir004="trace_house_noRandom"
# dir005="trace_medical_noRandom"

mkdir neural_network/$dir001
mkdir neural_network/$dir002
# mkdir neural_network/$dir003
# mkdir neural_network/$dir004
# mkdir neural_network/$dir005

run_num=110

# Prompt filename and execute the file using vPython / python3.9
# Make sure the files are in consecutively-numbered ascending order to have the renaming done correctly. 
# Otherwise, the renaming will be a mess.

# ################################ CAR #################################
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
mv vpython*.txt neural_network/$dir001


############################### DIABETES #################################
for (( i=1; i<=$run_num; i++ ))
do
    begin=$(printf "Executing diabetes.py (%03d)" "$i")
    echo "_____________________"
    echo "$begin"
    python3.9 ./neural_network/diabetes.py
    killall -9 python3.9

    # Renaming
    new=$(printf "vpython_diabetes_%03d.txt" "$i")
    mv vpython.txt "$new"
    echo "Renamed to $new"
    echo 
done
# Move all trace files to a folder
mv vpython*.txt neural_network/$dir002


################################ ENERGY #################################
# for (( i=1; i<=$run_num; i++ ))
# do
#     begin=$(printf "Executing energy.py (%03d)" "$i")
#     echo "_____________________"
#     echo "$begin"
#     python3.9 ./neural_network/energy.py
#     killall -9 python3.9

#     # Renaming
#     new=$(printf "vpython_energy_%03d.txt" "$i")
#     mv vpython.txt "$new"
#     echo "Renamed to $new"
#     echo 
# done
# # Move all trace files to a folder
# mv vpython*.txt neural_network/$dir003


# ############################## HOUSE ###################################
# for (( i=1; i<=$run_num; i++ ))
# do
#     begin=$(printf "Executing house.py (%03d)" "$i")
#     echo "_____________________"
#     echo "$begin"
#     python3.9 ./neural_network/house.py
#     killall -9 python3.9

#     # Renaming
#     new=$(printf "vpython_house_%03d.txt" "$i")
#     mv vpython.txt "$new"
#     echo "Renamed to $new"
#     echo 
# done
# # Move all trace files to a folder
# mv vpython*.txt neural_network/$dir004



# ############################# MEDICAL ####################################
# for (( i=1; i<=$run_num; i++ ))
# do
#     begin=$(printf "Executing medical.py (%03d)" "$i")
#     echo "_____________________"
#     echo "$begin"
#     python3.9 ./neural_network/medical.py
#     killall -9 python3.9

#     # Renaming
#     new=$(printf "vpython_medical_%03d.txt" "$i")
#     mv vpython.txt "$new"
#     echo "Renamed to $new"
#     echo 
# done
# # Move all trace files to a folder
# mv vpython*.txt neural_network/$dir005

# python3.8 neural_network/run_analysis_script.py
spd-say done