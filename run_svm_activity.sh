#!/bin/bash


# Clean vPython.txt in current directory and targeted trace dirs
rm -f vpython*.txt
rm -r programs/svm_activity/trace_*

# Create directories to store traces
dir001="programs/svm_activity/trace_pa"
dir002="programs/svm_activity/trace_pg"

program001="./programs/svm_activity/activity_01.py"
program002="./programs/svm_activity/activity_02.py"
program003="./programs/svm_activity/activity_03.py"
program004="./programs/svm_activity/activity_04.py"
program005="./programs/svm_activity/activity_05.py"
program006="./programs/svm_activity/activity_06.py"
program007="./programs/svm_activity/activity_07.py"

mkdir $dir001
mkdir $dir002

i=1
# Prompt filename and execute the file using vPython / python3.9
# Make sure the files are in consecutively-numbered ascending order to have the renaming done correctly. 
# Otherwise, the renaming will be a mess.

begin=$(printf "Executing $program001 (%03d)" "$i")
echo "_____________________"
echo "$begin"
python3.9 $program001
killall -9 python3.9

new=$(printf "vpython1_%03d.txt" "$i")
mv vpython.txt "$new"
echo "Renamed to $new"
echo 

mv vpython*.txt $dir001

###########################################################
((i=i+1))
begin=$(printf "Executing $program002 (%03d)" "$i")
echo "_____________________"
echo "$begin"
python3.9 $program002
killall -9 python3.9

new=$(printf "vpython1_%03d.txt" "$i")
mv vpython.txt "$new"
echo "Renamed to $new"
echo 

mv vpython*.txt $dir001


###########################################################
((i=i+1))
begin=$(printf "Executing $program003 (%03d)" "$i")
echo "_____________________"
echo "$begin"
python3.9 $program003
killall -9 python3.9

new=$(printf "vpython1_%03d.txt" "$i")
mv vpython.txt "$new"
echo "Renamed to $new"
echo 

mv vpython*.txt $dir001


###########################################################
((i=i+1))
begin=$(printf "Executing $program004 (%03d)" "$i")
echo "_____________________"
echo "$begin"
python3.9 $program004
killall -9 python3.9

new=$(printf "vpython1_%03d.txt" "$i")
mv vpython.txt "$new"
echo "Renamed to $new"
echo 

mv vpython*.txt $dir001

###########################################################
((i=i+1))
begin=$(printf "Executing $program005 (%03d)" "$i")
echo "_____________________"
echo "$begin"
python3.9 $program005
killall -9 python3.9

new=$(printf "vpython1_%03d.txt" "$i")
mv vpython.txt "$new"
echo "Renamed to $new"
echo 

mv vpython*.txt $dir001

###########################################################
((i=i+1))
begin=$(printf "Executing $program006 (%03d)" "$i")
echo "_____________________"
echo "$begin"
python3.9 $program006
killall -9 python3.9

new=$(printf "vpython1_%03d.txt" "$i")
mv vpython.txt "$new"
echo "Renamed to $new"
echo 

mv vpython*.txt $dir001

###########################################################
((i=i+1))
begin=$(printf "Executing $program007 (%03d)" "$i")
echo "_____________________"
echo "$begin"
python3.9 $program007
killall -9 python3.9

new=$(printf "vpython1_%03d.txt" "$i")
mv vpython.txt "$new"
echo "Renamed to $new"
echo 

mv vpython*.txt $dir001


###########################################################
# python programs/run_analysis_script.py
spd-say done