from odoo import models, fields


class SeapalDirecciones(models.Model):
    _name = 'direcciones'
    direccion = fields.Char(string='Dirección')
    titular = fields.Text(string='Titular')

