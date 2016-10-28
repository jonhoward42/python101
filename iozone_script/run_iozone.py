#!/usr/bin/env python

# Imports
from subprocess import PIPE
import subprocess

# Variable definitions
deviceIdentifier = "nvme"
deviceList = identify_devices()
deviceQuantity = device_quantity()
iozoneCmd = "/root/iozone3_465/src/current/iozone"
mountrPath = "/mnt"
iozoneFile = "iozone.dat"
fileSize = "4g"
recordSize = ["4k", "8k", "16k", "32k", "64k", "128K", "256k", "512k", "1024k"]

# Function to identify devices
def identify_devices():
        cmd = "lsblk | grep " + deviceIdentifier + " | awk '{print $1}'"
        process = subprocess.Popen(cmd, stdout=PIPE, stderr=PIPE, shell=True)
        data = process.communicate()[0].split()
	return data

# Function to count the number of detected devices
def device_quantity():
	data = len(identify_devices())
	return data

# Function to render mkdir commands
def render_mkdir_commands()

# Function to render mount commands
def render_mount_commands()

# Function to renver iozone commands
def render_iozone_commands()




