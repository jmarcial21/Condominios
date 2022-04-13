from odoo import models, fields


class SeapalPuestos(models.Model):
    _name = 'puestos'
    puesto = fields.Text('Puesto de Trabajo')
