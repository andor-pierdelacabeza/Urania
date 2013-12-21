import time
import picamera
import shutil


with picamera.PiCamera() as camera:
    camera.resolution = (320, 240)
    camera.start_preview()
    time.sleep(1)
    for i, filename in enumerate(camera.capture_continuous('/tmp/temppic.jpg')):
        print('Captured image %s' % filename)
	shutil.copyfile('/tmp/temppic.jpg','/tmp/pic.jpg')
        if i == 100:
            break
        #time.sleep(0.1)
    camera.stop_preview()
