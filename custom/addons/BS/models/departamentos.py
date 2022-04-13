from odoo import models, fields


class SeapalDepartamentos(models.Model):
    _name = 'seapal_departamentos'
    _rec_name = "departamento"
    departamento = fields.Char('Departamento', required=True)
    direccion = fields.Many2one(comodel_name="seapal_direcciones", string="Direccion", size=128, required=True)
