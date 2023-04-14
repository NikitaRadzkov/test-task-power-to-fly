from datetime import datetime


class Cache:
    def __init__(self, duration):
        self.duration = duration
        self.data = {}

    def get(self, key):
        now = datetime.utcnow()
        if key in self.data and (now - self.data[key]['timestamp']) < self.duration:
            return self.data[key]['value']
        else:
            return None

    def set(self, key, value):
        self.data[key] = {'value': value, 'timestamp': datetime.utcnow()}

    def clear(self):
        self.data.clear()
