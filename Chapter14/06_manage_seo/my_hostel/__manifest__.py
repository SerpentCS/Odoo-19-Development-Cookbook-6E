{
    "name": "Hostel Management",  # Module title
    "summary": "Manage Hostel easily",  # Module subtitle phrase
    "description": """
Manage Hostel
==============
Efficiently manage the entire residential facility in the school
    """,  # Supports reStructuredText(RST) format (description is Deprecated)
    "version": "19.0",
    "author": "Serpent Consulting Services Pvt. Ltd.",
    "category": "Tools",
    "website": "https://www.serpentcs.com",
    "license": "AGPL-3",
    "depends": ["website"],
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
}
