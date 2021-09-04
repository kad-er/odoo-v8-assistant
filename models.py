# -*- coding: utf-8 -*-

from datetime import timedelta, datetime
from openerp import models, fields, api, tools
from openerp.osv import fields,osv


class appel(models.Model):
	_inherit = 'crm.phonecall'

	_columns = {
	'date_end' : fields.date(string="Date fin", store=True,
        compute='_get_date_end'),
	}

	@api.onchange('date','duration')
	def _get_date_end(self):
		for r in self:
			if not (r.date and r.duration):
				r.date_end = r.date
				continue
				# Add duration to start_date, but: Monday + 5 days = Saturday, so
				# subtract one second to get on Friday instead
			start = fields.datetime.from_string(r.date)
			duration = timedelta(days=r.duration, seconds=-1)
			r.date_end = start + duration


class appelrdv(osv.osv):

	_name = "appel_rdv"
	_auto = False

	_columns = {
		'user_id':fields.char('user_id',size=20,readonly=True,store=True),
    	'type': fields.char('Type', size=12, readonly=True),
    	'name': fields.char('Name', size=12, readonly=True),
    	'date': fields.datetime('Date', readonly=True),
    	'date_stop':fields.datetime('date_stop',readonly=True),
		}

	def init(self, cr):
		tools.sql.drop_view_if_exists(cr, 'appel_rdv')
		cr.execute("""
		CREATE view appel_rdv as
		(SELECT c.user_id as user_id ,
		c.id || 'appel' as id, 
		'appel' as type,
		c.name as name,
		c.date as date,
		c.date_end as date_stop
		FROM crm_phonecall c
		GROUP BY c.user_id, type, c.name, c.date,c.id,date_end
		)
		UNION(
		SELECT m.user_id  user_id,
		m.id || 'rdv' as id,  
		'reunion' as type,
		m.name as name,
		m.start_datetime as date,
		m.stop_datetime as date_stop
		FROM calendar_event m
		GROUP BY m.user_id, type, m.name, m.start_datetime,m.id
		);
		
		""")


appelrdv()


class articles(models.Model):
	_inherit = 'product.template'
	
	_columns = {
	'limite_stock' : fields.float('stock limite minimal',required=True,default=300),
	}

	@api.constrains('limite_stock')
	def get_limite_stock(self):
		for r in self:
			if r.limite_stock<=0:
				raise ValidationError("La valeur du stock limite ne dois pas etre négatif ou nul")



class clientc(models.Model):
	_name="client_c"
	_auto=False

	_columns = {
	'display_name' : fields.char('Nom'),
	'function' : fields.char('Fonction'),
	'phone' : fields.char('Num'),
	'email' : fields.char('Email'),
	'is_company' : fields.char('Entreprise'),
	'id' : fields.char('ID'),
	'country_id' : fields.char('Pays'),
	'parent_id' : fields.char('ID parent'),

	}

	def init(self, cr):
		tools.sql.drop_view_if_exists(cr, 'client_c')
		cr.execute("""
		CREATE view client_c as
		(SELECT display_name,
function,
phone,
email,
is_company,
user_id as id,
country_id,
parent_id
FROM res_partner r
			WHERE r.id IN(
				SELECT c.partner_id FROM crm_phonecall c
				GROUP BY c.partner_id)
		GROUP BY display_name,
function,
phone,
email,
is_company,
user_id,
country_id,
parent_id);

GRANT ALL ON client_c TO odoo
		""")

clientc()
		