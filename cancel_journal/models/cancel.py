 
from odoo import api, fields, models

 
class cancelrights(models.Model):
    _inherit = 'account.invoice'


class canceljournals(models.Model):
    _inherit = 'account.move'
    
class customerinvoice(models.Model):
    _inherit ='account.invoice'