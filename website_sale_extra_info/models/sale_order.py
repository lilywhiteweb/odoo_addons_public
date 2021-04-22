# -*- coding: utf-8 -*-

from odoo import models, fields, api

# Override the Customer Model to include Area Field
class WebsiteSaleOrderExtraInfo(models.Model):
    _name = 'sale.order'
    _inherit = ['sale.order']

    x_website_delivery_date = fields.Date(string='Delivery Date', required=True)
