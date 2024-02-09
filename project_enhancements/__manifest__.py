# -*- coding: utf-8 -*-
{
    'name': "project_enhancements",

    'summary': """
        Adds additional fields and functionalities to the project management module in Odoo.""",

    'author': "Omar Adel",
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base','project','hr'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/project_view.xml',
        'views/collaborators_view.xml',
    ],
}
