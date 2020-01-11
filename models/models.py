from odoo import models, fields


class TodoCategory(models.Model):
    _name = 'todo.category'
    _description = 'Todo category'
    name = fields.Char(string="Todo Category name", required=True)


class Todo(models.Model):
    _name = 'todo.todo'  # Table name in database: todo_todo
    _description = 'Todo table'
    # _inherit = 'new_module.new_module'

    name = fields.Char(string="Todo name", required=True)
    description = fields.Html(
        string='Todo Description',
        required=False)
    due_date = fields.Datetime(
        string='Due Date',
        required=True, default=fields.Datetime.now())
    status = fields.Selection(
        string='Status',
        selection=[('draft', 'Draft'),
                   ('in_process', 'In Process'), ('done', 'Done'), ],
        required=True, default='draft')
    current_user = fields.Many2one(
        comodel_name='res.users',
        string='Current User',
        required=True)
    category = fields.Many2one(
        comodel_name='todo.category',
        string='Category',
        required=True)
