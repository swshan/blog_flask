#coding=utf-8

from time import time

class LRUCache(object):

    # @param length, an integer
    def __init__(self, length, expiration=30*60):
        self.cache = {}
        self.l = []
        self.length = length
        self.expiration = expiration

    # return an integer
    def get(self, key):
        self.cleanup()
        if key in self.cache:
            item = self.cache[key]
        else:
            item = None
        return item

    # @param key, an integer
    # @param value, an integer
    def set(self, key, value):
        self.cleanup()
        if key in self.cache:
            self.l.remove(key)
        elif len(self.cache) == self.length:
            self.cache.pop(self.l.pop(0))
        t = int(time())
        self.l.append(key)
        self.cache[key] = {'item': value,
                           'access_times': t,
                           'expiration_times': t + self.expiration
                          }
        print ('set cache ')

    def cleanup(self):
        t = int(time())
        # Del expired
        for k in self.cache.keys():
            print ('inside cleanup for')
            if self.cache[k]['expiration_times'] < t:
                print ('inside cleanup if')
                self.l.remove(k)
                del self.cache[k]
                print ('util list removed')

    def info(self, key):
        info = self.cache[key]
