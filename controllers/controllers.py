# -*- coding: utf-8 -*-
from odoo import http

# class WebMobile(http.Controller):
#     @http.route('/web_mobile/web_mobile/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/web_mobile/web_mobile/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('web_mobile.listing', {
#             'root': '/web_mobile/web_mobile',
#             'objects': http.request.env['web_mobile.web_mobile'].search([]),
#         })

#     @http.route('/web_mobile/web_mobile/objects/<model("web_mobile.web_mobile"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('web_mobile.object', {
#             'object': obj
#         })