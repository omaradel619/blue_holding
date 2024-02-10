from odoo import models, fields, api
from odoo.exceptions import UserError


class Employee(models.Model):
    _inherit = 'hr.employee'

    github_account = fields.Char(string='GitHub Account')
    collaborator_project_ids = fields.Many2many('project.project', string='Collaborator Projects',
                                                compute='_get_related_project')

    def _get_related_project(self):
        for rec in self:
            self.collaborator_project_ids = self.env['project.collaborators'].search(
                [('employee_id', '=', rec.id), ('status', '=', 'active')]).mapped('project_id')

    def write(self, vals):
        if 'active' in vals and not vals['active']:
            for employee in self:
                for line in employee.collaborator_project_ids:
                    if line.collaborator_ids.filtered(lambda c: c.status == 'active'):
                        raise UserError("Don't archive this employee! They are a collaborator in project(s).")
        return super(Employee, self).write(vals)
