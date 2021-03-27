from requests import get, put

class MessageManager():
    def __init__(self, url):
        self.url = url

    def get(self):
        response = get(self.url)
        return response

    def put(self, message):
        put(self.url, data={'msg':message})
        return message

