from odoo import models, fields, api,_
from odoo.exceptions import ValidationError


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _rec_name = "name"

    name = fields.Char("Name", required=True, track_visibility='always')
    age = fields.Integer("Age", group_operator=False)
    notes = fields.Text("Notes")
    image = fields.Image("Image")
    name_sec = fields.Char(string='Patient ID', required=True, copy=False,
                           readonly=True, index=True, default=lambda self: _('New'))
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ], defualt='male', string='Gender')
    group_age = fields.Selection([('major', 'Major'), ('minor', 'Minor'), ], string='Age Group', compute='set_age',store=True)
    appointment_count = fields.Integer(string='Appointment', compute='get_count_appointment')
    active = fields.Boolean('Active', default=True)
    doctor = fields.Many2one("hospital.doctor", 'Doctor')
    email = fields.Char("Email")
    user_id = fields.Many2one('res.users', 'Pro')
    upper_name = fields.Char('Upper Name', compute='get_upper', inverse="get_inv")
    @api.depends('name')
    def get_upper(self):
        for r in self:
            r.upper_name = r.name.upper()

    def get_inv(self):
        for r in self:
            r.name = r.upper_name.lower()



    @api.depends('age')
    def set_age(self):
      for rec in self:
        if rec.age > 18:
            rec.group_age = 'major'
        else:
            rec.group_age = 'minor'
    @api.model
    def create(self, vals):
        if vals.get('name_sec', _('New')) == _('New'):
            vals['name_sec'] = self.env['ir.sequence'].next_by_code('patient.sequence') or _('New')

        result = super().create(vals)
        return result
    @api.constrains('age')
    def correct_age(self):
      for rec in self:
        if rec.age < 5:
            raise ValidationError('sorry age of patient must be greater than 5.')

    def button_appointment(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'open_appointment',
            'view_mode': 'tree,form',
            'res_model': 'hospital.appointment',
            'domain': [('patient_id', '=', self.id)],
        }
    def get_count_appointment(self):
        for r in self:
            count = r.env['hospital.appointment'].search_count([('patient_id', '=', r.id)])
            r.appointment_count = count

    def name_get(self):
        res = []
        for r in self:
           # res.append((r.id, '%s-%s' % (r.name, r.name_sec)))
           # res.append((r.id, r.name+"-"+r.name_sec))
            res.append((r.id, f"{r.name}-{r.name_sec}"))

        return res

    def send_email(self):
        template_id = self.env.ref('om_hospital.email_patient').id
        template = self.env['mail.template'].browse(template_id)
        template.send_mail(self.id, force_send=True)

    def print_report_patient(self):
        return self.env.ref('om_hospital.patient_card').report_action(self)

