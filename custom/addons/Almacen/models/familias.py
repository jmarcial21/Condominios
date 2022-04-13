from odoo import models, fields
class familias(models.Model):
    _name = 'seapal_familias' #nombre de la tabla

    name = fields.Char(string='Familia', size=20, required=True)
    id_almacen = fields.Many2one(comodel_name='seapal_almacenes', string ='Almacen',  required=True)
    status = fields.Boolean(string='status')