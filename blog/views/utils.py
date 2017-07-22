#coding=utf-8

class LRUCache:

    # @param length, an integer
    def __init__(self, length):
        self.cache = {}
        self.used_list = []
        self.length = length

    # return an integer
    def get(self, key):
        if key in self.cache:
            if key != self.used_list[-1]:
                self.used.remove(key)
                self.used_list.append(key)
            return self.cache[key]
        else:
            return -1
    # @param key, an integer
    # @param value, an integer
    def set(self, key, value):
        if key in self.cache:
            self.used_list.remove(key)
        elif len(self.cache) == self.length:
            self.cache.pop(self.used_list.pop(0))
        self.used_list.append(key)
        self.cache[key] = value

