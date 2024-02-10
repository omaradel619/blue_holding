from odoo import http
from odoo.http import request
import json


class EmployeeController(http.Controller):

    @http.route('/project_enhancements/controllers', type='http', auth='public', methods=['GET'])
    def get_employees_with_projects(self):
        active_projects = request.env['project.project'].search(
            [('collaborator_ids', '!=', False)
                , ('collaborator_ids.status', '=', 'active')]).mapped(lambda project:
                                                                      {
                                                                          'Project Name': project.name,
                                                                          'Project ID': project.id,
                                                                          'EMP Info': project.collaborator_ids.mapped
                                                                          (lambda employee: {
                                                                              'Name': employee.employee_id.name,
                                                                              'Status': employee.status,
                                                                          }),
                                                                      })
        return json.dumps(active_projects)