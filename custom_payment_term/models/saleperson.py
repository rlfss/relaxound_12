from odoo import models, fields, api, _


class AccountInvoice(models.Model):
	_inherit = 'account.invoice'


	@api.onchange('partner_id')
	def payment_term(self):
		res=self.env['account.payment.term'].search([])
		for item in res:
			if item.name=='14 days after receipt of invoice':
				self.update({'payment_term_id':item.id})


