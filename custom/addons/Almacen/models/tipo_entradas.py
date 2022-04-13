from odoo import models, fields

class entradas_det(models.Model):
    _name = 'seapal_tipo_entradas'

    name = fields.Many2one('Tipo de entrada', size=20, required=True)
    status = fields.Boolean('Status')