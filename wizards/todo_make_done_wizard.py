from odoo import api, fields, models


class TodoMakeDoneWizard(models.TransientModel):
    _name = 'todo.make.done.wizard'
    _description = 'Make all Todo done'

    @api.multi
    def update_todos_done(self):
        list_todo = self.env['todo.todo'].search([('status','!=','done')]) 
        list_todo.write({'status': 'done'})
        # print('==================', list_todo)
        # for todo in list_todo:
        #     todo.write({'status': 'done'})
        return True

    
    