'''
@date 2016-6-2

@author Hong-She Liang <starofrainnight@gmail.com>
'''

import os
import os.path
from threading import Lock
from collections import UserDict
from .storage.jsonfilestorage import JsonFileStorage

__version__ = '0.0.2'


class SerializableDict(UserDict):
    def __init__(self,
                 initialdata=None,
                 storage=JsonFileStorage(),
                 batch_lock=Lock()):
        super().__init__(initialdata)

        self._batch_lock = batch_lock
        self.storage = storage

    def load(self):
        self.data.clear()
        self.data.update(self.storage.load())

    def save(self):
        """
        Save data to file
        """
        # Don't do real update if doing batch update
        if not self._batch_lock.acquire(False):
            return

        try:
            self.storage.save(self.data)
        finally:
            self._batch_lock.release()

    def __enter__(self):
        self._batch_lock.acquire()

    def __exit__(self, exc_type, exc_value, traceback):
        try:
            self.storage.save(self.data)
        finally:
            # Ensure lock be unlock even storage save raise an exception
            self._batch_lock.release()

    def __setitem__(self, key, value):
        self.data[key] = value
        self.save()
