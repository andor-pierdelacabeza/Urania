import os
import subprocess
from tornado.options import define, options
import opts

def getCpuTemp():
	if options.platform == 'rpi':
		cpufile = open('/sys/class/thermal/thermal_zone0/temp')
		cputemp = cpufile.read(2) + '.' + cpufile.read(1)
		cpufile.close()
		return(cputemp)
	else:
		return(00)

def getGpuTemp():
	if options.platform == 'rpi':
		gputemp = subprocess.check_output(["/opt/vc/bin/vcgencmd", "measure_temp"])
		gputemp = gputemp[5:9]
		return(gputemp)
	else:
		return(00)

