#!/bin/bash

DIR_READLINE="./strace_readline/" 

count=1
for i in "${DIR_READLINE}"load_with_readline_ds*.py
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
python3.9 "${DIR_READLINE}"load_with_readline_v2_ds01.py
mv vpython.txt vpython_v2_ds01.txt

python3.9 "${DIR_READLINE}"load_with_readline_v2_ds10.py
mv vpython.txt vpython_v2_ds10.txt
