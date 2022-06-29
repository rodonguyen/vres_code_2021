<!-- @format -->

# vres_code_2022

## Important files/folders:

- /utils contains utils functions to count stack traces and plot graphs
  - run_analysis_script.py: main file to put the functions you want to run: count stack traces, convert results, plot graphs.
- bash-script.sh in the main directory: automatically run the designated program and collect traces
- /Documents: Analyses and Journals

## Process to get stack_trace analysis

1. Run program with vpython which can include the following steps:
   1. Create a bash script
   1. Grant the access to run that bash script: `chmod u+x bashscript-name.sh`
   1. Edit the file names / paths in the scripts
   1. Run: `./bashscript-name.sh`
2. Run `/utils/run_analysis_script.py` with python3.8:
   1. Edit all the file names / paths in this file
   1. Run: `python3.8 utils/run_script.py`
3. The results and graphs are saved in `/count_result`

<br>

## Other useful commands

- `df -h` to check available storage
- `rsync -avzhe ssh Documents/vres_code_2022/localfile.sh rodo@192.168.10.11:/home/rodo/vres_code_2022/` to copy a local file to RPi. Be mindful about your current dir. Can reverse the 2 parameters to copy RPi file to local dir.
- `rsync -avzh Documents/vres_code_2022 rodo@192.168.18.21:/home/rodo/` to copy a local dir to RPi dir. Be mindful about your current dir. Can reverse the 2 parameters to copy RPi dir to a local dir to.
- `top` to view memory dashboard

## Todos

- Now: Run 1 with SVM
- new data
- new model: SVM, cknn, RF, bayes
