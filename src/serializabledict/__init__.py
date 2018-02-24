'''
@date 2016-6-2

@author Hong-She Liang <starofrainnight@gmail.com>
'''

import os
import os.path
import jsonpickle
import simplejson as json
from collections import UserDict

__version__ = '0.0.2'


class SerializableDict(UserDict):

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)

        self._dest_file_path = None
        self._is_batch_update = False

    def load(self, file_path):
        self._dest_file_path = file_path
        self.data.clear()

        if os.path.exists(file_path):
            with open(file_path, "rb") as afile:
                try:
                    self.data.update(jsonpickle.decode(
                        afile.read().decode("utf-8")))
                except json.scanner.JSONDecodeError:
                    pass

    def save(self):
        """
        Save data to file
        """
        # Don't do real update if doing batch update
        if self._is_batch_update:
            return

        if self._dest_file_path is None:
            return

        data = jsonpickle.encode(self.data)
        data = json.dumps(
            json.loads(data),
            ensure_ascii=False,
            indent=4 * ' ').encode("utf-8")

        new_file_path = self._dest_file_path + ".new"
        old_file_path = self._dest_file_path + ".old"

        # Removed new file
        if os.path.exists(new_file_path):
            os.remove(new_file_path)

        new_file = open(new_file_path, "wb")
        with new_file:
            # Generate a better style json file, so that we could modify it
            # manually
            new_file.write(data)

        # Removed old file
        if os.path.exists(old_file_path):
            os.remove(old_file_path)

        # Moved the configuration file as old file
        if os.path.exists(self._dest_file_path):
            os.rename(self._dest_file_path, old_file_path)

        # Moved the new file as our configuration file
        os.rename(new_file_path, self._dest_file_path)

        # Removed old file after all (clean the rubbish after all success
        # works)
        if os.path.exists(old_file_path):
            os.remove(old_file_path)

    def __enter__(self):
        self._is_batch_update = True

    def __exit__(self, exc_type, exc_value, traceback):
        self._is_batch_update = False
        self.save()

    def __setitem__(self, key, value):
        self.data[key] = value
        self.save()
