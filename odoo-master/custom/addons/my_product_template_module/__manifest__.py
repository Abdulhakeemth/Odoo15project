{
    'name': 'MY PRODUCT TEMPLATE MODULE',
    'summary': """ This module will add a record to store  report details""",
    'version': '1.1',
    'description' : """This module will add a record to store report details""",
    'author': 'Abdul Hakeem',
    'company': 'Zaeem Solutions',
    'website': 'https://www.zaeemsolutions.com',
    'category': 'Tools',
    'depends': ['base', 'product', 'sale'],
    'license': 'AGPL-3',
    'data': [
        'security/ir.model.access.csv',
        'views/product_template.xml',
        'views/sale_order_line.xml',


    ],
    'demo': [

    ],
    'installable': True,
    'auto_install': False,
    'application': True,

}
