'''
@date 2016-6-2

@author Hong-She Liang <starofrainnight@gmail.com>
'''

from threading import RLock
from collections import UserDict
from .storage.jsonfilestorage import JsonFileStorage

__version__ = '0.0.5'


class SerializableDict(UserDict):
    def __init__(self, initialdata=None, storage=JsonFileStorage()):
        super().__init__(initialdata)

        self._batch_lock = RLock()
        self._batch_counter = 0

        self.storage = storage

    def _batch_acquire(self, blocking=True, timeout=-1):
        ret = self._batch_lock.acquire(blocking, timeout)
        if ret:
            self._batch_counter += 1
        return ret

    def _batch_release(self):
        self._batch_lock.release()
        self._batch_counter -= 1

    def load(self):
        self.data.clear()
        self.data.update(self.storage.load())

    def save(self):
        """
        Save data to file
        """

        # Don't do real update if doing batch update
        if not self._batch_acquire(False):
            return

        try:
            is_last_exit = (self._batch_counter == 1)
            if is_last_exit:
                self.storage.save(self.data)
        finally:
            self._batch_release()

    def __enter__(self):
        self._batch_acquire()

    def __exit__(self, exc_type, exc_value, traceback):
        try:
            is_last_exit = (self._batch_counter == 1)
            if is_last_exit:
                self.storage.save(self.data)
        finally:
            # Ensure lock be unlock even storage save raise an exception
            self._batch_release()

    def __setitem__(self, key, value):
        self.data[key] = value
        self.save()
