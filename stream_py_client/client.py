from ._http import HttpClient
from .sources import ImageSource


class StreamPy(object):

    def __init__(self):
        self._http = HttpClient()
        self.source = ImageSource()

    def stream(self):
        while True:
            self._http.post_chunk(self.source)
