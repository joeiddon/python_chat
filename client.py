#this will be imported by the reciever.py and sender.py scripts to give
#them access to the Server class (so we don't duplicate code)
#when it is run, it will start the reciever.py and sender.py scripts

import os, urllib.request, os, json

SERVER_ADDR = 'http://10.1.128.195:12345/'

class Message():
    def __init__(self, user, content):
        self.user = user
        self.content = content

#the client uses this class to communicate with the server
class Server():
    def __init__(self):
        self.addr = SERVER_ADDR
        os.environ['NO_PROXY'] = self.addr
    def get_messages(self):
        response = urllib.request.urlopen(self.addr).read() #GET (no data sent, just that it is a GET)
        #aggregation as we are creating new Messgae instances that are not owned by this class so won't die
        return [Message(message['user'], message['content']) for message in json.loads(response)]
    def post(self, data):
        #data is a dictionary
		#sends the data as a POST request straight to the server (JSON encoded)
        response = urllib.request.urlopen(self.addr, json.dumps(data).encode('utf-8')).read()
        return response.decode('utf-8')
    def check_user(self, user):
        #returns True if username not taken, otherwise False
        return self.post({'type': 'check_user', 'user': user}) == 'valid'
    def send_message(self, user, content):
        response = self.post({'type': 'send_message', 'user': user, 'content': content})
        if response != 'thanks':
            print('some error!')

#when run as a program, will start the other scripts
if __name__ == '__main__':
	import subprocess
	subprocess.Popen(['python', 'sender.py'], creationflags=subprocess.CREATE_NEW_CONSOLE)
	subprocess.Popen(['python', 'receiver.py'], creationflags=subprocess.CREATE_NEW_CONSOLE)