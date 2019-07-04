#from openerp import models, fields
from openerp import models, fields, api, exceptions

class Marks(models.Model):
    _name = 'marks.lines'
    #_rec_name='name'
    name = fields.Char('Name')
    picking_id = fields.Many2one('pickings.orders', 'Picking')
    partnerid =fields.Many2one('res.partner','Partner')
    reference = fields.Many2one('stock.picking','Reference')
    status = fields.Char('Status')
    def name_get(self, cr, uid,ids):
        print('name')
        return "name"

class Stockpickings(models.Model):
    _inherit='stock.picking'
    _name = 'stock.pickingrevisi'
    namanya = fields.Char('Name')

    

class Pickings(models.Model):
    _name = 'pickings.orders'
    
    name = fields.Char('Name')
    #_rec_name = 'name'
    status = fields.Char('Status')
    person=fields.Char('Responsible Person')
    user_id = fields.Many2one('res.users', 'Responsible')
    reference=fields.Char('Reference')
    refe=fields.Char('Refe',compute='blaya_total')
    partnerid =fields.Many2one('res.partner','Responsible Person')
    picking_ids = fields.One2many('marks.lines', 'picking_id', string='Picking Lines')
    #picking_ids = fields.Many2many('marks', 'picking_id', 'Picking Lines')

    @api.model
    def create(self, vals):
        seq = self.env['ir.sequence'].next_by_code('pickorder')
        vals['name'] = seq
        print("create new sequence")
        return super(Pickings, self).create(vals)  
    #@api.model
    def do_target(self):
        print('target')
        view = { 
        'name':'student_action_menu',
        'view_mode': 'form',
        'view_id': False,
        'view_type': 'form',
        'res_model': 'pickings.orders',
        #'res_id': res_id,
        'type': 'ir.actions.act_window',
        'nodestroy': True,
        'target': 'self',
        'domain': '[]',
        #'context': context 
        }
        return True
    def do_save(self):
        print('save')
        return True   
    def print_report(self):
        return self.env['report'].get_action(self,'reportfel')
        
    @api.one  
    @api.depends('picking_ids')
    def blaya_total(self):
        balik=''
        #if self.picking_ids is not None:
        #print(self.picking_ids)
        for rec in self.picking_ids:
            print(rec)
            balik=balik+','+rec.reference.name
        self.refe = balik
        #self.user_id=1

    #@api.multi
   #@api.one
   #def r_get_total(self):
   #     try:
   #      self.thirdfield = self.first + self.second
   ##     except:
   #          raise "here add your exceptions"
   #     return True

             
    

   
    
