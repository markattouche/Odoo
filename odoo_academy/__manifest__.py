# -*- coding: utf-8 -*-

{
    'name': 'Odoo Academy',
    'summary': """Academy app to manage Training""",
    'description': """
        Academy Module to manage Training:
        - Cursos
        - Sesiones
        - Participantes
    """,
    'author': 'Odoo',
    'license': 'OEEL-1',
    'application': True,
    'installable': True,
    'website': 'https://minicode.odoo.com',
    'category': 'Training',
    'version': '0.1',
    'depends': ['sale', 'website'],
    'data': [
        'security/academy_security.xml',
        'security/ir.model.access.csv',
        'views/academy_menuitems.xml',
        'views/course_views.xml',
        'views/session_views.xml',
        'views/sale_views_inherit.xml',
        'views/product_views_inherit.xml',
        'wizard/sale_wizard_view.xml',
        'report/session_report_templates.xml',
        'views/academy_web_templates.xml',
        # 'views/addenda_test.xml',
    ],
    'demo': [
        'demo/academy_demo.xml'
    ]
}