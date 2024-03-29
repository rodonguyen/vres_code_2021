#!/bin/bash


# Clean vPython.txt in current directory and targeted trace dirs
rm -f vpython*.txt
rm -r programs/activity/v2_nb/trace_*

# Create directories to store traces
dir001="programs/activity/v2_nb/trace_pa"
# dir002="programs/activity/v2_nb/trace_pa_X100integer"
mkdir $dir001
# mkdir $dir002

###########################################################
base_dir="programs/activity/v2_nb/code_pa/"
i=1
for file in $base_dir*
do
    begin=$(printf "Executing $file (%03d)" "$i")
    echo "_____________________"
    echo "$begin"
    python3.8 "$file"
    killall -9 python3.9

    new=$(printf "vpython_%03d.txt" "$i")
    mv vpython.txt "$new"
    echo "Renamed to $new"

    ((i=i+1))
done
mv vpython*.txt $dir001
###########################################################

# ###########################################################
# base_dir="programs/activity/v2_nb/code_pa_X100integer/"
# i=1
# for file in $base_dir*
# do
#     begin=$(printf "Executing $file (%03d)" "$i")
#     echo "_____________________"
#     echo "$begin"
#     python3.9 "$file"
#     killall -9 python3.9

#     new=$(printf "vpython_%03d.txt" "$i")
#     mv vpython.txt "$new"
#     echo "Renamed to $new"

#     ((i=i+1))
# done
# mv vpython*.txt $dir002
# ###########################################################

# python programs/run_analysis_script.py
spd-say done