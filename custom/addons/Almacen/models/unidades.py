from odoo import models, fields

class unidades(models.Model):
    _name = 'seapal_unidades' #nombre de la tabla

    name = fields.Char(string="Unidad", size=20, required=True)
    status = fields.Boolean(string='status')
