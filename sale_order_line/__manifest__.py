# -*- coding: utf-8 -*-
{
    'name': "sale_order_line",

    'summary': """
        Module helps to calculate sale price by applying percentage on cost price""",

    'description': """
        Module helps to calculate sale price by applying percentage on cost price
    """,

    'author': "OdooFusion",
    'website': "https://www.odoofusion.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['sale','product'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
