#!/bin/bash
rm -f vpython.txt
rm -f vpython.txt

# Start from dataset 1
count=1
for i in ./linear_regression_pandas/code/dataset_length_increase/lr_ds_*.py
do
  # Prompt filename and execute the file using vPython / python3.9
  # Make sure the files are in consecutively-numbered ascending order to have the renaming done correctly. 
  # Otherwise, the renaming will be a mess.
  echo "Executing $i"
  python3.9 $i 
  
  # Renaming
  new=$(printf "vpython_ds_%02d.txt" "$count")
  mv vpython.txt "$new"

  # Prompt the new name for easier check
  echo "Renamed to $new"
  echo "Kill python3.9 process and Sleep 2s"
  echo ""
  killall -9 python3.9
  sleep 2

  # Iterate the 'count' to make new name
  let count=count+1
done

python3.8 utils/rename.py

spd-say done

# echo "Execute uncommon python codes"
