from odoo import api, models

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    # @api.multi
    def create_invoice(self):
        invoice_vals = {
            'type': 'out_invoice',
            'partner_id': self.partner_id.id,
            'invoice_origin': self.name,
            'invoice_line_ids': [(0, 0, {
                'name': 'Delivery Charge',
                'price_unit': self.delivery_charge,
                'quantity': 1,
                'account_id': self.env['account.account'].search([('name', '=', 'Delivery Account')]).id
            })],
        }
        invoice = self.env['account.move'].create(invoice_vals)
        return {
            'name': 'Invoice',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'account.move',
            'res_id': invoice.id,
            'type': 'ir.actions.act_window',
            'target': 'current',
        }
