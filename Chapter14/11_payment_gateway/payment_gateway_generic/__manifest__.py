{
    'name': 'Generic Payment Gateway Integration',
    'version': '19.0',
    'depends': ['payment', 'website_sale'],
    'data': [
        'views/payment_provider.xml',
        'views/payment_templates.xml',
        'data/payment_provider_data.xml'
    ],
    'installable': True,
    'application': False,
}
