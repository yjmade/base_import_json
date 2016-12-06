# base_import_json
make Odoo9 can export and import as JSON format .

It's also avaliable at [Odoo offical app store](https://apps.odoo.com/apps/modules/master/base_import_json/).


=====
Usage
=====
1. cd to your own odoo addons folder
2. ``git clone https://github.com/yjmade/base_import_json``
3. use debug mode go to odoo apps, click ``Update Apps List``, than search ``base_import_json`` in apps list, install it
4. now you should be able to see the JSON format when export and be able to import a JSON file

====
JSON Format
====

the json file to import should be in such format: a list of object which use field as key. And it require all the item in this json get the same fields

```JSON
[
  {
    "name": "import",
    "value": 1
  },
  {
    "name": "export",
    "value": 2
  }
]
```

The json file that export by this module is conform this format.
