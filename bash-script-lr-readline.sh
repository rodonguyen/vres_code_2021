#!/bin/bash
rm -f vpython.txt
rm -f vpython.txt


DIR="./linear_regression_readline/"
# Start from dataset 0
count=1
for i in "${DIR}"/code_length_increase/lr_ds*.py
do
  # Prompt filename and execute the file using vPython / python3.9
  # Make sure the files are in consecutively-numbered ascending order to have the Renaming done correctly. 
  # Otherwise, the renaming will be a mess.
  echo "Executing $i"
  python3.9 $i 
  
  # Renaming
  new=$(printf "vpython_ds%02d.txt" "$count")
  mv vpython.txt "$new"

  # Prompt the new name for easier check
  echo "Renamed to $new"
  echo ""

  # Iterate the 'count' to make new name
  let count=count+1
done
