# -*- coding: utf-8 -*-

from openerp import models
from openerp.addons.base_import import models as base_import_models
import json


base_import_models.FILE_TYPE_DICT["application/json"] = ("json", True, None)

base_import_models.EXTENSIONS[".json"] = True


class BaseImportJSON(models.TransientModel):
    _inherit = 'base_import.import'

    def _read_json(self, record, options):
        items = json.loads(record.file)
        if items:
            headers = items[0].keys()
            yield headers
            for item in items:
                yield [item[header] for header in headers]
