# .*. coding: utf-8 .*.

from odoo import models, fields, api

class Course(models.Model):
    _name = 'academy.course'
    _description = 'Course Info'
    
    name = fields.Char(string='Título', required=True)
    description = fields.Text(string='Description')
    
    level = fields.Selection(
        string='Level', selection=[
            ('beginner','Beginner'),
            ('intermediate','Intermediate'),
            ('advanced','Advanced')
        ], copy=False
    )
    active = fields.Boolean(string='Active', default=True)