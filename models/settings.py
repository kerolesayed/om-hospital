from odoo import models, fields, api


class settings(models.TransientModel):
    _inherit = 'res.config.settings'
    notes = fields.Char('notes')
    module_purchase = fields.Boolean("purchase")

    def set_values(self):
        res = super(settings, self).set_values()
        self.env['ir.config_parameter'].set_param('om_hospital.notes', self.notes)
        return res

    @api.model
    def get_values(self):
        res = super(settings, self).get_values()
        notes = self.env['ir.config_parameter'].get_param('om_hospital.notes')
        res.update(
            notes=notes
        )
        return res
