import http.server, socketserver, json

#https://docs.python.org/3.0/library/urllib.request.html
#"the HTTP request will be a POST instead of a GET when the data parameter is provided"

PORT = 12345
		
class Message():
    def __init__(self, user, content):
        self.user = user
        self.content = content

class History():
    def __init__(self):
        #encapsulation as only history instances can access
        #their own messsages, other objects must call the History's
        #get_all method
        self.messages = []
        self.users = set()
    def add_message(self, user, content):
        #composition - we create Message instances that are
        #owned by the History instance
        self.messages.append(Message(user, content))
        self.users.add(user)
    def get_all(self):
        return json.dumps([{'user':    message.user,
                            'content': message.content} for message in self.messages])
    def username_taken(self, user):
        #returns True is user in our history of users
        return user in self.users

#instantiation
message_history = History()
message_history.add_message('jim', 'hello')
message_history.add_message('john', 'hi')

#inhertitance from the http.server.BaseHTTPRequestHandler class which itself inherits
#from the base socketserver handler class. Each class provides new methods which implement different
#protocols e.g. the hypertext transfer protocol. We then implement our own methods (do_*) which are
#called by the base classes' methods. See here for better explanation:
#https://docs.python.org/3/library/http.server.html#http.server.BaseHTTPRequestHandler
class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        #called when client wants all the message history
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain')
        self.end_headers()
        self.wfile.write(message_history.get_all().encode('utf-8'))
    def do_POST(self):
        #called when either registering or sending a message
        content_length = int(self.headers['Content-Length'])
        request = json.loads(self.rfile.read(content_length))
        if request['type'] == 'check_user':
            response = b'invalid' if message_history.username_taken(request['user']) else b'valid'
            print(request, response)
        elif request['type'] == 'send_message':
            message_history.add_message(request['user'], request['content'])
            response = b'thanks'
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain')
        self.end_headers()
        self.wfile.write(response)

print('Serving on port', PORT)
with socketserver.TCPServer(('',PORT), Handler) as httpd:
    httpd.serve_forever()