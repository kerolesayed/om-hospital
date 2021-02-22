from odoo import api, models, _

class PatientCardReport(models.AbstractModel):
    _name = 'report.om_hospital.report_patient_view'
    _description = 'Patient card Report'

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env['hospital.patient'].browse(docids[0])
        appointments = self.env['hospital.appointment'].search([('patient_id', '=', docids[0])])
        appointment_list = []
        for app in appointments:
            vals = {
                'name': app.name,
                'patient_id': app.patient_id.name,
                'notes': app.notes,
                'date': app.date
            }
            appointment_list.append(vals)
        return {
            'doc_model': 'hospital.patient',
            'docs': docs,
            'appointment_list': appointment_list,
        }