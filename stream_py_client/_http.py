import requests


class HttpClient(object):

    BASE_URL = "http://127.0.0.1:5000"

    def post_chunk(self, source):
        requests.post(self.BASE_URL, data=source)
