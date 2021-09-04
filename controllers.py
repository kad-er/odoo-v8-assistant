# -*- coding: utf-8 -*-
from openerp import http

# class Assistant(http.Controller):
#     @http.route('/assistant/assistant/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/assistant/assistant/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('assistant.listing', {
#             'root': '/assistant/assistant',
#             'objects': http.request.env['assistant.assistant'].search([]),
#         })

#     @http.route('/assistant/assistant/objects/<model("assistant.assistant"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('assistant.object', {
#             'object': obj
#         })