from odoo import models, fields

class articulos(models.Model):
    _name = 'seapal_articulos'

    name = fields.Char(string='Articulo', size=180, required=True)
    codigo = fields.Integer('Codigo', required=True)
    id_almacen = fields.Many2one(comodel_name='seapal_almacenes', string='Almacen',  required=True)
    id_familia = fields.Many2one(comodel_name='seapal_familias', string='Familia', required=True)
    id_subfamilia = fields.Many2one(comodel_name='seapal_subfamilias', string='Subfamilia')
    existencia = fields.Float(string='Existencia')
    id_unidad = fields.Many2one(comodel_name="seapal_unidades", string="Unidad de medida", required=True)
    costo_prom = fields.Float(string='Costo promedio')
    ult_costo_ent = fields.Float(string='Ultimo costo de entrada')
    cog = fields.Char(string='COG', size=30)
    maximo = fields.Float(string='Maximo')
    minimo = fields.Float(string='Minimo')
    status = fields.Boolean(string='status')
