# -*- coding: utf-8 -*-

from odoo import models, fields, api


class reservas(models.Model):
    _name = 'reservas.reservas'
    _description = 'reservas.reservas'

    name = fields.Char(string='Nombre', required=True)
    juego_id = fields.Many2one('product.product', string='Juego', required=True)
    fecha_reserva = fields.Datetime(string='Fecha de Reserva', default=fields.Datetime.now)
    estado = fields.Selection([
        ('pendiente', 'Pendiente'),
        ('confirmada', 'Confirmada'),
        ('cancelada', 'Cancelada'),
    ], string='Estado', default='pendiente')
