<!-- @format -->

# vres_code_2022

## Process to get stack_trace analysis

1. Run program with vpython to collect traces, which can include the following steps:
   1. Create a bash script to run programs automatically. Some available ones are in the main directory with `.sh` tail
   1. Grant the access to run that bash script: `chmod u+x bashscript-name.sh`
   1. Edit the file names / paths in the scripts
   1. Run: `./bashscript-name.sh`
2. Run anaylysis code:
   1. Edit the directory `paths` that contain the stack traces
   1. Edit the variables in the designated section
   1. Run: `python3.8 utils/run_analysis_script.py`
3. Check the results and graphs which are saved in `/count_result`

## Important files/folders:

- /utils contains utils functions to count stack traces and plot graphs
  - run_analysis_script.py: main file to put the functions you want to run: count stack traces, convert results, plot graphs.
- bash-script.sh in the main directory: automatically run the designated program and collect traces
- /Documents: Analyses and Journals


<br>

## Other useful commands

- `df -h` to check available storage
- `rsync -avzhe ssh Documents/vres_code_2022/localfile.sh rodo@192.168.10.11:/home/rodo/vres_code_2022/` to copy a local file to RPi. Be mindful about your current dir. Can reverse the 2 parameters to copy RPi file to local dir.
- `rsync -avzh Documents/vres_code_2022 rodo@192.168.18.21:/home/rodo/` to copy a local dir to RPi dir. Be mindful about your current dir. Can reverse the 2 parameters to copy RPi dir to a local dir to.
- `top` to view memory dashboard

## Todos

- Now: Check prediction results if there is randomness, then check traces
- New data
- New model: SVM, cknn, RF, bayes (nope, because this is regression problem)
