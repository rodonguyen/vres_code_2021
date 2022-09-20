#!/bin/bash


# Clean vPython.txt in current directory and targeted trace dirs
rm -f vpython*.txt
rm -r programs/weather/trace*

# Create directories to store traces
dir001="programs/weather/trace"
mkdir $dir001
# mkdir $dir002

###########################################################
python utils/record_time.py empty
python utils/record_time.py


base_dir="programs/weather/code/"
i=1
for file in $base_dir*
do
    begin=$(printf "Executing $file (%03d)" "$i")
    echo "_____________________"
    echo "$begin"
    python3.9 "$file"
    python3.8 utils/record_time.py
    pkill -9 python3.9

    new=$(printf "vpython_%03d.txt" "$i")
    mv vpython.txt "$new"
    echo "Renamed to $new"

    ((i=i+1))
done
mv vpython*.txt $dir001
python programs/run_analysis_script.py
# rm -r programs/weather/trace/*

###########################################################
python utils/record_time.py empty
python utils/record_time.py empty
python utils/record_time.py


base_dir="programs/weather/code/"
for file in $base_dir*
do
    begin=$(printf "Executing $file (%03d)" "$i")
    echo "_____________________"
    echo "$begin"
    python3.8 "$file"
    python3.8 utils/record_time.py

done
###########################################################

spd-say done