import urllib.request
from urllib.error import URLError, HTTPError

def fetch(host="http://127.0.0.1:8888/", quest=""):
    if quest is not "":
        host = host + "quest/" + quest
    try:
        response = urllib.request.urlopen(host)
    except HTTPError as e:
        print('The server couldn\'t fulfill the request.')
        print('Error code: ', e.code)
        return 'The server couldn\'t fulfill the request.'
    except  URLError  as e:
        print('We failed to reach a server.')
        print('Reason: ', e.reason)
        return 'We failed to reach a server.'
    else:
        return response.read()

    
    #return urllib.request.urlopen(host).read()






