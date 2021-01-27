from odoo import models, fields


class HospitalPatient(models.Model):
    _name = "hospital.doctor"
    _rec_name = "name_doctor"

    name_doctor = fields.Char("Name", required=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ], defualt='male', string='Gender')
    related_user = fields.Many2one("res.users", "Related User")
