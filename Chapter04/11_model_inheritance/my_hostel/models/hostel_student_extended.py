from odoo import models, fields


class HostelStudentExtra(models.Model):
    _inherit = 'hostel.student'

    guardian_name = fields.Char(string='Guardian Name')
    student_code = fields.Char(string='Student Code')
