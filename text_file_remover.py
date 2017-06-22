# @author Ashraf
# This python code removes all text files with .SAC extension in current directory
# Make sure that the files in current folder are no being used by any other program(s)
# Recommended python version 2.7.x

import os

files = [f for f in os.listdir('.') if os.path.isfile(f) and f.endswith('.SAC')]
counter = 0
for curr_file in files:
    command = "file -bi " + curr_file
    f = os.popen(command, 'r')
    if f.read().startswith('text'):
        os.remove(curr_file)
        counter += 1

print("Total " + `counter` + " file(s) removed!")