from requests import get, put

class MessageManager():
    def __init__(self, url):
        self.url = url

    def get(self):
        response = get(self.url)
        return response

    def put(self, message):
        msg_id = len(self.get().json()) + 1
        url = self.url + str(msg_id)
        put(url, data={'msg':message})
        return message

