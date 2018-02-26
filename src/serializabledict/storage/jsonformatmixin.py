# -*- coding:utf-8 -*-

import jsonpickle
import simplejson as json
from .common import FormatMixin


class JsonFormatMixin(FormatMixin):

    def _do_load(self):
        with open(self.path, "rb") as afile:
            try:
                ret = jsonpickle.decode(afile.read().decode("utf-8"))
            except json.scanner.JSONDecodeError:
                pass

            return ret

    def _do_dumps(self, adict):
        data = jsonpickle.encode(adict)
        data = json.dumps(
            json.loads(data),
            ensure_ascii=False,
            indent=4 * ' ')
        return data
