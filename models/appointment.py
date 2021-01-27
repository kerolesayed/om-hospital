from odoo import models, fields, api,_

class Hospitalappointment(models.Model):
    _name = "hospital.appointment"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = 'date desc'

    patient_id = fields.Many2one("hospital.patient",string='Patient',required=True)
    patient_age = fields.Integer("Age",related='patient_id.age')
    notes = fields.Text("Registration Appointment")
    notes_doctor = fields.Text("Doctor Notes")
    notes_pharmacy = fields.Text("pharmacy None")
    date = fields.Date('Appointment Date')
    appointment_lines = fields.One2many('hospital.appointmentlines','appointment_id')
    name = fields.Char(string='Appointment ID', required=True, copy=False,
                           readonly=True, index=True, default=lambda self: _('New'))
    ref = fields.Reference(selection=[('res.partner', 'partner'),
                                      ('hospital.patient', 'patient'),
                                      ('res.user', 'user')], string='Reference')
    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('appointment.sequence') or _('New')

        result = super().create(vals)
        return result
    state = fields.Selection([('draft', 'Draft'),
                              ('confirm', 'Confirm'),
                              ('done', 'Done'),
                              ('cancelled', 'Cancelled'),
                              ], string='Status',default='draft',readonly=True)
    def action_confirm(self):
        for rec in self:
            rec.state = 'confirm'

    def action_done(self):
        for rec in self:
            rec.state = 'done'

    def delete_medicine(self):
        for r in self:
            r.appointment_lines = [(5, 0, 0)]


class Hospitalappointmentlines(models.Model):
    _name = "hospital.appointmentlines"

    medicine = fields.Many2one('product.product', string='Medicine')
    qty = fields.Integer(string='Quantity')
    appointment_id = fields.Many2one('hospital.appointment', string='ID')

