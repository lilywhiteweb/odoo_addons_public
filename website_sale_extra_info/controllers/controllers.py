# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSaleForm
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT
import datetime


# Extend the WebsiteSaleForm class
class WebsiteSaleFormExtraInfo(WebsiteSaleForm):

    @http.route('/website_form/shop.sale.order', type='http', auth="public", methods=['POST'], website=True)
    def website_form_saleorder(self, **kwargs):
        user_date_format = request.env['res.lang']._lang_get(request.env.user.lang).date_format
        # Loop through args and convert dates if required
        for k, v in kwargs.items():
            new_date = self.convert_date(v, user_date_format)
            if new_date:
                kwargs[k] = new_date
        res = super(WebsiteSaleFormExtraInfo, self).website_form_saleorder(**kwargs)

        return res

    # Helper function to convert a date from the user date format to the server date format
    def convert_date(self, custom_date, original_date_format, new_date_format=DEFAULT_SERVER_DATE_FORMAT):
        try:
            new_date = datetime.datetime.strptime(custom_date, original_date_format).strftime(new_date_format)
        except:
            return False

        return new_date
