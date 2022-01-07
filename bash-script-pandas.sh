#!/bin/bash

DIR_PANDAS="./strace_pandas/"

count=1
for i in "${DIR_PANDAS}"load_with_pd_ds*.py
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

echo "Execute uncommon python codes"
python3.9 "${DIR_PANDAS}"load_with_pd_v2_ds01.py
mv vpython.txt vpython_v2_s1.txt
