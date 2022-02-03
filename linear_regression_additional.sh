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
echo "Kill python3.9 process and Sleep 2s"
echo ""
killall -9 python3.9
sleep 2

echo "Executing diabetes.py"
python3.9 ./linear_regression_additional/code/diabetes.py
# Renaming
mv vpython.txt vpython_diabetes.txt
echo "Kill python3.9 process and Sleep 2s"
echo ""
killall -9 python3.9
sleep 2

echo "Executing car.py"
python3.9 ./linear_regression_additional/code/car.py
# Renaming
mv vpython.txt vpython_car.txt
echo "Kill python3.9 process and Sleep 2s"
echo ""
killall -9 python3.9
sleep 2


echo "Executing energy.py"
python3.9 ./linear_regression_additional/code/energy.py
# Renaming
mv vpython.txt vpython_energy.txt
echo "Kill python3.9 process and Sleep 2s"
echo ""
killall -9 python3.9
sleep 2

echo "Executing house.py"
python3.9 ./linear_regression_additional/code/house.py
# Renaming
mv vpython.txt vpython_house.txt
echo "Kill python3.9 process and Sleep 2s"
echo ""
killall -9 python3.9
sleep 2


spd-say done