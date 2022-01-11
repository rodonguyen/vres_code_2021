#!/bin/bash

DIR_NUMPY="./strace_numpy/" 

# Start from dataset 0
count=0
for i in "${DIR_NUMPY}"numpy_ds*.py
do
  # Prompt filename and execute the file using vPython / python3.9
  # Make sure the files are in consecutively-numbered ascending order to have the renaming done correctly. 
  # Otherwise, the renaming will be a mess.
  echo "Executing $i" 
  python3.9 $i 
  
  # Give computer sometime to rest and rename
  sleep 1
  new=$(printf "vpython_ds%02d.txt" "$count")
  mv vpython.txt "$new"

  # Prompt the new name for easier check
  echo "Renamed to $new"
  echo ""

  # Iterate the 'count' to make new name
  let count=count+1
done

# echo "Execute uncommon python codes"
# put uncommon files here to execute