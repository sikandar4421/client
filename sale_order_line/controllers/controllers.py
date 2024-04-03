# -*- coding: utf-8 -*-
# from odoo import http


# class SaleOrderLine(http.Controller):
#     @http.route('/sale_order_line/sale_order_line', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sale_order_line/sale_order_line/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sale_order_line.listing', {
#             'root': '/sale_order_line/sale_order_line',
#             'objects': http.request.env['sale_order_line.sale_order_line'].search([]),
#         })

#     @http.route('/sale_order_line/sale_order_line/objects/<model("sale_order_line.sale_order_line"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sale_order_line.object', {
#             'object': obj
#         })
