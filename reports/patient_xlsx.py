from odoo import models

class PartnerXlsx(models.AbstractModel):
    _name = 'report.om_hospital.report_patient_xlsx'
    _inherit = 'report.odoo_report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, lines):
        format1 = workbook.add_format({'font_size':14,'align':'vcenter','bold':True})
        sheet = workbook.add_worksheet('patient card')
        sheet.set_column(3,3,50)
        sheet.set_column(2,2,30)
        sheet.write(2, 2, 'name',format1)
        sheet.write(2, 3, lines.name,format1)
        sheet.write(3, 2, 'age',format1)
        sheet.write(3, 3, lines.age,format1)
        sheet.write(4, 2, 'gender',format1)
        sheet.write(4, 3, lines.gender,format1)
