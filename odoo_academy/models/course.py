# .*. coding: utf-8 .*.

from odoo import models, fields, api

class Course(models.Model):
    _name = 'academy.course'
    _description = 'Course Info'
    
    name = fields.Char(string='Título', required=True)
    description = fields.Text(string='Descripción')
    
    level = fields.Selection(string='Level', required=True
                                selection=[
                                    ('principiante','Principiante'),
                                    ('intermedio','Intermedio'),
                                    ('avanzado','Avanzado')
                                ], copy=False
                            )
    active = fields.Boolean(string-'Active', default=True)