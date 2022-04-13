from odoo import models, fields

class entradas_det(models.Model):
    _name = 'seapal_entradas_det'

    id_entrada = fields.Many2one('seapal_entradas', 'Entrada', required=True)
    partida = fields.Integer('Partida', required=True)
    id_arituculo =fields.Many2one('seapal_articulos','Articulo', required=True)
    cantidad = fields.Float('Cantidad', required=True)
    costo_unitario  = fields.Float('Costo Unitario', required=True)
    Subtotal = fields.Float('Subtotal',required=True)
    iva = fields.Float('IVA',required=True)
    total = fields.Float('Total', required=True)
    status = fields.Boolean(string="status")