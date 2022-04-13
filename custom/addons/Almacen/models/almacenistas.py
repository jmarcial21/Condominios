from odoo import models, fields
#creadndo modelo de articulos a partir de una clase
#este modelo es una tabla en BD
class usuariosalm(models.Model):
    _name = 'seapal_almacenistas' #nombre de la tabla

    name = fields.Char(string='Login', size=20, required=True)
    id_emppleado = fields.Many2one('seapal_empleados',string='nombre completo') #relacionar con tabla empleados de RH
    id_almacen = fields.Many2one(comodel_name='seapal_almacenes', string='Almacen')
    status = fields.Boolean(string='status')
    image = fields.Binary(String='Foto')