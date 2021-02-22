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

        print('appointment id', appointment)
        return {
            'type': "ir.action.no_nothing"
        }

    def print_report_app(self):
        data = {
            'model': 'create.appointment',
            'form': self.read()[0]
        }
        print(self.read()[0])
        print(self.read())
        print(self.browse(data))
        print(data)
        print(data['form']['namee'])

        return self.env.ref('om_hospital.appointment_card').report_action(self, data=data)



    def del_patient(self):
        for r in self:
          r.namee.unlink()




