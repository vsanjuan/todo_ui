# -*- coding: utf-8 -*-
from openerp import models, fields, api

class Tag(models.Model):
	_name = 'todo.task.tag'
	# name = fields.Char('Name',40,translate=True)
	name = fields.Char('Name',size=40,translate=True)
	task_ids = fields.Many2many('todo.task','Tasks')

class Stage(models.Model):
	_name = 'todo.task.stage'
	_order = 'sequence,name'
	_rec_name = 'name' # the default
	_table = 'todo_task_stage' # the default
	# name = fields.Char('Name',40,translate=True)
	# String fields: 
	name = fields.Char('Name',size=40,translate=True)
	desc = fields.Text('Description')
	state = fields.Selection([
		('draft','New'),
		('open','Started'),
		('done','Closed')
		])
	docs = fields.Html('Documentation')
	# Numeric fields:
	sequence = fields.Integer('Sequence')
	perc_complete = fields.Float('% Complete',(3,2))
	# Date fields:
	date_effective = fields.Date('Effective date')
	date_changed = fields.Datetime('Last changed')
	# Other fields:
	fold = fields.Boolean('Folded?')
	image = fields.Binary('Image')

	tasks = fields.One2many(
		'todo.task', # related model
		'stage_id',  # field for this on related model
		'Task in this stage')


class TodoTask(models.Model):
	_inherit = 'todo.task'
	stage_id = fields.Many2one('todo.task.stage','Stage')
	tags_id = fields.Many2many('todo.task.tag', string='Tags')