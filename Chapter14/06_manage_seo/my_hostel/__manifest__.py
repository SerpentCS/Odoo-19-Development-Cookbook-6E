# -*- coding: utf-8 -*-
{
    'name': "My Hostel",
    "version": "19.0.1.0.0",
    "summary": "Manage Hostel easily",  # Module subtitle phrase
    "description": """
Manage Hostel
==============
Efficiently manage the entire residential facility in the school
    """,  # Supports reStructuredText(RST) format (description is Deprecated)
    "category": "Tools",
    "website": "http://www.serpentcs.com",
    "depends": ['base','website'],
    "data": [
        "security/hostel_security.xml",
        "security/ir.model.access.csv",
        "data/data.xml",
        "views/hostel.xml",
        "views/hostel_room.xml",
        "views/hostel_amenities.xml",
        "views/hostel_student.xml",
        "views/hostel_categ.xml",
        "views/hostel_template.xml",
    ],
    "installable": True,
    "author": "Serpent Consulting Services Pvt. Ltd.",
    "license": "AGPL-3",
}
