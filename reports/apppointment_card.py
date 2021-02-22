from odoo import api, models, _

class PatientCardReport(models.AbstractModel):
    _name = 'report.om_hospital.report_appointment_view'
    _description = 'appointment card Report'

    @api.model
    def _get_report_values(self, docids, data=None):
        if data['form']['namee']:
            appointments = self.env['hospital.appointment'].search([('patient_id', '=', data['form']['namee'][0])])
        else:
            appointments = self.env['hospital.appointment'].search([])

        return {
            'doc_model': 'hospital.appointment',
            'appointments': appointments,
        }

