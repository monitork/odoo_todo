from odoo import api, fields, models


class TodoMakeDoneWizard(models.TransientModel):
    _name = 'todo.make.done.wizard'
    _description = 'Make all Todo done'
    @api.multi
    def update_todos_done(self):
        list_todo = self.env['todo.todo'].search([('status','!=','done')]) 
        for todo in list_todo:
            todo.update('status','done')
        return True

