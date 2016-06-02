'''
@date 2016-6-2

@author Hong-She Liang <starofrainnight@gmail.com>
'''

import os
import os.path
import jsonpickle
import simplejson as json

class SerializableDict(object):
    def __init__(self):
        self._dest_file_path = None
        self._data = dict()
        self._is_batch_update = False

    def load(self, file_path):
        self._dest_file_path = file_path
        self._data.clear()

        if os.path.exists(file_path):
            with open(file_path, "rb") as afile:
                try:
                    self._data.update(jsonpickle.decode(afile.read().decode("utf-8")))
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

        data = jsonpickle.encode(self._data)
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

        # Removed old file after all (clean the rubbish after all success works)
        if os.path.exists(old_file_path):
            os.remove(old_file_path)

    def __del__(self):
        self.save()

    def __enter__(self):
        self._is_batch_update = True

    def __exit__(self, exc_type, exc_value, traceback):
        self._is_batch_update = False
        self.save()

    def __setitem__(self, key, value):
        self._data[key] = value
        self.save()

    def __getitem__(self, key):
        return self._data[key]

    def __contains__(self, item):
        return item in self._data

    def __str__(self):
        return str(self._data)

