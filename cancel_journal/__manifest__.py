{
    'name':   'User Rights for Cancel Journal Entries (Enterprise)',
    'author': 'Itech Resources',
    'company': 'ItechResources',
    'summary': 'This module is for Odoo 11 Enterprise',
    'depends': [
                'base',
                'account',
                'sale',
                'purchase',
                'account_cancel',
                ],
    
    'data': [
        'views/cancel.xml',
        'security/cancel_rights.xml'
        ,
       
    ],
    
    'application': True,
    
    "price": 15.00,
    "currency": "EUR",
}
