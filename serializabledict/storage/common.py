# -*- coding:utf-8 -*-

import os.path


class Storage(object):
    def __init__(self):
        pass

    def load(self):
        return dict()

    def save(self, adict):
        raise NotImplemented()


class FileStorage(Storage):
    """
    Notice: You must implement _loads() and _dumps() methods
    """

    def __init__(self, apath=None):
        super().__init__()

        self.path = apath

    def load(self):
        if self.path is None:
            raise ValueError("Can't load 'None' path!")

        ret = super().load()

        if not os.path.exists(self.path):
            return ret

        with open(self.path, "rb") as afile:
            return self._loads(afile.read().decode("utf-8"))

    def save(self, adict):
        """
        Save data to file
        """

        if self.path is None:
            raise ValueError("Can't save to 'None' path!")

        data = self._dumps(adict).encode("utf-8")

        new_file_path = self.path + ".new"
        old_file_path = self.path + ".old"

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
        if os.path.exists(self.path):
            os.rename(self.path, old_file_path)

        # Moved the new file as our configuration file
        os.rename(new_file_path, self.path)

        # Removed old file after all (clean the rubbish after all success
        # works)
        if os.path.exists(old_file_path):
            os.remove(old_file_path)


class FormatMixin(object):
    def _loads(self, astr):
        raise NotImplemented()

    def _dumps(self, adict):
        raise NotImplemented()
