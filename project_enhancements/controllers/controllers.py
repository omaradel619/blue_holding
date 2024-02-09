from odoo import http
from odoo.http import request
import json


class EmployeeController(http.Controller):

    @http.route('/project_enhancements/controllers', type='http', auth='public', methods=['GET'])
    def get_employees_with_projects(self):
        employees = request.env['hr.employee'].search([])

        response = []
        for employee in employees:
            active_projects = request.env['project.project'].search(
                [('collaborator_ids.employee_id', '=', employee.id)
                    , ('collaborator_ids.status', '=', 'active')])

            project_data = []
            for project in active_projects:
                project_data.append({
                    'project_name': project.name,
                    'project_id': project.id
                })

            response.append({
                'EMP Name': employee.name,
                'EMP ID': employee.id,
                'Active Projects': project_data,
            })
        return json.dumps(response)
