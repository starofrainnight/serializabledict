# -*- coding:utf-8 -*-

import yaml
import io
from .common import FormatMixin


class YamlFormatMixin(FormatMixin):
    def _loads(self, astr):
        return yaml.safe_load(astr)

    def _dumps(self, adict):
        data = io.StringIO()
        yaml.dump(adict, data, default_flow_style=False)
        return data.getvalue()
