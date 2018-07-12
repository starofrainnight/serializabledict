# -*- coding:utf-8 -*-

from .common import FileStorage
from .jsonformatmixin import JsonFormatMixin


class JsonFileStorage(FileStorage, JsonFormatMixin):
    pass
