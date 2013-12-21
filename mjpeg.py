import tornado.ioloop
import tornado.web
import tornado.gen
import time, os
from PIL import Image, ImageDraw
from StringIO import StringIO
import random


#Cosas a definir
demoimg = '/tmp/pic.jpg'
listenPort = 8080

class OjeteHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Ojete, world")


class MJPEGHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self):
        loop = tornado.ioloop.IOLoop.current()
	self.set_status(200)
	self.set_header('Content-type','multipart/x-mixed-replace; boundary=--boundary')
        while True:
            staticimg = Image.open(demoimg)
	    imgx, imgy= staticimg.size
	    stamp = str(time.strftime("%d/%m/%Y")) + ' - ' + (time.strftime("%H:%M:%S"))
	    stampimg = ImageDraw.Draw(staticimg)
	    stampimg.text((imgx-130, imgy-15), stamp, 255)
	    img_io = StringIO()
	    staticimg.save(img_io, 'JPEG', quality=80)
	    self.write("--boundary\n")
	    self.write("Content-type: image/jpeg\r\n")
            self.write("Content-length: %s\r\n\r\n" % str(img_io.len))
            self.write(img_io.getvalue())
	    yield tornado.gen.Task(self.flush)
            yield tornado.gen.Task(loop.add_timeout, loop.time() + 0.33)

class JPEGHandler(tornado.web.RequestHandler):
    def get(self):
	staticimg = Image.open(demoimg)
	img_io = StringIO()
	staticimg.save(img_io, 'JPEG', quality=70)
        self.set_header('Content-type','image/jpeg')
        self.set_header('Content-length',str(img_io.len))
        self.write(img_io.getvalue())


class CamHandler(tornado.web.RequestHandler):
    def get(self):
	self.render("templates/cam.html")

settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
}


application = tornado.web.Application([
    (r"/image.mjpg", MJPEGHandler),
    (r"/image.jpg", JPEGHandler),
    (r"/cam", CamHandler),
    (r"/", OjeteHandler),
], **settings)



print 'Serving on ' + str(listenPort) + '...'
application.listen(listenPort)
tornado.ioloop.IOLoop.instance().start()
