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
    "depends": ['base','website'],
    "data": [
        "security/hostel_security.xml",
        "security/ir.model.access.csv",
        "views/hostel.xml",
        "views/hostel_template.xml",
        "views/custom_template.xml",
        "views/snippets.xml",
    ],
    "installable": True,
}
