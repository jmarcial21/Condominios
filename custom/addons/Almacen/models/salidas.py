from odoo import models,fields

class Salidas(models.Model):
    _name = 'seapal_salidas'

    cod_almacen = fields.Integer('Almacen', required=True) #tabla almacenes
    ejercicio = fields.Integer('Ejercicio', required=True)
    folio = fields.Integer('Folio', required=True)
    cod_jefatura = fields.Integer('Jefatura', required=True) #tabla de jefaturas
    cod_direccion = fields.Integer('Direccion', required=True) #tabla de direcciones
    cod_empleado = fields.Integer('Empleado', required=True) #tabla de empleados
    ubicacion = fields.Char('Ubicacion', size=500, required=True)
    motivo = fields.Char('Motivo', size=200, required=True)
    notas = fields.Char('Notas', size=600)
    tipo = fields.Char('Tipo', size=20, required=True) #tipo de dato fijo: manual, devolucion, etc
    status = fields.Boolean('status')
    resp_almacen = fields.Integer('Responsable almacen', required=True) #tabla de empleados
    total = fields.Float('Total', required=True)




