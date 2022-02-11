# .*. coding: utf-8 .*.

{
    'name': 'Odoo Academy',
    
    'summary': """App académica de Entrenamiento""",
    
    'description': """
        Módulo Académico de manejo de Entrenamiento:
            - Cursos
            - Sesiones
            - Participantes
    """,
    
    'author': 'Minicode',
    
    'website': 'https://minicode.odoo.com',
    
    'category': 'Training',
    
    'version': '0.1',
    
    'depends': ['base'],
    
    'data': [
        'security/academy_security.xml',
        'security/ir.model.access.csv',
        'views/academy_menuitems.xml'
    ],
    
    'demo': [
        'demo/academy_demo.xml',
    ]
}