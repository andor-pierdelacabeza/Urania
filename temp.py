import os
import subprocess

def getCpuTemp():
	#print('CPU Temp')
	cpufile = open('/sys/class/thermal/thermal_zone0/temp')
	cputemp = cpufile.read(2) + '.' + cpufile.read(1)
	cpufile.close()
	return(cputemp)


def getGpuTemp():
	#print('GPU Temp')
	gputemp = subprocess.check_output(["/opt/vc/bin/vcgencmd", "measure_temp"])
	gputemp = gputemp[5:9]
	return(gputemp)

