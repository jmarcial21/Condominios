from odoo import models, fields

class entradas(models.Model):
    _name = 'seapal_entradas'

    id_almacen = fields.Many2one('seapal_almacenes', 'Almacen', required=True)
    ejercicio = fields.Integer('Ejercicio', required=True)
    folio = fields.Integer('Folio de salida', required=True)
    fecha = fields.Date('Fecha de entrada')
    factura = fields.Char('Factura', size=30)
    id_tipo = fields.Many2one('seapal_tipo_entradas','Tipo de entrada', size=20)
    cod_orden_Compra = fields.Integer('Orden de compra')
    id_proveedor = fields.Many2one('seapal_proveedores', 'Proveedor')
    id_emple_devo = fields.Many2one('seapal_empleados','Empleado devolucion')
    notas = fields.Char('Notas', size=500)
    id_resp_almacen =  fields.Many2one('seapal_empleados','Responsable de Almacen')
    status = fields.Boolean(string="status")