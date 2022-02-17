import os
import subprocess
import shutil
import fileinput
import time
import re
import pandas as pd

file_name = 'Case5_III_C_3yrs_testsd'

"""
    Function that calls & reproduces the command line options for executing ats. It involves mainly the following steps:
    1. Creating a demo directory : mkdir output_file_name.demo
    2. 'cd' into the demo directory : cd out_file_name.demo
    3. Excecuting the ats command : ats --xml_file=../input_file_name.xml &>out.log
    
    Note: To execute the command - Please be in the directory where the input xml file is present.
    
    Parameters:
    
    -----
    INPUT
    
    file_name : string
    
    The input xml file name and the directory name (both are the same). Ex: infiltration
    
    
    -----
    OUTPUT:
    
    Runs the ats command and dumps all the outputs in file_name_i.demo
    
"""
# Removing the directory if it exists
if os.path.isdir(f'{file_name}.demo/'):
    shutil.rmtree(f'{file_name}.demo/')
    
# Making a new directory
os.mkdir(f'{file_name}.demo')
    
# Changing the directory to the demo directory
os.chdir(f'{file_name}.demo/')
    
# Running the ats command
ats_command = f"ats --xml_file=../{file_name}.xml >out.log"
    
os.system(ats_command)
#output = os.popen(ats_command).read()
    
#return output
    