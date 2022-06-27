# vres_code_2021

This repo includes:

- /strace\_\*: python codes and their stack trace files
- /dataset: Datasets
- bash-script-\*.sh: Bash scripts to automate running multiple python files with vpython and renaming them
- count_stack.py: count stack file and record it in text and csv files
- create_dataset.py: help automatically create dataset with consecutively-increasing values
- /Documents: Analysises and Journals

# Process to get stack_trace analysis
1. Initiate bash script: `chmod u+x bashscript-name.sh`
2. Make sure the path and python names are correct in the bashscript
3. Run the bashscript: `./bashscript-name.sh`
4. When all the trace files are ready, put the paths to the directories containing trace files in `/utils/run_script.py`
5. Run that `run_script.py` with python3.8: `python3.8 utils/run_script.py`
6. The number of memory operations is in `/count_result`


# Other useful commands
- `df -h` to check available storage 
- `rsync -avzhe ssh Documents/vres_code_2022/localfile.sh  rodo@192.168.10.11:/home/rodo/vres_code_2022/` to copy a local file to RPi. Be mindful about your current dir. Can reverse the 2 parameters to copy RPi file to local dir.
- `rsync -avzh Documents/vres_code_2022 rodo@192.168.18.21:/home/rodo/` to copy a local dir to RPi dir. Be mindful about your current dir. Can reverse the 2 parameters to copy RPi dir to a local dir to.
- `top` to view memory dashboard
