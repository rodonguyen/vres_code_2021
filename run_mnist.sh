#!/bin/bash

# Clean vPython.txt in current directory and traces
rm -f vpython*.txt
rm -r programs/neural_network/mnist/trace

# Create directories to store traces
dir010="programs/neural_network/mnist/trace"
mkdir $dir010


# declare -a StringArray=('10' '20' '30' '40' '50' '60' '70' '80' '90' '100' '200' '300' '400' '500' '600' '700' '800' '900' '1000' '2000' '3000' '4000' '5000' '6000' '7000' '8000' '9000' '10000' '20000' '30000' '40000' '50000' '60000')
declare -a StringArray=('26' '97' '150' '373' '642' '1234' '4880' '7601' '7899' '11890' '26090' '33333' '53011')

# # ################ VPYTHON ################# 
# python3.8 utils/record_time.py

# count=0
# for i in "${StringArray[@]}"; do
#     count=$((count+1))
#     filename=("programs/neural_network/mnist/code_test/mnist_$i.py")
#     echo "$count => $filename"
#     python3.9 $filename
#     pkill -9 python3.9

#     python3.8 utils/record_time.py

#     # Renaming
#     new=$(printf "vpython_mnist_%08d.txt" "$i")
#     mv vpython.txt "$new"
#     echo "Renamed to $new"
#     echo 

#     # Move all trace files to a folder every 3 programs run
#     if [ $((count%3)) == 0 ]; then
#         mv vpython*.txt $dir010
#         python3.8 programs/run_analysis_script.py
#         rm -r programs/neural_network/mnist/trace/vpython*.txt
#     fi

# done
# mv vpython*.txt $dir010
# python3.8 programs/run_analysis_script.py


################# NORMAL PYTHON ################ 
python3.8 utils/record_time.py

count=0
for i in "${StringArray[@]}"; do
    count=$((count+1))
    filename=("programs/neural_network/mnist/code3layers_test/mnist_$i.py")
    echo "$count => $filename"
    python3.8 $filename

    python3.8 utils/record_time.py
done


#####################################
spd-say done