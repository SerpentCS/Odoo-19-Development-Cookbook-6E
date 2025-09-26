# -*- coding: utf-8 -*-
{
    'name': "My Hostel",
    'summary': "Manage the Hostel",
    'website': "",
    'category': 'Website',
    'version': '19.0',
    "author": "Serpent Consulting Services Pvt. Ltd.",
    'depends': ['base', 'website'],
    "website": "https://www.serpentcs.com",
    'data': [
        # load views and templates here...
    ],
    'assets': {
        'web.assets_frontend': [
            'my_hostel/static/src/scss/hostel.scss',
            'my_hostel/static/src/js/hostel.js',
        ],
    },
}
