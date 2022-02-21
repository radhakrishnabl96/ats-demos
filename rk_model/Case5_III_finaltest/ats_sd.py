"""
    The function follows two main tasks:
    a. Changes the snow density value 
    b. Calls & reproduces the command line options for executing ats 
    
    It involves mainly the following steps:
    1. Access the snow density ratio from the xml file
    2. Assign a snow density ratio to a variable
    3. Access the measured snow depth
    4. Fill the snow depth missing data with an average value
    5. Concatatenating all the dataframes for the year 2016, 2017, 2018, 2019.
    6. Note: The year 2016 has 366 days, hence I am adding the Dec 31st value once more
    7. Creating a dataframe with four years of snow depth data
    8. The snow depth dataframe with the same index
    9. Calculating the snow water equivalent
    10. Storing the data in a seperate dataframe
    11. Opening the input h5 file
    12. Creating a variable with time instances for 1096 days
    13. Storing the variables in h5 file
    14. Closing the h5 file
    15. Creating a demo directory : mkdir output_file_name.demo
    16. 'cd' into the demo directory : cd out_file_name.demo
    17. Excecuting the ats command : ats --xml_file=../input_file_name.xml &>out.log
    
    Note: To execute the command - Please be in the directory where the input xml file is present.
    
    #### To define the SWE, the following file was considered: http://webarchiv.ethz.ch/arolla/Arolla_Data/SnowConditions/depth_to_swe.pdf
Snow water equivalent is the water content obtained from melting a sample of snow. Density is defined as the ratio of mass per unit volume. Since the mass of the sample is the same whether it is snow or water, the relationship can be expressed using the respective densities and volumes. 

Let $V_{snow}$ = the volume of the snow in the sample, $\rho_{snow}$ = the density of the snow in the sample, V_{water} = the volume of the water when the sample is melted, $\rho_{water}$ = the density of water.

Since the mass of the sample in snow and water remains the same:

$$ m_{water}  = m_{snow}$$

$$ \rho_{water} V_{water} = \rho_{snow} V_{snow} $$

Here, if the Area (A) is constant for both water and snow (it is!), then the $V_{water} = A * SWE$ and $V_{snow} = A * Z_s$ where SWE is the snow water equivalent, $Z_s$ is the depth of snow. We can now write the equation as

$$ \rho_{water} * A * SWE = \rho_{snow} * A * Z_s$$

Finally we have the equation:

$$  SWE = \frac{\rho_{snow} * Z_s}{\rho_{water}} $$

Here we also need the SWE in $m s^{-1}$ --> $Z_s$ is in m/day. $\rho_{water} = 1000 \frac{kg}{m^3}$, $\rho_{snow} = 1000 \frac{kg}{m^3}$. 

Based on the link - https://www.sciencelearn.org.nz/resources/1391-snow-and-ice-density, and Atchley article 2015. Assuming a average snow density between 50 - 1000 $\frac{kg}{m^3}$

Ex: $$ SWE (m s^{-1}) = \frac{450 * Z_s}{1000*86400} = 5.208E-06 * Z_s $$
    
    Parameters:
    
    -----
    INPUT
    
    file_name : string
    
    The input xml file name and the directory name (both are the same). Ex: infiltration
    
    
    -----
    OUTPUT:
    
    Runs the ats command and dumps all the outputs in file_name_i.demo
    
"""


import os
import subprocess
import shutil
import fileinput
import time
import re
import pandas as pd
import numpy as np
import h5py

file_name = 'Case5_III_C_3yrs_testsd'

# 1. To find the snow density from the xml file
filename = f'{file_name}.xml'
line_sd = 1011

with open(f'{filename}') as oldfile:
            for line, content in enumerate(oldfile):
                if line == line_sd: # Line 603 (+1) has the porosity_peat 
                    sd_line = str(content)
                    result = re.findall('\".*?\"', sd_line)
                    #print(result)
                    snow_dens_ratio = float(result[2].replace('"',''))
                    #print(snow_density_ratio)



# Snow depth is also a input parameter - data collected from Dr. Xiao's article
Snow_depth = pd.read_excel('/home/rk/ats_rk/testing/ats-demos/rk_model/Data/Data_Yakou/Yakou_met_data_ITP_rk/Final_data_excelsheet/Yakou_metstation_data_2017_snowdepth.xlsx',sheet_name='snow_depth',index_col=0, parse_dates=True) 

# Filling the snow depth missing data with an average value
Snow_depth = Snow_depth.fillna(np.average(Snow_depth.loc['2017-12']))
# Snow depth is also a input parameter - data collected from Dr. Xiao's article
Snow_depth = pd.read_excel('/home/rk/ats_rk/testing/ats-demos/rk_model/Data/Data_Yakou/Yakou_met_data_ITP_rk/Final_data_excelsheet/Yakou_metstation_data_2017_snowdepth.xlsx',sheet_name='snow_depth',index_col=0, parse_dates=True) 

# Filling the snow depth missing data with an average value
Snow_depth = Snow_depth.fillna(np.average(Snow_depth.loc['2017-12']))

# Concatatenating all the dataframes for the year 2016, 2017, 2018, 2019.

snow_depth_2016_2019 = np.concatenate([Snow_depth['Snow depth (m)'].values, Snow_depth['Snow depth (m)'].values, Snow_depth['Snow depth (m)'].values, Snow_depth['Snow depth (m)'].values])

# Note: The year 2016 has 366 days, hence I am adding the Dec 31st value once more
snow_depth_2016_2019 = np.insert(snow_depth_2016_2019, 366, Snow_depth['Snow depth (m)']['2017-12-31'])

# Creating a dataframe with four years of snow depth data

# The snow depth dataframe with the same index
Snow_depth_4_yrs = pd.DataFrame(index=pd.date_range(start='1/1/2016',end='31/12/2019',freq='D'),data = snow_depth_2016_2019, columns=['Snow depth (m)'])

# Calculating the snow water equivalent
Snow_depth_4_yrs['precipitation snow [m SWE s^-1]'] = Snow_depth_4_yrs['Snow depth (m)']*(snow_dens_ratio/86400)

# Storing the data in a seperate dataframe
data_SWE_input_calib = Snow_depth_4_yrs['2016':'2018']

# Opening the input file
hf_input = h5py.File('Snow_depth_data/SWE_2016_2018.h5','w')

# Creating a variable with time instances for 1096 days
no_days = len(data_SWE_input_calib) # Total number of days
no_secs_day = 86400 # Total number of seconds in a day
times = np.arange(0,no_days*no_secs_day,no_secs_day)
len(times)

# Changing the storage to numpy array
hf_input.create_dataset('time [s]', data=times)
hf_input.create_dataset('precipitation snow [m SWE s^-1]', data=data_SWE_input_calib['precipitation snow [m SWE s^-1]'].values)

hf_input.close()

### Reading the file once more to check
### Extracting the data from the example 'column_data.h5'.  
#with h5py.File(f'Snow_depth_data/SWE_2016_2018.h5','r') as hdf:
    #ls = list(hdf.keys())
    #print('List of datasets in this file: \n \n', ls)
    #print('\n')
    #sd_itr = np.array(hdf.get('precipitation snow [m SWE s^-1]'))

    #temperature_column = np.array(hdf.get('temperature.cell.0/1600'))
    
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
    


#print(snow_dens_ratio)
#print(sd_itr)