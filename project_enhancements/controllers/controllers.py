# -*- coding: utf-8 -*-
# from odoo import http


# class ProjectEnhancements(http.Controller):
#     @http.route('/project_enhancements/project_enhancements', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/project_enhancements/project_enhancements/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('project_enhancements.listing', {
#             'root': '/project_enhancements/project_enhancements',
#             'objects': http.request.env['project_enhancements.project_enhancements'].search([]),
#         })

#     @http.route('/project_enhancements/project_enhancements/objects/<model("project_enhancements.project_enhancements"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('project_enhancements.object', {
#             'object': obj
#         })
