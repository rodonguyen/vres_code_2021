#!/bin/bash

# Clean vPython.txt in current directory and targeted trace dirs
rm -f vpython*.txt
# rm -r programs/cknn/trace_*
# rm -r programs/svm/trace_*

# Create directories to store traces
dir001="programs/cknn/trace_cancer"
dir002="programs/cknn/trace_wine_bin"
dir003="programs/cknn/trace_wine_multi"
dir004="programs/svm/trace_cancer"
dir005="programs/svm/trace_wine_bin"
dir006="programs/svm/trace_wine_multi"

program001="./programs/cknn/cancer.py"
program002="./programs/cknn/wine_binary.py"
program003="./programs/cknn/wine_multi.py"
program004="./programs/svm/cancer.py"
program005="./programs/svm/wine_binary.py"
program006="./programs/svm/wine_multi.py"

mkdir $dir001
mkdir $dir002
mkdir $dir003
mkdir $dir004
mkdir $dir005
mkdir $dir006

run_num=1

# Prompt filename and execute the file using vPython / python3.9
# Make sure the files are in consecutively-numbered ascending order to have the renaming done correctly. 
# Otherwise, the renaming will be a mess.

################################ 1 #################################
for (( i=1; i<=$run_num; i++ ))
do
    begin=$(printf "Executing1 cancer.py (%03d)" "$i")
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


############################### 2 #################################
for (( i=1; i<=$run_num; i++ ))
do
    begin=$(printf "Executing 2 cknn wine_bin.py (%03d)" "$i")
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


############################### 3 #################################
for (( i=1; i<=$run_num; i++ ))
do
    begin=$(printf "Executing 3 wine_multi.py (%03d)" "$i")
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




################################ 4 #################################
for (( i=1; i<=$run_num; i++ ))
do
    begin=$(printf "Executing 4 cancer.py (%03d)" "$i")
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


############################### 5 #################################
for (( i=1; i<=$run_num; i++ ))
do
    begin=$(printf "Executing 5 wine_bin.py (%03d)" "$i")
    echo "_____________________"
    echo "$begin"
    python3.9 $program005
    killall -9 python3.9

    # Renaming
    new=$(printf "vpython5_%03d.txt" "$i")
    mv vpython.txt "$new"
    echo "Renamed to $new"
    echo 
done
# Move all trace files to a folder
mv vpython*.txt $dir005


############################### 6 #################################
for (( i=1; i<=$run_num; i++ ))
do
    begin=$(printf "Executing 6 wine_multi.py (%03d)" "$i")
    echo "_____________________"
    echo "$begin"
    python3.9 $program006
    killall -9 python3.9

    # Renaming
    new=$(printf "vpython6_%03d.txt" "$i")
    mv vpython.txt "$new"
    echo "Renamed to $new"
    echo 
done
# Move all trace files to a folder
mv vpython*.txt $dir006

# python3.8 cknn/run_analysis_script.py
spd-say done