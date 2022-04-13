# -*- coding: utf-8 -*-
{
    'name': "Empleados SEAPAL",
    'version': '1.0',
    'depends': [],
    'author': "Informática SEAPAL",
    'category': 'Recursos Humanos',
    'description': """
    Control de empleados
    """,
    'data': [
        'views/menu_view.xml',
        'views/direcciones_view.xml',
        'views/departamentos_view.xml',
        'views/puestos_view.xml',
        'views/empleados_view.xml',
        'security/empleado_security.xml',
        'security/ir.model.access.csv'
    ],
    'demo': [],
    'website': 'https://seapal.gob.mx',
    'license': 'LGPL-3',
    'application': True,
}
