from odoo import http
from odoo.http import request



class Hospital(http.Controller):
    @http.route('/hospital/patient/', website=True, auth='public')
    def hospital_patient(self, **kw):
        # return "Hello, world,im keroles"
        return request.render('om_hospital.patient_page',{})
