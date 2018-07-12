# -*- coding:utf-8 -*-

import jsonpickle
import simplejson as json
from .common import FormatMixin


class JsonFormatMixin(FormatMixin):
    def _loads(self, astr):
        try:
            ret = jsonpickle.decode(astr)
        except json.scanner.JSONDecodeError:
            pass

        return ret

    def _dumps(self, adict):
        data = jsonpickle.encode(adict)
        data = json.dumps(json.loads(data), ensure_ascii=False, indent=4 * ' ')
        return data
