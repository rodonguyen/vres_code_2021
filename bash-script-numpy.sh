#!/bin/bash

DIR_NUMPY="./strace_numpy/" 

count=1
for i in "${DIR_NUMPY}"numpy_ds*.py
do
  echo "Executing $i"
  python3.9 $i 
  
  sleep 1
  new=$(printf "vpython_ds%02d.txt" "$count")
  mv vpython.txt "$new"
  echo "Renamed to $new"
  echo ""
  let count=count+1
done

# echo "Execute uncommon python codes"
