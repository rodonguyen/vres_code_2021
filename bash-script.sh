#!/bin/bash

DIR_PANDAS="./strace_pandas/" 

python3.9 "${DIR_PANDAS}"load_with_pd.py 
mv vpython.txt vpython_ds1.txt