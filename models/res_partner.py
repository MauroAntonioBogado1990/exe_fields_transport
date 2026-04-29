# -*- coding: utf-8 -*-
from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    transport_company = fields.Char(string='Empresa de Transporte')
    transport_cuit = fields.Char(string='CUIT Transporte')
    transport_driver = fields.Char(string='Chofer')
    chassis_plate = fields.Char(string='Patente Chasis')
    trailer_plate = fields.Char(string='Patente Acoplado')