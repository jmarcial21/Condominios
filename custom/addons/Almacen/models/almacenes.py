from odoo import models, fields

class almacenes(models.Model):
    _name = 'seapal_almacenes'

    name = fields.Char(string='Almacen', required=True)
    jefe = fields.Many2one('seapal_empleados',string="Jefe", size=100) #relacionar tabla empleados RH
    encargado = fields.Many2one('seapal_empleados',string="Encargado", size=100) #relacionar tabla empleados RH
    status = fields.Boolean(string="status")