#!/bin/bash
rm -f vpython.txt
rm -f vpython.txt


# Prompt filename and execute the file using vPython / python3.9
# Make sure the files are in consecutively-numbered ascending order to have the renaming done correctly. 
# Otherwise, the renaming will be a mess.
echo "Executing medical.py"
python3.9 ./linear_regression_additional/code/medical.py
# Renaming
mv vpython.txt vpython_medical.txt
echo "Sleep 2s"
echo ""
sleep 2

echo "Executing medical.py"
python3.9 ./linear_regression_additional/code/diabetes.py
# Renaming
mv vpython.txt vpython_diabetes.txt
echo "Sleep 2s"
echo ""
sleep 2

spd-say done