from tornado.options import options,define

#Networking 
define("port", default=8080)

#Hardware
define("platform", default="rpi")
define("camera", default="raspicam")
