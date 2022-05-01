#!/bin/bash


# Clean vPython.txt in current directory
rm -f vpython*.txt
rm -r simple_one/trace*

# Create directories to store traces
mkdir simple_one/trace_pandas_play
mkdir simple_one/trace_print_nothing
mkdir simple_one/trace_importing1_many
mkdir simple_one/trace_importing2_pd
mkdir simple_one/trace_importing3_pd_and_load
mkdir simple_one/trace_importing4_manypd
mkdir simple_one/trace_importing5_manysklearn


# Prompt filename and execute the file using vPython / python3.9
# Make sure the files are in consecutively-numbered ascending order to have the renaming done correctly. 
# Otherwise, the renaming will be a mess.

################################ 
for i in {1..10}
do
    begin=$(printf "Executing pandas_play.py (%03d)" "$i")
    echo "_____________________"
    echo "$begin"
    python3.9 ./simple_one/pandas_play.py
    killall -9 python3.9

    # Renaming
    new=$(printf "vpython_pandas_play_%03d.txt" "$i")
    mv vpython.txt "$new"
    echo "Renamed to $new"
    echo 
done
# Move all trace files to a folder
mv vpython*.txt simple_one/trace_pandas_play


############################### 
for i in {1..10}
do
    begin=$(printf "Executing print_nothing.py (%03d)" "$i")
    echo "_____________________"
    echo "$begin"
    python3.9 ./simple_one/print_nothing.py
    killall -9 python3.9

    # Renaming
    new=$(printf "vpython_print_nothing_%03d.txt" "$i")
    mv vpython.txt "$new"
    echo "Renamed to $new"
    echo 
done
# Move all trace files to a folder
mv vpython*.txt simple_one/trace_print_nothing


################################ 
for i in {1..10}
do
    begin=$(printf "Executing importing1_many.py (%03d)" "$i")
    echo "_____________________"
    echo "$begin"
    python3.9 ./simple_one/importing1_many.py
    killall -9 python3.9

    # Renaming
    new=$(printf "vpython_importing1_many_%03d.txt" "$i")
    mv vpython.txt "$new"
    echo "Renamed to $new"
    echo 
done
# Move all trace files to a folder
mv vpython*.txt simple_one/trace_importing1_many

################################ 
for i in {1..10}
do
    begin=$(printf "Executing importing2_pd.py (%03d)" "$i")
    echo "_____________________"
    echo "$begin"
    python3.9 ./simple_one/importing2_pd.py
    killall -9 python3.9

    # Renaming
    new=$(printf "vpython_importing2_pd_%03d.txt" "$i")
    mv vpython.txt "$new"
    echo "Renamed to $new"
    echo 
done
# Move all trace files to a folder
mv vpython*.txt simple_one/trace_importing2_pd

################################ 
for i in {1..10}
do
    begin=$(printf "Executing importing3_pd_and_load.py (%03d)" "$i")
    echo "_____________________"
    echo "$begin"
    python3.9 ./simple_one/importing3_pd_and_load.py
    killall -9 python3.9

    # Renaming
    new=$(printf "vpython_importing3_pd_and_load_%03d.txt" "$i")
    mv vpython.txt "$new"
    echo "Renamed to $new"
    echo 
done
# Move all trace files to a folder
mv vpython*.txt simple_one/trace_importing3_pd_and_load


################################ 
for i in {1..25}
do
    begin=$(printf "Executing importing4_manypd.py (%03d)" "$i")
    echo "_____________________"
    echo "$begin"
    python3.9 ./simple_one/importing3_pd_and_load.py
    killall -9 python3.9

    # Renaming
    new=$(printf "vpython_importing4_manypd_%03d.txt" "$i")
    mv vpython.txt "$new"
    echo "Renamed to $new"
    echo 
done
# Move all trace files to a folder
mv vpython*.txt simple_one/trace_importing4_manypd


################################ 
for i in {1..25}
do
    begin=$(printf "Executing importing5_manysklearn.py (%03d)" "$i")
    echo "_____________________"
    echo "$begin"
    python3.9 ./simple_one/importing5_manysklearn.py
    killall -9 python3.9

    # Renaming
    new=$(printf "vpython_importing5_manysklearn_%03d.txt" "$i")
    mv vpython.txt "$new"
    echo "Renamed to $new"
    echo 
done
# Move all trace files to a folder
mv vpython*.txt simple_one/trace_importing5_manysklearn



################################
# Extract traces
python3.8 utils/run_script.py




spd-say done