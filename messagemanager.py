from request import get, put

class MessageManager():
    def __init__(self, url):
        self.url = url

    def get(self):
        response = get(url)
        return response

    def put(self, message):
        put(self.url, data={'data', message})
        return message


