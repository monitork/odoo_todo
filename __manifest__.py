# -*- coding: utf-8 -*-
{
    'name': "Todo Manager",
    'summary': """This is description of Todo Management""",
    'description': """
        Todo Manager :
            - create task
            - delete task
            - list task
    """,
    'author': "Monitor K",
    'website': "https://github.com/monitork/odoo_todo",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Extra Tools',
    'version': '0.1',
    'application': True,
    # any module necessary for this one to work correctly
    'depends': [],
    'data': [
        'wizards/todo_make_done_wizard.xml',
        'views/views.xml', 
    ],
}
