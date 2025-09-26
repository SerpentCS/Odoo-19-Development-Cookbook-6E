{
    "name": "Hostel Management",  # Module title
    "summary": "Manage Hostel easily",  # Module subtitle phrase
    "description": """
Manage Hostel
==============
Display Hostel records in the web page.
    """,  # Supports reStructuredText(RST) format (description is Deprecated)
    "version": "19.0",
    "author": "Serpent Consulting Services Pvt. Ltd.",
    "category": "Tools",
    "website": "https://www.serpentcs.com",
    "license": "AGPL-3",
    'depends': ['base', 'website', 'utm'],
    "data": [
        "security/hostel_security.xml",
        "security/ir.model.access.csv",
        'data/config_data.xml',
        "views/hostel.xml",
        "views/hostel_room.xml",
        "views/hostel_amenities.xml",
        "views/hostel_student.xml",
        "views/hostel_categ.xml",
        "views/hostel_issue_view.xml",
        "views/hostel_template.xml",
        "views/custom_template.xml",
        "views/snippets.xml",
        "views/inquiries_view.xml",
        "views/form_template.xml",
    ],
    'assets': {
        'web.assets_frontend': [
            'my_hostel/static/src/js/snippets.js',
        ],
    },
    "installable": True,
}
