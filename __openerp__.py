# -*- coding: utf-8 -*-
{
    'name': "base_import_json",

    'summary': """
        allow odoo to import and export as json format""",

    'author': "yjmade",
    'website': "https://github.com/yjmade",

    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ["web", 'base_import'],
    "qweb": ["static/src/xml/*.xml"]
}
