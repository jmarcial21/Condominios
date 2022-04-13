from odoo import models, fields


class SeapalDirecciones(models.Model):
    _name = 'seapal_direcciones'
    _rec_name = "direccion"
    direccion = fields.Char(string='Dirección', required=True, size=128)
    titular = fields.Char(string='Titular', size=254)

