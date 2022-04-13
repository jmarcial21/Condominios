from odoo import models,fields

class Salidas(models.Model):
    _name = 'seapal_salidas_det'

    num_partida = fields.Integer('Partida', required=True)
    cod_articulo = fields.Integer('Articulo', required=True) #tabña de articulos
    cantidad = fields.Float('Cantidad', required=True)
    costo_unitario = fields.Float('Costo', required=True)
    iva = fields.Float('IVA', required=True)
    status = fields.Boolean('status', required=True)
