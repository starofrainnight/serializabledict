'''
@date 2016-6-2

@author Hong-She Liang <starofrainnight@gmail.com>
'''

import os
import os.path
from collections import UserDict
from .storage.jsonfilestorage import JsonFileStorage

__version__ = '0.0.2'


class SerializableDict(UserDict):

    def __init__(self, initialdata=None, storage=JsonFileStorage()):
        super().__init__(initialdata)

        self._is_batch_update = False
        self.storage = storage

    def load(self):
        self.data.clear()
        self.data.update(self.storage.load())

    def save(self):
        """
        Save data to file
        """
        # Don't do real update if doing batch update
        if self._is_batch_update:
            return

        self.storage.save(self.data)

    def __enter__(self):
        self._is_batch_update = True

    def __exit__(self, exc_type, exc_value, traceback):
        self._is_batch_update = False
        self.save()

    def __setitem__(self, key, value):
        self.data[key] = value
        self.save()
