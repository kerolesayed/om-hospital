from odoo import models, fields, api,_

class createappointment(models.TransientModel):
    _name = "create.appointment"

    namee = fields.Many2one('hospital.patient', string='Patient')
    date = fields.Date('Date')

    def create_oppointment(self):
        vals = {
            'patient_id': self.namee.id,
            'date': self.date
        }
        self.env['hospital.appointment'].create(vals)
        self.namee.message_post(body='done appointment created')

    def get_data(self):
        appointment = self.env['hospital.appointment'].search([])

        for r in appointment:
            print('appointment id', r.name)

    # to overwrite in model by function
    def write(self, vals):
        res = super(createappointment, self).write(vals)
        return res



