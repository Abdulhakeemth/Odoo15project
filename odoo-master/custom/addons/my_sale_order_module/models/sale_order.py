from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    delivery_charge = fields.Float(string='Delivery Charge', compute='_compute_delivery_charge')
    computed_delivery_charge = fields.Float(
        string="Computed Delivery Charge", compute="_compute_delivery_charge", store=True
    )

    @api.depends('amount_total')
    def _compute_delivery_charge(self):
        for order in self:
            order.delivery_charge = order.amount_total * 0.1

class AccountMove(models.Model):
    _inherit = 'account.move'

    delivery_charge = fields.Monetary(
        string='Delivery Charge',
        compute='_compute_delivery_charge',
        store=True,
        readonly=True,
    )

    @api.depends('invoice_line_ids')
    def _compute_delivery_charge(self):
        for record in self:
            sale_order = self.env['sale.order'].search([('name', '=', record.invoice_origin)])
            if sale_order:
                record.delivery_charge = sale_order.delivery_charge
            else:
                record.delivery_charge = 0
