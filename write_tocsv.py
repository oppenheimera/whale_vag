#################################################
##################### USAGE #####################
"""
Change variables in script then from command
line, run the command:
$ python write_to_csv.py target_name.csv 
"""
#################################################

import sys
import pandas as pd
import data_utils as du

stationIDptreyes = '9415020' # Pt Reyes
stationIDlajolla = '9410230' # La Jolla
stationIDbroadway = '9410170' # San Diego
yearstart = 1975
yearend = 2015
hourly_height = 'hourly_height'
air_pressure = 'air_pressure'

filename = sys.argv[-1]
stationID = stationIDptreyes

#### get pressure ####
p, t_p = du.make_monthly_API_requests(stationID, yearstart, yearend, air_pressure)

#### get water level ####
h, t_h = du.make_yearly_API_requests(stationID, yearstart, yearend, hourly_height)

#### clean and interpolate over bad data ####
t_datetime, t_timestamp, pressure, water_level = du.interp_over_pressure_waterlevel(p, t_p, h, t_h)

d = {'date/time': t_datetime, 'timestamp':t_timestamp, 'pressure': pressure, 'water level': water_level}
df = pd.DataFrame(d)

df.to_csv(filename)
