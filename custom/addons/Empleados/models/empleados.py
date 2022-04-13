from odoo import models, fields


class SeapalEmpleados(models.Model):
    _name = 'seapal_historial_empleados'
    num_nomina = fields.Integer('Núm. de Empleado',required="True")
    nombre = fields.Char('Nombre', required=True, size=128)
    primer_apellido = fields.Char('Primer Apellido', required=True, size=128)
    segundo_apellido = fields.Char('Segundo Apellido', size=45)
    departamento = fields.Many2one(comodel_name="seapal_departamentos",required="True")
    puesto = fields.Many2one(comodel_name="seapal_puestos",required="True")
    rfc = fields.Char('rfc', size=13,required="True")
    curp = fields.Char('curp', size=18,required="True")
    activo = fields.Boolean('Activo',default=True)
    foto_perfil = fields.Binary('Foto')
    email = fields.Char('email', size=254)
    telefono = fields.Char('telefono', size=10)
