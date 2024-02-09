from odoo import models, fields, api


class ProjectEnhancement(models.Model):
    _inherit = 'project.project'

    odoo_version = fields.Integer(string='Odoo Version')
    odoo_type = fields.Selection([('community', 'Community'), ('enterprise', 'Enterprise')], default='enterprise',
                                 string='Odoo Type')
    github_repo_name = fields.Char(string='Github Repo Name')
    github_repo_url = fields.Char(string='GitHub Repo URL')
    hosting_selection = fields.Selection(
        [('on_prem', 'On-Prem'),
         ('cloud_hosting', 'Cloud Hosting'),
         ('odoo_sh', 'Odoo.sh'),
         ('odoo_online', 'Odoo Online')], string='Hosting Selection')
    hosting_description = fields.Html(string='Hosting Description')
    collaborator_ids = fields.One2many('project.collaborators', 'project_id', string='Collaborators')
