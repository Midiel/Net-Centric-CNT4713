'''
Midiel Rodriguez
Project: Web server in python to render video (mp4) and audio (mp3)
Sources: 
    - Video: https://www.w3schools.com/html/html5_video.asp
    - Audio: https://www.w3schools.com/html/html5_audio.asp
'''

from http.server import HTTPServer, BaseHTTPRequestHandler
from os import curdir, sep

PORT_NUMBER = 8080

class myHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.path = "/index.html"
        try:
            sendReply = False
            if self.path.endswith(".html"):
                mimetype = 'text/html'
                sendReply = True
            if self.path.endswith(".jpg"):
                mimetype = 'image/jpg'
                sendReply = True
            if self.path.endswith(".js"):
                mimetype = 'application/javascript'
                sendReply = True
            if self.path.endswith(".css"):
                mimetype = 'text/css'
                sendReply = True
            if self.path.endswith(".mp3"):
                mimetype = 'audio/mpeg'
                sendReply = True
            if self.path.endswit(".mp4"):
                mimetype = 'video/mp4'
                sendReply =  True

            if sendReply == True:
                f = open(curdir + sep + self.path)
                self.send_response(200)
                self.send_header('Content-type', mimetype)
                self.end_headers()
                self.wfile.write(f.read())
                f.close()
            return
        
        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)
try:
    #Create a web server and define the handler to manage the
    #incomeing request
    server = HTTPServer(('', PORT_NUMBER), myHandler)
    print('Started the web server on port number ', PORT_NUMBER)

    #Wait forever for incoming http requests
    server.serve_forever()

except KeyboardInterrupt:
    print('^C recieved, shutting down the web server')
    server.socket.close()