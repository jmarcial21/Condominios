from odoo import models, fields


class SeapalPuestos(models.Model):
    _name = 'empleados'
    num_nomina = fields.Integer('Puesto de Trabajo')
    nombre = fields.Text('Nombre')
    primer_apellido = fields.Text('Primer Apellido')
    segundo_apellido = fields.Text('Seggundo Apellido')
    departamento = fields.Many2one('departamentos', 'id')
    puesto = fields.Many2one('puestos', 'id')
    rfc = fields.Char('rfc')
    curp = fields.Char('curp')
    activo = fields.Boolean('Activo')
    foto_perfil = fields.Binary('Foto')