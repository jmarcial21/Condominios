from odoo import models, fields

class subfamilias(models.Model):
    _name = 'seapal_subfamilias'

    name = fields.Char(string='Sub Familia', size=20, required=True)
    id_familia = fields.Many2one('seapal_familias', string ='Familia',  required=True)
    status = fields.Boolean(string='status')

