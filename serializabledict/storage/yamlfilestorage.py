# -*- coding:utf-8 -*-

from .common import FileStorage
from .yamlformatmixin import YamlFormatMixin


class YamlFileStorage(FileStorage, YamlFormatMixin):
    pass
