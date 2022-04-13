from odoo import models,fields

class Proveedores(models.Model):
    _name = 'seapal_proveedores'

    name = fields.Char('Nombre', size=50, required=True)
    contacto = fields.Char("Contacto", size=50, required=True)
    telefonos = fields.Char("Telefonos", size=200, required=True)
    correo = fields.Char("Correo", size=100, required=True)
    rfc = fields.Char("RFC", size=14, required=True)
    banco = fields.Char("Banco", size=100, required=True)
    clabe = fields.Char("Clabe", size=50)
    status = fields.Boolean("status")

