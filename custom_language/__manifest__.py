# -*- coding: utf-8 -*-
# module template
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Custom Language',
    'version': '12.0',
    'category': 'Tools',
    'license': 'AGPL-3',
    'author': "Techspawn",
    'website': 'http://www.Techspawn.com/',
    'depends': ['contacts', 'account', 'mail'],

    'data': [
        'views/invoice_mail_template.xml',             
             ],
    'installable': True,
    'application': True,
}
