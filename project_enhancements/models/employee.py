from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Employee(models.Model):
    _inherit = 'hr.employee'

    github_account = fields.Char(string='GitHub Account')
    collaborator_project_ids = fields.Many2many('project.project', string='Collaborator Projects',
                                                compute='_get_related_project')

    def _get_related_project(self):
        for rec in self:
            self.collaborator_project_ids = self.env['project.collaborators'].search(
                [('employee_id', '=', rec.id), ('status', '=', 'active')]).mapped('project_id')
