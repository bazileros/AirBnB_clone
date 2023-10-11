#!/usr/bin/python3
# models/storage.py

class Storage:
    def __init__(self):
        self.data = {} 

    def save(self, data):
        self.data = {"key": "value"}
        storage.save(self.data)

storage = Storage()
