#!/usr/bin/python3

import time
import picamera
from picamera import PiCamera
from fractions import Fraction
import sys
from check_light_func import check_light
from time import sleep
from datetime import datetime
import yaml
# to move the ineligible file
import os
import shutil

### defines arguments as variables
configfile_location = (sys.argv[1])
#
with open(configfile_location, "r") as ymlfile:
   configfile = yaml.safe_load(ymlfile)

dest_photo_day = configfile['path_vars']['ddest_photo_day']
dest_location = configfile['path_vars']['dest_location']
ineligible_files = configfile['path_vars']['ineligible_files']
day_interval = configfile['day_config']['dinterval']
day_light_low_limit = configfile['day_config']['dlight_low_limit']
cam_resolution = configfile['camera_parameters']['resolution']

string_from_configfile = cam_resolution

### converting the string from configfile to tuple that will be used in the timelapse loop
# using map() + tuple() + int + split()
res = tuple(map(int, string_from_configfile.split(', ')))

# printing result
#print("Tuple after getting conversion from String : " + str(res))
cam_resolution1 = res

### Test Shot
def test_shot():
    camera = PiCamera()
    camera.resolution = (cam_resolution1)
    camera.start_preview()
    # Camera warm-up time
    sleep(2)
    camera.capture(ineligible_files+'testshot.jpg')
            
test_shot()
