from odoo import models, fields


class SeapalDepartamentos(models.Model):
    _name = 'departamentos'
    departamento = fields.Char('Departamento')
    direccion = fields.Many2one('direcciones','id')
