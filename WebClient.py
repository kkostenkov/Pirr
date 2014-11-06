import urllib

def check_connection():
	f = urllib.urlopen('http://192.168.1.115:8000')
	

def send_message(msg):
    f = urllib.urlopen('http://192.168.1.115:8000')
    answer = f.read()