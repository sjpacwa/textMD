import urllib.request
import urllib.parse

class textSend:
    def __init__(self, apiKey, apiSecret, sender):
        self.apiKey = apiKey
        self.apiSecret = apiSecret
        self.sender = sender

    def send(self, to, text):
        params = {
            'api_key': '5db9bc3b',
            'api_secret': 'f0ce2d8f4d354b64',
            'to': to,
            'from': self.sender,
            'text': text
        }

        url = 'https://rest.nexmo.com/sms/json?' + urllib.parse.urlencode(params)

        response = urllib.request.urlopen(url)
        print(response.read())


