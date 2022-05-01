#!/bin/bash

count=1
numberofiteration=100  # Edit the number of iterations here

while [ $count -le $numberofiteration ]
do
    nice_count=$(printf "%02d" "$count")
    printf "\n=================="
    printf "\n  run batch $nice_count"
    printf "\n==================\n\n"

    # ///////////////////////// EDIT ZONE \\\\\\\\\\\\\\\\\\\\\\\\\\\\\

    # Bash script you want to run: 
    ./linear_regression_additional.sh

    # Destination trace directory you want to store at:
    new_dir=$(printf "linear_regression_additional/trace/lra_%02d" "$count")
    mkdir $new_dir
    
    # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\ END /////////////////////////////

    # Move all trace files there
    mv vpython*.txt $new_dir

    let count=count+1
done