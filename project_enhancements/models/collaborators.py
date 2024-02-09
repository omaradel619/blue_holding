from odoo import models, fields, api


class ProjectCollaborators(models.Model):
    _name = 'project.collaborators'

    employee_id = fields.Many2one('hr.employee', string='Employee')
    status = fields.Selection(
        [('active', 'Active'),
         ('inactive', 'Inactive')], string='Status')
    project_id = fields.Many2one('project.project', string='Project')

    def action_toggle_status(self):
        if self.status == 'active':
            self.status = 'inactive'
        else:
            self.status = 'active'
        return True
