# -*- coding: utf-8 -*-
from odoo import models, fields,api


class TodoCategoryModel(models.Model):
    _name = 'todo.category'
    _description = 'Todo category'
    name = fields.Char(string="Todo Category name", required=True)


class TodoModel(models.Model):
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
    
    @api.multi
    def action_next(self):
        next_status = 'done'
        if self.status == 'draft':
            next_status = 'in_process' 
        return self.update({'status': next_status})
    
    @api.model
    def create(self, values):
        """
            Create a new record for a model ModelName
            @param values: provides a data for new record
    
            @return: returns a id of new record
        """
        print('============ CREATE', values)
    
        result = super(TodoModel, self).create(values)
    
        return result
    
    
    @api.multi
    def write(self, values):
        """
            Update all record(s) in recordset, with new value comes as {values}
            return True on success, False otherwise
    
            @param values: dict of new values to be set
    
            @return: True on success, False otherwise
        """
        print('================== WRITE', values)
        result = super(TodoModel, self).write(values)
    
        return result
    

