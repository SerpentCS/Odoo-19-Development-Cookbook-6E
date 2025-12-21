from odoo import models, fields, api

class HostelComplaint(models.Model):
    _name = 'hostel.complaint'
    _description = 'Hostel Complaint'

    name = fields.Char(string='Complaint Title', required=True)
    description = fields.Text(string='Details')
    date = fields.Date(string='Date', default=fields.Date.today)
    
    # Dynamic relation to any target model
    target_object_id = fields.Reference(
        selection=[
            ('hostel.room', 'Room'),
            ('hostel.student', 'Student'),
        ],
        string="Complaint About"
    )
