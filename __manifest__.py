# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Irokoo Profile',
    'version' : '1.0',
    'depends': ['base', 'website_sale', 'product', 'website'],
    'summary': 'Custom Developments',
    'description': """
    Custom addon made for developments
    """,
    'category': 'Few categories',
    'data': [
        'views/product_views.xml',
        'templates/website_sale_template.xml',
    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
    # 'auto_install': False,
}
