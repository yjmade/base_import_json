# -*- coding: utf-8 -*-
from openerp import http
from openerp.addons.web.controllers.main import Export as OrigExport, ExportFormat, serialize_exception
import json
from itertools import izip


class Export(OrigExport):

    @http.route('/web/export/formats', type='json', auth="user")
    def formats(self):
        res = super(Export, self).formats()
        res.append({'tag': 'json', 'label': 'JSON'})
        return res


class JSONExport(ExportFormat, http.Controller):

    @http.route('/web/export/json', type='http', auth="user")
    @serialize_exception
    def index(self, data, token):
        return self.base(data, token)

    @property
    def content_type(self):
        return 'application/json;charset=utf8'

    def filename(self, base):
        return base + '.json'

    def from_data(self, fields, rows):
        return json.dumps(
            [dict(izip(fields, row)) for row in rows],
            encoding='utf-8',
            indent=4
        )
