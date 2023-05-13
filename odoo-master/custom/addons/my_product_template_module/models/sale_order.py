from odoo import fields, models, api
from odoo.exceptions import UserError


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    brand_name = fields.Char(string='Brand', related='product_id.brand_id.name', store=True, readonly=False)

    @api.onchange('product_id')
    def _onchange_product_id(self):
        if self.product_id:
            self.brand_name = self.product_id.brand_id.name

    @api.constrains('product_uom_qty', 'price_unit', 'product_id')
    def _check_minimum_cost(self):
        for record in self:
            if record.price_unit < record.product_id.minimum_cost:
                raise UserError("Unit price should not be less than the minimum cost of the product.")

