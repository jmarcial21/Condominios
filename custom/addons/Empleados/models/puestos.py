from odoo import models, fields


class SeapalPuestos(models.Model):
    _name = 'seapal_puestos'
    _rec_name = "puesto"
    puesto = fields.Char('Puesto de Trabajo',size=45, required=True)
