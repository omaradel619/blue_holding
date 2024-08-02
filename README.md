Project Management and Employee Enhancement Module
This project involves enhancements to the project and employee modules within Odoo, including API development and report generation. Below are the details of the implemented features.

Project Module Enhancements

Odoo Version Field
Type: Integer
Added to store the version of Odoo.

Odoo Type
Type: Selection
Options: ['community', 'enterprise']
Default: 'enterprise'

GitHub Repo Name
Type: Character
Added to store the name of the GitHub repository.

GitHub Repo URL
Type: URL
Added to store the URL of the GitHub repository.

Hosting Selection
Type: Selection
Options: ['on_prem', 'cloud_hosting', 'odoo_sh', 'odoo_online']

Hosting Description
Type: Rich Text
Added to provide a description of the hosting.

Collaborators Tab
Introduces a new model with the following fields:

Employee: Many2one relation to employees.
Status: Selection with options ['active', 'inactive']
Implementation: Only tree view.
Buttons: Two buttons at the end of the tree row to make the record active or inactive.
Row Highlighting: Rows with active status are highlighted in green, and inactive in red.


Employee Module Enhancements

GitHub Account Field
Added to the employee model.

Tree View and Kanban View
GitHub account included in the views.

Projects Tab
Shows the projects that the employee is a collaborator in.
Functionality to mark a record as active or inactive.

Archiving Warning
Displays a warning if the employee is still active in a project when attempting to archive.


API Development
Get Employees with Active Projects
Method: GET
Authentication: Basic
Input: None
Response Format: JSON
Controller: Added to get all employees with their active projects.


Reports Generation
Project PDF Report
Includes the following information:
Project name
Project date
Project GitHub repo name
Project GitHub repo URL
Project Odoo version
Project Odoo type
Project hosting
List of collaborators
